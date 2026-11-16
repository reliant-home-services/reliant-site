"""Homeowner guides (articles), added Nov 16, 2026. Each entry builds /guides/<slug>/ and is listed on /guides/.
To add a guide: copy an entry in GUIDES, change the text, run: python tools/build.py
Rule: plain, honest and local. No invented prices or statistics. A section body is a list of paragraphs;
a paragraph that is itself a list becomes a bullet list."""
from config import *

GUIDES = [
 dict(slug="how-long-does-a-bathroom-remodel-take", date="2026-11-16", img="68f3b5f3faf82b7e98d370be",
   img_alt="Bathroom remodel with walk-in shower and glass doors",
   name="How Long Does a Bathroom Remodel Take?",
   title="Bathroom Remodel Timeline | Reliant Consulting and Construction",
   desc="Most of our bathroom remodels take about four weeks. See what happens in each phase and what makes a North Georgia bathroom remodel run longer.",
   intro="Many of the bathroom remodels we complete take about four weeks from demolition to final walkthrough. Here is where that time goes and what can stretch it.",
   service=("bathroom-remodeling", "bathroom remodeling"),
   sections=[
    ("The short answer", ["For a typical bathroom, plan on about four weeks of construction once work starts. A simple update with a new vanity, fixtures, flooring and paint is quicker. A large primary bathroom with a custom tile shower and plumbing moved to new locations takes longer.",
        "The planning that happens before the first day of work matters just as much. Choosing tile, fixtures and a vanity ahead of time is the single best way to keep a remodel on schedule."]),
    ("What happens in each phase", [["<b>Planning and selections.</b> We measure the room, agree on the layout and you choose materials. Anything with a long delivery time is ordered before work begins.",
        "<b>Demolition.</b> Old fixtures, tile and damaged drywall come out. This is when we find out what is behind the walls.",
        "<b>Rough-in work.</b> Framing changes, plumbing and electrical are done while the walls are open, followed by any required inspection.",
        "<b>Walls and waterproofing.</b> Backer board and drywall go up and the shower area is waterproofed.",
        "<b>Tile.</b> Floors, shower walls and niches are set and grouted. Tile needs time to cure before the next step, and it cannot be rushed.",
        "<b>Finish work.</b> Vanity, countertop, toilet, fixtures, glass, trim and paint.",
        "<b>Final walkthrough.</b> We go through the room with you and take care of anything that is not right."]]),
    ("What makes a bathroom remodel take longer", [["<b>Moving plumbing.</b> Relocating a toilet, shower or drain adds work under the floor.",
        "<b>Hidden water damage.</b> Rot around a tub or toilet is common in older bathrooms. It has to be repaired before new finishes go in.",
        "<b>Custom tile work.</b> Large showers, patterns and built-in niches take more time than a standard surround.",
        "<b>Special-order materials.</b> Custom vanities, glass and some tile have long lead times.",
        "<b>Changes after work starts.</b> Changing the plan mid-project usually means waiting on new materials."]]),
    ("How to keep your remodel on schedule", ["Make your selections early and stick with them. Ask your contractor for a written schedule before work begins, and ask which days the bathroom will be completely out of use so you can plan around it.",
        "At Reliant Consulting and Construction, Mark and Dylan give you a clear schedule with your estimate and keep you updated as each phase is finished."]),
   ]),

 dict(slug="kitchen-remodel-planning-checklist", date="2026-11-16", img="68f43c75722f75066b51c1f8",
   img_alt="Finished kitchen remodel with white cabinetry and a large island",
   name="Kitchen Remodel Planning Checklist",
   title="Kitchen Remodel Planning Checklist | Reliant Consulting and Construction",
   desc="A step-by-step checklist for planning a kitchen remodel in North Georgia: budget, layout, cabinets, countertops, permits and living through construction.",
   intro="A kitchen remodel goes smoothly when the decisions are made before construction starts. Use this checklist to get ready.",
   service=("kitchen-remodeling", "kitchen remodeling"),
   sections=[
    ("1. Decide what you want to fix", ["Write down what does not work in your kitchen now: not enough counter space, poor lighting, a cramped layout, worn cabinets. A clear list keeps the project focused and helps your contractor give you an accurate estimate."]),
    ("2. Set a budget and a priority list", ["Cabinets and countertops usually take the largest share of a kitchen budget, followed by labor, flooring and appliances. Decide which items matter most to you so you know where to spend and where to save. Keep some money in reserve for surprises behind the walls, especially in an older home."]),
    ("3. Decide whether the layout changes", ["Keeping the sink, range and walls where they are is the most economical route. Moving plumbing, gas lines or walls opens up more options but adds cost and time. If you want an island or an open plan, raise it at the first meeting so it can be planned properly."]),
    ("4. Choose materials early", [["Cabinet style, finish and hardware", "Countertop material", "Backsplash tile", "Flooring", "Sink, faucet and lighting", "Appliances, with their exact sizes"],
        "Cabinets and countertops often have the longest wait, so ordering them early keeps the job from stalling."]),
    ("5. Ask about permits", ["Cosmetic updates often do not need a permit, but structural, electrical and plumbing changes usually do. Requirements vary by city and county in North Georgia. A licensed contractor should handle the permits and inspections for you."]),
    ("6. Plan for life without a kitchen", ["Set up a temporary kitchen with a microwave, coffee maker and a small refrigerator in another room. Ask your contractor which days water and power to the kitchen will be off, and how the work area will be kept separate from the rest of the house."]),
    ("7. Get a detailed written estimate", ["A good estimate lists what is included, the materials, and the schedule. Compare estimates line by line, not just by the total. Reliant Consulting and Construction provides free, detailed estimates with no hidden costs, and Mark or Dylan walks you through every line."]),
   ]),

 dict(slug="water-damage-first-24-hours", date="2026-11-16", img="68fba25ad9a00deea85cf712",
   img_alt="Interior opened up for repairs during restoration",
   name="Water Damage: What to Do in the First 24 Hours",
   title="Water Damage: First 24 Hours | Reliant Consulting and Construction",
   desc="Found water damage in your North Georgia home? Follow these steps in the first 24 hours to stay safe, limit the damage and protect your insurance claim.",
   intro="A burst pipe or a leak can do a lot of damage quickly. What you do in the first day makes a real difference to the repair and to your insurance claim.",
   service=("water-damage-restoration", "water damage restoration"),
   sections=[
    ("1. Make it safe", ["If water is near outlets, appliances or your electrical panel, turn off power to that area at the breaker, and only if you can reach the panel without standing in water. Stay out of rooms with sagging ceilings. If the water may be contaminated, such as a sewer backup, keep people and pets away from it."]),
    ("2. Stop the water", ["For a plumbing leak, shut off the main water valve. Every adult in the house should know where it is. For a roof leak, catch the water in buckets and move belongings out of the way until the roof can be covered or repaired."]),
    ("3. Document everything", ["Before you move or throw anything away, take photos and video of the damage: the source, the wet areas and any damaged belongings. Your insurance company will want to see what happened."]),
    ("4. Call your insurance company", ["Report the damage and ask what your policy covers. In general, homeowners policies cover sudden, accidental damage such as a burst pipe, but often do not cover slow leaks that went on over time, and flooding from outside usually requires separate flood insurance. Policies differ, so your agent or adjuster is the one to confirm."]),
    ("5. Start drying", ["Remove standing water if it is safe to do so, lift furniture off wet floors and get air moving with fans. Building materials that stay wet can start to grow mold within a day or two, which is why speed matters."]),
    ("6. Call a restoration contractor", ["Water travels under flooring and inside walls where you cannot see it. A contractor can find how far it went, dry the structure properly, remove what cannot be saved and rebuild.",
        "Reliant Consulting and Construction handles the whole job, from water removal to the finished repair, and works directly with your insurance company."]),
    ("What not to do", [["Do not use a household vacuum to pick up water.", "Do not leave wet rugs, books or boxes sitting on carpet or wood floors.", "Do not wait several days to see if it dries on its own.", "Do not throw away damaged items before they are photographed."]]),
   ]),

 dict(slug="how-to-check-a-contractor-license-in-georgia", date="2026-11-16", img="68f2cef05675712fea75362a",
   img_alt="Contractor using a laser level to check a room during construction",
   name="How to Check a Contractor's License in Georgia",
   title="Check a Georgia Contractor License | Reliant Consulting and Construction",
   desc="Georgia requires a state license for most remodeling and construction jobs over $2,500. Here is how to look up a contractor's license before you hire.",
   intro="Before you hire anyone for a remodel or repair, take two minutes to confirm they are licensed. In Georgia it is free and easy to check.",
   service=None,
   sections=[
    ("When Georgia requires a contractor license", ["Georgia generally requires a state contractor license for residential construction, remodeling and repair work valued at more than $2,500. Licenses are issued by the State Licensing Board for Residential and General Contractors, which is part of the Georgia Secretary of State's office.",
        "Some trades, including electrical, plumbing and heating and air, are licensed separately. Cities and counties may also require a local business license."]),
    ("How to look up a license", [["Ask the contractor for their license number and the exact name on the license.",
        'Go to the Secretary of State\'s license lookup at <a href="https://verify.sos.ga.gov/verification/" rel="noopener">verify.sos.ga.gov</a>.',
        "Search by license number or by name.",
        "Check that the license is active, that the name matches the company you are hiring, and that the license type fits your project."]]),
    ("What else to ask for", [["<b>Proof of insurance.</b> Ask for a certificate of insurance showing general liability coverage.",
        "<b>A written estimate.</b> It should list the work, the materials and the price, with no vague lines.",
        "<b>A clear schedule.</b> You should know when work starts and roughly when it ends.",
        "<b>Who will be on the job.</b> Ask whether the person quoting the work is the person doing it."]]),
    ("Warning signs", [["No license number, or a number that does not match the company name", "Pressure to sign today", "A large cash payment demanded up front", "No written estimate or contract", "A price far below every other estimate"]]),
    ("Our license", [f"Reliant Consulting and Construction is licensed and insured. Our Georgia license number is {LICENSE}, and you are welcome to look it up. Mark and Dylan, the father-and-son owners, quote every job and are on every job site."]),
   ]),
]

BY_SLUG = {g["slug"]: g for g in GUIDES}
FOR_SERVICE = {g["service"][0]: g for g in GUIDES if g["service"]}

def guide_link(service_slug):
    """Sentence for a service page pointing at its guide (empty when there is none)."""
    g = FOR_SERVICE.get(service_slug)
    return f' Related guide: <a href="/guides/{g["slug"]}/">{g["name"]}</a>.' if g else ""

def _body(paras):
    out = ""
    for p in paras:
        out += ("<ul>" + "".join(f"<li>{x}</li>" for x in p) + "</ul>") if isinstance(p, list) else f"<p>{p}</p>"
    return out

def build(page, hero, pic, cta_band):
    cards = "".join(f'<a class="feat" style="text-decoration:none" href="/guides/{g["slug"]}/"><h3>{g["name"]}</h3><p>{g["intro"]}</p></a>' for g in GUIDES)
    body = hero("Homeowner Guides for North Georgia", "Straight answers about remodeling, construction and restoration from Mark and Dylan.", '<div class="crumbs"><a href="/">Home</a> / Guides</div>') + f'<section><div class="wrap"><div class="grid g3">{cards}</div></div></section>' + cta_band()
    page("/guides/", "Homeowner Guides | Reliant Consulting and Construction",
         "Remodeling, construction and restoration guides for North Georgia homeowners from Reliant Consulting and Construction in Jasper, GA.", body, cur="guides", crumb="Guides")
    for g in GUIDES:
        crumbs = f'<div class="crumbs"><a href="/">Home</a> / <a href="/guides/">Guides</a> / {g["name"]}</div>'
        secs = "".join(f"<h2>{h}</h2>{_body(ps)}" for h, ps in g["sections"])
        svc = f'<p>Learn more about our <a href="/services/{g["service"][0]}/">{g["service"][1]}</a> service, or see <a href="/services/">everything we do</a>.</p>' if g["service"] else '<p>See <a href="/services/">our services</a> or read more about <a href="/about/">Mark and Dylan</a>.</p>'
        others = "".join(f'<li><a href="/guides/{o["slug"]}/">{o["name"]}</a></li>' for o in GUIDES if o is not g)
        body = hero(g["name"], g["intro"], crumbs) + f'''
<section><div class="wrap" style="max-width:780px">{pic(g["img"], g["img_alt"], "card", eager=True)}
<div style="margin-top:26px">{secs}{svc}</div></div></section>
<section class="alt"><div class="wrap" style="max-width:780px"><h2>More guides</h2><ul>{others}</ul></div></section>''' + cta_band("Have a project in mind?", "Contact us for a free estimate. Mark and Dylan will personally meet with you to discuss it.")
        url = DOMAIN + f'/guides/{g["slug"]}/'
        art = {"@context": "https://schema.org", "@type": "Article", "headline": g["name"], "description": g["desc"], "datePublished": g["date"], "dateModified": g["date"],
               "image": f'{DOMAIN}/img/{g["img"]}.webp', "mainEntityOfPage": url, "author": {"@id": DOMAIN + "/#business"}, "publisher": {"@id": DOMAIN + "/#business"}}
        page(f'/guides/{g["slug"]}/', g["title"], g["desc"], body, cur="guides", og_img=g["img"], extra_ld=[art], crumb=g["name"])
