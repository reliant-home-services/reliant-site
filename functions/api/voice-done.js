// After the forwarded call ends. If nobody answered: text the caller back, alert the owner, take a voicemail.
import { twilioParams, owner, xml, sms, mailOwner, e164, BIZ, SITE } from "../../lib/twilio.js";

export async function onRequestPost({ request, env, waitUntil }) {
  const p = await twilioParams(request, env);
  if (!p) return new Response("Forbidden", { status: 403 });
  if (p.DialCallStatus === "completed") return xml("<Hangup/>");

  const caller = e164(p.From);
  if (caller && caller !== owner(env)) {
    waitUntil(Promise.allSettled([
      sms(env, caller, `Hi, this is ${BIZ}. Sorry we missed your call. How can we help? Reply here or request a free quote at ${SITE}/contact/ . Reply STOP to opt out.`),
      sms(env, owner(env), `Missed call from ${caller}. Auto-text sent. To reply from the business number, text: ${caller.slice(2)} your message`),
      mailOwner(env, `Missed call: ${caller}`, `Missed call from ${caller} at ${new Date().toLocaleString("en-US", { timeZone: "America/New_York" })}.\nThe caller was sent the missed-call text. Any voicemail will follow in a separate email.`)
    ]));
  }
  return xml(`<Say voice="Polly.Matthew">Thanks for calling ${BIZ}. We're on a job right now. Please leave your name, number and a short message after the tone, and we'll call you back.</Say>` +
    `<Record maxLength="120" playBeep="true" recordingStatusCallback="/api/voicemail" recordingStatusCallbackMethod="POST"/><Hangup/>`);
}
