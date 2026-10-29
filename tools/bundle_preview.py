"""Bundle dist/ into ONE self-contained preview page with #pN hash routing."""
import os, re, json, posixpath, sys
DIST = sys.argv[1]; OUT = sys.argv[2]
pages = {}
for r, _, fs in os.walk(DIST):
    for f in fs:
        if f == "index.html":
            key = posixpath.relpath(r, DIST).replace(os.sep, "/")
            pages["" if key == "." else key + "/"] = open(os.path.join(r, f), encoding="utf-8").read()
keys = sorted(pages); ids = {k: f"p{i}" for i, k in enumerate(keys)}
css = re.search(r"<style>(.*?)</style>", pages["en/"], re.S).group(1)
data = {}
for k, h in pages.items():
    lang = re.search(r'<html lang="([^"]+)"', h); d = re.search(r'dir="(rtl|ltr)"', h)
    title = re.search(r"<title>(.*?)</title>", h, re.S).group(1)
    bm = re.search(r"<body([^>]*)>(.*)</body>", h, re.S)
    cls = re.search(r'class="([^"]*)"', bm.group(1)) if bm else None
    body = re.sub(r"<script.*?</script>", "", bm.group(2) if bm else h, flags=re.S)
    def fix(m):
        href = m.group(1)
        if href.startswith(("http", "#", "mailto:")): return m.group(0)
        tgt = posixpath.normpath(posixpath.join("/" + k, href)).lstrip("/")
        tgt = "" if tgt in (".", "") else tgt + "/"
        return f'href="#{ids[tgt]}"' if tgt in ids else m.group(0)
    body = re.sub(r'href="([^"]*)"', fix, body)
    data[ids[k]] = [lang.group(1) if lang else "en", d.group(1) if d else "ltr", title, cls.group(1) if cls else "", body]
html = f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Duas of the Sunnah — multilingual site preview</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&family=Noto+Nastaliq+Urdu&display=swap">
<style>{css}</style></head><body><div id="app"></div>
<script>var P={json.dumps(data, ensure_ascii=False)};
function go(){{var id=(location.hash||'#p0').slice(1);var p=P[id]||P.p0;document.documentElement.lang=p[0];document.documentElement.dir=p[1];
document.title=p[2].replace(/&amp;/g,'&');document.body.className=p[3];document.getElementById('app').innerHTML=p[4];window.scrollTo(0,0);}}
window.addEventListener('hashchange',go);go();
document.addEventListener('click',function(e){{var b=e.target.closest('[data-copy]');if(!b)return;var t=document.getElementById(b.getAttribute('data-copy')).innerText;
try{{navigator.clipboard.writeText(t).then(function(){{var o=b.textContent;b.textContent=b.dataset.done;setTimeout(function(){{b.textContent=o}},1500)}})}}catch(_){{}}}});
</script></body></html>"""
open(OUT, "w", encoding="utf-8").write(html)
print(len(data), "pages,", round(len(html.encode())/1e6, 2), "MB")
