// Incoming call to the business number: ring the owner's cell for 20 s, showing the caller's number.
// Twilio number > Voice > "A call comes in" = Webhook POST https://<site>/api/voice
import { twilioParams, owner, xml, escX } from "../../lib/twilio.js";

export async function onRequestPost({ request, env }) {
  const p = await twilioParams(request, env);
  if (!p) return new Response("Forbidden", { status: 403 });
  const cell = owner(env);
  if (!cell) return xml(`<Redirect method="POST">/api/voice-done</Redirect>`);
  return xml(`<Dial timeout="20" answerOnBridge="true" callerId="${escX(p.From || env.TWILIO_FROM)}" action="/api/voice-done" method="POST"><Number>${escX(cell)}</Number></Dial>`);
}
