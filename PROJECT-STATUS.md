# Reliant site: status (Nov 8, 2026)
Done: GoDaddy signed in (Dylan); DNS inspected; original pages saved in _orig; 15 page texts in content/; 46 original photos in assets/img (35 MB, to be converted to WebP).
Original pages: home, services, generalconstruction, renovationsandremodels, restorationservices, aboutus, blog, service-area-1/2/3 (Jasper/Marietta/Ball Ground), Jasper, reviews, projects, contact-us. Phone (770) 508-0971. License 25959.
Next: GitHub + Cloudflare accounts (Dylan creates), build static site, lead Worker, test on pages.dev, DNS switch only with Dylan's OK.
Stack: static HTML/CSS, Cloudflare Pages (free), GitHub, Cloudflare Worker for form -> Gmail + phone push.

Nov 8 eve: pushed to GitHub reliant-home-services/reliant-site. wrangler logged in. Deployed to Cloudflare Pages project reliant-site (https://reliant-site.pages.dev) via 'npx wrangler pages deploy site --project-name reliant-site --branch main'. Pages/forms respond OK. TODO: Resend key secret for lead worker, connect GitHub auto-deploy, DNS switch only with Dylan OK.
