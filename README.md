# imothersofch.org

Website for **Israeli Mothers of Crown Heights Incorporated**, a 501(c)(3) nonprofit (EIN 42-2644115) in Brooklyn, NY.

It's a plain static site: HTML and CSS with a few lines of JavaScript, no frameworks, no images and no tracking. It loads fast and can be hosted for free.

## Pages

| Page | File |
|---|---|
| Home | `index.html` |
| About Us (history, who we serve, governance) | `about.html` |
| Mission (Article II purpose statement, values) | `mission.html` |
| Programs (Family Support, Emergency Assistance, Food Assistance) | `programs.html` |
| Events (photo gallery) | `events.html` |
| Contact | `contact.html` |
| Donate | `donate.html` |
| Privacy Policy | `privacy.html` |
| Not found | `404.html` |

## Editing

Don't edit the root `*.html` files directly, because they get regenerated.

- **Organization details** (address, phone, emails, EIN) are in the `ORG` block at the top of `build.py`. Change them once there and every page updates.
- **Page text** is in `_pages/<page>.html`.
- **Header and footer** are in `build.py` (`header()` and `footer()`).
- **Styles** are in `assets/styles.css`. Brand colors and fonts are documented in `BRAND.md`.

After making changes, run:

```bash
python3 build.py
```

Then commit the regenerated files.

## Hosting on Vercel

The site is set up for Vercel. There's no build step on Vercel's side: the finished pages are committed, and Vercel serves them as they are.

- `vercel.json` adds security headers and sets a one-hour browser cache on `/assets/`. It also redirects `/index.html` to `/`.
- `.vercelignore` keeps the source files (`_pages/`, `build.py`, this README, `BRAND.md`) off the live site.
- `404.html` is used automatically for missing pages.

### First deploy

1. In Vercel, choose **Add New → Project** and import this GitHub repository.
2. Set **Framework Preset** to **Other**. Leave Build Command and Output Directory empty.
3. Choose **Deploy**. After a minute or so you'll get a `*.vercel.app` preview address.

### Connect imothersofch.org

1. In the project, open **Settings → Domains** and add `imothersofch.org` and `www.imothersofch.org`. Set `www` to redirect to the main domain.
2. Vercel shows the DNS records to add. At your domain registrar, add them (normally an `A` record for `imothersofch.org` and a `CNAME` for `www`).
3. Keep the existing **MX** and **TXT** records for Google Workspace. Change only the records Vercel asks for, or email will stop working.
4. Vercel issues the HTTPS certificate automatically once DNS is in place.

Every push to the production branch redeploys the site. Other branches get their own preview addresses.

## Google for Nonprofits website checklist

| Requirement | How the site meets it |
|---|---|
| Live, HTTPS, no mixed content | All assets are local or loaded over `https://` (Google Fonts). Turn on HTTPS enforcement at the host. |
| Multiple pages | 8 distinct pages: Home, About, Mission, Programs, Events, Donate, Contact, Privacy |
| Mission, history, programs | Mission page (charter text), About page (history), Programs page (detailed descriptions) |
| No placeholder text | None. Every page has real content. |
| No AI-generated images | Real photos from the organization's own events (originals in `photos/`, web copies made by `tools/photos.py`, metadata stripped). The only other graphics are the candle logo and the brownstone line drawing in the footer, both simple hand-coded SVG (the drawing comes from `tools/brownstones.py`). |
| Org name in header and footer | On every page |
| Footer: EIN, admin email, domain, physical address | On every page |
| Contact email on the custom domain | admin@ and donate@imothersofch.org |
| Mobile-friendly | Responsive layout, checked at 375px wide |
| No broken links | All internal links and anchors checked automatically. Donate buttons use `mailto:` links. |
| Organizational clarity | About page says the organization is independent and explains its Chabad Lubavitch religious orientation |
