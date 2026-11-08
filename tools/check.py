"""Offline site check: broken links/images, titles, descriptions, h1, alt text, sizes.
Run: python tools/check.py     (exit code 1 if problems)"""
import os, re, sys, glob
from urllib.parse import urlparse
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); OUT = os.path.join(ROOT, "site")
problems = []; titles = {}; descs = {}
def exists(url):
    p = urlparse(url).path
    if p.startswith("/"):
        f = os.path.join(OUT, p.lstrip("/"))
        return os.path.isfile(f) or os.path.isfile(os.path.join(f, "index.html"))
    return True
pages = glob.glob(OUT + "/**/*.html", recursive=True)
for f in pages:
    rel = os.path.relpath(f, OUT); t = open(f, encoding="utf8").read()
    ti = re.search(r"<title>(.*?)</title>", t, re.S); de = re.search(r'<meta name="description" content="(.*?)"', t)
    if not ti or not (20 <= len(ti.group(1)) <= 70): problems.append(f"{rel}: title length {len(ti.group(1)) if ti else 0} (aim 20-70)")
    if not de or not (70 <= len(de.group(1)) <= 175): problems.append(f"{rel}: description length {len(de.group(1)) if de else 0} (aim 70-175)")
    if ti: titles.setdefault(ti.group(1), []).append(rel)
    if de: descs.setdefault(de.group(1), []).append(rel)
    if t.count("<h1") != 1: problems.append(f"{rel}: {t.count('<h1')} h1 tags (want 1)")
    for m in re.finditer(r"<img [^>]*>", t):
        if "alt=" not in m.group(0): problems.append(f"{rel}: image without alt")
    for m in re.finditer(r'(?:href|src)="([^"#]+)"', t):
        u = m.group(1)
        if u.startswith(("http", "tel:", "mailto:", "data:")): continue
        if not exists(u): problems.append(f"{rel}: broken link/file {u}")
    for bad in ("Coastline", "tree service", "Destin", "[email protected]", "850) 837"):
        if bad.lower() in t.lower(): problems.append(f"{rel}: leftover text '{bad}'")
for k, v in {**{("title", a): b for a, b in titles.items()}, **{("desc", a): b for a, b in descs.items()}}.items():
    if len(v) > 1: problems.append(f"duplicate {k[0]} on {v}")
big = [(os.path.getsize(f) // 1024, f) for f in glob.glob(OUT + "/img/**/*.webp", recursive=True) if os.path.getsize(f) > 500 * 1024]
for kb, f in big: problems.append(f"large image {kb} KB: {os.path.relpath(f, OUT)}")
print(f"checked {len(pages)} pages")
print("\n".join(problems) if problems else "ALL CLEAR")
sys.exit(1 if problems else 0)
