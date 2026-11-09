import re, json, glob, os
base = os.path.join(os.path.dirname(__file__), '..', 'site')
for f in sorted(glob.glob(base + '/**/index.html', recursive=True)):
    h = open(f, encoding='utf8').read()
    rel = os.path.relpath(f, base)
    t = re.search(r'<title>(.*?)</title>', h)
    d = re.search(r'name="description" content="(.*?)"', h)
    ld = re.findall(r'ld\+json">(.*?)</script>', h, re.S)
    types = []
    for x in ld:
        try:
            j = json.loads(x); types.append(j.get('@type'))
        except Exception as e:
            types.append('BAD JSON')
    h1 = len(re.findall(r'<h1', h)); imgs = re.findall(r'<img[^>]*>', h)
    noalt = [i for i in imgs if 'alt=' not in i]
    print(rel, '| title', len(t.group(1)) if t else None, '| desc', len(d.group(1)) if d else None, '| h1', h1, '| imgs', len(imgs), 'noalt', len(noalt), '| ld', types, '| canon', 'canonical' in h)
h = open(base + '/index.html', encoding='utf8').read()
print(re.findall(r'ld\+json">(.*?)</script>', h, re.S)[0][:1800])
