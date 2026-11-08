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
| Contact | `contact.html` |
| Donate | `donate.html` |
| Privacy Policy | `privacy.html` |
| Not found | `404.html` |

## Editing

Don't edit the root `*.html` files directly, because they get regenerated.

- **Organization details** (address, phone, emails, EIN) are in the `ORG` block at the top of `build.py`. Change them once there and every page updates.
- **Page text** is in `_pages/<page>.html`.
- **Header and footer** are in `build.py` (`header()` and `footer()`).
- **Styles** are in `assets/styles.css`.

After making changes, run:

```bash
python3 build.py
```

Then commit the regenerated files.

## Hosting

The site is ready for **GitHub Pages**:

1. In the repository, open Settings → Pages, choose "Deploy from a branch", and pick the branch with folder `/ (root)`.
2. The `CNAME` file already sets the custom domain to `imothersofch.org`. At your domain registrar, add GitHub Pages' DNS records (A records for the apex domain, and a CNAME for `www` pointing to `<user>.github.io`).
3. Once the certificate is issued, tick **Enforce HTTPS**.

Netlify or Cloudflare Pages also work: set the publish directory to the repository root with no build command.

## Google for Nonprofits website checklist

| Requirement | How the site meets it |
|---|---|
| Live, HTTPS, no mixed content | All assets are local or loaded over `https://` (Google Fonts). Turn on HTTPS enforcement at the host. |
| Multiple pages | 7 distinct pages: Home, About, Mission, Programs, Donate, Contact, Privacy |
| Mission, history, programs | Mission page (charter text), About page (history), Programs page (detailed descriptions) |
| No placeholder text | None. Every page has real content. |
| No AI-generated images | The site uses no photos. The logo (two Shabbos candles), icons and background pattern are simple hand-coded SVG. |
| Org name in header and footer | On every page |
| Footer: EIN, admin email, domain, physical address | On every page |
| Contact email on the custom domain | admin@ and donate@imothersofch.org |
| Mobile-friendly | Responsive layout, checked at 375px wide |
| No broken links | All internal links and anchors checked automatically. Donate buttons use `mailto:` links. |
| Organizational clarity | About page says the organization is independent and explains its Chabad Lubavitch religious orientation |
