import os, sys, json, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *
import towns

HERO = "68f3b5f3a144cd15d4ea493b"

# ---------- HOME ----------
cards = "".join(f'''<article class="card">{pic(s[3], s[4])}<div class="pad"><h3>{s[1]}</h3><p>{s[2]}</p><a class="more" href="/services/{s[0]}/">Learn More &rarr;</a></div></article>''' for s in SERVICES)
why = [("30+ Years Combined Experience", "Father and son team with decades of expertise in construction, renovation, and restoration."),
       ("Family Owned & Operated", "Personal service from start to finish. We're not a faceless corporation - you work directly with Mark and Dylan."),
       ("Licensed & Insured", "Fully licensed, bonded, and insured for your peace of mind and protection."),
       ("Quality You Can Trust", "We stand behind every job with a commitment to excellence and lasting results.")]
steps = [("Free Consultation", "We visit your property to understand your vision and needs"),
         ("Detailed Estimate", "Receive a comprehensive, transparent quote with no hidden costs"),
         ("Quality Execution", "Mark and Dylan personally oversee every aspect of your project"),
         ("Final Walkthrough", "We ensure every detail meets your expectations before completion")]
faqs = [("What types of projects does Reliant Consulting and Construction handle?", "Reliant Consulting and Construction provides full remodeling, renovation, and new construction services for both residential and commercial properties. Whether you are updating a kitchen or bathroom, expanding your space, or building a new home or office, our team delivers quality work from start to finish."),
        ("How long does a remodel or renovation take?", "Project timelines vary based on size and scope, but many bathroom remodels are completed in about four weeks. Larger renovations and new builds may take longer. Mark and Dylan provide a clear schedule before work begins so you always know what to expect."),
        ("Do you offer free estimates?", "Yes. Reliant Consulting and Construction provides free, detailed estimates for all remodeling and construction projects. We take the time to understand your goals, explain your options, and outline costs upfront so there are no surprises later."),
        ("What areas do you serve?", "Reliant Consulting and Construction proudly serves Jasper, Ball Ground, Marietta, Alpharetta, and surrounding North Georgia communities. If you are unsure whether your area is covered, contact our team and we will be happy to help.")]

def faq_html(items):
    return "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in items)

def faq_ld(items):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}

body = f'''
<section class="hero" style="background-image:url(/img/{HERO}.webp)"><div class="wrap">
<p class="eyebrow">Construction and Remodeling in Jasper, Georgia</p>
<h1>Quality Construction and Remodeling Work By Local Professionals</h1>
<p>Reliant Consulting and Construction is your trusted local contractor for all your remodeling and construction needs. As a family-owned and operated business, we take pride in serving North Georgia with honesty, quality workmanship, and reliable service. When you need a contractor you can count on, contact Reliant Consulting and Construction and experience the difference personal attention makes.</p>
<div class="cta-row"><a class="btn" href="/contact/">Get Free Estimate</a><a class="btn ghost" href="/services/">View Our Services</a></div>
<p style="margin-top:22px">Call Us Today: <a style="color:#e3c176;font-weight:700" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></p>
</div></section>
<section><div class="wrap">
<div class="center"><h2>Our Services</h2><p class="lead">Comprehensive construction solutions for residential and commercial projects across North Georgia</p></div>
<div class="grid g3" style="margin-top:30px">{cards}</div></div></section>
<section class="alt"><div class="wrap split"><div>
<p class="eyebrow" style="color:#8a6a1f">Reliant Consulting and Construction</p><h2>A father-and-son team serving North Georgia</h2>
<p>Reliant Consulting and Construction is a father-and-son team serving North Georgia with honest construction, expert renovations, and reliable restoration services. With over 30 years of combined experience, we treat every project as if it were our own home.</p>
<div class="stats"><div><b>30+</b>years combined experience</div><div><b>25959</b>Georgia license no.</div></div>
<div class="cta-row"><a class="btn dark" href="/about/">About Us</a></div></div>
{pic("68f2cef05675712fea75362a","Contractor using a laser level to check a room during construction")}</div></section>
<section class="dark"><div class="wrap"><div class="center"><h2>Why Choose Reliant?</h2><p class="lead" style="color:#b9b6ad">When you choose Reliant, you're choosing a partner who cares about doing things right</p></div>
<div class="grid g4" style="margin-top:30px">{"".join(f'<div class="feat"><h3>{t}</h3><p>{d}</p></div>' for t,d in why)}</div></div></section>
<section><div class="wrap"><div class="center"><h2>Recent Work</h2><p class="lead">A few finished projects from homes across North Georgia.</p></div>
<div class="grid g4" style="margin-top:26px">
{pic("68f43c75722f75066b51c1f8","Finished modern kitchen with white cabinetry, large island and stainless steel appliances","card")}
{pic("68f428108e5daa7de496a6db","Finished bathroom with large walk-in shower, gold fixtures and white tile","card")}
{pic("68f3b5e74a04cbe2cc1b1048","Finished retaining wall and terraced lawn with backyard patio","card")}
{pic("68fba25445057e121aa79020","Finished rustic living room with fireplace, leather seating and large windows","card")}
</div><p class="center" style="margin-top:24px"><a class="btn dark" href="/projects/">See all projects</a></p></div></section>
<section><div class="wrap" data-greviews data-max="3"></div></section>
<section class="alt"><div class="wrap"><div class="center"><h2>How We Work</h2><p class="lead">Transform your space with expert craftsmanship</p></div>
<div class="grid g4" style="margin-top:30px">{"".join(f'<div class="feat"><div class="num">{i+1}</div><h3>{t}</h3><p>{d}</p></div>' for i,(t,d) in enumerate(steps))}</div></div></section>
<section><div class="wrap" style="max-width:860px"><h2 class="center">Frequently Asked Questions About Our Services in Jasper</h2>
<p class="lead center">When it comes to your home or business, we know how important it is to feel confident in who you hire. That is why our team is always ready to answer your questions and explain every step of the process.</p>
<div style="margin-top:26px">{faq_html(faqs)}</div></div></section>
<section class="alt"><div class="wrap contact-grid"><div><h2>Ready to Get Started?</h2><p class="lead">Contact us today for a free estimate. Mark and Dylan will personally meet with you to discuss your project.</p>
<ul class="ticks"><li>Free, detailed estimates</li><li>Licensed &amp; insured (License {LICENSE})</li><li>Serving Jasper, Marietta, Ball Ground, Alpharetta and nearby</li></ul>
<p><a class="btn" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a></p></div>{form("q-home")}</div></section>'''
page("/", "Reliant Consulting and Construction | Jasper, GA Remodeling",
     "Family-owned Jasper, GA contractor: construction, kitchen and bathroom remodels, fire, water and storm restoration. Licensed & insured. Call (770) 508-0971.",
     body, cur="/", extra_ld=[faq_ld(faqs)], preload=f"/img/{HERO}.webp")

# ---------- SERVICES ----------
body = hero("Our Services", "Reliant Consulting and Construction is your single local team for construction, renovation and restoration across North Georgia.") + f'''
<section><div class="wrap"><div class="grid g3">{cards}</div></div></section>
<section class="alt"><div class="wrap center"><h2>Serving North Georgia</h2><p class="lead">Including Jasper, Marietta, Ball Ground, Alpharetta, Cumming, Canton, Woodstock, Roswell, and surrounding communities</p>
<div class="cta-row" style="justify-content:center"><a class="btn dark" href="/service-areas/">See service areas</a></div></div></section>''' + cta_band()
page("/services/", "Our Services | Reliant Consulting and Construction",
     "General construction, renovations and remodels, and restoration services from a family-owned Jasper, GA contractor. Licensed & insured. Free estimates.", body, cur="services")

def svc_page(slug, title, intro, blocks, gallery, extra_h=""):
    crumbs = '<div class="crumbs"><a href="/">Home</a> / <a href="/services/">Services</a></div>'
    body = hero(title, intro, crumbs) + extra_h + f'''<section class="alt"><div class="wrap"><h2>{title} Gallery</h2><div class="gallery" style="margin-top:20px">{gallery}</div>
<p style="margin-top:14px"><a href="/projects/">View more projects &rarr;</a></p></div></section>''' + cta_band()
    return body

def fig(n, alt, cat="all"):
    return f'<figure data-c="{cat}">{pic(n, alt)}</figure>'

# general construction
gc = [("Framing & Structural Work", "Expert framing for new construction, additions, and structural modifications. We ensure every frame is square, level, and built to code."),
      ("Drywall Installation & Finishing", "Professional drywall hanging, taping, mudding, and finishing. Smooth walls ready for paint or texture."),
      ("Concrete & Foundation Work", "Solid foundations, slabs, driveways, and concrete pads built to last. Proper preparation and finishing for durability."),
      ("Roofing Installation & Repair", "Complete roofing services, including installation, repair, and replacement. We work with asphalt shingles, metal roofing, and more."),
      ("Deck & Patio Construction", "Custom decks and patios that extend your living space outdoors. Quality materials and craftsmanship for years of enjoyment."),
      ("Garage Construction", "Detached and attached garage construction. From foundation to roofing, we handle every aspect of your garage project."),
      ("Home Additions", "Expand your living space with a professionally built addition that seamlessly matches your existing home."),
      ("New Construction Projects", "Ground-up construction for residential properties. We manage every phase from permits to final inspection.")]
g = "".join([fig("68f428108e5daafa4596a6d9", "Professionally poured concrete driveway in a wooded residential setting"),
    fig("68f428101e167416f0edd38d", "Finished asphalt driveway with concrete curb"),
    fig("68f3b5e74a04cbe2cc1b1048", "Finished retaining wall and terraced lawn with patio"),
    fig("68fcf6eed672b4c0f9c32cf4", "Pavilion with wrap-around porch and stone accents"),
    fig("68f428106a7dfa7e5af7cf7d", "Framed interior walls with insulation before finishing"),
    fig("68f428101e167434c5edd38e", "Unfinished drywall stage during construction")])
body = svc_page("general-construction", "General Construction", "Mark and Dylan bring over 30 years of combined experience to every construction project, ensuring quality workmanship from start to finish.", None, g,
    extra_h=f'<section><div class="wrap"><h2>Our Construction Services</h2><div class="grid g4" style="margin-top:24px">{"".join(f"<div class=feat><h3>{t}</h3><p>{d}</p></div>" for t,d in gc)}</div></div></section>')
page("/services/general-construction/", "General Construction | Reliant Consulting and Construction",
     "Framing, drywall, concrete and foundations, roofing, decks, garages, additions and new construction in Jasper, GA and North Georgia. Family owned, licensed & insured.", body, cur="general-construction", og_img="68f428108e5daafa4596a6d9")

# renovations
rn = ["Kitchen Remodels", "Bathroom Remodels", "Basement Finishing", "Whole-Home Renovations", "Room Additions", "Interior Remodeling", "Framing and Structural Work", "Custom Cabinetry and Fixtures", "Flooring Installation"]
rsteps = [("Initial Consultation", "We meet with you to discuss your vision, budget, and timeline. We'll assess the space and provide expert recommendations."),
          ("Design & Planning", "Detailed plans and material selections are finalized. We handle permits and coordinate with any necessary specialists."),
          ("Renovation Execution", "Mark and Dylan personally oversee all work, maintaining clean job sites and keeping you informed every step of the way."),
          ("Final Walkthrough", "We ensure every detail meets your expectations before considering the project complete. Your satisfaction is our priority.")]
g = "".join([fig("68f67ba318c4204457427f58", "Finished kitchen renovation with white cabinetry and large island"),
    fig("68f2cd7074ee542470b85f68", "Finished white kitchen with a live-edge wood island countertop"),
    fig("68fba254409d6af8e1fc3152", "Kitchen remodel with marble-topped island and rustic wood cabinetry"),
    fig("68f3b5f3a144cd15d4ea493b", "Walk-in shower with white marble walls and gold fixtures"),
    fig("68f3b5f3faf82b7e98d370be", "Bathroom remodel with walk-in shower and glass doors"),
    fig("68f2cba7175e598b489657ed", "Bathroom with custom stone vanity and vessel sink"),
    fig("68f3b5f36edd49724407a5b2", "Finished home theater with large screen and media console"),
    fig("68fba25445057e121aa79020", "Rustic living room with fireplace and leather seating")])
body = svc_page("renovations-and-remodels", "Renovations and Remodels", "Transform your space with expert kitchen, bathroom, and whole-home renovations. A proven process that ensures quality results and clear communication from start to finish.", None, g,
    extra_h=f'''<section><div class="wrap split"><div><h2>Renovation Services</h2><ul class="ticks">{"".join(f"<li>{x}</li>" for x in rn)}</ul></div>{pic("68f43c75722f75066b51c1f8","Finished modern kitchen remodel by Reliant Consulting and Construction")}</div></section>
<section class="dark"><div class="wrap"><div class="center"><h2>Our Renovation Process</h2><p class="lead" style="color:#b9b6ad">A proven process that ensures quality results and clear communication from start to finish</p></div>
<div class="grid g4" style="margin-top:28px">{"".join(f'<div class="feat"><div class="num">{i+1}</div><h3>{t}</h3><p>{d}</p></div>' for i,(t,d) in enumerate(rsteps))}</div></div></section>''')
page("/services/renovations-and-remodels/", "Remodeling | Reliant Consulting and Construction",
     "Kitchen remodels, bathroom remodels, basement finishing and whole-home renovations in Jasper, GA and North Georgia. Family owned, licensed & insured. Free estimates.", body, cur="renovations-and-remodels", og_img="68f67ba318c4204457427f58")

# restoration
rs = [("Fire Damage Restoration", "Complete fire damage restoration, including smoke and soot removal, odor elimination, and rebuilding services.", ["Smoke and soot removal", "Structural assessment", "Full reconstruction", "Insurance coordination"]),
      ("Storm Damage Repair", "Expert storm damage repair, including roof repairs, structural fixes, and complete property restoration.", ["Roof repair and replacement", "Structural repairs", "Debris removal and reconstruction", "Insurance claim support"]),
      ("Water Damage Restoration", "Fast response to water damage from burst pipes, flooding, or leaks. We extract water, dry structures, and restore your property.", ["Mold prevention", "Complete restoration", "Water extraction and removal", "Insurance documentation"])]
g = "".join([fig("68fba25b304c6e84668ad33b", "Fire damaged home structure before restoration"),
    fig("68fcf6ee295ec0813d5c7876", "Property overgrown with heavy branches and debris before cleanup"),
    fig("68fba25444eecb4fd3b2875b", "Before and after photos of a full interior demolition and renovation")])
body = svc_page("restoration-services", "Restoration Services", "Water, fire, and storm damage restoration with full insurance support. We help you recover quickly and rebuild better than before.", None, g,
    extra_h=f'''<section><div class="wrap"><div class="grid g3">{"".join(f'<div class="feat"><h3>{t}</h3><p>{d}</p><ul class="ticks" style="margin-top:12px">{"".join(f"<li>{x}</li>" for x in l)}</ul></div>' for t,d,l in rs)}</div></div></section>''')
page("/services/restoration-services/", "Restoration | Reliant Consulting and Construction",
     "Fire, water and storm damage restoration with insurance support in Jasper, GA and North Georgia. Family owned, licensed & insured. Call (770) 508-0971.", body, cur="restoration-services", og_img="68fba25b304c6e84668ad33b")

# ---------- ABOUT ----------
vals = [("Quality Work", "We never cut corners. Every project is built to the highest standards with attention to detail and lasting craftsmanship."),
        ("Honest Communication", "Clear, upfront communication from start to finish. No surprises, no hidden fees - just honest conversation about your project."),
        ("Local Experience", "Over 30 years serving North Georgia families. We know the area, understand local building codes, and stand by our work."),
        ("Licensed and Insured", "Fully licensed and insured for your protection and peace of mind on every job, big or small."),
        ("Upfront and Fair Pricing", "Transparent pricing with no hidden costs. We provide detailed estimates so you know exactly what to expect.")]
body = hero("About Reliant Consulting and Construction", "30+ years of combined experience. Father and son, Mark and Dylan.", '<div class="crumbs"><a href="/">Home</a> / About Us</div>') + f'''
<section><div class="wrap split"><div><h2>Our Story</h2>
<p>Reliant Consulting and Construction is a family-owned and operated company led by father and son, Mark and Dylan. With more than thirty years of combined experience, they bring true craftsmanship, care, and attention to detail to every project they touch. What began as Mark's vision has grown into a partnership built on doing things the right way the first time.</p>
<p>They are not a large corporate contractor. They are a small, hands-on team that takes the time to understand your goals, answer your questions, and make sure everything is completed with excellence. When you hire Reliant, you get Mark and Dylan on your job site - not a rotation of subcontractors you have never met.</p>
<p>From interior remodels and complete renovations to insurance restoration work, Reliant Consulting and Construction has helped families across North Georgia update, rebuild, and restore their homes. Their reputation is built on honesty, reliability, and lasting quality.</p>
<p>For Mark and Dylan, building is more than work. It is their passion and their family name on every project. They don't just transform spaces - they build trust, one home at a time.</p></div>
{pic("68f2cef05675712fea75362a","Contractor using a laser level to check a room during construction")}</div></section>
<section class="alt"><div class="wrap"><div class="center"><h2>Our Values at Reliant Consulting and Construction</h2></div><div class="grid g3" style="margin-top:26px">{"".join(f"<div class=feat><h3>{t}</h3><p>{d}</p></div>" for t,d in vals)}</div></div></section>
<section><div class="wrap"><div class="center"><h2>How We Work</h2><p class="lead">Transform your space with expert craftsmanship</p></div><div class="grid g4" style="margin-top:28px">{"".join(f'<div class="feat"><div class="num">{i+1}</div><h3>{t}</h3><p>{d}</p></div>' for i,(t,d) in enumerate(steps))}</div></div></section>''' + cta_band()
page("/about/", "About Us | Reliant Consulting and Construction",
     "Meet Mark and Dylan, the father-and-son team behind Reliant Consulting and Construction. 30+ years of combined experience across North Georgia.", body, cur="about", og_img="68f2cef05675712fea75362a")

# ---------- PROJECTS ----------
G = [("kitchens", "Kitchen Remodels", [("68f43c75722f75066b51c1f8", "Kitchen remodel with white cabinetry and large island"), ("68f67ba318c4204457427f58", "Kitchen renovation with large island and high-end appliances"), ("68f67ba3c1945b376eb3be1a", "Kitchen renovation with granite island and wood cabinetry"), ("68fba254409d6af8e1fc3152", "Kitchen with marble-topped island and rustic cabinets"), ("68f2cd7074ee542470b85f68", "White kitchen with live-edge wood island"), ("68f3b5e7a144cdf698ea47f6", "Modern kitchen with white cabinetry and live-edge island"), ("68fba25444eecb3ee0b2875a", "Open-concept kitchen and dining area")]),
     ("baths", "Bathroom Remodels", [("68f3b5f3a144cd15d4ea493b", "Walk-in shower with white marble and gold fixtures"), ("68f3b5f3a144cd526bea4938", "Bathroom with white marble tile and built-in niches"), ("68f3b5f3a144cde8bdea4939", "Bathroom with pedestal sink and modern tub"), ("68f3b5f3faf82b616ad370b5", "Bathroom with grey walls and wood-look flooring"), ("68f3b5f3faf82b7e98d370be", "Bathroom with walk-in shower and glass doors"), ("68f428108e5daa7de496a6db", "Bathroom with large walk-in shower and gold fixtures"), ("68f2cba7175e598b489657ed", "Bathroom with custom stone vanity and vessel sink"), ("68f3b5e7faf82b6e89d36f4a", "Double vanity with marble countertop and olive-green cabinets")]),
     ("outdoor", "Outdoor & Concrete", [("68f428101e167416f0edd38d", "New asphalt driveway with concrete curb"), ("68f428107b55a73ace9a15f2", "Asphalt driveway installation with landscaping"), ("68f428108e5daafa4596a6d9", "Poured concrete driveway in a wooded setting"), ("68f3b5e74a04cbe2cc1b1048", "Retaining wall and terraced lawn with patio and gazebo"), ("68fcf6eed672b4c0f9c32cf4", "Pavilion with wrap-around porch and stone accents")]),
     ("interiors", "Interiors", [("68f3b5f36edd49724407a5b2", "Home theater with large screen and media console"), ("68fba25445057e121aa79020", "Living room with fireplace and leather seating")]),
     ("progress", "Before & In Progress", [("68fba25444eecb4fd3b2875b", "Before and after of a full interior demolition and renovation"), ("68fba25454fb620f47717c27", "Kitchen before and after transformation"), ("68fcd917afcd21b82ad16277", "Kitchen and living area before and after"), ("68f3b5f3a144cd3bd2ea4933", "Basement before renovation"), ("68f3b5f37b55a744158354d6", "Bathroom renovation underway"), ("68f3b5f36edd49773107a5af", "Bathroom renovation in progress"), ("68f3b5f34a04cbb8ec1b11be", "Room under renovation with exposed framing"), ("68f428106a7dfa7e5af7cf7d", "Framed walls with insulation"), ("68f428101e167434c5edd38e", "Drywall stage"), ("68f42810722f7513ef4fb7a7", "Driveway and patio before replacement"), ("68f43e5b8e5daafcee98d6ea", "Basement before finishing"), ("68fba25ad9a00deea85cf712", "Interior demolition before renovation"), ("69124294b0326a460958b783", "Open living area before renovation")])]
filters = '<button aria-pressed="true" data-f="all">All</button>' + "".join(f'<button aria-pressed="false" data-f="{k}">{n}</button>' for k, n, _ in G)
figs = "".join(f'<figure data-c="{k}">{pic(n, a)}<figcaption>{t}</figcaption></figure>' for k, t, items in G for n, a in items)
body = hero("Our Projects", "Real projects from real homeowners across North Georgia.", '<div class="crumbs"><a href="/">Home</a> / Projects</div>') + f'''
<section><div class="wrap"><div class="filters" role="group" aria-label="Filter projects">{filters}</div><div class="gallery">{figs}</div></div></section>''' + cta_band("Ready to Start Your Project?", "Let's create something beautiful together. Contact us for a free consultation.")
page("/projects/", "Projects & Photo Gallery | Reliant Consulting and Construction",
     "See finished kitchen and bathroom remodels, concrete and driveways, and renovation projects by Reliant Consulting and Construction across North Georgia.", body, cur="projects", og_img="68f43c75722f75066b51c1f8")

# ---------- REVIEWS ----------
rev_cards = "".join(f'<div class="feat"><p>&ldquo;{r["text"]}&rdquo;</p><p><b>{r["name"]}</b>{", " + r["town"] if r.get("town") else ""}</p></div>' for r in REVIEWS)
rev_block = f'<section><div class="wrap"><h2 class="center">What Our Customers Say</h2><div class="grid g3" style="margin-top:24px">{rev_cards}</div></div></section>' if REVIEWS else ""
gbtn = f'<p><a class="btn" href="{GOOGLE_REVIEWS_URL}" rel="noopener">Read our Google reviews</a></p>' if GOOGLE_REVIEWS_URL else ""
promise = [("Transparent Estimates", "At Reliant Consulting and Construction, you will always know what to expect before work begins. We provide clear, detailed estimates with no hidden costs. Every step of your project is explained so you can make confident decisions and stay within your budget while receiving quality craftsmanship you can trust."),
           ("Respect for Every Space", "We believe in treating your property with the same care we would our own. From the first visit to the final cleanup, our team keeps your home or business protected, organized, and safe. As a fully licensed and insured company, your project is always in reliable hands."),
           ("The Reliant Promise", "We understand that construction and remodeling can feel stressful. That is why Mark and Dylan stand behind every project they complete. If something is not up to our standards, we make it right. You can count on our family to deliver results built on integrity, skill, and lasting trust.")]
body = hero("Customer Reviews", "Built on trust and quality. Tell us about your next project and let our team help bring it to life.", '<div class="crumbs"><a href="/">Home</a> / Reviews</div>') + rev_block + '<section><div class="wrap"><h2 class="center">What Our Customers Say on Google</h2><div data-greviews data-max="12" style="margin-top:12px"></div></div></section>' + f'''
<section class="alt"><div class="wrap"><div class="center"><h2>Why Choose Us?</h2>{gbtn}</div><div class="grid g3" style="margin-top:24px">{"".join(f"<div class=feat><h3>{t}</h3><p>{d}</p></div>" for t,d in promise)}</div></div></section>
<section><div class="wrap"><div class="center"><h2>Our Projects</h2><p class="lead">Take a look at some of our recent projects and see the quality and care that go into every build and remodel.</p></div>
<div class="grid g4" style="margin-top:24px">
<a href="/projects/">{pic("68f67ba3c1945b376eb3be1a","Kitchen remodel",'card')}<h3 style="margin-top:8px">Kitchen Remodel</h3></a>
<a href="/projects/">{pic("68f3b5f3a144cd3bd2ea4933","Basement renovation",'card')}<h3 style="margin-top:8px">Finishing Basement</h3></a>
<a href="/projects/">{pic("68f428101e167416f0edd38d","Driveway",'card')}<h3 style="margin-top:8px">Driveway</h3></a>
<a href="/projects/">{pic("68f3b5f3faf82b7e98d370be","Bathroom remodel",'card')}<h3 style="margin-top:8px">Bathroom Remodels</h3></a></div></div></section>''' + cta_band("Built on Trust and Quality", "Tell us about your next project and let our team help bring it to life.")
page("/reviews/", "Customer Reviews | Reliant Consulting and Construction",
     "Why North Georgia homeowners trust Reliant Consulting and Construction: transparent estimates, respect for your space, and a promise to make it right.", body, cur="reviews")

# ---------- FAQ ----------
body = hero("Frequently Asked Questions", "Straight answers about working with Reliant Consulting and Construction.", '<div class="crumbs"><a href="/">Home</a> / FAQ</div>') + f'<section><div class="wrap" style="max-width:860px">{faq_html(faqs)}</div></section>' + cta_band("Still have a question?", "Call or send us a message. Mark and Dylan are happy to help.")
page("/faq/", "FAQ | Reliant Consulting and Construction",
     "How long does a remodel take? Do you offer free estimates? What areas do you serve? Answers from Reliant Consulting and Construction in Jasper, GA.", body, cur="faq", extra_ld=[faq_ld(faqs)])

# ---------- CONTACT ----------
body = hero("Contact Us", "Request a free estimate. Mark and Dylan will personally meet with you to discuss your project.", '<div class="crumbs"><a href="/">Home</a> / Contact</div>') + f'''
<section><div class="wrap contact-grid"><div><h2>Let's talk about your project</h2>
<p class="lead">Call, or send the form and we will call you back.</p>
<p style="font-size:1.4rem"><a href="tel:{PHONE_TEL}"><b>{PHONE_DISPLAY}</b></a></p>
<ul class="ticks"><li>Free, detailed estimates</li><li>Licensed &amp; insured (License {LICENSE})</li><li>Serving Jasper, Marietta, Ball Ground, Alpharetta and surrounding North Georgia</li></ul></div>{form("q-contact")}</div></section>'''
page("/contact/", "Contact Us | Reliant Consulting and Construction",
     "Request a free estimate from Reliant Consulting and Construction. Call (770) 508-0971 or send a message. Serving Jasper, Marietta, Ball Ground, Alpharetta and North Georgia.", body, cur="contact")

# ---------- PRIVACY ----------
body = hero("Privacy", "How we handle what you send us.") + f'''<section><div class="wrap" style="max-width:760px"><p>When you submit the quote form we receive your name, phone, email, address and project details. We use them only to contact you about your project. We do not sell or share them. This site uses no advertising trackers. To have your details removed, call <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>.</p></div></section>'''
page("/privacy/", "Privacy | Reliant Consulting and Construction", "How Reliant Consulting and Construction handles information you send through the quote form.", body)

# ---------- TOWNS ----------
towns.build(page, hero, pic, cta_band, form, faq_html, faq_ld, SERVICES)

# ---------- 404 ----------
body = hero("Page not found", "Sorry, we couldn't find that page.") + '<section><div class="wrap center"><a class="btn" href="/">Back to home</a></div></section>'
page("/404/", "Page not found | Reliant Consulting and Construction", "Sorry, that page could not be found. Visit the Reliant Consulting and Construction home page or call (770) 508-0971 for help.", body)
os.replace(os.path.join(OUT, "404", "index.html"), os.path.join(OUT, "404.html")); os.rmdir(os.path.join(OUT, "404")); PAGES.remove("/404/")

# ---------- sitemap, robots, redirects, headers ----------
import datetime
today = datetime.date.today().isoformat()
open(os.path.join(OUT, "sitemap.xml"), "w").write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + "".join(f"<url><loc>{DOMAIN}{p}</loc><lastmod>{today}</lastmod></url>" for p in PAGES if p != "/privacy/") + "</urlset>")
open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")
open(os.path.join(OUT, "_redirects"), "w").write("""/generalconstruction /services/general-construction/ 301
/renovationsandremodels /services/renovations-and-remodels/ 301
/restorationservices /services/restoration-services/ 301
/aboutus /about/ 301
/blog /about/ 301
/Jasper /service-areas/jasper/ 301
/jasper /service-areas/jasper/ 301
/service-area-1 /service-areas/jasper/ 301
/service-area-2 /service-areas/marietta/ 301
/service-area-3 /service-areas/ball-ground/ 301
/contact-us /contact/ 301
""")
open(os.path.join(OUT, "_headers"), "w").write("""/*
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  X-Frame-Options: SAMEORIGIN
  Permissions-Policy: camera=(), microphone=(), geolocation=(), payment=(), usb=()
  Strict-Transport-Security: max-age=31536000; includeSubDomains
  Cross-Origin-Opener-Policy: same-origin
  Content-Security-Policy: default-src 'self'; img-src 'self' data: https://*.googleusercontent.com; style-src 'self' 'unsafe-inline'; script-src 'self'; connect-src 'self'; form-action 'self'; frame-ancestors 'self'; base-uri 'self'; object-src 'none'
/img/*
  Cache-Control: public, max-age=31536000, immutable
/css/*
  Cache-Control: public, max-age=86400
/js/*
  Cache-Control: public, max-age=86400
""")
print("built", len(PAGES), "pages")
