# Duas of the Sunnah: multilingual static site

This is a static site of authentic duas with SEO built in. It is in **24 languages**:
English, Arabic, Urdu (with Roman Urdu), Hindi, Bengali, Indonesian, Malay, Turkish, Persian, Pashto, French, Spanish, German, Russian, Chinese (Simplified), Portuguese, Swahili, Hausa, Somali, Uzbek, Azerbaijani, Bosnian, Albanian and Malayalam.

## Review workflow (important for SEO)
- `REVIEWED_LANGS` in `src/data.py` lists the languages that are live for Google. At the moment these are en, ur, hi and id.
- Every other language is built, but as a **draft**. Draft pages carry `noindex` and are left out of the hreflang tags and the sitemap. Unreviewed machine-quality religious text would hurt trust, so it is kept away from Google until checked.
- Once a native speaker who reads Arabic has checked a language pack in `src/packs/`, add its code to `REVIEWED_LANGS` and rebuild. That language then gets hreflang tags and is listed in the sitemap.
- Hausa, Somali, Uzbek, Pashto and Malayalam need the most careful review.

## Add another language
1. Copy any pack in `src/packs/` and translate it. A pack holds the UI strings, 5 category names and slugs, and 18 duas, each with a slug, title, meaning and when-to-recite text. An optional 5th field per dua is a local transliteration.
2. Import the new pack in `data.py` and add its code to the `LANGS` order list.
3. Run `python3 src/build.py`. The build stops if any dua or category is missing.

## Build
    python3 src/build.py      # writes dist/ (no dependencies)

You can deploy `dist/` to any static host, such as Cloudflare Pages, Netlify, Vercel or GitHub Pages.

## Before going live
1. Set `BASE_URL` in `src/data.py` to the real domain and rebuild.
2. **Have a qualified scholar review every Arabic text, translation and reference.** Religious content must not go live unreviewed.
3. Submit `sitemap.xml` in Google Search Console and Bing Webmaster Tools.

## What's built in (SEO)
- Language subfolders `/en/ /ur/ /hi/ /id/`, with slugs in each language's own search wording, for example `/ur/sone-ki-dua/` and `/id/doa-sebelum-tidur/`.
- hreflang on every page, plus x-default pointing to the language chooser at `/`. There is no IP redirect.
- `lang` and `dir="rtl"` set for Urdu. The Arabic text is marked up with `lang="ar"`.
- JSON-LD: BreadcrumbList, Article, FAQPage, ItemList and WebSite.
- A canonical URL, Open Graph locales, an XML sitemap with xhtml:link alternates, and robots.txt.
- One H1 per page, question-style FAQs, related-dua links, and every dua within two clicks of the home page.
- Inline CSS and a tiny script, with no framework, so pages load fast on mobile.

## Add content
Add a dict to `DUAS` in `src/data.py`. The build refuses to run if any language field is missing or a slug is duplicated.
To add a language, add its code to `LANGS`, fill in `LANG_META` and `UI`, and add the language to every dua and category.

## Next
Add audio recitation (an `audio_url` field plus AudioObject schema), the remaining approximately 190 duas, topic hubs for Ramadan, Hajj and morning and evening adhkar, printable cards, and Bengali and Arabic.
