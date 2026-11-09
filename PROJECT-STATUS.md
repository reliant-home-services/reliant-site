# Reliant site: status (Nov 8, 2026)
Done: GoDaddy signed in (Dylan); DNS inspected; original pages saved in _orig; 15 page texts in content/; 46 original photos in assets/img (35 MB, to be converted to WebP).
Original pages: home, services, generalconstruction, renovationsandremodels, restorationservices, aboutus, blog, service-area-1/2/3 (Jasper/Marietta/Ball Ground), Jasper, reviews, projects, contact-us. Phone (770) 508-0971. License 25959.
Next: GitHub + Cloudflare accounts (Dylan creates), build static site, lead Worker, test on pages.dev, DNS switch only with Dylan's OK.
Stack: static HTML/CSS, Cloudflare Pages (free), GitHub, Cloudflare Worker for form -> Gmail + phone push.

Nov 8 eve: pushed to GitHub reliant-home-services/reliant-site. wrangler logged in. Deployed to Cloudflare Pages project reliant-site (https://reliant-site.pages.dev) via 'npx wrangler pages deploy site --project-name reliant-site --branch main'. Pages/forms respond OK. TODO: Resend key secret for lead worker, connect GitHub auto-deploy, DNS switch only with Dylan OK.

Nov 8 night: Google Cloud project 'My First Project' (account authuser=1) has Places API (New) enabled + key 'Maps Platform API Key' stored as Pages secret GOOGLE_PLACES_KEY. functions/api/reviews.js deployed (REVIEWS_SOURCE=places default; switch to gbp by one variable; optional REVIEWS_KV to keep all reviews). Widget on home + reviews page hides itself until data. BLOCKED: listing not found by Places search; need Dylan's Google Maps link/Place ID -> set Pages variable PLACE_ID (+ GOOGLE_REVIEWS_URL). TODO: restrict key to Places API (New) only, quota cap, $1 budget alert, GBP access request (Option B), KV for accumulation.
