"""On-page SEO audit over dist/: python3 tools/seo_audit.py dist"""
import os, re, json, sys, collections, xml.dom.minidom
from html.parser import HTMLParser
D = sys.argv[1]; BASE = "https://masnoonduaien.online"
class P(HTMLParser):
    def __init__(s): super().__init__(); s.a=[]; s.ld=[]; s.inld=False; s.h1=0; s.title=""; s.intitle=False; s.meta={}; s.links=[]; s.alts={}; s.canon=None; s.imgs=[]
    def handle_starttag(s, t, a):
        a = dict(a)
        if t == "a" and "href" in a: s.a.append(a["href"])
        if t == "script" and a.get("type") == "application/ld+json": s.inld = True
        if t == "h1": s.h1 += 1
        if t == "title": s.intitle = True
        if t == "meta": s.meta[a.get("name") or a.get("property")] = a.get("content")
        if t == "link" and a.get("rel") == "canonical": s.canon = a["href"]
        if t == "link" and a.get("rel") == "alternate" and a.get("hreflang"): s.alts[a["hreflang"]] = a["href"]
        if t == "link" and a.get("rel") in ("icon", "apple-touch-icon", "manifest"): s.links.append(a["href"])
    def handle_data(s, d):
        if s.inld: s.ld.append(d)
        if s.intitle: s.title += d
    def handle_endtag(s, t):
        if t == "script": s.inld = False
        if t == "title": s.intitle = False
issues = collections.Counter(); ex = {}; titles = collections.defaultdict(list); pages = {}
def bad(k, f): issues[k] += 1; ex.setdefault(k, f)
for r, _, fs in os.walk(D):
    for f in fs:
        if not f.endswith(".html") or f == "404.html": continue
        fp = os.path.join(r, f); p = P(); p.feed(open(fp, encoding="utf-8").read())
        rel = "/" + os.path.relpath(r, D).replace(os.sep, "/") + "/"; rel = "/" if rel == "/./" else rel
        pages[rel] = p
        for j in p.ld:
            try: json.loads(j)
            except Exception: bad("invalid JSON-LD", fp)
        if p.h1 != 1: bad("H1 count != 1", fp)
        if not p.title: bad("missing title", fp)
        elif len(p.title) > 65: bad("title > 65 chars", fp)
        d = p.meta.get("description") or ""
        if not d: bad("missing meta description", fp)
        elif len(d) > 160: bad("description > 160 chars", fp)
        if p.canon != BASE + rel: bad("canonical mismatch", fp)
        img = p.meta.get("og:image", "")
        if not img: bad("missing og:image", fp)
        elif not os.path.exists(os.path.join(D, img.replace(BASE + "/", ""))): bad("og:image file missing", fp)
        for l in p.links:
            if not os.path.exists(os.path.join(D, l.lstrip("/"))): bad("icon/manifest file missing", fp)
        for h in p.a:
            if h.startswith(("http", "#", "mailto:")): continue
            t = os.path.normpath(os.path.join(r, h)); t = os.path.join(t, "index.html") if h.endswith("/") else t
            if not os.path.exists(t): bad("broken internal link", fp + " -> " + h)
        if "noindex" not in (p.meta.get("robots") or ""): titles[p.title].append(fp)
# hreflang reciprocity
for rel, p in pages.items():
    for hl, url in p.alts.items():
        tgt = pages.get(url.replace(BASE, ""))
        if tgt is None: bad("hreflang target missing", rel + " -> " + url)
        elif BASE + rel not in tgt.alts.values(): bad("hreflang not reciprocal", rel + " -> " + url)
dups = {t: v for t, v in titles.items() if len(v) > 1}
xml.dom.minidom.parse(os.path.join(D, "sitemap.xml"))
idx = sum(1 for p in pages.values() if "noindex" not in (p.meta.get("robots") or ""))
print(f"pages: {len(pages)}  indexable: {idx}  noindex drafts: {len(pages)-idx}")
print("duplicate titles among indexable pages:", len(dups))
for k, v in issues.items(): print(f"ISSUE {k}: {v}  e.g. {ex[k]}")
if not issues and not dups: print("ALL CHECKS PASSED")
