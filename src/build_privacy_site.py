#!/usr/bin/env python3
"""Build the Prameya privacy site.

Reads per-app policy markdown from privacy-content/<slug>/{policy.md,health-data.md}
and emits a static, Jekyll-free site into the repo clone.

Design decisions:
  * .nojekyll — no build step on GitHub's side, so nothing can silently fail to render.
    The previous repo served PRIVACY.md as raw text/markdown; that is the bug being fixed.
  * Every policy is its own directory with an index.html, so URLs are clean and stable
    (/privacy/omnisalub/) and can be pasted straight into App Store Connect.
  * Consumer health data policies live at /<slug>/health-data/ and are linked *distinctly*
    from the main policy, because RCW 19.373.020 requires a separate link, not a section.
  * Light/dark via prefers-color-scheme, plus a print stylesheet — people print policies.
"""

import os
import re
import sys
import html
import shutil
import datetime

import markdown

EFFECTIVE = "2026-08-08"

# (light accent, dark accent) — taken from each app's shipped brand file.
APPS = [
    ("omnisalub",  "OmniSalub",  "Chronic-condition companion",              "#1577A8", "#318CB9", True),
    ("omnident",   "OmniDent",   "Dental photo analysis and coaching",       "#037C84", "#2AA3AB", True),
    ("omniderm",   "OmniDerm",   "Skin analysis and tracking",               "#875FA9", "#9975B8", True),
    ("omnirx",     "OmniRx",     "Medication education and habit support",   "#3547EB", "#7E89EA", True),
    ("omnilex",    "OmniLex",    "On-device legal document assistant",       "#2D4D77", "#7B93B2", False),
    ("omniwealth", "OmniWealth", "Financial education and habit support",    "#816B22", "#9B853C", False),
    ("omnimath",   "OmniMath",   "Discrete mathematics for computer science","#6D28D9", "#A78BFA", False),
    ("omnibuild",  "OmniBuild",  "Construction and skilled-trades reference","#854200", "#F28C06", False),
]

# --------------------------------------------------------------------------- contrast


def _lin(c):
    c = c / 255.0
    return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4


def luminance(hexcolor):
    h = hexcolor.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return 0.2126 * _lin(r) + 0.7152 * _lin(g) + 0.0722 * _lin(b)


def contrast(a, b):
    la, lb = luminance(a), luminance(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


# --------------------------------------------------------------------------- css

CSS = """
:root{
  --bg:#ffffff; --card:#f7f7f8; --ink:#1a1a19; --muted:#5b5f66;
  --rule:#e3e5e8; --accent:#1577A8; --accent-ink:#ffffff;
  --maxw:46rem;
}
@media (prefers-color-scheme: dark){
  :root{ --bg:#131316; --card:#1a1a19; --ink:#f2f2f0; --muted:#a6a9ad;
         --rule:#2c2e33; --accent:#318CB9; --accent-ink:#10151a; }
}
*,*::before,*::after{ box-sizing:border-box; }
html{ -webkit-text-size-adjust:100%; }
body{
  margin:0; background:var(--bg); color:var(--ink);
  font:400 1.0625rem/1.65 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
}
.skip{ position:absolute; left:-9999px; }
.skip:focus{ left:1rem; top:1rem; position:fixed; background:var(--accent);
  color:var(--accent-ink); padding:.6rem 1rem; border-radius:.5rem; z-index:10; }
.wrap{ max-width:var(--maxw); margin:0 auto; padding:2rem 1.25rem 5rem; }
header.site{ border-bottom:1px solid var(--rule); }
header.site .wrap{ padding-block:1.25rem; display:flex; gap:1rem;
  align-items:baseline; justify-content:space-between; flex-wrap:wrap; }
.brand{ font-weight:650; letter-spacing:-.01em; text-decoration:none; color:var(--ink); }
.brand span{ color:var(--accent); }
nav.crumb a{ color:var(--muted); text-decoration:none; font-size:.9375rem; }
nav.crumb a:hover{ color:var(--accent); text-decoration:underline; }
h1{ font-size:clamp(1.75rem,1.2rem + 2vw,2.375rem); line-height:1.2;
  letter-spacing:-.02em; margin:1.5rem 0 .5rem; }
h2{ font-size:1.3125rem; line-height:1.3; margin:2.5rem 0 .75rem;
  padding-top:1.25rem; border-top:1px solid var(--rule); letter-spacing:-.01em; }
h3{ font-size:1.0625rem; margin:1.75rem 0 .5rem; }
p,ul,ol,table{ margin:0 0 1rem; }
ul,ol{ padding-left:1.25rem; }
li{ margin:.35rem 0; }
a{ color:var(--accent); text-underline-offset:.15em; }
strong{ font-weight:650; }
hr{ border:0; border-top:1px solid var(--rule); margin:2rem 0; }
code{ font:.9em/1.5 ui-monospace,SFMono-Regular,Menlo,monospace;
  background:var(--card); padding:.15em .4em; border-radius:.3em; }
blockquote{ margin:1.25rem 0; padding:.75rem 1rem; border-left:3px solid var(--accent);
  background:var(--card); border-radius:0 .5rem .5rem 0; color:var(--muted); }
blockquote p:last-child{ margin-bottom:0; }
.meta{ color:var(--muted); font-size:.9375rem; margin:0 0 1.5rem; }
.lede{ font-size:1.125rem; color:var(--muted); }
.tablewrap{ overflow-x:auto; -webkit-overflow-scrolling:touch; margin:0 0 1rem; }
table{ border-collapse:collapse; width:100%; font-size:.9688rem; }
th,td{ text-align:left; padding:.55rem .7rem; border-bottom:1px solid var(--rule);
  vertical-align:top; }
th{ font-weight:650; background:var(--card); }
.callout{ background:var(--card); border:1px solid var(--rule); border-radius:.75rem;
  padding:1rem 1.15rem; margin:1.5rem 0; }
.callout h2,.callout h3{ border:0; padding-top:0; margin-top:0; }
.callout.distinct{ border-color:var(--accent); border-left-width:4px; }
.cards{ list-style:none; padding:0; display:grid; gap:.75rem;
  grid-template-columns:repeat(auto-fill,minmax(15rem,1fr)); }
.cards li{ margin:0; }
.cards a{ display:block; height:100%; background:var(--card); border:1px solid var(--rule);
  border-left:4px solid var(--dot,var(--accent)); border-radius:.75rem;
  padding:.9rem 1rem; text-decoration:none; color:var(--ink); }
.cards a:hover{ border-color:var(--dot,var(--accent)); }
.cards .n{ font-weight:650; display:block; }
.cards .d{ color:var(--muted); font-size:.9375rem; display:block; margin-top:.15rem; }
.cards .h{ color:var(--dot,var(--accent)); font-size:.8125rem; display:block;
  margin-top:.5rem; font-weight:600; }
footer.site{ border-top:1px solid var(--rule); color:var(--muted); font-size:.9375rem; }
footer.site .wrap{ padding-block:1.5rem 3rem; }
@media print{
  :root{ --bg:#fff; --ink:#000; --muted:#333; --card:#fff; --rule:#bbb; }
  header.site,footer.site nav,.skip{ display:none; }
  .wrap{ max-width:none; padding:0; }
  a{ color:#000; text-decoration:underline; }
  h2{ page-break-after:avoid; } table,blockquote{ page-break-inside:avoid; }
}
"""

# --------------------------------------------------------------------------- template

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="index,follow">
<link rel="canonical" href="{canonical}">
<style>{css}</style>
<style>:root{{--accent:{al};--accent-ink:{ail}}}
@media (prefers-color-scheme: dark){{:root{{--accent:{ad};--accent-ink:{aid}}}}}</style>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site"><div class="wrap">
  <a class="brand" href="{root}/">Prameya <span>Privacy</span></a>
  <nav class="crumb">{crumb}</nav>
</div></header>
<main id="main" class="wrap">
{body}
</main>
<footer class="site"><div class="wrap">
  <p>Prameya LLC · <a href="mailto:admin@prameya.legal">admin@prameya.legal</a></p>
  <p>Effective {effective}. <a href="{root}/">All app privacy policies</a></p>
</div></footer>
</body>
</html>
"""


def render_md(text):
    # nl2br is safe here: the source is not hard-wrapped (prose lines average 150-220
    # chars), so a single newline is an intended break — e.g. the Effective date /
    # Publisher / Contact block at the top of each policy, which otherwise runs together.
    md = markdown.Markdown(
        extensions=["tables", "attr_list", "sane_lists", "toc", "nl2br"]
    )
    out = md.convert(text)
    # Tables must scroll inside their own container, never the page body.
    out = re.sub(r"<table>", '<div class="tablewrap"><table>', out)
    out = re.sub(r"</table>", "</table></div>", out)
    return out


def first_para(md_text):
    for line in md_text.splitlines():
        s = line.strip()
        if s and not s.startswith("#") and not s.startswith(">"):
            return re.sub(r"[*_`\[\]]|\(http[^)]*\)", "", s)[:180]
    return "Privacy policy."


def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def build(content_dir, out_dir, site_root):
    # Wipe only the generated surface; keep .git and README.
    for slug, *_ in APPS:
        shutil.rmtree(os.path.join(out_dir, slug), ignore_errors=True)
    for stale in ("PRIVACY.md",):
        p = os.path.join(out_dir, stale)
        if os.path.exists(p):
            os.remove(p)

    write(os.path.join(out_dir, ".nojekyll"), "")
    write(os.path.join(out_dir, "assets", "style.css"), CSS)

    built, missing, warnings = [], [], []

    for slug, name, tagline, al, ad, health in APPS:
        # Contrast gate: an accent that fails AA does not ship.
        cl, cd = contrast(al, "#ffffff"), contrast(ad, "#131316")
        if cl < 4.5:
            warnings.append(f"{name}: light accent {al} vs #ffffff = {cl:.2f}:1 (below AA 4.5)")
        if cd < 4.5:
            warnings.append(f"{name}: dark accent {ad} vs #131316 = {cd:.2f}:1 (below AA 4.5)")

        src = os.path.join(content_dir, slug, "policy.md")
        if not os.path.exists(src):
            missing.append(f"{name}: policy.md")
            continue
        body_md = open(src, encoding="utf-8").read()

        hd_src = os.path.join(content_dir, slug, "health-data.md")
        has_hd = os.path.exists(hd_src) and open(hd_src, encoding="utf-8").read().strip()

        extra = ""
        if has_hd:
            # RCW 19.373.020 wants a distinct link, not a buried section.
            extra = (
                '<div class="callout distinct">'
                f'<h3>Consumer Health Data Privacy Policy</h3>'
                f'<p>{name} processes consumer health data. Washington State law requires a '
                f'separate policy for that data, published at its own address:</p>'
                f'<p><strong><a href="{site_root}/{slug}/health-data/">'
                f'{name} Consumer Health Data Privacy Policy</a></strong></p>'
                "</div>"
            )

        page = PAGE.format(
            title=f"{name} Privacy Policy — Prameya LLC",
            desc=html.escape(first_para(body_md), quote=True),
            canonical=f"{site_root}/{slug}/",
            css=CSS, al=al, ad=ad, ail="#ffffff", aid="#10151a",
            root=site_root,
            crumb=f'<a href="{site_root}/">← All policies</a>',
            body=render_md(body_md) + extra,
            effective=EFFECTIVE,
        )
        write(os.path.join(out_dir, slug, "index.html"), page)
        built.append(f"{slug}/")

        if has_hd:
            hd_md = open(hd_src, encoding="utf-8").read()
            hp = PAGE.format(
                title=f"{name} Consumer Health Data Privacy Policy — Prameya LLC",
                desc=html.escape(first_para(hd_md), quote=True),
                canonical=f"{site_root}/{slug}/health-data/",
                css=CSS, al=al, ad=ad, ail="#ffffff", aid="#10151a",
                root=site_root,
                crumb=f'<a href="{site_root}/{slug}/">← {name} privacy policy</a>',
                body=render_md(hd_md),
                effective=EFFECTIVE,
            )
            write(os.path.join(out_dir, slug, "health-data", "index.html"), hp)
            built.append(f"{slug}/health-data/")

    # ------------------------------------------------------------------ hub
    cards = []
    for slug, name, tagline, al, ad, health in APPS:
        if not os.path.exists(os.path.join(out_dir, slug, "index.html")):
            continue
        hd = os.path.exists(os.path.join(out_dir, slug, "health-data", "index.html"))
        cards.append(
            f'<li><a href="{site_root}/{slug}/" style="--dot:{al}">'
            f'<span class="n">{name}</span><span class="d">{tagline}</span>'
            + (f'<span class="h">+ Consumer Health Data policy</span>' if hd else "")
            + "</a></li>"
        )

    hub_body = f"""<h1>Privacy policies</h1>
<p class="lede">Prameya LLC publishes a separate privacy policy for each app, because the apps
do genuinely different things with data. Pick the app you use.</p>
<ul class="cards">{''.join(cards)}</ul>
<div class="callout">
<h2 style="border:0;padding-top:0;margin-top:0">How these apps are built</h2>
<p>Prameya apps run their analysis <strong>on your device</strong>. We do not operate a server that
receives your content, and we do not keep user profiles. Some apps download an AI model from
Hugging Face the first time you use a feature that needs one — that download requests a model, it
does not send your content anywhere.</p>
<p>Where an app touches health information, US state law requires a separate consumer health data
policy. Those are linked above and from each app's policy.</p>
</div>
<h2>Contact</h2>
<p>Prameya LLC · <a href="mailto:admin@prameya.legal">admin@prameya.legal</a></p>
"""
    write(os.path.join(out_dir, "index.html"), PAGE.format(
        title="App Privacy Policies — Prameya LLC",
        desc="Privacy policies for Prameya LLC apps. Each app has its own policy.",
        canonical=f"{site_root}/", css=CSS,
        al="#1577A8", ad="#318CB9", ail="#ffffff", aid="#10151a",
        root=site_root, crumb="", body=hub_body, effective=EFFECTIVE,
    ))
    built.append("/ (hub)")

    return built, missing, warnings


if __name__ == "__main__":
    content = sys.argv[1]
    out = sys.argv[2]
    root = sys.argv[3] if len(sys.argv) > 3 else "https://prameyallc.github.io/privacy"
    b, m, w = build(content, out, root)
    print(f"built {len(b)} pages")
    for p in b:
        print("  +", p)
    if w:
        print("\nCONTRAST WARNINGS:")
        for x in w:
            print("  !", x)
    if m:
        print("\nMISSING CONTENT:")
        for x in m:
            print("  -", x)
        sys.exit(1)
