// Twilio calls this when a voicemail recording is ready: email + text the owner the link.
import { twilioParams, owner, sms, mailOwner, e164 } from "../../lib/twilio.js";

export async function onRequestPost({ request, env }) {
  const p = await twilioParams(request, env);
  if (!p) return new Response("Forbidden", { status: 403 });
  if (p.RecordingStatus !== "completed" || !p.RecordingUrl) return new Response("", { status: 204 });
  // Caller number is not in this callback; look it up from the call.
  let from = "";
  try {
    const r = await fetch(`https://api.twilio.com/2010-04-01/Accounts/${env.TWILIO_SID}/Calls/${p.CallSid}.json`, { headers: { Authorization: "Basic " + btoa(env.TWILIO_SID + ":" + env.TWILIO_TOKEN) } });
    if (r.ok) from = e164((await r.json()).from);
  } catch {}
  const url = p.RecordingUrl + ".mp3";
  await Promise.allSettled([
    mailOwner(env, `Voicemail${from ? " from " + from : ""} (${p.RecordingDuration}s)`, `Listen: ${url}\nCaller: ${from || "unknown"}`),
    sms(env, owner(env), `Voicemail${from ? " from " + from : ""} (${p.RecordingDuration}s): ${url}`)
  ]);
  return new Response("", { status: 204 });
}
