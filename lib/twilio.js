// Shared helpers for the phone/text functions (Twilio). Free Cloudflare side; Twilio bills per use.
// Settings (Cloudflare Pages > Settings > Variables and Secrets):
//   SMS_ENABLED="true"  TWILIO_SID  TWILIO_TOKEN (secret)  TWILIO_FROM (business number, +1...)  OWNER_CELL (+1..., where calls/texts forward)

export const on = env => env.SMS_ENABLED === "true" && env.TWILIO_SID && env.TWILIO_TOKEN && env.TWILIO_FROM;
export const owner = env => env.OWNER_CELL || env.SMS_TO || "";
export const xml = s => new Response(`<?xml version="1.0" encoding="UTF-8"?><Response>${s}</Response>`, { headers: { "Content-Type": "text/xml" } });
export const escX = s => String(s).replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&apos;" }[c]));

// "+1 (770) 555-1234" / "7705551234" -> "+17705551234"; "" if not a US number
export function e164(s) {
  const d = String(s || "").replace(/\D/g, "");
  if (d.length === 10) return "+1" + d;
  if (d.length === 11 && d[0] === "1") return "+" + d;
  return "";
}

// Read Twilio's form post and reject anything not signed with our auth token.
export async function twilioParams(request, env) {
  const params = Object.fromEntries(new URLSearchParams(await request.text()));
  const sig = request.headers.get("X-Twilio-Signature") || "";
  if (!env.TWILIO_TOKEN || !sig) return null;
  const data = request.url + Object.keys(params).sort().map(k => k + params[k]).join("");
  const key = await crypto.subtle.importKey("raw", new TextEncoder().encode(env.TWILIO_TOKEN), { name: "HMAC", hash: "SHA-1" }, false, ["sign"]);
  const mac = btoa(String.fromCharCode(...new Uint8Array(await crypto.subtle.sign("HMAC", key, new TextEncoder().encode(data)))));
  if (mac.length !== sig.length || !timingSafe(mac, sig)) return null;
  return params;
}
function timingSafe(a, b) { let r = 0; for (let i = 0; i < a.length; i++) r |= a.charCodeAt(i) ^ b.charCodeAt(i); return r === 0; }

export async function sms(env, to, body) {
  if (!on(env) || !to) return false;
  const r = await fetch(`https://api.twilio.com/2010-04-01/Accounts/${env.TWILIO_SID}/Messages.json`, {
    method: "POST",
    headers: { Authorization: "Basic " + btoa(env.TWILIO_SID + ":" + env.TWILIO_TOKEN), "Content-Type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams({ From: env.TWILIO_FROM, To: to, Body: String(body).slice(0, 640) })
  });
  if (!r.ok) console.log("twilio sms", r.status, await r.text());
  return r.ok;
}

// Plain email to the owner through Resend (same settings as the quote form).
export async function mailOwner(env, subject, text) {
  if (!env.RESEND_API_KEY || !env.LEAD_TO_EMAIL) return false;
  const r = await fetch("https://api.resend.com/emails", {
    method: "POST", headers: { Authorization: "Bearer " + env.RESEND_API_KEY, "Content-Type": "application/json" },
    body: JSON.stringify({ from: env.FROM_EMAIL || "Reliant Consulting and Construction Leads <onboarding@resend.dev>", to: [env.LEAD_TO_EMAIL], subject, text })
  });
  if (!r.ok) console.log("resend", r.status, await r.text());
  return r.ok;
}

export const BIZ = "Reliant Consulting and Construction";
export const SITE = "https://reliantconsultingandconstruction.com";
