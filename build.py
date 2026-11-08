#!/usr/bin/env python3
"""Build the static site for Israeli Mothers of Crown Heights Incorporated.

Each page's main content lives in _pages/<name>.html. This script wraps every
page in the shared header and footer and writes the finished file to the
repository root, which is what gets published.

Edit organization details (address, emails, EIN, phone) in ORG below, then run:

    python3 build.py
"""
from pathlib import Path
import html

ROOT = Path(__file__).parent

ORG = {
    "legal_name": "Israeli Mothers of Crown Heights Incorporated",
    "short_name": "Israeli Mothers of Crown Heights",
    "domain": "imothersofch.org",
    "url": "https://imothersofch.org",
    "ein": "42-2644115",
    "street": "49 E 43 St",
    "city": "Brooklyn",
    "state": "NY",
    "zip": "11203",
    "phone_display": "(718) 499-7229",
    "phone_tel": "+17184997229",
    "admin_email": "admin@imothersofch.org",
    "donate_email": "donate@imothersofch.org",
    "founded": "2026",
}

# (file name, nav label, <title>, meta description). Order = nav order.
PAGES = [
    ("index", "Home", f"{ORG['legal_name']} | Crown Heights, Brooklyn",
     "Israeli Mothers of Crown Heights Incorporated is a 501(c)(3) nonprofit providing family support, emergency assistance and food assistance to Jewish families in Crown Heights, Brooklyn."),
    ("about", "About Us", f"About Us | {ORG['short_name']}",
     "The history of Israeli Mothers of Crown Heights: more than a decade of quiet help to Crown Heights families, formally incorporated as a 501(c)(3) nonprofit in 2026."),
    ("mission", "Mission", f"Our Mission | {ORG['short_name']}",
     "The mission and purpose of Israeli Mothers of Crown Heights Incorporated, as set out in its certificate of incorporation."),
    ("programs", "Programs", f"Programs & Services | {ORG['short_name']}",
     "Family support, emergency assistance and food assistance programs offered by Israeli Mothers of Crown Heights in Brooklyn, New York."),
    ("events", "Events", f"Events | {ORG['short_name']}",
     "Photos from community events hosted by Israeli Mothers of Crown Heights for women in Crown Heights, Brooklyn."),
    ("contact", "Contact", f"Contact Us | {ORG['short_name']}",
     "Contact Israeli Mothers of Crown Heights Incorporated by email, phone or mail. Request assistance confidentially."),
    ("donate", "Donate", f"Donate | {ORG['short_name']}",
     "Support Jewish families in Crown Heights. Donations to Israeli Mothers of Crown Heights Incorporated (EIN 42-2644115) are tax-deductible to the extent allowed by law."),
    ("privacy", None, f"Privacy Policy | {ORG['short_name']}",
     "Privacy policy for imothersofch.org."),
    ("404", None, f"Page Not Found | {ORG['short_name']}",
     "The page you were looking for could not be found."),
]

CANDLES_SVG = """<svg class="brand-mark" viewBox="0 0 48 48" aria-hidden="true" focusable="false">
  <circle cx="24" cy="24" r="23" fill="var(--plum)"/>
  <path d="M14 15.5c2 3 3 4.6 3 6.4a3 3 0 0 1-6 0c0-1.8 1-3.4 3-6.4z" fill="var(--champagne)"/>
  <path d="M24 10.5c2 3 3 4.6 3 6.4a3 3 0 0 1-6 0c0-1.8 1-3.4 3-6.4z" fill="var(--champagne)"/>
  <path d="M34 15.5c2 3 3 4.6 3 6.4a3 3 0 0 1-6 0c0-1.8 1-3.4 3-6.4z" fill="var(--champagne)"/>
  <rect x="12" y="26" width="4" height="11" rx="1" fill="#fff"/>
  <rect x="22" y="21" width="4" height="16" rx="1" fill="#fff"/>
  <rect x="32" y="26" width="4" height="11" rx="1" fill="#fff"/>
  <rect x="9" y="37" width="30" height="2.5" rx="1.25" fill="#fff" opacity=".75"/>
</svg>"""


def header(active: str) -> str:
    links = []
    for name, label, _t, _d in PAGES:
        if not label:
            continue
        href = "/" if name == "index" else f"/{name}.html"
        cls = ' class="nav-donate"' if name == "donate" else ""
        cur = ' aria-current="page"' if name == active else ""
        links.append(f'<li><a href="{href}"{cls}{cur}>{label}</a></li>')
    nav = "\n          ".join(links)
    return f"""<a class="skip-link" href="#main">Skip to main content</a>
  <header class="site-header">
    <div class="topbar">
      <div class="container topbar-inner">
        <span lang="he" dir="rtl" class="bsd">בס״ד</span>
        <span class="topbar-note">A 501(c)(3) nonprofit organization &middot; EIN {ORG['ein']}</span>
      </div>
    </div>
    <div class="container header-inner">
      <a class="brand" href="/" aria-label="{ORG['legal_name']} – home">
        {CANDLES_SVG}
        <span class="brand-text">
          <span class="brand-name">Israeli Mothers</span>
          <span class="brand-sub">of Crown Heights <span class="brand-inc">Inc.</span></span>
        </span>
      </a>
      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav">
        <span class="nav-toggle-bars" aria-hidden="true"></span>
        <span class="nav-toggle-label">Menu</span>
      </button>
      <nav id="site-nav" class="site-nav" aria-label="Main">
        <ul>
          {nav}
        </ul>
      </nav>
    </div>
  </header>"""


def footer() -> str:
    o = ORG
    return f"""<footer class="site-footer">
    <div class="container footer-skyline">
      <img src="/assets/brownstones.svg" alt="" width="1200" height="202" loading="lazy" decoding="async">
    </div>
    <div class="container footer-grid">
      <div class="footer-org">
        <p class="footer-name">{o['legal_name']}</p>
        <p>A New York not-for-profit corporation recognized by the IRS as a tax-exempt public charity under section 501(c)(3) of the Internal Revenue Code.</p>
        <dl class="footer-facts">
          <div><dt>EIN / Tax ID</dt><dd>{o['ein']}</dd></div>
          <div><dt>Address</dt><dd>{o['street']}, {o['city']}, {o['state']} {o['zip']}</dd></div>
          <div><dt>Website</dt><dd><a href="{o['url']}/">{o['domain']}</a></dd></div>
          <div><dt>Administrator email</dt><dd><a href="mailto:{o['admin_email']}">{o['admin_email']}</a></dd></div>
          <div><dt>Donations</dt><dd><a href="mailto:{o['donate_email']}">{o['donate_email']}</a></dd></div>
        </dl>
      </div>
      <nav class="footer-nav" aria-label="Footer">
        <p class="footer-heading">Explore</p>
        <ul>
          <li><a href="/about.html">About Us</a></li>
          <li><a href="/mission.html">Mission</a></li>
          <li><a href="/programs.html">Programs</a></li>
          <li><a href="/events.html">Events</a></li>
          <li><a href="/donate.html">Donate</a></li>
          <li><a href="/contact.html">Contact</a></li>
          <li><a href="/privacy.html">Privacy Policy</a></li>
        </ul>
      </nav>
    </div>
    <div class="container footer-bottom">
      <p>&copy; <span data-year>2026</span> {o['legal_name']}. All rights reserved.</p>
      <p>Contributions are tax-deductible to the extent allowed by law. No goods or services are provided in exchange for donations unless stated in writing.</p>
    </div>
  </footer>"""


def page(name: str, title: str, desc: str, body: str) -> str:
    canonical = f"{ORG['url']}/" if name == "index" else f"{ORG['url']}/{name}.html"
    ld = ""
    if name == "index":
        o = ORG
        ld = f"""
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "NGO",
    "name": "{o['legal_name']}",
    "alternateName": "{o['short_name']}",
    "url": "{o['url']}/",
    "email": "{o['admin_email']}",
    "telephone": "{o['phone_tel']}",
    "foundingDate": "{o['founded']}",
    "taxID": "{o['ein']}",
    "nonprofitStatus": "Nonprofit501c3",
    "address": {{
      "@type": "PostalAddress",
      "streetAddress": "{o['street']}",
      "addressLocality": "{o['city']}",
      "addressRegion": "{o['state']}",
      "postalCode": "{o['zip']}",
      "addressCountry": "US"
    }}
  }}
  </script>"""
    robots = '\n  <meta name="robots" content="noindex">' if name == "404" else ""
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <meta name="description" content="{html.escape(desc)}">{robots}
  <link rel="canonical" href="{canonical}">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="{ORG['legal_name']}">
  <meta property="og:title" content="{html.escape(title)}">
  <meta property="og:description" content="{html.escape(desc)}">
  <meta property="og:url" content="{canonical}">
  <meta name="theme-color" content="#5b2149">
  <link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Frank+Ruhl+Libre:wght@500&family=Mulish:wght@400;600;700&display=swap">
  <link rel="stylesheet" href="/assets/styles.css">
  <script src="/assets/site.js" defer></script>{ld}
</head>
<body>
  {header(name)}
  <main id="main">
{body}
  </main>
  {footer()}
</body>
</html>
"""


def fill(text: str) -> str:
    for k, v in ORG.items():
        text = text.replace("{{" + k + "}}", v)
    return text


def main() -> None:
    for name, _label, title, desc in PAGES:
        body = fill((ROOT / "_pages" / f"{name}.html").read_text(encoding="utf-8"))
        (ROOT / f"{name}.html").write_text(page(name, title, desc, body), encoding="utf-8")
        print(f"built {name}.html")


if __name__ == "__main__":
    main()
