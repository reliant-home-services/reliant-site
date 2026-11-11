// Texts to the business number.
//  - From a customer: forwarded to the owner's cell (and email).
//  - From the owner's cell, starting with a 10-digit number: sent to that customer FROM the business number.
//    Example:  7705551234 Hi, we can come out Thursday at 10.
// STOP/HELP are handled by Twilio automatically.
// Twilio number > Messaging > "A message comes in" = Webhook POST https://<site>/api/sms
import { twilioParams, owner, xml, sms, mailOwner, e164 } from "../../lib/twilio.js";

export async function onRequestPost({ request, env, waitUntil }) {
  const p = await twilioParams(request, env);
  if (!p) return new Response("Forbidden", { status: 403 });
  const from = e164(p.From), body = String(p.Body || "").trim(), cell = owner(env);

  if (from && from === cell) {
    const m = body.match(/^\+?1?[\s.-]*\(?(\d{3})\)?[\s.-]*(\d{3})[\s.-]*(\d{4})\s+([\s\S]+)$/);
    if (!m) return xml(`<Message>To text a customer from the business line, start with their number: 7705551234 your message</Message>`);
    const to = "+1" + m[1] + m[2] + m[3];
    const ok = await sms(env, to, m[4]);
    return xml(`<Message>${ok ? "Sent to " + to : "Could not send to " + to + ". Check the number."}</Message>`);
  }

  const media = Number(p.NumMedia || 0) ? `\n(${p.NumMedia} photo(s): ${p.MediaUrl0 || ""})` : "";
  waitUntil(Promise.allSettled([
    sms(env, cell, `Text from ${from || p.From}: ${body}${media}\n\nReply: ${(from || "").slice(2)} your message`),
    mailOwner(env, `Text from ${from || p.From}`, `${body}${media}`)
  ]));
  return xml("");
}
