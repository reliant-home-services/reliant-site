import os, json, html, re
from PIL import Image
from config import *

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "site")
IMG = os.path.join(OUT, "img")
os.makedirs(os.path.join(IMG, "t"), exist_ok=True)

_dims = {}
def img_info(name):
    """name = file stem. Returns (w,h); makes a 640px thumbnail."""
    if name in _dims: return _dims[name]
    p = os.path.join(IMG, name + ".webp")
    im = Image.open(p); w, h = im.size
    t = os.path.join(IMG, "t", name + ".webp")
    if not os.path.exists(t):
        s = min(1, 640 / w); im.resize((max(1, int(w*s)), max(1, int(h*s))), Image.LANCZOS).save(t, quality=74, method=6)
    _dims[name] = (w, h)
    return _dims[name]

def esc(s): return html.escape(s, quote=True)

def pic(name, alt, cls="", eager=False, thumb=True, sizes="(max-width:700px) 100vw, 600px"):
    w, h = img_info(name)
    tw = 640 if w > 640 else w; th = int(h * tw / w)
    src = f"/img/t/{name}.webp" if (thumb and w > 640) else f"/img/{name}.webp"
    full = f"/img/{name}.webp"
    ld = "" if eager else ' loading="lazy"'
    c = f' class="{cls}"' if cls else ""
    return f'<img src="{src}" data-full="{full}" alt="{esc(alt)}" width="{tw}" height="{th}"{ld} decoding="async"{c}>'

SERVICES = [
    ("general-construction", "General Construction", "From framing to roofing, we handle all aspects of general construction with precision and care. New builds, additions, decks, and structural work.", "68f428108e5daafa4596a6d9", "Professionally poured concrete driveway in a wooded North Georgia setting"),
    ("renovations-and-remodels", "Renovations and Remodels", "Transform your space with expert kitchen, bathroom, and whole-home renovations. We bring your vision to life with quality craftsmanship.", "68f67ba318c4204457427f58", "Finished kitchen renovation with white cabinetry and a large island"),
    ("restoration-services", "Restoration Services", "Water, fire, and storm damage restoration with full insurance support. We help you recover quickly and rebuild better than before.", "68fba25b304c6e84668ad33b", "Fire damaged home structure awaiting restoration"),
]

def nav(cur):
    def a(href, text, key=None):
        c = ' aria-current="page"' if (key or href) == cur else ""
        return f'<a href="{href}"{c}>{text}</a>'
    svc = "".join(f"<li>{a('/services/'+s[0]+'/', s[1], s[0])}</li>" for s in SERVICES)
    twn = "".join(f"<li>{a('/service-areas/'+t[0]+'/', t[1], t[0])}</li>" for t in TOWNS)
    return f'''<nav id="nav" aria-label="Main"><ul>
<li>{a('/services/', 'Services', 'services')}<ul class="sub">{svc}</ul></li>
<li>{a('/about/', 'About Us', 'about')}</li>
<li>{a('/service-areas/', 'Service Areas', 'areas')}<ul class="sub">{twn}</ul></li>
<li>{a('/projects/', 'Projects', 'projects')}</li>
<li>{a('/reviews/', 'Reviews', 'reviews')}</li>
<li>{a('/faq/', 'FAQ', 'faq')}</li>
<li>{a('/contact/', 'Contact', 'contact')}</li>
</ul></nav>'''

def header(cur):
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="top"><div class="wrap">
<a class="brand" href="/" aria-label="{NAME} home"><img src="/img/logo-mark.webp" width="54" height="42" alt=""><span>{NAME}<small>Family owned &amp; operated</small></span></a>
{nav(cur)}
<div class="hdr-cta"><a class="btn ghost" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a><a class="btn quote-btn" href="/contact/">Request a Quote</a><button class="menu-btn" aria-expanded="false" aria-controls="nav">Menu</button></div>
</div></header>'''

def footer():
    svc = "".join(f'<li><a href="/services/{s[0]}/">{s[1]}</a></li>' for s in SERVICES)
    twn = "".join(f'<li><a href="/service-areas/{t[0]}/">{t[1]}, GA</a></li>' for t in TOWNS)
    return f'''<footer><div class="wrap">
<div class="grid g4">
<div><h3>{NAME}</h3><p>Family owned and operated construction company serving North Georgia with honesty, reliability, and quality craftsmanship.</p><p>License Number {LICENSE}<br><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></p></div>
<div><h3>Services</h3><ul>{svc}</ul></div>
<div><h3>Service Areas</h3><ul>{twn}</ul></div>
<div><h3>Quick Links</h3><ul><li><a href="/">Home</a></li><li><a href="/about/">About Us</a></li><li><a href="/services/">All Services</a></li><li><a href="/projects/">Projects</a></li><li><a href="/reviews/">Reviews</a></li><li><a href="/faq/">FAQ</a></li><li><a href="/contact/">Contact Us</a></li></ul></div>
</div>
<div class="legal"><span>&copy; 2026 {NAME}. Licensed &amp; insured. License {LICENSE}.</span><span><a href="/privacy/">Privacy</a></span></div>
</div></footer>
<div class="sticky-call"><a class="btn ghost" href="tel:{PHONE_TEL}">Call now</a><a class="btn" href="/contact/">Free quote</a></div>
<div id="lb" role="dialog" aria-label="Photo viewer"><button aria-label="Close">&times;</button><img alt=""></div>
<script src="/js/site.js" defer></script>'''

def form(idp="q", title="Request A Quote"):
    return f'''<form class="form" data-lead method="post" action="/api/lead" id="{idp}">
<h2>{title}</h2><p class="fine">Free estimates. We reply fast. Prefer to talk? Call <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>.</p>
<div class="row"><label>Full Name *<input name="name" required autocomplete="name" maxlength="120"></label>
<label>Phone *<input name="phone" type="tel" required autocomplete="tel" maxlength="40"></label></div>
<label>Email *<input name="email" type="email" required autocomplete="email" maxlength="160"></label>
<label>Street Address / Town<input name="address" autocomplete="street-address" maxlength="200"></label>
<label>Project Details *<textarea name="details" rows="4" required maxlength="2000" placeholder="Tell us what you have in mind"></textarea></label>
<div class="hp" aria-hidden="true"><label>Website<input name="website" tabindex="-1" autocomplete="off"></label></div>
<button class="btn" type="submit">Send Message</button>
<div class="msg" role="status" aria-live="polite"></div>
<p class="fine">By submitting this form, you agree to be contacted by {NAME} regarding your project.</p>
</form>'''

def cta_band(title="Ready to Get Started?", text="Contact us today for a free estimate. Mark and Dylan will personally meet with you to discuss your project."):
    return f'''<section class="cta-band"><div class="wrap"><h2>{title}</h2><p>{text}</p>
<div class="cta-row" style="justify-content:center"><a class="btn" href="/contact/">Request Free Estimate</a><a class="btn ghost" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a></div></div></section>'''

def jsonld(extra=None):
    d = {"@context": "https://schema.org", "@type": ["GeneralContractor", "HomeAndConstructionBusiness"],
         "@id": DOMAIN + "/#business", "name": NAME, "url": DOMAIN + "/", "telephone": PHONE_TEL, "sameAs": [GOOGLE_REVIEWS_URL], "hasMap": GOOGLE_REVIEWS_URL,
         "image": DOMAIN + "/img/logo.webp", "logo": DOMAIN + "/img/logo.webp",
         "description": "Family owned and operated general contractor in Jasper, Georgia: construction, renovations and remodels, and restoration services across North Georgia.",
         "priceRange": "$$", "identifier": "Georgia contractor license " + LICENSE,
         "address": {"@type": "PostalAddress", "addressLocality": "Jasper", "addressRegion": "GA", "addressCountry": "US"},
         "areaServed": [{"@type": "City", "name": t[1] + ", GA"} for t in TOWNS],
         "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Services", "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": s[1]}} for s in SERVICES]}}
    out = [d]
    if extra: out += extra
    return "".join('<script type="application/ld+json">' + json.dumps(x, ensure_ascii=False) + "</script>" for x in out)

PAGES = []
def page(path, title, desc, body, cur="", og_img="68f3b5f3a144cd15d4ea493b", extra_ld=None, preload=None):
    canon = DOMAIN + path
    pl = f'<link rel="preload" as="image" href="{preload}" fetchpriority="high">' if preload else ""
    h = f'''<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title><meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{canon}">
<meta property="og:type" content="website"><meta property="og:site_name" content="{NAME}"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:url" content="{canon}"><meta property="og:image" content="{DOMAIN}/img/{og_img}.webp">
<meta name="theme-color" content="#111214"><link rel="icon" href="/img/logo-mark.webp" type="image/webp">
{pl}<link rel="stylesheet" href="/css/style.css">{jsonld(extra_ld)}</head><body>
{header(cur)}<main id="main">{body}</main>{footer()}</body></html>'''
    fp = os.path.join(OUT, path.strip("/"), "index.html") if path != "/" else os.path.join(OUT, "index.html")
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    open(fp, "w", encoding="utf-8").write(h)
    PAGES.append(path)

def hero(title, sub, crumbs=""):
    return f'<section class="page-hero"><div class="wrap">{crumbs}<h1>{title}</h1><p>{sub}</p></div></section>'
