# -*- coding: utf-8 -*-
"""Static site generator: python3 src/build.py  ->  dist/"""
import html, json, os, posixpath, shutil, sys, urllib.parse
sys.path.insert(0, os.path.dirname(__file__))
from data import (SITE_EMAIL, GSC_VERIFICATION, BING_VERIFICATION, DATE_PUBLISHED, DATE_MODIFIED, BASE_URL, SITE_NAME, DEFAULT_LANG, LANGS, LANG_META, UI, CATEGORIES, DUAS, REVIEWED_LANGS, HIDE_TRANSLIT)
from ui_extra import X, KEYS
for _l in LANGS:
    UI[_l].update(dict(zip(KEYS, X[_l])))
INDEXABLE = [l for l in LANGS if l in REVIEWED_LANGS]

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIST = os.path.join(ROOT, "dist")
import re
E = html.escape
def T(t):
    """Escape a title and isolate (Latin) parentheticals so they render correctly inside RTL text."""
    return re.sub(r"\(([A-Za-z][^)]*)\)", r'<bdi dir="ltr">(\1)</bdi>', E(t))
CAT = {c["id"]: c for c in CATEGORIES}

# time-of-day suggestion: (start hour, end hour, dua id)
TIME_SLOTS = [(4, 10, "waking"), (10, 15, "before-eating"), (15, 20, "anxiety"), (20, 28, "sleeping")]

# ---------- URL helpers ----------
def p_home(l): return f"/{l}/"
def p_cat(l, c): return f"/{l}/category/{c['slug'][l]}/"
def p_dua(l, d): return f"/{l}/{d['slug'][l]}/"
def p_about(l): return f"/{l}/about/"
def absu(p): return BASE_URL.rstrip("/") + p
def rel(frm, to):
    r = posixpath.relpath(to, frm)
    return "./" if r == "." else r + "/"

def trim(txt, n=158):
    txt = " ".join(txt.split())
    if len(txt) <= n: return txt
    cut = txt[:n - 1].rsplit(" ", 1)[0]
    return cut.rstrip(",;:—-") + "…"

def fit_title(main, suffix, n=62):
    full = f"{main} — {suffix}"
    return full if len(full) <= n else main

ORG = {"@type": "Organization", "@id": BASE_URL + "/#org", "name": SITE_NAME, "url": BASE_URL + "/",
       "logo": {"@type": "ImageObject", "url": BASE_URL + "/assets/icons/icon-512.png", "width": 512, "height": 512},
       "email": SITE_EMAIL, "contactPoint": {"@type": "ContactPoint", "email": SITE_EMAIL, "contactType": "customer support",
       "availableLanguage": [LANG_META[l]["name"] for l in LANGS]}}

# ---------- icons (stroke, currentColor) ----------
ICON = {
 "daily": '<path d="M4 11.5 12 5l8 6.5V20a1 1 0 0 1-1 1h-4.5v-5.5h-5V21H5a1 1 0 0 1-1-1z"/>',
 "salah": '<path d="M12 3c2.8 2 5 4.3 5 7.2V11H7v-.8C7 7.3 9.2 5 12 3zM5 11h14v10H5zM10 21v-4a2 2 0 0 1 4 0v4M3 21h18"/>',
 "travel": '<path d="M2.5 19h19M10.5 13.5 4 12l-1.5-3 4 .8L9 8 7 3h2.5l5 5.5 4.6-.9a1.8 1.8 0 0 1 .6 3.5L10.5 13.5z"/>',
 "quran": '<path d="M12 6.5C10 5 7 4.5 3.5 5v13c3.5-.5 6.5 0 8.5 1.5 2-1.5 5-2 8.5-1.5V5C17 4.5 14 5 12 6.5zM12 6.5v13"/>',
 "hardship": '<path d="M12 20s-7.5-4.4-7.5-10A4.3 4.3 0 0 1 12 7.4 4.3 4.3 0 0 1 19.5 10c0 5.6-7.5 10-7.5 10z"/>',
 "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.6 3.8 5.6 3.8 9s-1.3 6.4-3.8 9c-2.5-2.6-3.8-5.6-3.8-9S9.5 5.6 12 3z"/>',
 "search": '<circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/>',
 "copy": '<rect x="8" y="8" width="12" height="12" rx="2"/><path d="M16 8V5a1 1 0 0 0-1-1H5a1 1 0 0 0-1 1v10a1 1 0 0 0 1 1h3"/>',
 "share": '<path d="M12 3a9 9 0 0 0-7.8 13.5L3 21l4.6-1.2A9 9 0 1 0 12 3z"/><path d="M9 9.5c.3 2.3 2.2 4.2 4.5 4.5l1.2-1.2 1.8.8c-.2 1.3-1.2 2-2.4 1.9A6.6 6.6 0 0 1 8 9.4c-.1-1.2.6-2.2 1.9-2.4l.8 1.8z"/>',
 "book": '<path d="M5 4h11a3 3 0 0 1 3 3v13H8a3 3 0 0 1-3-3z"/><path d="M5 17a3 3 0 0 1 3-3h11"/>',
 "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3.5 6.5 8.5 7 8.5-7"/>',
 "prev": '<path d="m15 5-7 7 7 7"/>', "next": '<path d="m9 5 7 7-7 7"/>',
}
def icon(name, cls="ic"):
    return f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICON[name]}</svg>'

# 8-point star (khatam) tile, brass on night
STAR = ("data:image/svg+xml," + urllib.parse.quote(
    '<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 64 64" fill="none" stroke="#C8A24A" stroke-width="1" opacity=".32">'
    '<rect x="20" y="20" width="24" height="24"/><rect x="20" y="20" width="24" height="24" transform="rotate(45 32 32)"/>'
    '<path d="M0 32h8M56 32h8M32 0v8M32 56v8"/></svg>'))

CSS = """
:root{--night:#0F2236;--lapis:#1C4B73;--brass:#C8A24A;--brass-soft:#E9DDB8;--paper:#F2F5F3;--card:#FFFFFF;--ink:#18222E;--muted:#58646F;--line:#D9E1DD;--jade:#1F7A63;--ar-size:2.1rem}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--paper);color:var(--ink);font:1.0625rem/1.65 "Noto Sans","Noto Sans Devanagari","Noto Sans Bengali","Noto Sans Malayalam",system-ui,-apple-system,"Segoe UI",sans-serif}
body.ur,body.ur button,body.ur input{font-family:"Noto Nastaliq Urdu","Jameel Noori Nastaleeq",serif;line-height:2.15}
body.fa,body.ps,body.ar{font-family:"Noto Naskh Arabic","Noto Sans Arabic",system-ui,sans-serif;line-height:1.95}
a{color:var(--lapis)}a:focus-visible,button:focus-visible,input:focus-visible,summary:focus-visible{outline:3px solid var(--brass);outline-offset:2px;border-radius:6px}
.wrap{max-width:920px;margin:0 auto;padding:0 20px}.narrow{max-width:720px}
/* top bar */
.bar{background:var(--night);color:#fff;position:sticky;top:0;z-index:20}
.bar .wrap{display:flex;align-items:center;justify-content:space-between;min-height:60px;gap:12px;position:relative}
.brand{display:flex;align-items:center;gap:10px;color:#fff;text-decoration:none;font-weight:600;font-size:1rem;min-width:0}
.brand b{font-family:Amiri,"Noto Naskh Arabic",serif;font-size:1.55rem;color:var(--brass);font-weight:700;line-height:1}
.brand span{white-space:nowrap;overflow:hidden;text-overflow:ellipsis;opacity:.92}
details.lang>summary{list-style:none;display:flex;align-items:center;gap:6px;cursor:pointer;color:#fff;border:1px solid rgba(255,255,255,.28);padding:6px 12px;border-radius:999px;font-size:.9rem;white-space:nowrap}
details.lang>summary::-webkit-details-marker{display:none}
details.lang .ic{width:18px;height:18px}
.langs{position:absolute;left:12px;right:12px;top:calc(100% + 6px);background:var(--card);color:var(--ink);border-radius:16px;padding:14px;display:grid;grid-template-columns:repeat(auto-fill,minmax(140px,1fr));gap:4px;box-shadow:0 18px 40px rgba(15,34,54,.25)}
.langs a{display:block;padding:8px 10px;border-radius:10px;text-decoration:none;color:var(--ink);font-size:.95rem}
.langs a:hover{background:var(--paper)}.langs a[aria-current]{background:var(--night);color:#fff}
/* hero */
.hero{background:var(--night) url("STAR") repeat;background-size:64px;color:#fff;padding:44px 0 56px}
.hero h1{font-size:clamp(1.7rem,4.2vw,2.5rem);line-height:1.2;margin:0 0 10px;font-weight:700;max-width:22ch}
.hero p{margin:0 0 26px;color:#C9D5E0;max-width:56ch}
.search{display:flex;align-items:center;gap:10px;background:#fff;border-radius:14px;padding:4px 16px;max-width:560px;box-shadow:0 10px 30px rgba(0,0,0,.25)}
.search .ic{width:20px;height:20px;color:var(--muted);flex:none}
.search input{border:0;outline:0;font:inherit;font-size:1.05rem;padding:12px 0;width:100%;background:transparent;color:var(--ink)}
/* now card */
.now{margin-top:-30px;background:var(--card);border-radius:18px;border:1px solid var(--line);padding:22px 24px;display:grid;grid-template-columns:1fr auto;gap:6px 18px;align-items:center;text-decoration:none;color:var(--ink);box-shadow:0 8px 24px rgba(15,34,54,.08);position:relative}
.now small{color:var(--jade);font-weight:600;font-size:.88rem}
.now strong{font-size:1.2rem;display:block}
.now .ar{grid-column:1/-1;font-family:Amiri,"Noto Naskh Arabic",serif;font-size:1.7rem;line-height:1.9;direction:rtl;text-align:right;color:var(--night)}
.now .go{width:42px;height:42px;border-radius:50%;background:var(--night);color:var(--brass);display:grid;place-items:center}
.now .go .ic{width:22px;height:22px}
[dir=rtl] .now .go .ic{transform:scaleX(-1)}
/* sections */
h2{font-size:1.25rem;margin:40px 0 14px}
.cats{display:flex;gap:10px;overflow-x:auto;padding:2px 2px 8px;margin:0;list-style:none;scrollbar-width:thin}
.cats a{display:flex;align-items:center;gap:10px;white-space:nowrap;text-decoration:none;color:var(--ink);background:var(--card);border:1px solid var(--line);border-radius:999px;padding:9px 16px 9px 10px;font-size:.96rem}
.cats a:hover{border-color:var(--lapis)}
.cats .ic{width:30px;height:30px;padding:6px;border-radius:50%;background:var(--night);color:var(--brass);flex:none}
.cats em{font-style:normal;color:var(--muted);font-size:.85rem}
.list{list-style:none;padding:0;margin:0;background:var(--card);border:1px solid var(--line);border-radius:18px;overflow:hidden}
.list li+li{border-top:1px solid var(--line)}
.list a{display:grid;grid-template-columns:1fr minmax(0,44%);gap:16px;align-items:center;padding:15px 20px;text-decoration:none;color:var(--ink)}
.list a:hover{background:#F7FAF8}
.list b{font-weight:600;display:block}.list small{color:var(--muted);display:block;font-size:.9rem;line-height:1.5;margin-top:2px;overflow:hidden;display:-webkit-box;-webkit-line-clamp:1;-webkit-box-orient:vertical}
.list .ar{font-family:Amiri,"Noto Naskh Arabic",serif;direction:rtl;text-align:end;font-size:1.25rem;color:var(--lapis);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
[dir=rtl] .list .ar{text-align:start}
.empty{display:none;padding:22px;color:var(--muted);text-align:center}
/* dua page */
.crumbs{font-size:.88rem;color:var(--muted);margin:22px 0 0}.crumbs a{color:var(--muted)}
.head h1{font-size:clamp(1.6rem,3.6vw,2.2rem);line-height:1.25;margin:10px 0 6px}
.head p{color:var(--muted);margin:0}
.tools{display:flex;flex-wrap:wrap;gap:8px;margin:22px 0 10px;align-items:center}
.chip{font:inherit;font-size:.9rem;border:1px solid var(--line);background:var(--card);color:var(--ink);border-radius:999px;padding:6px 14px;cursor:pointer}
.chip[aria-pressed=true]{background:var(--night);color:#fff;border-color:var(--night)}
.size{display:inline-flex;border:1px solid var(--line);border-radius:999px;overflow:hidden;margin-inline-start:auto}
.size button{font:inherit;border:0;background:var(--card);padding:6px 14px;cursor:pointer;color:var(--ink)}
.size button+button{border-inline-start:1px solid var(--line)}
.panel{position:relative;background:var(--card);border-radius:20px;padding:40px 30px 30px;border:1px solid var(--line)}
.panel::before{content:"";position:absolute;inset:8px;border:1px solid var(--brass-soft);border-radius:14px;pointer-events:none}
.panel .orn{position:absolute;top:-17px;left:50%;transform:translateX(-50%);width:34px;height:34px;background:var(--night) url("STAR") center/48px;border-radius:50%;border:2px solid var(--brass)}
.panel .arabic{font-family:Amiri,"Noto Naskh Arabic","Scheherazade New",serif;font-size:var(--ar-size);line-height:2.05;direction:rtl;text-align:center;margin:0;color:var(--night)}
.panel .tr{margin:22px 0 0;padding-top:18px;border-top:1px dashed var(--line);text-align:center;color:var(--lapis);font-style:italic;font-size:1.05rem}
.panel .mn{margin:16px 0 0;text-align:center;font-size:1.1rem;max-width:60ch;margin-inline:auto}
.hide-tr .tr,.hide-mn .mn{display:none}
.actions{display:flex;gap:10px;margin:16px 0 0;flex-wrap:wrap}
.btn{display:inline-flex;align-items:center;gap:8px;font:inherit;font-size:.95rem;border-radius:12px;padding:10px 16px;border:1px solid var(--line);background:var(--card);color:var(--ink);text-decoration:none;cursor:pointer}
.btn .ic{width:19px;height:19px}.btn.main{background:var(--jade);border-color:var(--jade);color:#fff}
.count{margin-inline-start:auto;display:inline-flex;align-items:center;gap:10px}
.count output{min-width:2.2em;text-align:center;font-weight:700;font-size:1.15rem;color:var(--night)}
.src{display:flex;gap:12px;align-items:flex-start;background:#E9F2EE;border-radius:14px;padding:14px 16px}
.src .ic{width:22px;height:22px;color:var(--jade);flex:none;margin-top:3px}
details.q{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:4px 18px;margin:8px 0}
details.q summary{cursor:pointer;font-weight:600;padding:10px 0}details.q p{margin:0 0 12px;color:var(--muted)}
.pn{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:34px 0 0}
.pn a{display:flex;align-items:center;gap:10px;background:var(--card);border:1px solid var(--line);border-radius:14px;padding:14px;text-decoration:none;color:var(--ink);font-size:.95rem}
.pn a.n{justify-content:flex-end;text-align:end}.pn .ic{width:20px;height:20px;flex:none;color:var(--lapis)}
[dir=rtl] .pn .ic{transform:scaleX(-1)}
footer{margin-top:56px;background:var(--night);color:#C9D5E0;padding:26px 0;font-size:.9rem}
footer a{color:#fff}.fnav{display:flex;flex-wrap:wrap;gap:8px 18px;margin-bottom:10px}
.other{display:flex;flex-wrap:wrap;gap:8px;list-style:none;padding:0;margin:0}.other a{display:inline-block;background:var(--card);border:1px solid var(--line);border-radius:999px;padding:6px 12px;font-size:.88rem;text-decoration:none;color:var(--ink)}
.mailbox{display:flex;gap:10px;align-items:center;background:var(--card);border:1px solid var(--line);border-radius:14px;padding:14px 16px;margin-top:20px}.mailbox .ic{width:22px;height:22px;color:var(--jade)}
@media(max-width:620px){.list a{grid-template-columns:1fr}.list .ar{text-align:start}[dir=rtl] .list .ar{text-align:end}.panel{padding:36px 18px 24px}.count{margin-inline-start:0}.brand span{max-width:52vw}}
@media(prefers-reduced-motion:reduce){*{scroll-behavior:auto!important}}
""".replace("STAR", STAR)

JS = """
(function(){var d=document;function ls(k,v){try{if(v===undefined)return localStorage.getItem(k);localStorage.setItem(k,v)}catch(e){return null}}
var q=d.getElementById('q');if(q){var items=[].slice.call(d.querySelectorAll('[data-s]')),em=d.getElementById('empty');
q.addEventListener('input',function(){var t=q.value.trim().toLowerCase(),n=0;items.forEach(function(li){var ok=!t||li.getAttribute('data-s').indexOf(t)>-1;li.hidden=!ok;if(ok)n++});em.style.display=n?'none':'block'})}
var now=d.getElementById('now');if(now){var h=new Date().getHours();if(h<4)h+=24;var S=JSON.parse(now.getAttribute('data-slots'));
for(var i=0;i<S.length;i++){if(h>=S[i][0]&&h<S[i][1]){var o=S[i][2];now.href=o[0];now.querySelector('strong').innerHTML=o[1];now.querySelector('.ar').textContent=o[2];break}}}
var p=d.getElementById('panel');if(p){var sz=parseFloat(ls('arSize'))||2.1;function setS(v){sz=Math.min(3.4,Math.max(1.5,v));d.documentElement.style.setProperty('--ar-size',sz+'rem');ls('arSize',sz)}setS(sz);
d.querySelectorAll('[data-size]').forEach(function(b){b.addEventListener('click',function(){setS(sz+parseFloat(b.getAttribute('data-size')))})});
d.querySelectorAll('[data-toggle]').forEach(function(b){var c=b.getAttribute('data-toggle');if(ls(c)==='1'){p.classList.add(c);b.setAttribute('aria-pressed','false')}
b.addEventListener('click',function(){var on=p.classList.toggle(c);b.setAttribute('aria-pressed',on?'false':'true');ls(c,on?'1':'0')})});
var c=0,out=d.getElementById('cnt');var cb=d.getElementById('countbtn');if(cb)cb.addEventListener('click',function(){c++;out.value=c;if(navigator.vibrate)try{navigator.vibrate(15)}catch(e){}});
var cp=d.getElementById('copy');if(cp)cp.addEventListener('click',function(){var t=p.innerText;try{navigator.clipboard.writeText(t).then(function(){var l=cp.querySelector('span'),o=l.textContent;l.textContent=cp.getAttribute('data-done');setTimeout(function(){l.textContent=o},1500)})}catch(e){}})}
})();
"""

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&family=Noto+Sans:wght@400;600;700'
         '&family=Noto+Naskh+Arabic:wght@400;600&family=Noto+Nastaliq+Urdu&display=swap">')

HEAD_EXTRA = ('<link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">'
              '<link rel="apple-touch-icon" href="/assets/icons/apple-touch-icon.png"><link rel="manifest" href="/manifest.webmanifest">'
              + (f'<meta name="google-site-verification" content="{GSC_VERIFICATION}">' if GSC_VERIFICATION else "")
              + (f'<meta name="msvalidate.01" content="{BING_VERIFICATION}">' if BING_VERIFICATION else ""))

def alternates(paths):
    out = [f'<link rel="alternate" hreflang="{LANG_META[l]["html"]}" href="{absu(p)}">' for l, p in paths.items() if l in INDEXABLE]
    out.append(f'<link rel="alternate" hreflang="x-default" href="{absu(paths.get(DEFAULT_LANG, "/"))}">')
    return "\n".join(out)

def brand_name(lang):
    return UI[lang]["site_title"].split("—")[0].strip()

def page(lang, path, title, desc, body, alts, jsonld=(), og_type="website", image="/assets/og/default.png", img_alt=None):
    m = LANG_META[lang]; u = UI[lang]; idx = lang in INDEXABLE
    langnav = "".join(
        f'<a href="{rel(path, alts.get(l, p_home(l)))}" hreflang="{LANG_META[l]["html"]}" lang="{LANG_META[l]["html"]}"'
        f'{" aria-current=\"page\"" if l == lang else ""}>{E(LANG_META[l]["native"])}</a>' for l in LANGS)
    ld = "\n".join(f'<script type="application/ld+json">{json.dumps(j, ensure_ascii=False)}</script>' for j in jsonld)
    ogalt = "".join(f'<meta property="og:locale:alternate" content="{LANG_META[l]["og"]}">' for l in alts if l != lang and l in INDEXABLE)
    return f"""<!DOCTYPE html>
<html lang="{m['html']}" dir="{m['dir']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(trim(desc))}">
<link rel="canonical" href="{absu(path)}">
{alternates(alts) if idx else ""}
<meta name="robots" content="{'index,follow,max-image-preview:large' if idx else 'noindex,follow'}">
<meta property="og:type" content="{og_type}"><meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(trim(desc, 200))}">
<meta property="og:image" content="{absu(image)}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="{E(img_alt or title)}">
<meta property="og:url" content="{absu(path)}"><meta property="og:site_name" content="{E(SITE_NAME)}"><meta property="og:locale" content="{m['og']}">{ogalt}
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:image" content="{absu(image)}"><meta name="theme-color" content="#0F2236">
{HEAD_EXTRA}
{FONTS}
<style>{CSS}</style>
{ld}
</head>
<body class="{lang}">
<header class="bar"><div class="wrap">
<a class="brand" href="{rel(path, p_home(lang))}"><b>دعاء</b><span>{E(brand_name(lang))}</span></a>
<details class="lang"><summary aria-label="{E(u['lang_label'])}">{icon('globe')}{E(m['native'])}</summary><nav class="langs" aria-label="{E(u['lang_label'])}">{langnav}</nav></details>
</div></header>
<main>
{body}
</main>
<footer><div class="wrap">
<nav class="fnav" aria-label="{E(u['categories'])}">{"".join(f'<a href="{rel(path, p_cat(lang, c))}">{E(c["name"][lang])}</a>' for c in CATEGORIES)}</nav>
<p><a href="{rel(path, p_home(lang))}">{E(u['home'])}</a> &nbsp;|&nbsp; <a href="{rel(path, p_about(lang))}">{E(u['about'])}</a> &nbsp;|&nbsp; <a href="mailto:{SITE_EMAIL}">{SITE_EMAIL}</a></p>
<p>{E(u['review_note'])} © {DATE_PUBLISHED[:4]} {E(SITE_NAME)}</p>
</div></footer>
<script>{JS}</script>
</body></html>"""

def crumbs(lang, path, items):
    parts, ld = [], []
    for i, (name, p) in enumerate(items, 1):
        parts.append(f'<a href="{rel(path, p)}">{E(name)}</a>' if p and p != path else E(name))
        ld.append({"@type": "ListItem", "position": i, "name": name, "item": absu(p or path)})
    sep = " ‹ " if LANG_META[lang]["dir"] == "rtl" else " › "
    return (f'<nav class="crumbs" aria-label="breadcrumb">{sep.join(parts)}</nav>',
            {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": ld})

def translit(lang, d):
    if lang in HIDE_TRANSLIT:
        return None
    if d.get("translit_l", {}).get(lang):
        return d["translit_l"][lang]
    return d["translit_hi"] if lang == "hi" else d["translit"]

def first_arabic(d):
    return d["arabic"].split(" — ")[0]

def dua_list(lang, path, duas, search=False):
    u = UI[lang]; out = []
    for d in duas:
        s = (d["title"][lang] + " " + d["meaning"][lang] + " " + (translit(lang, d) or "")).lower()
        out.append(f'<li data-s="{E(s)}"><a href="{rel(path, p_dua(lang, d))}"><span><b>{T(d["title"][lang])}</b>'
                   f'<small>{E(d["meaning"][lang])}</small></span><span class="ar" lang="ar">{E(first_arabic(d))}</span></a></li>')
    empty = f'<p class="empty" id="empty">{E(u["none"])}</p>' if search else ""
    return f'<ul class="list">{"".join(out)}</ul>{empty}'

def cat_chips(lang, path):
    u = UI[lang]
    return '<ul class="cats">' + "".join(
        f'<li><a href="{rel(path, p_cat(lang, c))}">{icon(c["id"])}<span>{E(c["name"][lang])}</span>'
        f'<em>{sum(1 for d in DUAS if d["cat"] == c["id"])}</em></a></li>' for c in CATEGORIES) + "</ul>"

# ---------- pages ----------
def build_home(lang):
    u = UI[lang]; path = p_home(lang)
    byid = {d["id"]: d for d in DUAS}
    slots = [[a, b, [rel(path, p_dua(lang, byid[i])), T(byid[i]["title"][lang]), first_arabic(byid[i])]] for a, b, i in TIME_SLOTS]
    d0 = byid["sleeping"]
    body = f"""<section class="hero"><div class="wrap">
<h1>{T(u['home_h1'])}</h1>
<p>{E(u['home_lead'])}</p>
<label class="search">{icon('search')}<input id="q" type="search" placeholder="{E(u['search'])}" aria-label="{E(u['search'])}" autocomplete="off"></label>
</div></section>
<div class="wrap">
<a class="now" id="now" href="{rel(path, p_dua(lang, d0))}" data-slots="{E(json.dumps(slots, ensure_ascii=False))}">
<span><small>{E(u['now'])}</small><strong>{T(d0['title'][lang])}</strong></span><span class="go">{icon('next')}</span>
<span class="ar" lang="ar">{E(first_arabic(d0))}</span></a>
<h2>{E(u['categories'])}</h2>{cat_chips(lang, path)}
<h2>{E(u['all'])}</h2>{dua_list(lang, path, DUAS, search=True)}
</div>"""
    site_ld = {"@context": "https://schema.org", "@graph": [ORG, {"@type": "WebSite", "@id": absu(path) + "#website", "name": u["site_title"],
               "alternateName": SITE_NAME, "url": absu(path), "inLanguage": LANG_META[lang]["html"], "publisher": {"@id": ORG["@id"]}}]}
    return path, page(lang, path, u["site_title"], u["home_meta"], body, {l: p_home(l) for l in LANGS}, [site_ld])

def build_cat(lang, c):
    u = UI[lang]; path = p_cat(lang, c)
    duas = [d for d in DUAS if d["cat"] == c["id"]]
    cr, cr_ld = crumbs(lang, path, [(u["home"], p_home(lang)), (c["name"][lang], None)])
    body = f"""<div class="wrap">{cr}<div class="head"><h1>{E(c['name'][lang])}</h1><p>{E(u['count'].format(n=len(duas)))}</p></div>
<h2>{E(u['all'])}</h2>{dua_list(lang, path, duas)}<h2>{E(u['categories'])}</h2>{cat_chips(lang, path)}</div>"""
    list_ld = {"@context": "https://schema.org", "@type": "ItemList", "itemListElement": [
        {"@type": "ListItem", "position": i, "url": absu(p_dua(lang, d)), "name": d["title"][lang]} for i, d in enumerate(duas, 1)]}
    return path, page(lang, path, fit_title(c['name'][lang], u['site_title']), u["cat_meta"].format(c=c["name"][lang]), body,
                      {l: p_cat(l, c) for l in LANGS}, [cr_ld, list_ld])

def build_dua(lang, d):
    u = UI[lang]; path = p_dua(lang, d); c = CAT[d["cat"]]; t = d["title"][lang]; tr = translit(lang, d)
    i = DUAS.index(d); prv = DUAS[i - 1]; nxt = DUAS[(i + 1) % len(DUAS)]
    cr, cr_ld = crumbs(lang, path, [(u["home"], p_home(lang)), (c["name"][lang], p_cat(lang, c)), (t, None)])
    faqs = [(u["q_meaning"].format(t=t), d["meaning"][lang]), (u["q_when"].format(t=t), d["when"][lang]),
            (u["q_ref"].format(t=t), u["a_ref"].format(r=d["ref"])),
            (u["q_arabic"].format(t=t), d["arabic"] + (f" ({tr})" if tr else ""))]
    faq_html = "".join(f'<details class="q"><summary>{E(q)}</summary><p>{E(a)}</p></details>' for q, a in faqs)
    related = [x for x in DUAS if x["cat"] == d["cat"] and x is not d][:5]
    if len(related) < 4:
        related += [x for x in DUAS if x is not d and x not in related][: 5 - len(related)]
    share = "\n\n".join(x for x in [t, d["arabic"], tr, d["meaning"][lang], absu(path)] if x)
    wa = "https://api.whatsapp.com/send?text=" + urllib.parse.quote(share)
    tr_html = f'<p class="tr" lang="{"hi" if lang == "hi" else "ar-Latn"}" dir="ltr">{E(tr)}</p>' if tr else ""
    tr_btn = f'<button class="chip" type="button" data-toggle="hide-tr" aria-pressed="true">{E(u["translit"])}</button>' if tr else ""
    body = f"""<div class="wrap narrow">{cr}
<article>
<div class="head"><h1>{T(t)}</h1><p>{E(d['when'][lang])}</p></div>
<div class="tools">{tr_btn}<button class="chip" type="button" data-toggle="hide-mn" aria-pressed="true">{E(u['meaning'])}</button>
<span class="size"><button type="button" data-size="-0.25" aria-label="A-">A−</button><button type="button" data-size="0.25" aria-label="A+">A+</button></span></div>
<div class="panel" id="panel"><span class="orn" aria-hidden="true"></span>
<p class="arabic" lang="ar" dir="rtl">{E(d['arabic'])}</p>{tr_html}
<p class="mn">{E(d['meaning'][lang])}</p></div>
<div class="actions">
<button class="btn main" id="copy" type="button" data-done="{E(u['copied'])}">{icon('copy')}<span>{E(u['copy'])}</span></button>
<a class="btn" href="{E(wa)}" target="_blank" rel="noopener">{icon('share')}<span>{E(u['share'])}</span></a>
<span class="count"><button class="btn" id="countbtn" type="button">{E(u['tap'])}</button><output id="cnt">0</output></span>
</div>
<h2>{E(u['reference'])}</h2>
<p class="src">{icon('book')}<span><a href="{E(d['ref_url'])}" target="_blank" rel="noopener">{E(d['ref'])}</a></span></p>
<h2>{E(u['faq'])}</h2>{faq_html}
<nav class="pn"><a href="{rel(path, p_dua(lang, prv))}">{icon('prev')}<span>{E(prv['title'][lang])}</span></a>
<a class="n" href="{rel(path, p_dua(lang, nxt))}"><span>{E(nxt['title'][lang])}</span>{icon('next')}</a></nav>
</article>
<h2>{E(u['related'])}</h2>{dua_list(lang, path, related)}
<h2>{icon('globe')} {E(u['lang_label'])}</h2>
<ul class="other">{"".join(f'<li><a href="{rel(path, p_dua(l, d))}" hreflang="{LANG_META[l]["html"]}" lang="{LANG_META[l]["html"]}" dir="{LANG_META[l]["dir"]}">{E(d["title"][l])}</a></li>' for l in LANGS if l != lang)}</ul>
</div>"""
    art_ld = {"@context": "https://schema.org", "@type": "Article", "headline": t[:110], "inLanguage": LANG_META[lang]["html"],
              "description": trim(d["meaning"][lang]), "mainEntityOfPage": absu(path), "image": absu(f"/assets/og/{d['id']}.png"),
              "datePublished": DATE_PUBLISHED, "dateModified": DATE_MODIFIED, "author": ORG, "publisher": ORG,
              "citation": d["ref"], "isPartOf": {"@id": absu(p_home(lang)) + "#website"}, "about": {"@type": "Thing", "name": "Dua"}}
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}
    return path, page(lang, path, fit_title(t, u['title_suffix']), u["dua_meta"].format(t=t, w=d["when"][lang], r=d["ref"]),
                      body, {l: p_dua(l, d) for l in LANGS}, [cr_ld, art_ld, faq_ld], og_type="article",
                      image=f"/assets/og/{d['id']}.png", img_alt=f"{t}: {first_arabic(d)}")

def build_about(lang):
    u = UI[lang]; path = p_about(lang)
    cr, cr_ld = crumbs(lang, path, [(u["home"], p_home(lang)), (u["about"], None)])
    body = (f'<div class="wrap narrow">{cr}<div class="head"><h1>{E(u["about_h1"])}</h1></div>' + "".join(f"<p>{E(x)}</p>" for x in u["about_body"])
            + f'<p class="mailbox">{icon("mail")}<a href="mailto:{SITE_EMAIL}">{SITE_EMAIL}</a></p></div>')
    ab_ld = {"@context": "https://schema.org", "@graph": [ORG, {"@type": "AboutPage", "url": absu(path), "inLanguage": LANG_META[lang]["html"], "publisher": {"@id": ORG["@id"]}}]}
    return path, page(lang, path, fit_title(u['about'], SITE_NAME), u["about_body"][0], body, {l: p_about(l) for l in LANGS}, [cr_ld, ab_ld])

def build_root():
    links = "".join(f'<li><a href="{rel("/", p_home(l))}" hreflang="{LANG_META[l]["html"]}" lang="{LANG_META[l]["html"]}" dir="{LANG_META[l]["dir"]}">'
                    f'<span><b>{E(LANG_META[l]["native"])}</b><small>{E(UI[l]["site_title"])}</small></span><span class="ar">{E(LANG_META[l]["name"])}</span></a></li>' for l in LANGS)
    alts = "\n".join(f'<link rel="alternate" hreflang="{LANG_META[l]["html"]}" href="{absu(p_home(l))}">' for l in INDEXABLE)
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(SITE_NAME)} — Daily Duas in {len(LANGS)} Languages</title>
<meta name="description" content="Authentic duas from the Quran and Sunnah in {len(LANGS)} languages, with Arabic text, transliteration, meaning and references.">
<link rel="canonical" href="{absu('/')}">
<meta name="theme-color" content="#0F2236">{HEAD_EXTRA}<meta property="og:image" content="{absu('/assets/og/default.png')}"><meta name="twitter:card" content="summary_large_image">{FONTS}<style>{CSS}</style>
<script type="application/ld+json">{json.dumps({"@context": "https://schema.org", "@graph": [ORG, {"@type": "WebSite", "@id": absu("/") + "#website", "name": SITE_NAME, "url": absu("/"), "publisher": {"@id": ORG["@id"]}, "inLanguage": [LANG_META[l]["html"] for l in LANGS]}]}, ensure_ascii=False)}</script></head><body>
<section class="hero"><div class="wrap"><h1>{E(SITE_NAME)}</h1><p>{" · ".join(E(UI[l]["choose"]) for l in LANGS[:8])}</p></div></section>
<main class="wrap"><h2>{E(UI['en']['choose'])}</h2><ul class="list">{links}</ul></main></body></html>"""

def sitemap(entries, images=None):
    urls = []
    for alts in entries:
        alts = {l: p for l, p in alts.items() if l in INDEXABLE}
        links = "".join(f'<xhtml:link rel="alternate" hreflang="{LANG_META[l]["html"]}" href="{absu(p)}"/>' for l, p in alts.items())
        links += f'<xhtml:link rel="alternate" hreflang="x-default" href="{absu(alts[DEFAULT_LANG])}"/>'
        img = (images or {}).get(alts[DEFAULT_LANG])
        im = f"<image:image><image:loc>{absu(img)}</image:loc></image:image>" if img else ""
        for l, p in alts.items():
            urls.append(f"<url><loc>{absu(p)}</loc><lastmod>{DATE_MODIFIED}</lastmod>{links}{im}</url>")
    return ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
            'xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n' + "\n".join(urls) + "\n</urlset>\n")

def write(path, content):
    fp = os.path.join(DIST, path.lstrip("/"), "index.html") if path.endswith("/") else os.path.join(DIST, path.lstrip("/"))
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    with open(fp, "w", encoding="utf-8") as f:
        f.write(content)

def main():
    for d in DUAS:
        for l in LANGS:
            for k in ("slug", "title", "meaning", "when"):
                assert d[k].get(l), f"missing {k}[{l}] for {d['id']}"
    for l in LANGS:
        slugs = [d["slug"][l] for d in DUAS] + ["category", "about"]
        assert len(slugs) == len(set(slugs)), f"duplicate slug in {l}"
    if os.path.exists(DIST):
        shutil.rmtree(DIST)
    count = 0
    for lang in LANGS:
        jobs = [lambda: build_home(lang), lambda: build_about(lang)] + [lambda c=c: build_cat(lang, c) for c in CATEGORIES] + \
               [lambda d=d: build_dua(lang, d) for d in DUAS]
        for job in jobs:
            p, h = job(); write(p, h); count += 1
    write("/", build_root()); count += 1
    sets = [{l: p_home(l) for l in LANGS}, {l: p_about(l) for l in LANGS}] + \
           [{l: p_cat(l, c) for l in LANGS} for c in CATEGORIES] + [{l: p_dua(l, d) for l in LANGS} for d in DUAS]
    write("/sitemap.xml", sitemap(sets, {p_dua(DEFAULT_LANG, d): f"/assets/og/{d['id']}.png" for d in DUAS}))
    shutil.copytree(os.path.join(ROOT, "static"), DIST, dirs_exist_ok=True)
    write("/manifest.webmanifest", json.dumps({"name": SITE_NAME, "short_name": "Duaien", "start_url": "/", "display": "standalone",
          "background_color": "#0F2236", "theme_color": "#0F2236", "icons": [
          {"src": "/assets/icons/icon-192.png", "sizes": "192x192", "type": "image/png"},
          {"src": "/assets/icons/icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any maskable"}]}, indent=1))
    write("/_headers", "/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n  X-Frame-Options: SAMEORIGIN\n"
          "/assets/*\n  Cache-Control: public, max-age=31536000, immutable\n/*.html\n  Cache-Control: public, max-age=0, must-revalidate\n")
    write("/robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {absu('/sitemap.xml')}\n")
    write("/404.html", build_root().replace(f"<h1>{E(SITE_NAME)}</h1>", f"<h1>404 · {E(SITE_NAME)}</h1>", 1))
    print(f"built {count} pages for {len(LANGS)} languages into {DIST}")

if __name__ == "__main__":
    main()
