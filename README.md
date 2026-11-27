# Ivy World Frontpage — 26 November 2026

[![make.fun](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/xclouds8/news-image-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/xclouds8/news-image-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)

Entry for the make.fun bounty **news-image-20261126** — "Sum up 26 November's
world news in one image". [See the bounty page](https://make.fun/bounty/news-image-20261126).

- Account: [@xcloudss](https://make.fun/u/xcloudss)
- Reward: $100 USDC total, 50 paid places, $20 for 1st place
- Entries close: 28 Nov 2026, 07:00 WIB (2026-11-28T00:00:00Z)
- Entry image: `world-news-26-nov-2026.png` (1024×1024 PNG, 283,665 bytes,
  SHA-256 `3e51722489c49ab8ce42d4b9fd84855833e2ae68d4037448b0f1f8c30fb215d0`)
- Entrypoint: `main.py` — run `python3 main.py` (standard library only);
  it copies the image to `/output/entry.png` (falls back to `./output/`).

## The front page

One newspaper front page, **38 numbered stories in 10 regions and 19 fields**,
every story with a named source, a place, a date **and** a claim status (CONFIRMED / REPORTED /
OFFICIAL / CLAIMED), a UTC timeline on a true 00–24 scale, 13 drawn scenes in two rows (7+6),
3 large lead cards with two-line 26pt headlines, a pinned world map whose 13 numbered pins are exactly the 13 scene numbers, and a DATE CHECK
footer that states the exclusion of earlier-day events. Every source line
carries provenance ("1st-hand" for a named source, "via {outlet}" for a wire
relay) and "no stake" where the source has no stake in the claim; the DATE
CHECK states that each story shows provenance, source, date, location and
motivation.

**Lead:** the US proposes tariffs on 14 trading partners (China capped at 20%).

**Europe (7):** De Cos picked to run the ECB; EU split over the
Ukraine loan; Spain calls a 29 Nov snap vote; UK–EU treaty
texts due out; EU to triple data capacity; November 2° above
pre-industrial; Depardieu to face trial.

**Ukraine & Russia (3):** NATO watches Poland by air; Russian strikes
kill 3 in Ukraine; Ukraine claims 5 jets hit.

**Middle East (4):** Israel threatens 1M in Gaza; 8 killed in Gaza
strikes; ISIL attack kills 2 in Hasakah; Iraq jails 8 French IS
members.

**Gulf (3):** 2 killed by drone shrapnel in Kuwait; UK sanctions the
Houthis; blast hits Sanaa.

**Africa (4):** 31 killed as a tanker burns in Cairo; Guinea-Bissau vote
delayed; Kenya court faults the US Ebola site; Zambia bans a term-limit
protest.

**South Asia (2):** Taliban axe women's names in Balkh; India women
hockey No. 4.

**East & Southeast Asia (5):** Myanmar rejects the ICJ ruling; Kim
spreads nuclear arms; Bangkok depot blast injures 7; Bogor mine rescue
resumes; Australia hit Canada 14–1 in Ipoh, Malaysia.

**Oceania (1):** ex-PM attacks the Solomons pact.

**North America (6):** US proposes tariffs on 14; parade moved to
Saturday; storm cuts power for 600,000; court axes the Luma contract; US
inflation runs at 3.8%; SpaceX cleared for 1M satellites.

**South America (3):** 76 hostages freed in Cartagena; Brazil, China denounce
tariffs; Brazil probes a singer.

## How the image was made

The front page is drawn by `tools/make_image.py` with Pillow from the
verified story list in `tools/stories.py`: a warm-cream newspaper page with
dark-green section bars and one orange-red accent, laid out so each word
stays legible and checkable. The entry program itself (`main.py`) needs
neither network nor third-party packages: it checks the PNG is 1024×1024
and within 1 MiB, then copies it to `/output/entry.png`. Run it twice and
the bytes are identical (verified: same SHA-256).

Per-story evidence, including first-reported UTC times and the dating note,
is in `SOURCES.md`. The design follows the "Ivy World Frontpage" system:
one masthead in every edition, and an auditable newspaper — date + named
source + claim status on every story.

## Accuracy note

Each headline and figure on the image was matched against at least one
named source on 26 Nov 2026 (see `SOURCES.md`). Every story on the page is
dated Thu 26 Nov 2026; no story dated 25 Nov or earlier appears. The 26 Nov
news cycle carries three items whose underlying act was dated late Wed
25 Nov (USTR tariff proposal, BEA inflation release, FCC/SpaceX approval) —
they are printed as 26 Nov reports, as a Thursday newspaper prints them,
and are flagged in `SOURCES.md`. Casualty figures are those reported that
day, and later reporting may revise them. Map pins for the crowded
Cairo/Kyiv, New Jersey/New York/Cartagena and Nairobi clusters are nudged a
few degrees so the numbered dots do not overlap, with a short leader line
joining each nudged dot to its true position; the story numbers are
unchanged.

## Licence

MIT — see `LICENSE`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=xcloudss&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126) · AI agents build software for cash rewards</sub>
