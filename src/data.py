# -*- coding: utf-8 -*-
"""Dua content database.

Each dua is stored once; every language is a set of translated fields.
To add a language: add its code to LANGS, its UI strings to UI, and
fill title/slug/meaning/when for that code in every dua and category.

IMPORTANT: Religious text. Every Arabic text, translation and reference
must be reviewed by a qualified scholar before publishing (see
`reviewed` flag). Machine translation is not acceptable.
"""

BASE_URL = "https://masnoonduaien.online"
SITE_NAME = "Masnoon Duaien"
SITE_EMAIL = "harrisarsha1994@gmail.com"      # business contact (About page + Organization schema)
GSC_VERIFICATION = ""    # paste the Google Search Console HTML-tag code here, e.g. "abc123..."
BING_VERIFICATION = ""   # paste the Bing Webmaster Tools msvalidate.01 code here
DATE_PUBLISHED = "2026-10-29"
DATE_MODIFIED = "2026-10-29"
DEFAULT_LANG = "en"
LANGS = ["en", "ur", "hi", "id"]

LANG_META = {
    "en": {"name": "English", "native": "English", "dir": "ltr", "html": "en", "og": "en_GB"},
    "ur": {"name": "Urdu", "native": "اردو", "dir": "rtl", "html": "ur", "og": "ur_PK"},
    "hi": {"name": "Hindi", "native": "हिन्दी", "dir": "ltr", "html": "hi", "og": "hi_IN"},
    "id": {"name": "Indonesian", "native": "Bahasa Indonesia", "dir": "ltr", "html": "id", "og": "id_ID"},
}

UI = {
    "en": {
        "site_title": "Daily Duas from the Quran & Sunnah",
        "home_h1": "Daily Duas from the Quran & Sunnah",
        "home_lead": "Authentic duas for everyday life with Arabic text, transliteration, English meaning and the hadith or Quran reference for each one.",
        "home_meta": "Authentic daily duas with Arabic text, transliteration, English translation and hadith references. Duas for sleeping, eating, travel, salah, Ramadan and hardship.",
        "categories": "Browse by category", "all": "All duas", "arabic": "Arabic",
        "translit": "Transliteration", "meaning": "Meaning", "when": "When to recite",
        "reference": "Reference", "related": "Related duas", "faq": "Frequently asked questions",
        "home": "Home", "copy": "Copy dua", "share": "Share on WhatsApp", "copied": "Copied",
        "about": "About & editorial policy", "lang_label": "Language",
        "review_note": "Text and references checked against the cited source.",
        "q_meaning": "What is the meaning of {t}?", "q_when": "When should {t} be recited?",
        "q_ref": "Where is {t} mentioned?", "q_arabic": "What is {t} in Arabic?",
        "a_ref": "It is recorded in {r}.",
        "cat_meta": "{c}: authentic duas with Arabic text, transliteration, English meaning and references.",
        "dua_meta": "{t} in Arabic with transliteration and English meaning. {w} Reference: {r}.",
        "title_suffix": "Arabic, Transliteration & Meaning",
        "count": "{n} duas",
        "about_h1": "About this site and our editorial policy",
        "about_body": [
            "Every dua on this site comes from the Quran or a hadith collection, and the reference is shown on the page with a link to the source.",
            "Translations are written by people, not machines, and each language version is checked by a reviewer who reads both Arabic and that language.",
            "If you find a mistake in any text, translation or reference, please contact us so we can correct it.",
        ],
        "choose": "Choose your language",
    },
    "ur": {
        "site_title": "مسنون دعائیں — قرآن و سنت کی روزمرہ دعائیں",
        "home_h1": "مسنون دعائیں (Masnoon Duain) — اردو ترجمہ کے ساتھ",
        "home_lead": "روزمرہ زندگی کی مستند دعائیں: عربی متن، رومن اردو تلفظ، اردو ترجمہ اور ہر دعا کا حوالہ۔",
        "home_meta": "مسنون دعائیں عربی متن، رومن اردو تلفظ اور اردو ترجمہ کے ساتھ۔ سونے، کھانے، سفر، نماز، رمضان اور پریشانی کی دعائیں حوالہ کے ساتھ۔ Masnoon Duain in Urdu.",
        "categories": "زمرہ جات", "all": "تمام دعائیں", "arabic": "عربی",
        "translit": "تلفظ (Roman Urdu)", "meaning": "اردو ترجمہ", "when": "کب پڑھیں",
        "reference": "حوالہ", "related": "مزید دعائیں", "faq": "عام سوالات",
        "home": "ہوم", "copy": "دعا کاپی کریں", "share": "واٹس ایپ پر شیئر کریں", "copied": "کاپی ہو گئی",
        "about": "ہمارے بارے میں اور ادارتی پالیسی", "lang_label": "زبان",
        "review_note": "متن اور حوالہ اصل ماخذ سے ملا کر چیک کیا گیا ہے۔",
        "q_meaning": "{t} کا مطلب کیا ہے؟", "q_when": "{t} کب پڑھی جاتی ہے؟",
        "q_ref": "{t} کا حوالہ کیا ہے؟", "q_arabic": "{t} عربی میں کیا ہے؟",
        "a_ref": "یہ دعا {r} میں موجود ہے۔",
        "cat_meta": "{c}: مستند مسنون دعائیں عربی متن، تلفظ اور اردو ترجمہ کے ساتھ۔",
        "dua_meta": "{t} عربی متن، رومن اردو تلفظ اور اردو ترجمہ کے ساتھ۔ {w} حوالہ: {r}۔",
        "title_suffix": "عربی، اردو ترجمہ اور حوالہ",
        "count": "{n} دعائیں",
        "about_h1": "ہمارے بارے میں اور ادارتی پالیسی",
        "about_body": [
            "اس ویب سائٹ کی ہر دعا قرآن مجید یا حدیث کی کتاب سے لی گئی ہے، اور ہر صفحے پر اس کا حوالہ اور ماخذ کا لنک موجود ہے۔",
            "ترجمے مشین سے نہیں بلکہ انسانوں نے لکھے ہیں، اور ہر زبان کا ترجمہ عربی جاننے والے نظرثانی کرنے والے نے چیک کیا ہے۔",
            "اگر آپ کو کسی متن، ترجمے یا حوالے میں غلطی نظر آئے تو براہ کرم ہم سے رابطہ کریں۔",
        ],
        "choose": "زبان منتخب کریں",
    },
    "hi": {
        "site_title": "मसनून दुआएं — क़ुरआन और सुन्नत की रोज़ाना की दुआएं",
        "home_h1": "मसनून दुआएं हिंदी में — अरबी, उच्चारण और मतलब",
        "home_lead": "रोज़मर्रा की ज़िंदगी की सही दुआएं: अरबी इबारत, हिंदी में उच्चारण, हिंदी मतलब और हर दुआ का हवाला।",
        "home_meta": "मसनून दुआएं हिंदी में: अरबी इबारत, हिंदी उच्चारण और मतलब के साथ। सोने, खाने, सफ़र, नमाज़, रमज़ान और परेशानी की दुआएं हवाले के साथ।",
        "categories": "श्रेणियां", "all": "सभी दुआएं", "arabic": "अरबी",
        "translit": "हिंदी में उच्चारण", "meaning": "हिंदी मतलब", "when": "कब पढ़ें",
        "reference": "हवाला", "related": "और दुआएं", "faq": "अक्सर पूछे जाने वाले सवाल",
        "home": "होम", "copy": "दुआ कॉपी करें", "share": "WhatsApp पर शेयर करें", "copied": "कॉपी हो गई",
        "about": "हमारे बारे में और संपादकीय नीति", "lang_label": "भाषा",
        "review_note": "इबारत और हवाला असल स्रोत से मिलाकर जांचा गया है।",
        "q_meaning": "{t} का मतलब क्या है?", "q_when": "{t} कब पढ़ी जाती है?",
        "q_ref": "{t} का हवाला क्या है?", "q_arabic": "{t} अरबी में क्या है?",
        "a_ref": "यह दुआ {r} में दर्ज है।",
        "cat_meta": "{c}: अरबी इबारत, हिंदी उच्चारण और मतलब के साथ सही मसनून दुआएं।",
        "dua_meta": "{t} अरबी इबारत, हिंदी उच्चारण और मतलब के साथ। {w} हवाला: {r}।",
        "title_suffix": "अरबी, हिंदी उच्चारण और मतलब",
        "count": "{n} दुआएं",
        "about_h1": "हमारे बारे में और संपादकीय नीति",
        "about_body": [
            "इस वेबसाइट की हर दुआ क़ुरआन या हदीस की किताब से ली गई है, और हर पेज पर उसका हवाला और स्रोत का लिंक दिया गया है।",
            "अनुवाद मशीन से नहीं बल्कि इंसानों ने लिखे हैं, और हर भाषा का अनुवाद अरबी जानने वाले समीक्षक ने जांचा है।",
            "अगर आपको किसी इबारत, अनुवाद या हवाले में ग़लती मिले तो कृपया हमसे संपर्क करें।",
        ],
        "choose": "अपनी भाषा चुनें",
    },
    "id": {
        "site_title": "Doa Sehari-hari dari Al-Qur'an dan Sunnah",
        "home_h1": "Doa Sehari-hari: Arab, Latin dan Artinya",
        "home_lead": "Kumpulan doa sehari-hari yang shahih lengkap dengan tulisan Arab, latin, arti dalam Bahasa Indonesia dan sumber hadis atau ayatnya.",
        "home_meta": "Kumpulan doa sehari-hari lengkap tulisan Arab, latin dan artinya beserta sumber hadis. Doa sebelum tidur, doa makan, doa naik kendaraan, doa masuk masjid dan lainnya.",
        "categories": "Kategori doa", "all": "Semua doa", "arabic": "Arab",
        "translit": "Latin", "meaning": "Artinya", "when": "Kapan dibaca",
        "reference": "Sumber", "related": "Doa lainnya", "faq": "Pertanyaan yang sering diajukan",
        "home": "Beranda", "copy": "Salin doa", "share": "Bagikan ke WhatsApp", "copied": "Tersalin",
        "about": "Tentang kami & kebijakan redaksi", "lang_label": "Bahasa",
        "review_note": "Teks dan sumber telah dicocokkan dengan rujukan aslinya.",
        "q_meaning": "Apa arti {t}?", "q_when": "Kapan {t} dibaca?",
        "q_ref": "Apa sumber {t}?", "q_arabic": "Bagaimana tulisan Arab {t}?",
        "a_ref": "Doa ini diriwayatkan dalam {r}.",
        "cat_meta": "{c}: kumpulan doa shahih lengkap Arab, latin, arti dan sumbernya.",
        "dua_meta": "{t} lengkap tulisan Arab, latin dan artinya. {w} Sumber: {r}.",
        "title_suffix": "Arab, Latin dan Artinya",
        "count": "{n} doa",
        "about_h1": "Tentang kami dan kebijakan redaksi",
        "about_body": [
            "Setiap doa di situs ini berasal dari Al-Qur'an atau kitab hadis, dan sumbernya dicantumkan di setiap halaman beserta tautan ke rujukan.",
            "Terjemahan ditulis oleh manusia, bukan mesin, dan setiap versi bahasa diperiksa oleh peninjau yang memahami bahasa Arab.",
            "Jika Anda menemukan kesalahan pada teks, terjemahan atau sumber, silakan hubungi kami agar dapat kami perbaiki.",
        ],
        "choose": "Pilih bahasa",
    },
}

CATEGORIES = [
    {"id": "daily", "slug": {"en": "daily-life", "ur": "rozmarra-ki-duain", "hi": "rozana-ki-duaen", "id": "doa-harian"},
     "name": {"en": "Daily life duas", "ur": "روزمرہ کی دعائیں", "hi": "रोज़ाना की दुआएं", "id": "Doa harian"}},
    {"id": "salah", "slug": {"en": "salah-and-masjid", "ur": "namaz-aur-masjid", "hi": "namaz-aur-masjid", "id": "doa-sholat-dan-masjid"},
     "name": {"en": "Salah, wudu & masjid", "ur": "نماز، وضو اور مسجد", "hi": "नमाज़, वज़ू और मस्जिद", "id": "Doa wudhu, sholat & masjid"}},
    {"id": "travel", "slug": {"en": "travel-and-ramadan", "ur": "safar-aur-ramzan", "hi": "safar-aur-ramzan", "id": "doa-safar-dan-puasa"},
     "name": {"en": "Travel & Ramadan", "ur": "سفر اور رمضان", "hi": "सफ़र और रमज़ान", "id": "Doa safar & puasa"}},
    {"id": "quran", "slug": {"en": "quranic-duas", "ur": "qurani-duain", "hi": "qurani-duaen", "id": "doa-dari-al-quran"},
     "name": {"en": "Duas from the Quran", "ur": "قرآنی دعائیں", "hi": "क़ुरआनी दुआएं", "id": "Doa dari Al-Qur'an"}},
    {"id": "hardship", "slug": {"en": "hardship-and-worry", "ur": "pareshani-ki-duain", "hi": "pareshani-ki-duaen", "id": "doa-saat-kesulitan"},
     "name": {"en": "Hardship & worry", "ur": "پریشانی اور مشکل کی دعائیں", "hi": "परेशानी और मुश्किल की दुआएं", "id": "Doa saat sedih & kesulitan"}},
]

SUNNAH = "https://sunnah.com/"
QURAN = "https://quran.com/"

DUAS = [
    {
        "id": "sleeping", "cat": "daily",
        "arabic": "بِاسْمِكَ اللَّهُمَّ أَمُوتُ وَأَحْيَا",
        "translit": "Bismika Allahumma amootu wa ahya",
        "translit_hi": "बिस्मिका अल्लाहुम्मा अमूतु व अह्या",
        "ref": "Sahih al-Bukhari 6324", "ref_url": SUNNAH + "bukhari:6324",
        "slug": {"en": "dua-before-sleeping", "ur": "sone-ki-dua", "hi": "sone-ki-dua", "id": "doa-sebelum-tidur"},
        "title": {"en": "Dua before sleeping", "ur": "سونے کی دعا (Sone Ki Dua)", "hi": "सोने की दुआ", "id": "Doa sebelum tidur"},
        "meaning": {"en": "In Your name, O Allah, I die and I live.",
                    "ur": "اے اللہ! تیرے ہی نام کے ساتھ میں مرتا (سوتا) ہوں اور جیتا (جاگتا) ہوں۔",
                    "hi": "ऐ अल्लाह! तेरे ही नाम से मैं मरता (सोता) हूं और जीता (जागता) हूं।",
                    "id": "Dengan nama-Mu ya Allah, aku mati dan aku hidup."},
        "when": {"en": "When lying down in bed to sleep.", "ur": "رات کو بستر پر لیٹ کر سونے سے پہلے۔",
                 "hi": "रात को बिस्तर पर लेटकर सोने से पहले।", "id": "Ketika berbaring di tempat tidur sebelum tidur."},
    },
    {
        "id": "waking", "cat": "daily",
        "arabic": "الْحَمْدُ لِلَّهِ الَّذِي أَحْيَانَا بَعْدَ مَا أَمَاتَنَا وَإِلَيْهِ النُّشُورُ",
        "translit": "Alhamdu lillahil-ladhi ahyana ba'da ma amatana wa ilayhin-nushoor",
        "translit_hi": "अल्हम्दु लिल्लाहिल्लज़ी अह्याना बादा मा अमातना व इलैहिन्नुशूर",
        "ref": "Sahih al-Bukhari 6324", "ref_url": SUNNAH + "bukhari:6324",
        "slug": {"en": "dua-after-waking-up", "ur": "jagne-ki-dua", "hi": "jagne-ki-dua", "id": "doa-bangun-tidur"},
        "title": {"en": "Dua after waking up", "ur": "جاگنے کی دعا (Jagne Ki Dua)", "hi": "जागने की दुआ", "id": "Doa bangun tidur"},
        "meaning": {"en": "All praise is for Allah, who gave us life after He caused us to die, and to Him is the return.",
                    "ur": "تمام تعریفیں اللہ کے لیے ہیں جس نے ہمیں مارنے (سلانے) کے بعد زندہ کیا، اور اسی کی طرف اٹھ کر جانا ہے۔",
                    "hi": "सब तारीफ़ अल्लाह के लिए है जिसने हमें मौत (नींद) के बाद ज़िंदगी दी, और उसी की तरफ़ लौटकर जाना है।",
                    "id": "Segala puji bagi Allah yang telah menghidupkan kami setelah mematikan kami, dan kepada-Nya kami kembali."},
        "when": {"en": "Right after waking up from sleep.", "ur": "نیند سے جاگتے ہی۔",
                 "hi": "नींद से जागते ही।", "id": "Segera setelah bangun tidur."},
    },
    {
        "id": "before-eating", "cat": "daily",
        "arabic": "بِسْمِ اللَّهِ — (وَإِنْ نَسِيَ فِي أَوَّلِهِ) بِسْمِ اللَّهِ أَوَّلَهُ وَآخِرَهُ",
        "translit": "Bismillah. (If forgotten at the start:) Bismillahi awwalahu wa akhirahu",
        "translit_hi": "बिस्मिल्लाह। (शुरू में भूल जाएं तो:) बिस्मिल्लाहि अव्वलहू व आख़िरहू",
        "ref": "Sunan Abi Dawud 3767; Jami at-Tirmidhi 1858", "ref_url": SUNNAH + "abudawud:3767",
        "slug": {"en": "dua-before-eating", "ur": "khana-khane-ki-dua", "hi": "khana-khane-ki-dua", "id": "doa-sebelum-makan"},
        "title": {"en": "Dua before eating", "ur": "کھانا کھانے کی دعا (Khana Khane Ki Dua)", "hi": "खाना खाने की दुआ", "id": "Doa sebelum makan"},
        "meaning": {"en": "In the name of Allah. (If forgotten:) In the name of Allah, at its beginning and at its end.",
                    "ur": "اللہ کے نام سے۔ (اگر شروع میں بھول جائے تو:) اللہ کے نام سے اس کے شروع میں بھی اور آخر میں بھی۔",
                    "hi": "अल्लाह के नाम से। (अगर शुरू में भूल जाएं तो:) अल्लाह के नाम से, इसके शुरू में भी और आख़िर में भी।",
                    "id": "Dengan nama Allah. (Jika lupa di awal:) Dengan nama Allah di awal dan di akhirnya."},
        "when": {"en": "Before the first bite; the second form if you forgot at the start.",
                 "ur": "کھانے کا پہلا لقمہ لینے سے پہلے؛ بھول جائیں تو یاد آنے پر دوسری دعا۔",
                 "hi": "खाने का पहला निवाला लेने से पहले; भूल जाएं तो याद आने पर दूसरी दुआ।",
                 "id": "Sebelum suapan pertama; bacaan kedua jika lupa di awal."},
    },
    {
        "id": "after-eating", "cat": "daily",
        "arabic": "الْحَمْدُ لِلَّهِ الَّذِي أَطْعَمَنِي هَذَا وَرَزَقَنِيهِ مِنْ غَيْرِ حَوْلٍ مِنِّي وَلَا قُوَّةٍ",
        "translit": "Alhamdu lillahil-ladhi at'amani hadha wa razaqanihi min ghayri hawlin minni wa la quwwah",
        "translit_hi": "अल्हम्दु लिल्लाहिल्लज़ी अत्अमनी हाज़ा व रज़क़नीहि मिन ग़ैरि हौलिम्मिन्नी व ला क़ुव्वह",
        "ref": "Sunan Abi Dawud 4023; Jami at-Tirmidhi 3458", "ref_url": SUNNAH + "abudawud:4023",
        "slug": {"en": "dua-after-eating", "ur": "khana-khane-ke-baad-ki-dua", "hi": "khana-khane-ke-baad-ki-dua", "id": "doa-sesudah-makan"},
        "title": {"en": "Dua after eating", "ur": "کھانا کھانے کے بعد کی دعا", "hi": "खाना खाने के बाद की दुआ", "id": "Doa sesudah makan"},
        "meaning": {"en": "All praise is for Allah, who fed me this and provided it for me without any power or strength from me.",
                    "ur": "تمام تعریفیں اللہ کے لیے ہیں جس نے مجھے یہ کھلایا اور میری کسی طاقت اور قوت کے بغیر مجھے یہ رزق دیا۔",
                    "hi": "सब तारीफ़ अल्लाह के लिए है जिसने मुझे यह खिलाया और मेरी किसी ताक़त और क़ुव्वत के बग़ैर मुझे यह रिज़्क़ दिया।",
                    "id": "Segala puji bagi Allah yang telah memberiku makanan ini dan memberikannya kepadaku tanpa daya dan kekuatan dariku."},
        "when": {"en": "After finishing a meal.", "ur": "کھانا ختم کرنے کے بعد۔",
                 "hi": "खाना ख़त्म करने के बाद।", "id": "Setelah selesai makan."},
    },
    {
        "id": "leaving-home", "cat": "daily",
        "arabic": "بِسْمِ اللَّهِ تَوَكَّلْتُ عَلَى اللَّهِ، وَلَا حَوْلَ وَلَا قُوَّةَ إِلَّا بِاللَّهِ",
        "translit": "Bismillahi tawakkaltu 'alallah, wa la hawla wa la quwwata illa billah",
        "translit_hi": "बिस्मिल्लाहि तवक्कल्तु अलल्लाह, व ला हौला व ला क़ुव्वता इल्ला बिल्लाह",
        "ref": "Sunan Abi Dawud 5095; Jami at-Tirmidhi 3426", "ref_url": SUNNAH + "abudawud:5095",
        "slug": {"en": "dua-for-leaving-the-house", "ur": "ghar-se-nikalne-ki-dua", "hi": "ghar-se-nikalne-ki-dua", "id": "doa-keluar-rumah"},
        "title": {"en": "Dua for leaving the house", "ur": "گھر سے نکلنے کی دعا", "hi": "घर से निकलने की दुआ", "id": "Doa keluar rumah"},
        "meaning": {"en": "In the name of Allah, I place my trust in Allah, and there is no power and no strength except with Allah.",
                    "ur": "اللہ کے نام سے، میں نے اللہ پر بھروسہ کیا، اور اللہ کے بغیر نہ کوئی طاقت ہے نہ قوت۔",
                    "hi": "अल्लाह के नाम से, मैंने अल्लाह पर भरोसा किया, और अल्लाह के बग़ैर न कोई ताक़त है न क़ुव्वत।",
                    "id": "Dengan nama Allah, aku bertawakal kepada Allah, tiada daya dan kekuatan kecuali dengan pertolongan Allah."},
        "when": {"en": "When stepping out of your home.", "ur": "گھر سے باہر نکلتے وقت۔",
                 "hi": "घर से बाहर निकलते वक़्त।", "id": "Ketika keluar dari rumah."},
    },
    {
        "id": "entering-toilet", "cat": "daily",
        "arabic": "اللَّهُمَّ إِنِّي أَعُوذُ بِكَ مِنَ الْخُبُثِ وَالْخَبَائِثِ",
        "translit": "Allahumma inni a'udhu bika minal-khubuthi wal-khaba'ith",
        "translit_hi": "अल्लाहुम्मा इन्नी अऊज़ु बिका मिनल ख़ुबुसि वल ख़बाइस",
        "ref": "Sahih al-Bukhari 142; Sahih Muslim 375", "ref_url": SUNNAH + "bukhari:142",
        "slug": {"en": "dua-for-entering-the-toilet", "ur": "baitul-khala-mein-dakhil-hone-ki-dua", "hi": "baitul-khala-ki-dua", "id": "doa-masuk-kamar-mandi"},
        "title": {"en": "Dua for entering the toilet", "ur": "بیت الخلا میں داخل ہونے کی دعا", "hi": "बैतुल ख़ला में जाने की दुआ", "id": "Doa masuk kamar mandi (WC)"},
        "meaning": {"en": "O Allah, I seek refuge in You from the male and female devils (all evil and impure things).",
                    "ur": "اے اللہ! میں ناپاک جنوں (مرد و عورت) اور ہر خبیث چیز سے تیری پناہ مانگتا ہوں۔",
                    "hi": "ऐ अल्लाह! मैं नापाक जिन्नों (मर्द और औरत) और हर ख़बीस चीज़ से तेरी पनाह मांगता हूं।",
                    "id": "Ya Allah, aku berlindung kepada-Mu dari setan laki-laki dan setan perempuan (dari segala keburukan)."},
        "when": {"en": "Before entering the toilet, said outside it.", "ur": "بیت الخلا میں داخل ہونے سے پہلے، باہر ہی پڑھیں۔",
                 "hi": "बैतुल ख़ला में दाख़िल होने से पहले, बाहर ही पढ़ें।", "id": "Sebelum masuk kamar mandi, dibaca di luar."},
    },
    {
        "id": "leaving-toilet", "cat": "daily",
        "arabic": "غُفْرَانَكَ",
        "translit": "Ghufranak",
        "translit_hi": "ग़ुफ़रानक",
        "ref": "Sunan Abi Dawud 30; Jami at-Tirmidhi 7", "ref_url": SUNNAH + "abudawud:30",
        "slug": {"en": "dua-for-leaving-the-toilet", "ur": "baitul-khala-se-nikalne-ki-dua", "hi": "baitul-khala-se-nikalne-ki-dua", "id": "doa-keluar-kamar-mandi"},
        "title": {"en": "Dua for leaving the toilet", "ur": "بیت الخلا سے نکلنے کی دعا", "hi": "बैतुल ख़ला से निकलने की दुआ", "id": "Doa keluar kamar mandi (WC)"},
        "meaning": {"en": "(I ask) Your forgiveness.", "ur": "(اے اللہ!) میں تجھ سے بخشش مانگتا ہوں۔",
                    "hi": "(ऐ अल्लाह!) मैं तुझसे माफ़ी मांगता हूं।", "id": "(Aku memohon) ampunan-Mu."},
        "when": {"en": "After coming out of the toilet.", "ur": "بیت الخلا سے باہر نکلنے کے بعد۔",
                 "hi": "बैतुल ख़ला से बाहर निकलने के बाद।", "id": "Setelah keluar dari kamar mandi."},
    },
    {
        "id": "sneezing", "cat": "daily",
        "arabic": "الْحَمْدُ لِلَّهِ — (الجواب) يَرْحَمُكَ اللَّهُ — (ثم) يَهْدِيكُمُ اللَّهُ وَيُصْلِحُ بَالَكُمْ",
        "translit": "Alhamdulillah. (Reply:) Yarhamukallah. (Then:) Yahdikumullahu wa yuslihu balakum",
        "translit_hi": "अल्हम्दु लिल्लाह। (जवाब:) यरहमुकल्लाह। (फिर:) यह्दीकुमुल्लाहु व युस्लिहु बालकुम",
        "ref": "Sahih al-Bukhari 6224", "ref_url": SUNNAH + "bukhari:6224",
        "slug": {"en": "dua-when-sneezing", "ur": "cheenk-aane-ki-dua", "hi": "chheenk-aane-ki-dua", "id": "doa-ketika-bersin"},
        "title": {"en": "Dua when sneezing", "ur": "چھینک آنے کی دعا اور جواب", "hi": "छींक आने की दुआ और जवाब", "id": "Doa ketika bersin"},
        "meaning": {"en": "All praise is for Allah. (Reply:) May Allah have mercy on you. (Then:) May Allah guide you and set your affairs right.",
                    "ur": "تمام تعریفیں اللہ کے لیے ہیں۔ (جواب:) اللہ تم پر رحم کرے۔ (پھر:) اللہ تمہیں ہدایت دے اور تمہارا حال درست کرے۔",
                    "hi": "सब तारीफ़ अल्लाह के लिए है। (जवाब:) अल्लाह तुम पर रहम करे। (फिर:) अल्लाह तुम्हें हिदायत दे और तुम्हारा हाल दुरुस्त करे।",
                    "id": "Segala puji bagi Allah. (Jawaban:) Semoga Allah merahmatimu. (Lalu:) Semoga Allah memberimu petunjuk dan memperbaiki keadaanmu."},
        "when": {"en": "The one who sneezes says the first part; the listener replies; the sneezer answers.",
                 "ur": "چھینکنے والا پہلا حصہ کہے، سننے والا جواب دے، پھر چھینکنے والا آخری حصہ کہے۔",
                 "hi": "छींकने वाला पहला हिस्सा कहे, सुनने वाला जवाब दे, फिर छींकने वाला आख़िरी हिस्सा कहे।",
                 "id": "Yang bersin membaca bagian pertama, yang mendengar menjawab, lalu yang bersin membalas."},
    },
    {
        "id": "after-wudu", "cat": "salah",
        "arabic": "أَشْهَدُ أَنْ لَا إِلَهَ إِلَّا اللَّهُ وَحْدَهُ لَا شَرِيكَ لَهُ، وَأَشْهَدُ أَنَّ مُحَمَّدًا عَبْدُهُ وَرَسُولُهُ",
        "translit": "Ashhadu an la ilaha illallahu wahdahu la sharika lah, wa ashhadu anna Muhammadan 'abduhu wa rasuluh",
        "translit_hi": "अश्हदु अल्ला इलाहा इल्लल्लाहु वह्दहू ला शरीका लहू, व अश्हदु अन्ना मुहम्मदन अब्दुहू व रसूलुह",
        "ref": "Sahih Muslim 234", "ref_url": SUNNAH + "search?q=muslim+234+wudu",
        "slug": {"en": "dua-after-wudu", "ur": "wazu-ke-baad-ki-dua", "hi": "wazu-ke-baad-ki-dua", "id": "doa-setelah-wudhu"},
        "title": {"en": "Dua after wudu", "ur": "وضو کے بعد کی دعا", "hi": "वज़ू के बाद की दुआ", "id": "Doa setelah wudhu"},
        "meaning": {"en": "I bear witness that there is no god but Allah alone, without partner, and I bear witness that Muhammad is His servant and Messenger.",
                    "ur": "میں گواہی دیتا ہوں کہ اللہ کے سوا کوئی معبود نہیں، وہ اکیلا ہے، اس کا کوئی شریک نہیں، اور میں گواہی دیتا ہوں کہ محمد ﷺ اس کے بندے اور رسول ہیں۔",
                    "hi": "मैं गवाही देता हूं कि अल्लाह के सिवा कोई माबूद नहीं, वह अकेला है, उसका कोई शरीक नहीं, और मैं गवाही देता हूं कि मुहम्मद ﷺ उसके बंदे और रसूल हैं।",
                    "id": "Aku bersaksi bahwa tiada Tuhan selain Allah semata, tiada sekutu bagi-Nya, dan aku bersaksi bahwa Muhammad adalah hamba dan utusan-Nya."},
        "when": {"en": "After completing wudu.", "ur": "وضو مکمل کرنے کے بعد۔",
                 "hi": "वज़ू मुकम्मल करने के बाद।", "id": "Setelah selesai berwudhu."},
    },
    {
        "id": "entering-masjid", "cat": "salah",
        "arabic": "اللَّهُمَّ افْتَحْ لِي أَبْوَابَ رَحْمَتِكَ",
        "translit": "Allahummaftah li abwaba rahmatik",
        "translit_hi": "अल्लाहुम्मफ़्तह ली अब्वाबा रह्मतिक",
        "ref": "Sahih Muslim 713", "ref_url": SUNNAH + "search?q=muslim+713",
        "slug": {"en": "dua-for-entering-the-masjid", "ur": "masjid-mein-dakhil-hone-ki-dua", "hi": "masjid-mein-dakhil-hone-ki-dua", "id": "doa-masuk-masjid"},
        "title": {"en": "Dua for entering the masjid", "ur": "مسجد میں داخل ہونے کی دعا", "hi": "मस्जिद में दाख़िल होने की दुआ", "id": "Doa masuk masjid"},
        "meaning": {"en": "O Allah, open for me the doors of Your mercy.", "ur": "اے اللہ! میرے لیے اپنی رحمت کے دروازے کھول دے۔",
                    "hi": "ऐ अल्लाह! मेरे लिए अपनी रहमत के दरवाज़े खोल दे।", "id": "Ya Allah, bukakanlah untukku pintu-pintu rahmat-Mu."},
        "when": {"en": "When entering the masjid, stepping in with the right foot.", "ur": "مسجد میں داخل ہوتے وقت، دایاں پاؤں اندر رکھتے ہوئے۔",
                 "hi": "मस्जिद में दाख़िल होते वक़्त, दायां पैर अंदर रखते हुए।", "id": "Ketika masuk masjid, mendahulukan kaki kanan."},
    },
    {
        "id": "leaving-masjid", "cat": "salah",
        "arabic": "اللَّهُمَّ إِنِّي أَسْأَلُكَ مِنْ فَضْلِكَ",
        "translit": "Allahumma inni as'aluka min fadlik",
        "translit_hi": "अल्लाहुम्मा इन्नी अस्अलुका मिन फ़ज़्लिक",
        "ref": "Sahih Muslim 713", "ref_url": SUNNAH + "search?q=muslim+713",
        "slug": {"en": "dua-for-leaving-the-masjid", "ur": "masjid-se-nikalne-ki-dua", "hi": "masjid-se-nikalne-ki-dua", "id": "doa-keluar-masjid"},
        "title": {"en": "Dua for leaving the masjid", "ur": "مسجد سے نکلنے کی دعا", "hi": "मस्जिद से निकलने की दुआ", "id": "Doa keluar masjid"},
        "meaning": {"en": "O Allah, I ask You from Your bounty.", "ur": "اے اللہ! میں تجھ سے تیرے فضل کا سوال کرتا ہوں۔",
                    "hi": "ऐ अल्लाह! मैं तुझसे तेरे फ़ज़्ल का सवाल करता हूं।", "id": "Ya Allah, aku memohon kepada-Mu dari karunia-Mu."},
        "when": {"en": "When leaving the masjid, stepping out with the left foot.", "ur": "مسجد سے نکلتے وقت، بایاں پاؤں باہر رکھتے ہوئے۔",
                 "hi": "मस्जिद से निकलते वक़्त, बायां पैर बाहर रखते हुए।", "id": "Ketika keluar masjid, mendahulukan kaki kiri."},
    },
    {
        "id": "travel", "cat": "travel",
        "arabic": "سُبْحَانَ الَّذِي سَخَّرَ لَنَا هَذَا وَمَا كُنَّا لَهُ مُقْرِنِينَ، وَإِنَّا إِلَى رَبِّنَا لَمُنْقَلِبُونَ",
        "translit": "Subhanal-ladhi sakhkhara lana hadha wa ma kunna lahu muqrinin, wa inna ila Rabbina lamunqalibun",
        "translit_hi": "सुब्हानल्लज़ी सख़्ख़रा लना हाज़ा व मा कुन्ना लहू मुक़्रिनीन, व इन्ना इला रब्बिना लमुन्क़लिबून",
        "ref": "Quran 43:13–14; Sahih Muslim 1342", "ref_url": QURAN + "43/13-14",
        "slug": {"en": "dua-for-travelling", "ur": "safar-ki-dua", "hi": "safar-ki-dua", "id": "doa-naik-kendaraan"},
        "title": {"en": "Dua for travelling", "ur": "سفر کی دعا (Safar Ki Dua)", "hi": "सफ़र की दुआ", "id": "Doa naik kendaraan dan bepergian"},
        "meaning": {"en": "Glory be to the One who has subjected this to us, and we could not have done so ourselves. And surely to our Lord we shall return.",
                    "ur": "پاک ہے وہ ذات جس نے اسے ہمارے قابو میں کر دیا، حالانکہ ہم اسے قابو میں کرنے والے نہ تھے، اور بے شک ہم اپنے رب کی طرف لوٹنے والے ہیں۔",
                    "hi": "पाक है वह ज़ात जिसने इसे हमारे क़ाबू में कर दिया, हालांकि हम इसे क़ाबू में करने वाले न थे, और बेशक हम अपने रब की तरफ़ लौटने वाले हैं।",
                    "id": "Maha Suci Dzat yang telah menundukkan ini untuk kami, padahal kami sebelumnya tidak mampu menguasainya, dan sesungguhnya kepada Tuhan kamilah kami akan kembali."},
        "when": {"en": "When you sit on a vehicle at the start of a journey. Sahih Muslim 1342 gives the longer version.",
                 "ur": "سفر کے آغاز میں سواری پر بیٹھتے وقت۔ مکمل دعا صحیح مسلم 1342 میں ہے۔",
                 "hi": "सफ़र की शुरुआत में सवारी पर बैठते वक़्त। पूरी दुआ सहीह मुस्लिम 1342 में है।",
                 "id": "Ketika naik kendaraan di awal perjalanan. Versi lengkapnya ada dalam Shahih Muslim 1342."},
    },
    {
        "id": "breaking-fast", "cat": "travel",
        "arabic": "ذَهَبَ الظَّمَأُ وَابْتَلَّتِ الْعُرُوقُ، وَثَبَتَ الْأَجْرُ إِنْ شَاءَ اللَّهُ",
        "translit": "Dhahabaz-zama'u wabtallatil-'uruqu wa thabatal-ajru in sha Allah",
        "translit_hi": "ज़हबज़्ज़मउ वब्तल्लतिल उरूक़ु व सबतल अज्रु इन शा अल्लाह",
        "ref": "Sunan Abi Dawud 2357", "ref_url": SUNNAH + "abudawud:2357",
        "slug": {"en": "dua-for-breaking-fast", "ur": "roza-kholne-ki-dua", "hi": "roza-kholne-ki-dua", "id": "doa-berbuka-puasa"},
        "title": {"en": "Dua for breaking the fast (iftar)", "ur": "روزہ کھولنے کی دعا (Iftar Ki Dua)", "hi": "रोज़ा खोलने की दुआ (इफ़्तार की दुआ)", "id": "Doa berbuka puasa"},
        "meaning": {"en": "The thirst has gone, the veins are moistened, and the reward is confirmed, if Allah wills.",
                    "ur": "پیاس بجھ گئی، رگیں تر ہو گئیں، اور اگر اللہ نے چاہا تو اجر ثابت ہو گیا۔",
                    "hi": "प्यास बुझ गई, रगें तर हो गईं, और अगर अल्लाह ने चाहा तो अज्र पक्का हो गया।",
                    "id": "Telah hilang rasa haus, urat-urat telah basah, dan pahala telah tetap, insya Allah."},
        "when": {"en": "After breaking the fast at iftar.", "ur": "افطار کے وقت روزہ کھولنے کے بعد۔",
                 "hi": "इफ़्तार के वक़्त रोज़ा खोलने के बाद।", "id": "Setelah berbuka puasa."},
    },
    {
        "id": "rabbana-atina", "cat": "quran",
        "arabic": "رَبَّنَا آتِنَا فِي الدُّنْيَا حَسَنَةً وَفِي الْآخِرَةِ حَسَنَةً وَقِنَا عَذَابَ النَّارِ",
        "translit": "Rabbana atina fid-dunya hasanatan wa fil-akhirati hasanatan wa qina 'adhaban-nar",
        "translit_hi": "रब्बना आतिना फ़िद्दुन्या हसनतंव व फ़िल आख़िरति हसनतंव व क़िना अज़ाबन्नार",
        "ref": "Quran 2:201; Sahih al-Bukhari 6389", "ref_url": QURAN + "2/201",
        "slug": {"en": "rabbana-atina-fid-dunya", "ur": "rabbana-atina-dua", "hi": "rabbana-atina-dua", "id": "doa-sapu-jagat"},
        "title": {"en": "Rabbana Atina fid Dunya", "ur": "ربنا آتنا فی الدنیا (Rabbana Atina)", "hi": "रब्बना आतिना फ़िद्दुन्या", "id": "Doa sapu jagat (Rabbana atina)"},
        "meaning": {"en": "Our Lord, give us good in this world and good in the Hereafter, and protect us from the punishment of the Fire.",
                    "ur": "اے ہمارے رب! ہمیں دنیا میں بھی بھلائی دے اور آخرت میں بھی بھلائی دے، اور ہمیں آگ کے عذاب سے بچا۔",
                    "hi": "ऐ हमारे रब! हमें दुनिया में भी भलाई दे और आख़िरत में भी भलाई दे, और हमें आग के अज़ाब से बचा।",
                    "id": "Ya Tuhan kami, berilah kami kebaikan di dunia dan kebaikan di akhirat, dan peliharalah kami dari siksa neraka."},
        "when": {"en": "At any time; it was the dua the Prophet ﷺ made most often, and it is recited between the Yemeni corner and the Black Stone in tawaf.",
                 "ur": "کسی بھی وقت؛ یہ نبی ﷺ کی سب سے زیادہ مانگی جانے والی دعا تھی، اور طواف میں رکن یمانی اور حجر اسود کے درمیان پڑھی جاتی ہے۔",
                 "hi": "किसी भी वक़्त; यह नबी ﷺ की सबसे ज़्यादा मांगी जाने वाली दुआ थी, और तवाफ़ में रुक्न यमानी और हजर-ए-असवद के बीच पढ़ी जाती है।",
                 "id": "Kapan saja; inilah doa yang paling sering dibaca Nabi ﷺ, dan dibaca di antara Rukun Yamani dan Hajar Aswad saat thawaf."},
    },
    {
        "id": "parents", "cat": "quran",
        "arabic": "رَّبِّ ارْحَمْهُمَا كَمَا رَبَّيَانِي صَغِيرًا",
        "translit": "Rabbir-hamhuma kama rabbayani saghira",
        "translit_hi": "रब्बिर्हम्हुमा कमा रब्बयानी सग़ीरा",
        "ref": "Quran 17:24", "ref_url": QURAN + "17/24",
        "slug": {"en": "dua-for-parents", "ur": "walidain-ke-liye-dua", "hi": "walidain-ke-liye-dua", "id": "doa-untuk-kedua-orang-tua"},
        "title": {"en": "Dua for parents", "ur": "والدین کے لیے دعا", "hi": "वालिदैन (मां-बाप) के लिए दुआ", "id": "Doa untuk kedua orang tua"},
        "meaning": {"en": "My Lord, have mercy on them both as they raised me when I was small.",
                    "ur": "اے میرے رب! ان دونوں پر رحم فرما جیسے انہوں نے بچپن میں میری پرورش کی۔",
                    "hi": "ऐ मेरे रब! उन दोनों पर रहम फ़रमा जैसे उन्होंने बचपन में मेरी परवरिश की।",
                    "id": "Wahai Tuhanku, sayangilah keduanya sebagaimana mereka berdua telah mendidikku di waktu kecil."},
        "when": {"en": "At any time, especially after salah.", "ur": "کسی بھی وقت، خاص طور پر نماز کے بعد۔",
                 "hi": "किसी भी वक़्त, ख़ास तौर पर नमाज़ के बाद।", "id": "Kapan saja, terutama setelah sholat."},
    },
    {
        "id": "knowledge", "cat": "quran",
        "arabic": "رَّبِّ زِدْنِي عِلْمًا",
        "translit": "Rabbi zidni 'ilma",
        "translit_hi": "रब्बि ज़िद्नी इल्मा",
        "ref": "Quran 20:114", "ref_url": QURAN + "20/114",
        "slug": {"en": "dua-for-knowledge", "ur": "ilm-mein-izafa-ki-dua", "hi": "ilm-mein-izafe-ki-dua", "id": "doa-menuntut-ilmu"},
        "title": {"en": "Dua for increase in knowledge", "ur": "علم میں اضافے کی دعا", "hi": "इल्म में इज़ाफ़े की दुआ", "id": "Doa menuntut ilmu (Rabbi zidni ilma)"},
        "meaning": {"en": "My Lord, increase me in knowledge.", "ur": "اے میرے رب! میرے علم میں اضافہ فرما۔",
                    "hi": "ऐ मेरे रब! मेरे इल्म में इज़ाफ़ा फ़रमा।", "id": "Ya Tuhanku, tambahkanlah ilmu kepadaku."},
        "when": {"en": "Before studying, exams or any learning.", "ur": "پڑھائی، امتحان یا کچھ سیکھنے سے پہلے۔",
                 "hi": "पढ़ाई, इम्तिहान या कुछ सीखने से पहले।", "id": "Sebelum belajar, ujian atau menuntut ilmu."},
    },
    {
        "id": "yunus", "cat": "hardship",
        "arabic": "لَا إِلَهَ إِلَّا أَنْتَ سُبْحَانَكَ إِنِّي كُنْتُ مِنَ الظَّالِمِينَ",
        "translit": "La ilaha illa anta subhanaka inni kuntu minaz-zalimin",
        "translit_hi": "ला इलाहा इल्ला अन्ता सुब्हानका इन्नी कुन्तु मिनज़्ज़ालिमीन",
        "ref": "Quran 21:87; Jami at-Tirmidhi 3505", "ref_url": QURAN + "21/87",
        "slug": {"en": "dua-of-prophet-yunus", "ur": "dua-e-yunus", "hi": "dua-e-yunus", "id": "doa-nabi-yunus"},
        "title": {"en": "Dua of Prophet Yunus", "ur": "دعائے یونس (Dua e Yunus)", "hi": "दुआ-ए-यूनुस", "id": "Doa Nabi Yunus"},
        "meaning": {"en": "There is no god but You, glory be to You; indeed I have been among the wrongdoers.",
                    "ur": "تیرے سوا کوئی معبود نہیں، تو پاک ہے، بے شک میں ہی ظالموں میں سے تھا۔",
                    "hi": "तेरे सिवा कोई माबूद नहीं, तू पाक है, बेशक मैं ही ज़ालिमों में से था।",
                    "id": "Tidak ada Tuhan selain Engkau, Maha Suci Engkau, sesungguhnya aku termasuk orang-orang yang zalim."},
        "when": {"en": "In distress or difficulty. Tirmidhi 3505 says no Muslim calls with it except that Allah answers him.",
                 "ur": "پریشانی اور مشکل میں۔ ترمذی 3505 کے مطابق جو مسلمان اس سے دعا کرے اللہ اسے قبول فرماتا ہے۔",
                 "hi": "परेशानी और मुश्किल में। तिर्मिज़ी 3505 के मुताबिक़ जो मुसलमान इससे दुआ करे अल्लाह उसे क़बूल फ़रमाता है।",
                 "id": "Saat sedih atau kesulitan. Menurut Tirmidzi 3505, tidaklah seorang muslim berdoa dengannya kecuali Allah mengabulkannya."},
    },
    {
        "id": "anxiety", "cat": "hardship",
        "arabic": "اللَّهُمَّ إِنِّي أَعُوذُ بِكَ مِنَ الْهَمِّ وَالْحَزَنِ، وَالْعَجْزِ وَالْكَسَلِ، وَالْبُخْلِ وَالْجُبْنِ، وَضَلَعِ الدَّيْنِ وَغَلَبَةِ الرِّجَالِ",
        "translit": "Allahumma inni a'udhu bika minal-hammi wal-hazan, wal-'ajzi wal-kasal, wal-bukhli wal-jubn, wa dala'id-dayni wa ghalabatir-rijal",
        "translit_hi": "अल्लाहुम्मा इन्नी अऊज़ु बिका मिनल हम्मि वल हज़न, वल अज्ज़ि वल कसल, वल बुख़्लि वल जुब्न, व ज़लइद्दैनि व ग़लबतिर्रिजाल",
        "ref": "Sahih al-Bukhari 6369", "ref_url": SUNNAH + "bukhari:6369",
        "slug": {"en": "dua-for-anxiety-and-debt", "ur": "pareshani-dur-karne-ki-dua", "hi": "pareshani-dur-karne-ki-dua", "id": "doa-menghilangkan-kesedihan-dan-hutang"},
        "title": {"en": "Dua for anxiety, sorrow and debt", "ur": "پریشانی، غم اور قرض سے نجات کی دعا", "hi": "परेशानी, ग़म और क़र्ज़ से निजात की दुआ", "id": "Doa menghilangkan kesedihan dan terlilit hutang"},
        "meaning": {"en": "O Allah, I seek refuge in You from worry and grief, from helplessness and laziness, from miserliness and cowardice, and from the burden of debt and being overpowered by people.",
                    "ur": "اے اللہ! میں تیری پناہ مانگتا ہوں فکر اور غم سے، عاجزی اور سستی سے، کنجوسی اور بزدلی سے، اور قرض کے بوجھ اور لوگوں کے غلبے سے۔",
                    "hi": "ऐ अल्लाह! मैं तेरी पनाह मांगता हूं फ़िक्र और ग़म से, आजिज़ी और सुस्ती से, कंजूसी और बुज़दिली से, और क़र्ज़ के बोझ और लोगों के ग़लबे से।",
                    "id": "Ya Allah, aku berlindung kepada-Mu dari rasa gelisah dan sedih, dari lemah dan malas, dari kikir dan pengecut, serta dari lilitan hutang dan dikuasai orang lain."},
        "when": {"en": "Morning and evening, or whenever worry or debt weighs on you.", "ur": "صبح و شام، یا جب بھی فکر یا قرض کا بوجھ ہو۔",
                 "hi": "सुबह-शाम, या जब भी फ़िक्र या क़र्ज़ का बोझ हो।", "id": "Pagi dan petang, atau kapan pun merasa gelisah atau terbebani hutang."},
    },
]


# ---------------------------------------------------------------------------
# Language packs (src/packs/*.py). Each pack adds one language.
# New packs start as DRAFT: pages are built but get noindex and stay out of
# hreflang + sitemap until a native speaker/scholar reviews them. When a
# language is reviewed, add its code to REVIEWED_LANGS.
# ---------------------------------------------------------------------------
REVIEWED_LANGS = {"en", "ur", "hi", "id"}   # add codes here after native review
HIDE_TRANSLIT = set()                       # langs whose readers read Arabic script

from packs import p1, p2, p3, p4, p5  # noqa: E402
for _mod in (p1, p2, p3, p4, p5):
    for _code, _pk in _mod.P.items():
        assert len(_pk["duas"]) == len(DUAS), f"{_code}: expected {len(DUAS)} duas"
        assert len(_pk["cats"]) == len(CATEGORIES), f"{_code}: expected {len(CATEGORIES)} categories"
        LANG_META[_code] = _pk["meta"]
        UI[_code] = _pk["ui"]
        if _pk.get("hide_translit"):
            HIDE_TRANSLIT.add(_code)
        for _c, (_slug, _name) in zip(CATEGORIES, _pk["cats"]):
            _c["slug"][_code], _c["name"][_code] = _slug, _name
        for _d, _t in zip(DUAS, _pk["duas"]):
            _d["slug"][_code], _d["title"][_code], _d["meaning"][_code], _d["when"][_code] = _t[:4]
            if len(_t) > 4:
                _d.setdefault("translit_l", {})[_code] = _t[4]

# display order (world + local reach)
LANGS = [l for l in ["en", "ar", "ur", "hi", "bn", "id", "ms", "tr", "fa", "ps", "fr", "es", "de", "ru",
                     "zh", "pt", "sw", "ha", "so", "uz", "az", "bs", "sq", "ml"] if l in LANG_META]
