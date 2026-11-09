// GET /api/reviews  ->  { rating, count, url, reviews: [{name, rating, text, when, photo}], source }
//
// Source is chosen by ONE setting (Cloudflare Pages variable REVIEWS_SOURCE):
//   "places" (default)  Google Places API (New). Needs secret GOOGLE_PLACES_KEY and variable PLACE_ID.
//   "gbp"               Google Business Profile API (all reviews). Needs GBP_CLIENT_ID, GBP_CLIENT_SECRET,
//                       GBP_REFRESH_TOKEN, GBP_ACCOUNT, GBP_LOCATION (secrets/variables).
// To switch: change REVIEWS_SOURCE to gbp in Cloudflare (Pages > reliant-site > Settings > Variables). No code change.
//
// Optional KV binding REVIEWS_KV: every review ever seen is kept, so the list grows past Google's 5-per-request limit.
// Results are cached for 6 hours. If Google is unreachable, the last good copy is served.

const TTL = 6 * 3600;
const JSON_HEADERS = { "content-type": "application/json; charset=utf-8" };

export async function onRequestGet({ request, env, waitUntil }) {
  const cache = caches.default;
  const key = new Request(new URL("/api/reviews", request.url).toString());
  const hit = await cache.match(key);
  if (hit) return hit;

  let data;
  try {
    data = (env.REVIEWS_SOURCE || "places") === "gbp" ? await fromGbp(env) : await fromPlaces(env);
    if (env.REVIEWS_KV) data = await accumulate(env, data);
    if (env.REVIEWS_KV) await env.REVIEWS_KV.put("last_good", JSON.stringify(data));
  } catch (e) {
    let stale = env.REVIEWS_KV ? await env.REVIEWS_KV.get("last_good") : null;
    if (stale) return new Response(stale, { headers: { ...JSON_HEADERS, "cache-control": "public, max-age=300" } });
    return new Response(JSON.stringify({ error: "reviews_unavailable", reviews: [] }), {
      status: 200, headers: { ...JSON_HEADERS, "cache-control": "public, max-age=120" },
    });
  }
  const res = new Response(JSON.stringify(data), {
    headers: { ...JSON_HEADERS, "cache-control": `public, max-age=${TTL}` },
  });
  waitUntil(cache.put(key, res.clone()));
  return res;
}

async function fromPlaces(env) {
  if (!env.GOOGLE_PLACES_KEY || !env.PLACE_ID) throw new Error("places not configured");
  const r = await fetch(`https://places.googleapis.com/v1/places/${encodeURIComponent(env.PLACE_ID)}`, {
    headers: {
      "X-Goog-Api-Key": env.GOOGLE_PLACES_KEY,
      "X-Goog-FieldMask": "rating,userRatingCount,reviews,googleMapsUri",
    },
  });
  if (!r.ok) throw new Error("places " + r.status);
  const p = await r.json();
  return {
    source: "places",
    rating: p.rating || null,
    count: p.userRatingCount || 0,
    url: env.GOOGLE_REVIEWS_URL || p.googleMapsUri || "",
    reviews: (p.reviews || []).map((x) => ({
      id: x.name || `${x.authorAttribution?.displayName}|${x.publishTime}`,
      name: x.authorAttribution?.displayName || "Google user",
      photo: x.authorAttribution?.photoUri || "",
      rating: x.rating || 5,
      text: x.originalText?.text || x.text?.text || "",
      time: x.publishTime || "",
    })).filter((x) => x.text),
  };
}

async function fromGbp(env) {
  const need = ["GBP_CLIENT_ID", "GBP_CLIENT_SECRET", "GBP_REFRESH_TOKEN", "GBP_ACCOUNT", "GBP_LOCATION"];
  if (need.some((k) => !env[k])) throw new Error("gbp not configured");
  const t = await fetch("https://oauth2.googleapis.com/token", {
    method: "POST",
    headers: { "content-type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams({
      client_id: env.GBP_CLIENT_ID, client_secret: env.GBP_CLIENT_SECRET,
      refresh_token: env.GBP_REFRESH_TOKEN, grant_type: "refresh_token",
    }),
  });
  if (!t.ok) throw new Error("gbp token " + t.status);
  const { access_token } = await t.json();
  const stars = { ONE: 1, TWO: 2, THREE: 3, FOUR: 4, FIVE: 5 };
  let reviews = [], pageToken = "", avg = null, total = 0;
  for (let i = 0; i < 10; i++) {
    const u = `https://mybusiness.googleapis.com/v4/accounts/${env.GBP_ACCOUNT}/locations/${env.GBP_LOCATION}/reviews?pageSize=50${pageToken ? "&pageToken=" + pageToken : ""}`;
    const r = await fetch(u, { headers: { authorization: "Bearer " + access_token } });
    if (!r.ok) throw new Error("gbp " + r.status);
    const j = await r.json();
    avg = j.averageRating ?? avg; total = j.totalReviewCount ?? total;
    for (const x of j.reviews || []) {
      reviews.push({
        id: x.reviewId || x.name,
        name: x.reviewer?.displayName || "Google user",
        photo: x.reviewer?.profilePhotoUrl || "",
        rating: stars[x.starRating] || 5,
        text: x.comment || "",
        time: x.createTime || "",
      });
    }
    if (!j.nextPageToken) break;
    pageToken = j.nextPageToken;
  }
  return { source: "gbp", rating: avg, count: total, url: env.GOOGLE_REVIEWS_URL || "", reviews: reviews.filter((x) => x.text) };
}

async function accumulate(env, data) {
  let all = {};
  try { all = JSON.parse((await env.REVIEWS_KV.get("all")) || "{}"); } catch (_) {}
  for (const r of data.reviews) all[r.id] = r;
  await env.REVIEWS_KV.put("all", JSON.stringify(all));
  data.reviews = Object.values(all).sort((a, b) => (b.time || "").localeCompare(a.time || ""));
  return data;
}
