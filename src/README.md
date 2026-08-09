# Source for this site

⛔ **The `.md` files here are the source. Every `index.html` in this repo is GENERATED from
them and must not be hand-edited** — the next build would silently overwrite the edit.

Until 2026-08-09 this source existed **only in a session temp directory** while the generated
HTML was the sole thing under version control. The published policies are legally operative
documents for eight apps; had that directory been cleared, they would have had to be
reverse-engineered from rendered HTML. That is the reason this directory exists.

## Layout

    src/<app>/policy.md        the app's privacy policy
    src/<app>/health-data.md   its consumer health data policy (WA MHMDA), where it has one
    src/build_privacy_site.py  the generator

## Building

    python3 src/build_privacy_site.py src . https://prameyallc.github.io/privacy

Regenerates every page plus the hub index. It refuses to build if an accent colour fails the
WCAG AA contrast gate, so a page cannot ship unreadable.

## Rules

- Edit the `.md`, never the `.html`.
- `.nojekyll` must stay — GitHub Pages would otherwise mangle the output.
- A policy change is a change to a legal document. Verify what shipped by fetching the live
  URL afterwards, not by trusting the build log.
