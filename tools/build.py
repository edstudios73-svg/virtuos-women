import os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

PAGES = [("index.html", "Home"), ("about.html", "About"), ("outreach.html", "Outreach"), ("gallery.html", "Gallery"), ("contact.html", "Visit &amp; Contact")]

SITE = "https://www.virtouswomenofdestiny.org"

JSONLD = """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "NGO",
  "name": "Virtuous Women of Destiny",
  "alternateName": "Women of Destiny",
  "slogan": "Women of Destiny. We are highly honoured.",
  "description": "A non-profit women's ministry with a missionary outreach vision in East Legon, Accra.",
  "url": "https://www.virtouswomenofdestiny.org/",
  "logo": "https://www.virtouswomenofdestiny.org/assets/icon-512.png",
  "image": "https://www.virtouswomenofdestiny.org/assets/og-image.jpg",
  "telephone": "+233546878015",
  "founder": {"@type": "Person", "name": "Prophetess Dr. Gifty Ezekiel", "jobTitle": "Founder and President"},
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Christian Service Church, Jungle Avenue Road",
    "addressLocality": "East Legon, Accra",
    "addressCountry": "GH"
  },
  "geo": {"@type": "GeoCoordinates", "latitude": 5.6359, "longitude": -0.1498}
}
</script>
"""

def head(title, desc, fname="index.html", extra=""):
    url = SITE + ("/" if fname == "index.html" else "/" + fname)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Virtuous Women of Destiny">
<meta property="og:locale" content="en_GH">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE}/assets/og-image.jpg">
<meta property="og:image:type" content="image/jpeg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Women of Destiny. Photos of Prophetess Dr. Gifty Ezekiel, Founder and President.">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{SITE}/assets/og-image.jpg">
<meta name="theme-color" content="#0d0d0d">
<meta name="apple-mobile-web-app-title" content="Women of Destiny">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<link rel="manifest" href="/site.webmanifest">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="/assets/icon-192.png">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@300;400;500&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
{extra}</head>
<body>
"""

def nav(current):
    items = "\n".join(
        f'      <li><a href="{'/' if f == 'index.html' else f}"{" aria-current=\"page\"" if f == current else ""}>{n}</a></li>'
        for f, n in PAGES)
    return f"""<header class="bar">
  <a class="mark" href="/"><img src="assets/logo.webp" alt="" width="34" height="34"><span>Virtuous Women of Destiny</span></a>
  <button class="menu-btn" aria-expanded="false" aria-controls="menu"><span class="txt">Menu</span><span class="lines" aria-hidden="true"></span></button>
</header>
<nav class="menu" id="menu" aria-label="Main">
  <ol>
{items}
  </ol>
  <aside>
    <div><span class="label">Gathering</span>Every Tuesday<br>9:00 AM – 12:00 Noon</div>
    <div><span class="label">Where</span>Christian Service Church<br>Jungle Avenue Road, East Legon, Accra</div>
    <div><span class="label">Talk to us</span><a href="https://wa.me/233546878015" target="_blank" rel="noopener">+233 54 687 8015</a></div>
  </aside>
</nav>
"""

FOOT = """<footer class="foot">
  <p class="big rv">With Jesus Christ our helper,<br><em>all things are possible.</em></p>
  <div class="foot-grid">
    <div><span class="label">Gathering</span>Every Tuesday<br>9:00 AM – 12:00 Noon</div>
    <div><span class="label">Where</span>Christian Service Church<br>Jungle Avenue Road<br>East Legon, Accra</div>
    <div><span class="label">Contact</span><a href="tel:+233546878015">+233 54 687 8015</a><br><a href="https://wa.me/233546878015" target="_blank" rel="noopener">WhatsApp</a></div>
    <div><span class="label">Pages</span><a href="about.html">About</a><br><a href="outreach.html">Outreach</a><br><a href="gallery.html">Gallery</a><br><a href="contact.html">Contact</a></div>
  </div>
  <div class="legal"><span>© <span class="yr">2026</span> Virtuous Women of Destiny. A non-profit women's ministry.</span><span>Numbers 6:24–25</span></div>
</footer>
<script src="script.js"></script>
</body>
</html>
"""

def page(fname, title, desc, body, extra="", scripts=""):
    with open(os.path.join(OUT, fname), "w") as f:
        f.write(head(title, desc, fname, extra) + nav(fname) + "<main>\n" + body + "\n</main>\n" + FOOT.replace("<script src=\"script.js\"></script>", scripts + "<script src=\"script.js\"></script>"))

def phead(label, h1, p):
    return f"""<section class="page-head">
  <p class="label">{label}</p>
  <h1 class="rv">{h1}</h1>
  <p class="rv">{p}</p>
</section>"""

# ---------- HOME ----------
page("index.html", "Virtuous Women of Destiny | East Legon, Accra",
"A non-profit women's ministry with a missionary outreach vision. Every Tuesday, 9 AM to 12 Noon, at Christian Service Church, East Legon.",
"""<section class="hero">
  <div class="slides" aria-hidden="true">
    <div class="col">
      <img src="assets/hero-1.webp" alt="" width="600" height="863">
      <img src="assets/hero-2.webp" alt="" width="600" height="863">
      <img src="assets/hero-3.webp" alt="" width="600" height="720">
      <img src="assets/hero-4.webp" alt="" width="560" height="672">
    </div>
    <div class="col">
      <img src="assets/hero-1.webp" alt="" width="600" height="863">
      <img src="assets/hero-2.webp" alt="" width="600" height="863">
      <img src="assets/hero-3.webp" alt="" width="600" height="720">
      <img src="assets/hero-4.webp" alt="" width="560" height="672">
    </div>
    <div class="col">
      <img src="assets/hero-1.webp" alt="" width="600" height="863">
      <img src="assets/hero-2.webp" alt="" width="600" height="863">
      <img src="assets/hero-3.webp" alt="" width="600" height="720">
      <img src="assets/hero-4.webp" alt="" width="560" height="672">
    </div>
  </div>
  <div class="hero-top">
    <div class="counter label"><span class="num">01</span><span class="progress"><b></b></span><span>04</span></div>
    <span class="label">East Legon, Accra</span>
  </div>
  <div class="hero-inner">
    <div>
      <p class="label">A women's ministry with a missionary outreach vision</p>
      <h1><span><i>Women of</i></span><span><i><em>Destiny.</em></i></span></h1>
    </div>
    <div class="hero-side">
      <p>We are highly honoured. Every Tuesday we pray, learn and go out to serve the city together.</p>
      <a class="hero-cta" href="contact.html">Join us on Tuesday <span aria-hidden="true">→</span></a>
    </div>
  </div>
  <span class="scroll" aria-hidden="true"></span>
</section>

<section class="sec">
  <div class="row">
    <p class="label">01 &middot; About</p>
    <div>
      <p class="lede rv">Not a church. A fellowship of women who believe <em>faith is something you do.</em></p>
      <div class="body rv"><p>Founded and led by our President, <strong>Prophetess Dr. Gifty Ezekiel</strong>, we bring women together to grow in faith, find their purpose and serve the people around them. Women from any church or background are welcome.</p></div>
      <a class="more rv" href="about.html">Read our story <span aria-hidden="true">→</span></a>
    </div>
  </div>
</section>
<section class="sec" style="padding-top:0">
  <div class="split founder">
    <figure class="photo rv" style="aspect-ratio:4/5"><img src="assets/hero-2.webp" alt="Prophetess Dr. Gifty Ezekiel" loading="lazy"><figcaption>Founder &amp; President</figcaption></figure>
    <div>
      <p class="label" style="color:var(--grey)">Our founder</p>
      <p class="lede rv" style="margin-top:22px">&ldquo;Every woman has a God-given purpose, <em>and she shouldn&rsquo;t have to find it alone.&rdquo;</em></p>
      <div class="body rv"><p><strong>Prophetess Dr. Gifty Ezekiel</strong> answered a calling to gather women in faith, purpose and service. Today she leads Virtuous Women of Destiny as its Founder and President.</p></div>
      <a class="more rv" href="about.html">Meet our founder <span aria-hidden="true">→</span></a>
    </div>
  </div>
</section>

<section class="sec" style="padding-top:0">
  <div class="row">
    <p class="label">Tuesday mornings</p>
    <div>
      <p class="lede rv">Three hours that <em>carry us through the week.</em></p>
      <ol class="steps">
        <li class="rv"><figure><img src="assets/photos/eyes-closed-in-worship.webp" alt="A woman worshipping with her eyes closed" loading="lazy"></figure><small>01</small><h3>We pray</h3><p>We open the morning in worship and prayer, for each other and for the city.</p></li>
        <li class="rv"><figure><img src="assets/photos/listening.webp" alt="A woman listening during the service" loading="lazy"></figure><small>02</small><h3>We study the Word</h3><p>We open the Bible together and ask what it means for the week ahead.</p></li>
        <li class="rv"><figure><img src="assets/photos/celebration.webp" alt="Celebrating together at a service" loading="lazy"></figure><small>03</small><h3>We go and serve</h3><p>We plan who we&rsquo;ll visit and how we&rsquo;ll help, then go out together.</p></li>
      </ol>
      <a class="more rv" href="contact.html">Join us on Tuesday <span aria-hidden="true">→</span></a>
    </div>
  </div>
</section>

<section class="sec dark">
  <div class="row">
    <p class="label">02 &middot; Outreach</p>
    <div>
      <p class="lede rv">Empowerment <em>through Christ.</em></p>
      <ul class="reach rv">
        <li>The unsaved</li><li>The poor</li><li>Orphanages</li><li>Prisons</li><li>Hospitals</li><li>Widows</li><li>Street children</li>
      </ul>
      <div class="body rv"><p>Outreach isn't something we do on the side. It's the reason we gather. We also offer free direction to women growing a business.</p></div>
      <figure class="band rv"><img src="assets/photos/praying-together.webp" alt="Women praying together" loading="lazy"></figure>
      <a class="more rv" href="outreach.html">See our outreach <span aria-hidden="true">→</span></a>
    </div>
  </div>
</section>
<section class="sec">
  <div class="row">
    <p class="label">Kingdom investment</p>
    <div>
      <p class="lede rv">Your business is part of your calling, <em>too.</em></p>
      <div class="body rv"><p>Our experts give free direction to women who want to invest, expand, secure, protect, recover or build. Bring the idea, the shop or the side hustle, and leave with a clear next step.</p></div>
      <a class="more rv" href="https://wa.me/233546878015?text=Hello%2C%20I%27d%20like%20free%20direction%20to%20grow%20my%20business." target="_blank" rel="noopener">Ask for free direction <span aria-hidden="true">→</span></a>
    </div>
  </div>
</section>

<section class="motto">
  <img src="assets/photos/clapping-in-praise.webp" alt="Women clapping in praise" loading="lazy">
  <div class="motto-inner">
    <p class="label">Our motto</p>
    <p class="rv">Women of Destiny.<br><em>We are highly honoured.</em></p>
  </div>
</section>

<section class="sec">
  <div class="row">
    <p class="label">03 &middot; Gallery</p>
    <div>
      <p class="lede rv">Moments <em>&amp; memories.</em></p>
      <a class="strip rv" href="gallery.html" aria-label="Open the gallery">
        <img src="assets/photos/praying-in-white.webp" alt="Praying in white lace" loading="lazy">
        <img src="assets/photos/singing.webp" alt="Singing in worship" loading="lazy">
        <img src="assets/photos/little-one.webp" alt="A little one at the service" loading="lazy">
        <img src="assets/photos/hands-raised.webp" alt="Hands raised in prayer" loading="lazy">
      </a>
      <a class="more rv" href="gallery.html">View the gallery <span aria-hidden="true">→</span></a>
    </div>
  </div>
</section>
<section class="sec" style="padding-top:0">
  <div class="row">
    <p class="label">What we stand for</p>
    <div>
      <ul class="values rv">
        <li><small>01</small><h3>Faith</h3><p>We stand on God&rsquo;s Word.</p></li>
        <li><small>02</small><h3>Purpose</h3><p>Every woman has a calling.</p></li>
        <li><small>03</small><h3>Integrity</h3><p>Truth in private and in public.</p></li>
        <li><small>04</small><h3>Compassion</h3><p>Christ&rsquo;s love, shown in care.</p></li>
        <li><small>05</small><h3>Leadership</h3><p>Wisdom and courage.</p></li>
        <li><small>06</small><h3>Service</h3><p>Our time, given to others.</p></li>
      </ul>
      <a class="more rv" href="about.html">Our mission &amp; vision <span aria-hidden="true">→</span></a>
    </div>
  </div>
</section>

<section class="sec find" style="padding-top:0">
  <div class="row">
    <div><p class="label">04 &middot; Visit &amp; Contact</p><a class="more" href="contact.html" style="margin-top:18px">Plan your visit <span aria-hidden="true">→</span></a></div>
    <div class="map-wrap rv">
      <div id="map" class="map" role="img" aria-label="Map of East Legon, Accra, with a marker on Jungle Avenue, near Christian Service Church"></div>
      <div class="map-grain" aria-hidden="true"></div>
      <div class="map-hud map-hud-top" aria-hidden="true"><span>05.6359&deg; N</span><span>00.1498&deg; W</span></div>
      <div class="map-card">
        <p class="label">Every Tuesday &middot; 9 AM &ndash; 12 Noon</p>
        <h3>Christian Service Church</h3>
        <p>Jungle Avenue Road, East Legon, Accra</p>
        <div class="actions">
          <a class="btn btn-light" href="https://www.google.com/maps/dir/?api=1&amp;destination=Christian+Service+Church+Jungle+Avenue+East+Legon+Accra" target="_blank" rel="noopener">Get directions &rarr;</a>
          <a class="btn btn-ghost-light" href="https://wa.me/233546878015?text=Hello%2C%20I%27m%20coming%20on%20Tuesday.%20Could%20you%20share%20directions%3F" target="_blank" rel="noopener">Ask on WhatsApp</a>
        </div>
      </div>
    </div>
  </div>
</section>""",
extra='<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.css">\n<link rel="preconnect" href="https://tile.openstreetmap.org">\n' + JSONLD,
scripts='<script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.js" defer></script>\n<script src="map.js" defer></script>\n')

# ---------- ABOUT ----------
page("about.html", "About | Virtuous Women of Destiny",
"Founded by Prophetess Dr. Gifty Ezekiel, Virtuous Women of Destiny is a women's fellowship in East Legon, Accra.",
phead("About", "A sisterhood,<br><em>not a church.</em>",
"Founded by Prophetess Dr. Gifty Ezekiel to bring women together in faith, purpose and service.") + f"""
<section class="sec">
  <div class="split">
    <figure class="photo rv" style="aspect-ratio:4/5"><img src="assets/hero-3.webp" alt="Prophetess Dr. Gifty Ezekiel speaking at a service" loading="lazy"><figcaption>Prophetess Dr. Gifty Ezekiel, Founder &amp; President</figcaption></figure>
    <div>
      <p class="lede rv">It started as a calling. <em>It became a family.</em></p>
      <div class="body rv">
        <p>Virtuous Women of Destiny began with one conviction: every woman has a God-given purpose, and she shouldn't have to find it alone.</p>
        <p>What started as a calling on <strong>Prophetess Dr. Gifty Ezekiel's</strong> life has grown into a fellowship of women who support, encourage and empower one another. We are a non-profit women's ministry, not a church, and women from every church and background meet with us.</p>
        <p>We gather every Tuesday morning at Christian Service Church in East Legon to pray, study the Word and plan how we'll serve. New to faith or walking with Christ for years, there's a seat for you.</p>
      </div>
    </div>
  </div>
</section>

<section class="sec" style="padding-top:0">
  <div class="row">
    <p class="label">Leadership</p>
    <div class="leaders solo">
      <figure class="rv"><div class="photo"><img src="assets/hero-2.webp" alt="Prophetess Dr. Gifty Ezekiel" loading="lazy"></div><figcaption><h3>Prophetess Dr. Gifty Ezekiel</h3><p>Founder &amp; President</p></figcaption></figure>
    </div>
  </div>
</section>

<section class="sec" style="padding-top:0">
  <div class="row">
    <p class="label">Motto</p>
    <p class="lede rv">Women of Destiny. <em>We are highly honoured.</em></p>
  </div>
</section>

<section class="sec" style="padding-top:0">
  <div class="split">
    <div class="row" style="grid-template-columns:1fr"><p class="label">Mission</p><p class="body" style="margin-top:0;color:var(--ink);font-size:19px">To help women grow strong in faith, build true friendships and serve their communities with love.</p></div>
    <div class="row" style="grid-template-columns:1fr"><p class="label">Vision</p><p class="body" style="margin-top:0;color:var(--ink);font-size:19px">Women who live with faith, purpose, integrity and compassion, who lead well and bring change to their families and communities.</p></div>
  </div>
</section>

<section class="sec" style="padding-top:0">
  <div class="row">
    <p class="label">What we stand for</p>
    <ol class="list">
      <li><h3>Faith</h3><p>We stand on God's Word and follow the Holy Spirit in all we do.</p></li>
      <li><h3>Purpose</h3><p>We help every woman discover and live out her calling.</p></li>
      <li><h3>Integrity</h3><p>Honesty and truth, in private and in public.</p></li>
      <li><h3>Compassion</h3><p>Christ's love shown through real care for others.</p></li>
      <li><h3>Leadership</h3><p>Women who lead with wisdom and courage.</p></li>
      <li><h3>Service</h3><p>Our time and resources, given to help others.</p></li>
    </ol>
  </div>
</section>

<section class="sec" style="padding-top:0">
  <div class="row">
    <p class="label">Common questions</p>
    <div>
      <details><summary>When do you meet?</summary><p>Every Tuesday from 9:00 AM to 12:00 Noon.</p></details>
      <details><summary>Where?</summary><p>Christian Service Church, Jungle Avenue Road, East Legon, Accra, Ghana.</p></details>
      <details><summary>Do I need to belong to a particular church?</summary><p>No. We're a women's ministry, not a church. Women from any church or background are welcome.</p></details>
      <details><summary>Who leads the ministry?</summary><p>Prophetess Dr. Gifty Ezekiel, who founded the ministry and serves as its President.</p></details>
    </div>
  </div>
</section>""")

# ---------- OUTREACH ----------
page("outreach.html", "Outreach | Virtuous Women of Destiny",
"Empowerment through Christ: reaching the unsaved, the poor, orphanages, prisons, hospitals, widows and street children.",
phead("Outreach statement", "Empowerment<br><em>through Christ.</em>",
"Outreach isn't something we do on the side. It's the reason we gather.") + f"""
<section class="sec">
  <div class="row">
    <p class="label">We reach out to</p>
    <ol class="list">
      <li><h3>The unsaved</h3><p>Sharing the gospel in word and, more often, in deed.</p></li>
      <li><h3>The poor</h3><p>Food, supplies and practical help for struggling families.</p></li>
      <li><h3>The orphanage</h3><p>Time, gifts and a mother's attention for children waiting for a family.</p></li>
      <li><h3>Prisons</h3><p>Visiting, praying, and reminding people they haven't been forgotten.</p></li>
      <li><h3>Hospitals</h3><p>Sitting with the sick and praying with their families.</p></li>
      <li><h3>The widows</h3><p>Standing beside women who have lost their husbands.</p></li>
      <li><h3>Street children</h3><p>Meals, care and safety for children the city overlooks.</p></li>
      <li><h3><em>Etc.</em></h3><p>Wherever we're needed next.</p></li>
    </ol>
  </div>
</section>

<section class="sec" style="padding-top:0">
  <div class="pair">
    <figure class="photo rv"><img src="assets/photos/open-hands.webp" alt="A woman praying with open hands" loading="lazy"></figure>
    <figure class="photo rv"><img src="assets/photos/lost-in-prayer.webp" alt="A woman lost in prayer" loading="lazy"></figure>
  </div>
</section>

<section class="sec" style="padding-top:0">
  <div class="row" style="grid-template-columns:1fr;border:0;padding:0">
    <p class="label" style="color:var(--grey)">We are a family</p>
    <div class="trio">
      <div class="rv"><p class="label">We give</p><h3>Joy</h3><p>to the hopeless.</p></div>
      <div class="rv"><p class="label">We give</p><h3>Peace</h3><p>to the weary.</p></div>
      <div class="rv"><p class="label">We reach out to</p><h3><em>The broken-hearted.</em></h3><p>And we stay.</p></div>
    </div>
  </div>
</section>

<section class="sec dark">
  <div class="row">
    <p class="label">Kingdom investment</p>
    <div>
      <p class="lede rv">Your business is part of your calling, <em>too.</em></p>
      <div class="verbs rv"><span>invest,</span><span>expand,</span><span>secure,</span><span>protect,</span><span>recover,</span><span>build.</span></div>
      <div class="body rv"><p>Our experts will give you direction, free of charge, to grow your business. Bring the idea, the shop or the side hustle. Sit with women who've done it, and leave with a clear next step.</p></div>
      <div class="actions"><a class="btn" href="https://wa.me/233546878015?text=Hello%2C%20I%27d%20like%20free%20direction%20to%20grow%20my%20business." target="_blank" rel="noopener">Ask for free direction →</a></div>
    </div>
  </div>
</section>""")

# ---------- GALLERY ----------
G = [("praying-in-white","prayer","Praying in white lace"),("celebration","fellowship","Cutting the birthday cake"),("clapping-in-praise","worship","Clapping in praise"),
     ("hands-raised","prayer","Hands raised in prayer"),("little-one","fellowship","A little one at the service"),("singing","worship","Singing in worship"),
     ("praying-together","prayer","Praying together"),("at-the-front","fellowship","At the front of the hall"),("eyes-closed-in-worship","worship","Eyes closed in worship"),
     ("open-hands","prayer","Open hands"),("seated-portrait","fellowship","A seated portrait"),("standing-in-worship","worship","Standing in worship"),
     ("lost-in-prayer","prayer","Lost in prayer"),("listening","worship","Listening to the Word"),("standing-firm","worship","Standing in the service")]
tiles = "\n".join(f'    <button data-c="{c}"><img src="assets/photos/{n}.webp" alt="{a}" loading="lazy"></button>' for n, c, a in G)
page("gallery.html", "Gallery | Virtuous Women of Destiny",
"Gatherings, prayer, outreach and fellowship moments from Virtuous Women of Destiny.",
phead("Gallery", "Moments<br><em>&amp; memories.</em>", "Prayer, worship and fellowship from our services.") + f"""
<section class="sec">
  <div class="filters" role="group" aria-label="Filter">
    <button class="on" data-f="all">All</button><button data-f="prayer">Prayer</button><button data-f="worship">Worship</button><button data-f="fellowship">Fellowship</button>
  </div>
  <div class="masonry">
{tiles}
  </div>
  <p class="note credit">Photos from Dr. Ezekiel's Birthday Service II by BEEP Photography.</p>
</section>
<div class="lightbox" hidden><button>Close ✕</button><figure><img alt=""><p></p></figure></div>""")

# ---------- CONTACT ----------
page("contact.html", "Visit &amp; Contact | Virtuous Women of Destiny",
"Join Virtuous Women of Destiny every Tuesday, 9 AM to 12 Noon, at Christian Service Church, Jungle Avenue Road, East Legon.",
phead("Visit &amp; contact", "Come as<br><em>you are.</em>", "Every Tuesday morning. Bring a friend, or just bring yourself.") + """
<section class="sec">
  <div class="info rv">
    <div><span class="label">When</span><p>Every Tuesday<br>9:00 AM – 12:00 Noon</p></div>
    <div><span class="label">Where</span><p>Christian Service Church<br>Jungle Avenue Road, East Legon</p></div>
    <div><span class="label">Call or WhatsApp</span><p><a href="tel:+233546878015">+233 54 687 8015</a></p></div>
  </div>
  <div class="actions">
    <a class="btn fill" href="https://wa.me/233546878015" target="_blank" rel="noopener">Chat on WhatsApp</a>
    <a class="btn" href="https://www.google.com/maps/search/?api=1&amp;query=Christian+Service+Church+Jungle+Avenue+East+Legon+Accra" target="_blank" rel="noopener">Get directions</a>
  </div>
</section>

<section class="sec" style="padding-top:0">
  <div class="row">
    <div><p class="label">Send a note</p><figure class="photo side rv"><img src="assets/photos/singing.webp" alt="A woman singing in worship" loading="lazy"></figure></div>
    <form id="note">
      <label><span class="label">Your name</span><input name="name" required autocomplete="name"></label>
      <label><span class="label">About</span>
        <select name="topic">
          <option>I'd like to visit on Tuesday</option>
          <option>Prayer request</option>
          <option>Free business direction</option>
          <option>I'd like to support the outreach</option>
          <option>Something else</option>
        </select>
      </label>
      <label><span class="label">Message</span><textarea name="message" rows="3" required></textarea></label>
      <div><button class="btn fill" type="submit">Send on WhatsApp →</button><p class="note" style="margin-top:12px">This opens WhatsApp with your message filled in.</p></div>
    </form>
  </div>
</section>""")
print("ok")
