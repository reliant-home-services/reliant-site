# Phone + text replacement for GoHighLevel (built Nov 11, 2026)

Code is live but switched OFF until a Twilio number is connected. Nothing here costs money until Twilio is set up.

## What it does (once on)
- Call to the business number -> rings Dylan's cell for 20 s, showing the customer's number.
- Missed call -> customer gets: "Hi, this is Reliant Consulting and Construction. Sorry we missed your call..." + voicemail recorded.
  Dylan gets a text + email (and a second one with the voicemail link).
- Customer texts the business number -> forwarded to Dylan's cell + email.
- Dylan replies FROM the business number by texting it:  7705551234 your message
- Quote form -> email to reliantcandc@gmail.com (live now), thank-you email to customer (live now),
  text alert to Dylan, and a text to the customer only if they ticked the opt-in box.

## Files
functions/api/lead.js (form), voice.js, voice-done.js, voicemail.js, sms.js; shared code lib/twilio.js.
All Twilio requests are signature-checked (unsigned requests get 403).

## Turn it on
1. Twilio account (Dylan, needs a card). Upgrade from trial.
2. Get the number into Twilio:
   - Keep (770) 508-0971: if it is a GoHighLevel/LC Phone number, the GHL account owner asks HighLevel Support for an
     "LC Phone -> Twilio" migration with our Twilio Account SID. Do NOT cancel GHL before the move is confirmed.
   - Or buy a new local number ($1.15/mo) and later port.
3. A2P 10DLC registration in Twilio (required to text US phones): Low-Volume Standard brand + "Customer Care"/"Mixed" campaign.
   Opt-in proof for reviewers: the checkbox on /contact/ and the SMS paragraph on /privacy/.
4. Number settings in Twilio:
   Voice "A call comes in" -> Webhook POST https://reliantconsultingandconstruction.com/api/voice
   Messaging "A message comes in" -> Webhook POST https://reliantconsultingandconstruction.com/api/sms
5. Cloudflare Pages secrets: SMS_ENABLED=true, TWILIO_SID, TWILIO_TOKEN, TWILIO_FROM=+1..., OWNER_CELL=+1...
   then redeploy.
6. Test: call and don't answer; text the number; send the form with the box ticked.

Tip: if Dylan's cell voicemail picks up before 20 s, the system thinks the call was answered. Lower timeout in voice.js.
