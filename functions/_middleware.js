// Keep the temporary *.pages.dev test address out of Google; the real domain is indexed normally.
export async function onRequest({ request, next }) {
  const res = await next();
  const host = new URL(request.url).hostname;
  if (host.endsWith(".pages.dev")) {
    const r = new Response(res.body, res);
    r.headers.set("X-Robots-Tag", "noindex, nofollow");
    return r;
  }
  return res;
}
