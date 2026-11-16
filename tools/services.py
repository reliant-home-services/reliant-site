"""Detailed service pages (one page per job type), added Nov 16, 2026.
Each entry in PAGES_DATA builds /services/<slug>/. Edit the text here, then run: python tools/build.py
Rule: nothing invented. No prices, no certifications, no promises the owners have not made elsewhere on the site."""
from config import *
import guides

# parent = which of the 3 main service pages links to it
PAGES_DATA = [
 dict(slug="kitchen-remodeling", parent="renovations-and-remodels", name="Kitchen Remodeling", svc="Kitchen remodeling",
   h1="Kitchen Remodeling in Jasper and North Georgia",
   title="Kitchen Remodeling in Jasper, GA | Reliant Consulting and Construction",
   desc="Kitchen remodeling in Jasper, GA and North Georgia: cabinets, countertops, islands, flooring and full layouts. Family owned, licensed & insured. Free estimates.",
   sub="Cabinets, countertops, islands, flooring and full layout changes, built by the father-and-son team who quote the job.",
   hero="68f43c75722f75066b51c1f8", hero_alt="Finished kitchen remodel with white cabinetry and a large island",
   paras=["The kitchen is the room most homeowners want to change first, and the one where the details matter most. Reliant Consulting and Construction remodels kitchens across Jasper, Pickens County and North Georgia, from a cabinet and countertop refresh to a full tear-out with a new layout.",
          "Mark and Dylan handle the whole job: demolition, framing changes, drywall, cabinets, countertops, tile, flooring, trim and paint. When a kitchen needs plumbing or electrical moved, we plan that work into the schedule so the project keeps moving.",
          "You get a detailed written estimate before anything starts, and you deal with the owners from the first walk-through to the final one."],
   included=["Custom and semi-custom cabinetry", "Countertops and backsplashes", "Kitchen islands and breakfast bars", "Layout changes and wall removal", "Flooring installation", "Lighting and fixture updates", "Drywall, trim and paint", "Framing and structural changes"],
   cost_h="What affects the cost and timeline of a kitchen remodel",
   cost=["The biggest factors are the size of the kitchen, whether the layout changes, and the materials you choose. Keeping sinks, ranges and walls where they are costs less than moving them. Cabinets and countertops are usually the largest share of the budget.",
         "Timelines depend on scope and on how long cabinets and countertops take to arrive. We give you a schedule before work begins, order long-lead materials early, and tell you up front which days the kitchen will be out of use."],
   faqs=[("How long does a kitchen remodel take?", "It depends on the scope. A cabinet and countertop update is much shorter than a full tear-out with layout changes. We give you a clear schedule with your estimate so you know what to expect before work begins."),
         ("Can you change the layout of my kitchen?", "Yes. We remove and move walls, add islands and rework the layout. Structural changes are planned and built to code, and we handle the permits the work requires."),
         ("Do you offer free kitchen remodeling estimates?", "Yes. Mark or Dylan visits your home, measures the kitchen, talks through your options and provides a free, detailed estimate with no hidden costs."),
         ("Do I need to move out during a kitchen remodel?", "Most homeowners stay in the home. We keep the work area contained, clean up as we go, and tell you ahead of time when water or power to the kitchen will be off.")],
   gallery=[("68f43c75722f75066b51c1f8", "Kitchen remodel with white cabinetry and large island"), ("68f67ba318c4204457427f58", "Kitchen renovation with large island and high-end appliances"), ("68f67ba3c1945b376eb3be1a", "Kitchen renovation with granite island and wood cabinetry"), ("68fba254409d6af8e1fc3152", "Kitchen with marble-topped island and rustic wood cabinets"), ("68f2cd7074ee542470b85f68", "White kitchen with a live-edge wood island"), ("68fba25454fb620f47717c27", "Kitchen before and after remodeling")]),

 dict(slug="bathroom-remodeling", parent="renovations-and-remodels", name="Bathroom Remodeling", svc="Bathroom remodeling",
   h1="Bathroom Remodeling in Jasper and North Georgia",
   title="Bathroom Remodeling in Jasper, GA | Reliant Consulting and Construction",
   desc="Bathroom remodeling in Jasper, GA and North Georgia: walk-in showers, tile, vanities and full renovations. Family owned, licensed & insured. Free estimates.",
   sub="Walk-in showers, tile, vanities and full bathroom renovations, with many projects finished in about four weeks.",
   hero="68f3b5f3faf82b7e98d370be", hero_alt="Bathroom remodel with walk-in shower and glass doors",
   paras=["A bathroom remodel is one of the most useful upgrades you can make to a home. Reliant Consulting and Construction remodels bathrooms in Jasper and across North Georgia, from a new vanity and tile to a complete gut and rebuild.",
          "We build walk-in showers with tile walls and built-in niches, replace tubs, install vanities and countertops, lay tile and wood-look flooring, and update lighting and fixtures. Behind the walls we replace damaged framing and subfloor so the new finishes last.",
          "Mark and Dylan do the work themselves and keep the job site clean, which matters when the room being remodeled is one your family uses every day."],
   included=["Walk-in and tile showers", "Tub replacement and tub-to-shower conversions", "Vanities, sinks and countertops", "Tile floors, walls and niches", "Glass shower doors", "Lighting, fans and fixtures", "Subfloor and framing repair", "Drywall, trim and paint"],
   cost_h="What affects the cost and timeline of a bathroom remodel",
   cost=["Size, tile choices and plumbing changes drive the budget. Keeping the toilet, shower and vanity in the same positions is the most economical route. Moving drains, enlarging the shower or adding custom tile work adds labor.",
         "Many of our bathroom remodels are completed in about four weeks. Larger primary bathrooms or projects with layout changes can take longer. You get the schedule in writing before we start."],
   faqs=[("How long does a bathroom remodel take?", "Many bathroom remodels are completed in about four weeks. The exact time depends on the size of the room, the tile work and whether plumbing is moved. We provide a schedule before work begins."),
         ("Can you convert a tub to a walk-in shower?", "Yes. Tub-to-shower conversions are one of our most common bathroom projects, including tile walls, built-in niches and glass doors."),
         ("Do you repair water damage found during a bathroom remodel?", "Yes. If we open a wall or floor and find rot or water damage, we show you, explain the fix and repair the framing or subfloor before new finishes go in."),
         ("Do you offer free bathroom remodeling estimates?", "Yes. We provide free, detailed estimates and explain your options and costs upfront.")],
   gallery=[("68f3b5f3a144cd15d4ea493b", "Walk-in shower with white marble walls and gold fixtures"), ("68f3b5f3a144cd526bea4938", "Bathroom with white marble tile and built-in niches"), ("68f3b5f3a144cde8bdea4939", "Bathroom with pedestal sink and modern tub"), ("68f2cba7175e598b489657ed", "Bathroom with custom stone vanity and vessel sink"), ("68f3b5e7faf82b6e89d36f4a", "Double vanity with marble countertop and olive-green cabinets"), ("68f3b5f37b55a744158354d6", "Bathroom before renovation")]),

 dict(slug="basement-finishing", parent="renovations-and-remodels", name="Basement Finishing", svc="Basement finishing",
   h1="Basement Finishing in Jasper and North Georgia",
   title="Basement Finishing in Jasper, GA | Reliant Consulting and Construction",
   desc="Basement finishing in Jasper, GA and North Georgia: framing, insulation, drywall, flooring, bathrooms and media rooms. Family owned, licensed & insured.",
   sub="Turn an unfinished basement into living space: family rooms, bedrooms, bathrooms, offices and media rooms.",
   hero="68f3b5f36edd49724407a5b2", hero_alt="Finished home theater room with large screen and media console",
   paras=["Finishing a basement is usually the least expensive way to add living space, because the foundation, walls and roof are already there. Reliant Consulting and Construction finishes basements for homeowners in Jasper and across North Georgia.",
          "We frame the walls, insulate, hang and finish drywall, install flooring and trim, and build the rooms you need: a family room, guest bedroom, bathroom, office, gym or media room. We handle the permits and coordinate the inspections the work requires.",
          "Many North Georgia homes sit on sloped lots with walk-out basements, which makes them good candidates for bright, comfortable finished space."],
   included=["Wall framing and insulation", "Drywall hanging and finishing", "Flooring installation", "Basement bathrooms", "Bedrooms and home offices", "Media rooms and family rooms", "Trim, doors and paint", "Permits and inspections"],
   cost_h="What affects the cost and timeline of finishing a basement",
   cost=["The main factors are square footage, how many rooms you divide the space into, and whether you add a bathroom or wet bar. Plumbing below grade and extra egress windows add to the scope.",
         "Before we frame anything we look for moisture. A basement needs to be dry before it is finished, so if we see signs of water we tell you what should be addressed first."],
   faqs=[("How long does it take to finish a basement?", "It depends on the size of the basement and what goes into it. An open family room is quicker than a basement with a bedroom, bathroom and media room. We give you a schedule with your estimate."),
         ("Do I need a permit to finish my basement?", "Finishing a basement usually requires a permit because it involves framing, electrical and often plumbing. We handle the permits and inspections as part of the job."),
         ("Can you add a bathroom in a basement?", "Yes. We build basement bathrooms, including the framing, tile and fixtures, and coordinate the plumbing work it requires."),
         ("What if my basement has moisture?", "We check for moisture before work starts. If there is a problem, we explain what needs to be corrected before the space is finished so your new walls and floors are protected.")],
   gallery=[("68f3b5f36edd49724407a5b2", "Finished home theater with large screen and media console"), ("68f43e5b8e5daafcee98d6ea", "Basement before finishing"), ("68f3b5f3a144cd3bd2ea4933", "Unfinished basement before renovation"), ("68f428106a7dfa7e5af7cf7d", "Framed walls with insulation before drywall")]),

 dict(slug="home-additions", parent="general-construction", name="Home Additions", svc="Home additions",
   h1="Home Additions in Jasper and North Georgia",
   title="Home Additions in Jasper, GA | Reliant Consulting and Construction",
   desc="Home additions in Jasper, GA and North Georgia: room additions, garages and expanded living space built to match your home. Family owned, licensed & insured.",
   sub="Room additions, garages and expanded living space, built to match your existing home from foundation to roof.",
   hero="68f3b5f34a04cbb8ec1b11be", hero_alt="Room under construction with exposed framing",
   paras=["When you like where you live but need more room, an addition is often a better answer than moving. Reliant Consulting and Construction builds home additions in Jasper and across North Georgia.",
          "We manage every phase: foundation, framing, roofing, siding, drywall and interior finishes. The goal is an addition that looks like it was always part of the house, with rooflines, siding and trim that match.",
          "Mark and Dylan bring over 30 years of combined experience in framing and structural work, and they manage permits and inspections from start to final sign-off."],
   included=["Bedroom and living room additions", "Room additions that match your home", "Attached and detached garages", "Foundations and concrete slabs", "Framing and structural work", "Roofing tied into the existing roof", "Drywall and interior finishes", "Permits and inspections"],
   cost_h="What affects the cost and timeline of a home addition",
   cost=["Size, foundation type and what goes inside the new space are the main factors. A bedroom costs less per square foot than a bathroom or kitchen addition because it has less plumbing and fewer fixtures. Sloped lots can add foundation work.",
         "An addition involves permits, inspections and weather, so we lay out the schedule phase by phase before we break ground and keep you updated as each phase is completed."],
   faqs=[("Do you handle permits for home additions?", "Yes. We manage the permits and inspections for the addition, from the first application to the final inspection."),
         ("Will the addition match my existing house?", "That is the goal on every project. We match rooflines, siding, trim and interior finishes so the new space blends with the original home."),
         ("Can you build a garage?", "Yes. We build attached and detached garages, handling every part of the project from the foundation to the roof."),
         ("Do you offer free estimates for additions?", "Yes. We meet with you at your home, look at the site and provide a free, detailed estimate.")],
   gallery=[("68f3b5f34a04cbb8ec1b11be", "Room under construction with exposed framing"), ("68f428106a7dfa7e5af7cf7d", "Framed interior walls with insulation"), ("68f428101e167434c5edd38e", "Drywall stage during construction"), ("68fba25445057e121aa79020", "Finished living room with fireplace and large windows")]),

 dict(slug="decks-and-patios", parent="general-construction", name="Decks and Patios", svc="Deck and patio construction",
   h1="Decks, Patios and Outdoor Living in North Georgia",
   title="Decks and Patios in Jasper, GA | Reliant Consulting and Construction",
   desc="Decks, patios, porches, pavilions, retaining walls and driveways in Jasper, GA and North Georgia. Family owned, licensed & insured. Free estimates.",
   sub="Custom decks, patios, porches, pavilions, retaining walls and concrete work that extend your living space outdoors.",
   hero="68f3b5e74a04cbe2cc1b1048", hero_alt="Finished retaining wall and terraced lawn with backyard patio and gazebo",
   paras=["North Georgia weather makes outdoor space usable most of the year. Reliant Consulting and Construction builds decks, patios, porches and pavilions for homeowners in Jasper and the surrounding communities.",
          "Many lots here are sloped, so outdoor projects often start with the ground: retaining walls, terracing and proper footings. We build the structure to code with quality materials so it holds up for years.",
          "We also pour concrete slabs, pads and driveways, and replace worn-out driveways and patios."],
   included=["Custom deck construction", "Patios and concrete pads", "Covered porches", "Pavilions and gazebos", "Retaining walls and terracing", "Concrete and asphalt driveways", "Driveway and patio replacement", "Stairs and railings"],
   cost_h="What affects the cost of a deck or patio",
   cost=["Size, height off the ground and materials are the main factors. A ground-level patio is simpler than a raised deck with stairs and railings. Covered structures such as porches and pavilions add framing and roofing.",
         "Slope matters too. A steep yard may need retaining walls or taller posts and deeper footings. We look at the site with you and explain the options before you commit to a design."],
   faqs=[("Do you build covered porches and pavilions?", "Yes. We build covered porches, pavilions and gazebos, including the framing, roofing and finish details."),
         ("Can you build on a sloped yard?", "Yes. Sloped lots are common in North Georgia. We build retaining walls and terraces and set proper footings so decks and patios are solid on uneven ground."),
         ("Do you pour driveways?", "Yes. We pour concrete driveways, slabs and pads and install asphalt driveways, including replacing old, damaged ones."),
         ("Do you offer free estimates?", "Yes. We visit the site, talk through your ideas and provide a free, detailed estimate.")],
   gallery=[("68f3b5e74a04cbe2cc1b1048", "Retaining wall and terraced lawn with patio and gazebo"), ("68fcf6eed672b4c0f9c32cf4", "Pavilion with wrap-around porch and stone accents"), ("68f428108e5daafa4596a6d9", "Poured concrete driveway in a wooded setting"), ("68f428101e167416f0edd38d", "New asphalt driveway with concrete curb"), ("68f42810722f7513ef4fb7a7", "Driveway and patio before replacement")]),

 dict(slug="fire-damage-restoration", parent="restoration-services", name="Fire Damage Restoration", svc="Fire damage restoration",
   h1="Fire Damage Restoration in Jasper and North Georgia",
   title="Fire Damage Restoration, Jasper GA | Reliant Consulting and Construction",
   desc="Fire damage restoration in Jasper, GA and North Georgia: smoke and soot removal, structural repair and full rebuilds, with insurance help. Licensed & insured.",
   sub="Smoke and soot removal, structural repair and full reconstruction, with help on the insurance claim.",
   hero="68fba25b304c6e84668ad33b", hero_alt="Fire damaged home structure before restoration",
   paras=["A house fire is overwhelming, and the damage goes beyond what burned. Smoke, soot and the water used to put the fire out all affect the structure. Reliant Consulting and Construction restores fire-damaged homes in Jasper and across North Georgia.",
          "We assess the structure, remove damaged materials, clean smoke and soot, deal with odor, and rebuild. Because we are general contractors, the same team that tears out the damage frames, drywalls and finishes the repair. You are not handed from one company to another.",
          "We work directly with your insurance company and document the damage so the claim is as simple as it can be."],
   included=["Structural assessment", "Smoke and soot removal", "Odor elimination", "Demolition of damaged materials", "Framing and structural repair", "Drywall, flooring and finishes", "Full reconstruction", "Insurance coordination"],
   cost_h="What to do after a fire",
   cost=["Once the fire department says it is safe, call your insurance company to start a claim, and avoid cleaning soot yourself, since wiping it can set stains deeper. Take photos if you can do so safely.",
         "Then call us. We inspect the damage, explain what can be cleaned and what must be replaced, and give your insurer the documentation they ask for. Most fire restoration is paid through homeowners insurance, and what is covered depends on your policy."],
   faqs=[("Do you work with insurance companies on fire damage?", "Yes. We work directly with your insurance company and provide the documentation needed for the claim."),
         ("Can you rebuild after a major fire?", "Yes. We handle everything from smoke and soot removal to full reconstruction, including framing, roofing, drywall and finishes."),
         ("Can smoke odor be removed?", "In most cases, yes. Odor removal is part of our fire restoration work, along with removing materials that cannot be cleaned."),
         ("How soon should I call after a fire?", "Call as soon as the property is safe to enter. The sooner the damage is assessed and the home is secured, the less secondary damage there is from soot and water.")],
   gallery=[("68fba25b304c6e84668ad33b", "Fire damaged home structure before restoration"), ("68fba25ad9a00deea85cf712", "Interior demolition before rebuilding"), ("68fba25444eecb4fd3b2875b", "Before and after of a full interior demolition and renovation")]),

 dict(slug="water-damage-restoration", parent="restoration-services", name="Water Damage Restoration", svc="Water damage restoration",
   h1="Water Damage Restoration in Jasper and North Georgia",
   title="Water Damage Restoration, Jasper GA | Reliant Consulting and Construction",
   desc="Water damage restoration in Jasper, GA and North Georgia: water extraction, drying and repairs after leaks, burst pipes and flooding. Licensed & insured.",
   sub="Fast response to burst pipes, leaks and flooding: water removal, drying, repair and full restoration.",
   hero="68fba25ad9a00deea85cf712", hero_alt="Interior opened up for repairs before restoration",
   paras=["Water damage gets worse by the hour. Wet drywall, insulation and flooring hold moisture, and mold can follow if they are not dried or removed. Reliant Consulting and Construction responds to water damage in Jasper and across North Georgia.",
          "We extract the water, dry the structure, remove what cannot be saved and rebuild: framing, subfloor, drywall, flooring, cabinets and trim. One team handles it from the first visit to the finished repair.",
          "We document the damage for your insurance company and work with your adjuster directly."],
   included=["Water extraction and removal", "Structural drying", "Mold prevention", "Removal of damaged drywall and flooring", "Subfloor and framing repair", "Drywall, flooring and cabinet replacement", "Complete restoration", "Insurance documentation"],
   cost_h="What to do when you find water damage",
   cost=["If it is safe, shut off the water at the main valve and turn off power to the affected area. Move furniture and valuables out of the water, take photos, and call your insurance company.",
         "Then call us. Homeowners insurance often covers sudden damage such as a burst pipe, while slow leaks and flooding from outside are treated differently, so check your policy or ask your agent. We tell you plainly what we find and what it takes to fix."],
   faqs=[("How quickly should water damage be handled?", "As quickly as possible. The longer materials stay wet, the more has to be replaced and the higher the chance of mold. Call as soon as you find the problem."),
         ("Do you work with insurance on water damage claims?", "Yes. We document the damage and work directly with your insurance company and adjuster."),
         ("Do you repair the damage or only dry it out?", "Both. We remove the water and dry the structure, then rebuild what was damaged, including subfloor, drywall, flooring and cabinets."),
         ("Does homeowners insurance cover water damage?", "It depends on the cause and your policy. Sudden events like a burst pipe are often covered, while gradual leaks and outside flooding may not be. Your agent can confirm what applies to you.")],
   gallery=[("68fba25ad9a00deea85cf712", "Interior demolition before restoration"), ("68f428101e167434c5edd38e", "Drywall stage during a rebuild"), ("68fba25444eecb4fd3b2875b", "Before and after of a full interior demolition and renovation")]),

 dict(slug="storm-damage-repair", parent="restoration-services", name="Storm Damage Repair", svc="Storm damage repair",
   h1="Storm Damage Repair in Jasper and North Georgia",
   title="Storm Damage Repair in Jasper, GA | Reliant Consulting and Construction",
   desc="Storm damage repair in Jasper, GA and North Georgia: roof repair, structural fixes and debris removal, with insurance claim support. Licensed & insured.",
   sub="Roof repairs, structural fixes, debris removal and full reconstruction after wind, hail and fallen trees.",
   hero="68fcf6ee295ec0813d5c7876", hero_alt="Property covered in heavy branches and debris before cleanup",
   paras=["North Georgia storms bring high wind, hail and falling trees, and the damage to a home can be sudden. Reliant Consulting and Construction repairs storm damage in Jasper and the surrounding communities.",
          "We repair and replace roofs, fix structural damage from fallen trees and limbs, remove debris, and restore the inside of the home when water gets in. As general contractors we handle the roof, the framing and the interior in one project.",
          "We support your insurance claim with documentation of the damage and work with your adjuster."],
   included=["Roof repair and replacement", "Structural repairs", "Fallen tree and limb damage", "Debris removal", "Complete property restoration", "Interior water damage repair", "Reconstruction", "Insurance claim support"],
   cost_h="What to do after a storm",
   cost=["Stay clear of downed power lines and damaged parts of the structure. From the ground, photograph the roof, siding and any fallen trees, then report the damage to your insurance company.",
         "Call us to inspect it. Storm damage is not always visible from the yard, and a damaged roof can leak for weeks before a stain shows on the ceiling. We explain what we find and give you and your insurer a clear scope of the repair."],
   faqs=[("Do you help with storm damage insurance claims?", "Yes. We document the damage and support your claim, working with your insurance company and adjuster."),
         ("Do you repair roofs after a storm?", "Yes. We repair and replace storm-damaged roofs and fix any structural or interior damage that came with it."),
         ("A tree fell on my house. Can you fix it?", "Yes. We repair structural damage from fallen trees and limbs, including framing, roofing and the interior."),
         ("How do I know if my roof has storm damage?", "Missing shingles, dented metal and granules in the gutters are common signs, but some damage cannot be seen from the ground. An inspection is the reliable way to know.")],
   gallery=[("68fcf6ee295ec0813d5c7876", "Property with heavy branches and debris before cleanup"), ("68fba25444eecb4fd3b2875b", "Before and after of a full interior demolition and renovation"), ("68fba25ad9a00deea85cf712", "Interior demolition before rebuilding")]),
]

BY_SLUG = {d["slug"]: d for d in PAGES_DATA}
PARENTS = {"general-construction": "General Construction", "renovations-and-remodels": "Renovations and Remodels", "restoration-services": "Restoration Services"}
# words used on the town pages -> detailed page
TOWN_LINKS = {"Kitchen Renovations": "kitchen-remodeling", "Bathroom Remodels": "bathroom-remodeling", "Basement Finishing": "basement-finishing",
              "Home Additions": "home-additions", "Deck Construction": "decks-and-patios", "Patios & Retaining Walls": "decks-and-patios",
              "Decks, Porches & Pavilions": "decks-and-patios", "Storm Damage Restoration": "storm-damage-repair", "Storm Damage Repair": "storm-damage-repair",
              "Emergency Water Damage": "water-damage-restoration"}

STEPS = [("Free Consultation", "Mark or Dylan visits your property, looks at the work and listens to what you need."),
         ("Detailed Estimate", "You receive a clear, written estimate with no hidden costs."),
         ("Quality Work", "Mark and Dylan personally oversee the job and keep the site clean and safe."),
         ("Final Walkthrough", "We walk the finished work with you and make sure every detail is right.")]

def linkify(label):
    """Town-page list item -> link to the detailed page when one exists."""
    s = TOWN_LINKS.get(label)
    return f'<a href="/services/{s}/">{label}</a>' if s else label

def kids_html(parent):
    """Cards on a main service page linking to its detailed pages."""
    kids = [d for d in PAGES_DATA if d["parent"] == parent]
    cards = "".join(f'<a class="feat" style="text-decoration:none" href="/services/{d["slug"]}/"><h3>{d["name"]}</h3><p>{d["sub"]}</p></a>' for d in kids)
    return f'<section class="alt"><div class="wrap"><h2>Learn more about each service</h2><div class="grid g3" style="margin-top:22px">{cards}</div></div></section>'

def all_links_html():
    items = "".join(f'<li><a href="/services/{d["slug"]}/">{d["name"]}</a></li>' for d in PAGES_DATA)
    return f'<section><div class="wrap"><div class="center"><h2>Popular Projects</h2><p class="lead">Details on the jobs homeowners ask us about most</p></div><ul class="ticks list" style="margin-top:22px">{items}</ul></div></section>'

def build(page, hero, pic, cta_band, faq_html, faq_ld):
    towns = ", ".join(f'<a href="/service-areas/{s}/">{n}</a>' for s, n, _ in TOWNS)
    for d in PAGES_DATA:
        crumbs = f'<div class="crumbs"><a href="/">Home</a> / <a href="/services/">Services</a> / <a href="/services/{d["parent"]}/">{PARENTS[d["parent"]]}</a> / {d["name"]}</div>'
        gal = "".join(f'<figure data-c="all">{pic(n, a)}</figure>' for n, a in d["gallery"])
        others = [o for o in PAGES_DATA if o["parent"] == d["parent"] and o is not d]
        related = " and ".join(f'<a href="/services/{o["slug"]}/">{o["name"].lower()}</a>' for o in others)
        body = hero(d["h1"], d["sub"], crumbs) + f'''
<section><div class="wrap split"><div><h2>{d["name"]} by a local, family-owned contractor</h2>{"".join(f"<p>{p}</p>" for p in d["paras"])}
<div class="cta-row"><a class="btn" href="/contact/">Get Free Estimate</a><a class="btn dark" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a></div></div>{pic(d["hero"], d["hero_alt"], eager=True)}</div></section>
<section class="alt"><div class="wrap"><div class="center"><h2>What our {d["name"].lower()} service includes</h2></div><ul class="ticks list" style="margin-top:22px">{"".join(f"<li>{x}</li>" for x in d["included"])}</ul></div></section>
<section><div class="wrap" style="max-width:860px"><h2>{d["cost_h"]}</h2>{"".join(f"<p>{p}</p>" for p in d["cost"])}</div></section>
<section class="dark"><div class="wrap"><div class="center"><h2>How We Work</h2></div><div class="grid g4" style="margin-top:28px">{"".join(f'<div class="feat"><div class="num">{i+1}</div><h3>{t}</h3><p>{x}</p></div>' for i, (t, x) in enumerate(STEPS))}</div></div></section>
<section class="alt"><div class="wrap"><h2>{d["name"]} Photos</h2><div class="gallery" style="margin-top:20px">{gal}</div><p style="margin-top:14px"><a href="/projects/">View more projects &rarr;</a></p></div></section>
<section><div class="wrap" style="max-width:860px"><h2>{d["name"]} FAQs</h2>{faq_html(d["faqs"])}</div></section>
<section class="alt"><div class="wrap" style="max-width:860px"><h2>Where we work</h2><p>Reliant Consulting and Construction is based in Jasper, Georgia and provides {d["name"].lower()} in {towns} and surrounding North Georgia communities. We also offer {related}, and you can see everything we do on our <a href="/services/{d["parent"]}/">{PARENTS[d["parent"]].lower()}</a> page.{guides.guide_link(d["slug"])}</p></div></section>''' + cta_band()
        page(f'/services/{d["slug"]}/', d["title"], d["desc"], body, cur=d["parent"], og_img=d["hero"], extra_ld=[faq_ld(d["faqs"])], crumb=d["name"], svc=d["svc"])
