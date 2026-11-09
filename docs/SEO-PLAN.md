# SEO plan: Reliant (written Nov 9, 2026)

## What is already built (checked by tools/check.py: ALL CLEAR on 17 pages)
- Unique title + description + canonical on every page; one H1; alt text on every photo; WebP images.
- Sitemap + robots.txt; old GoHighLevel URLs 301-redirect to the new ones (/aboutus, /service-area-1 ...).
- Structured data: local business (with link to the Google listing), FAQ, services.
- Security headers (CSP, HSTS, no framing). Test address *.pages.dev is set to noindex so it never competes.
- Google reviews widget (5.0, 11 reviews) pulled live from Google; /review short link sends customers straight to the
  Google "write a review" box (reliantconsultingandconstruction.com/review).

## GO-LIVE RUNBOOK (do in this order, only after Dylan says go)
1. **Before touching DNS**: list every GoDaddy DNS record (MX, TXT, CNAME). GoHighLevel may use some for email/text
   replies. Keep those. Do NOT cancel GoHighLevel until texts + call patch-through have replacements.
2. Add custom domain in Cloudflare Pages (reliant-site project): apex + www. Point DNS (easiest: move nameservers to
   Cloudflare, free; otherwise CNAME at GoDaddy). Keep MX/TXT records unchanged.
3. Test: home, a town page, a service page, the quote form (lead email arrives), /review link, phone link, old URLs redirect.
4. Google Search Console: add the domain property, verify with a DNS TXT record, submit /sitemap.xml, request indexing of Home.
5. Bing Webmaster Tools: "Import from Google Search Console" (one click), submit sitemap. Also Bing Places (see GBP checklist).
6. Resend: verify reliantconsultingandconstruction.com (3 DNS records). Then leads come from a branded address and the
   customer gets an automatic "we got your request" email.
7. Cloudflare Web Analytics (free, no cookies): turn on, then allow its script in the CSP header (site/_headers).
8. Google Business Profile: website field = the live domain; add UTM tag ?utm_source=gbp so you can see GBP clicks.
9. Old copies: reliantcandc.wordpress.com still shows in Google. Replace its content with a short page pointing to the
   new site, or delete it. (Two sites with the same text split your ranking.)

## Content roadmap (this is what actually moves rankings)
Priority 1: more town pages. The Google listing covers Canton, Jasper and 5 other areas, but the site has 4 towns
(Jasper, Marietta, Ball Ground, Alpharetta). Add Canton, Woodstock, Cumming, Roswell, Ellijay, Dawsonville (confirm which Dylan truly serves).
Priority 2: town x service pages ("Bathroom remodel in Marietta GA", "Water damage restoration in Ball Ground GA") with a real project
photo, a real price range, timeline, and a short local detail. One page per combination you really want jobs from.
Priority 3: project case studies (before/after, what was done, how long, rough cost). Use the real photos.
Priority 4: 1-2 helpful posts a month answering real questions ("How much does a bathroom remodel cost in North Georgia",
"Does homeowners insurance cover water damage"). Short, honest, local.
Keyword notes: I have not pulled search volumes yet (needs a keyword tool). Target pattern: "[service] [town] GA",
"[service] near me", "general contractor [town]". Google Search Console shows the real queries after ~2-4 weeks.

## Things that hurt SEO (avoid)
- Different business names across the web (see Google Business checklist: name consistency).
- Buying backlinks or fake reviews. Copying text between town pages (each page must be genuinely different).
- Big uncompressed photos, popups that cover the page on phones.

## Monthly 15-minute check (Dylan or Jarvis on request only)
Search Console: clicks, top queries, pages not indexed. Google Business: calls, direction requests, review count.
