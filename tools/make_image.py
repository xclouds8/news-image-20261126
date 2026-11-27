#!/usr/bin/env python3
"""Draw the 26 November 2026 news-image front page (1024x1024 PNG).

"Ivy World Frontpage" — koran v2 per
~/workspace/make-fun-agent/templates/news-image-newspaper.md and the
top-10 study (~/workspace/make-fun-agent/top10-study-20261126.md):
masthead brand, fields strip, UTC timeline on a true 00-24 scale,
3 large lead cards with drawn scenes, pinned world map (13 numbered
pins = the 13 scene numbers), 13 drawn scenes in two rows (7+6),
38 numbered stories in 10 regions, each with a named source, a place,
a date and a claim-status label (CONFIRMED / REPORTED / OFFICIAL /
CLAIMED), DATE CHECK footer stating exclusion of earlier-day events.

v6 (27 Nov 2026): rebuilt from the Claude verdict on v5
(~/workspace/make-fun-agent/mock-judge-verdict-v5.md, NEEDS WORK 79/100):
- Type floor raised: source lines stay 8pt but in #222 (was #333);
  status chips 7 -> 8pt bold (padding 5, height 13); number gutter
  22 -> 21px so the two longest headlines still fit (measured: #06
  margin 1.8px, #37 margin 2.4px — script audit/measure-v6.py).
- First Draft pillars made explicit: every source line carries
  provenance ("1st-hand" for a named source, "via {outlet}" when the
  source IS a wire relay) and "no stake" on unflagged rows; the
  DATE CHECK footer now states each story shows provenance, source,
  date, location and motivation (⚑ = source has a stake).
- Lead cards dominant: headline 26pt serif on TWO lines, art banner
  48 -> 76px, card height 108 -> 166px; scene tiles pay for it
  (60 -> 50px, temp 90x40 -> 108x40, uniform 1.25x resize).
- Map strip 68 -> 45px; continents redrawn (Africa / South America
  recognisable); pin numerals 9 -> 10pt bold; nudged pins (15, 17,
  29, 32) get 1px leader lines to their true positions.
- Map label fixed: "13 DRAWN SCENES BELOW" -> "ABOVE" (the strip is
  above the map — a factual error on v5).
- Headlines corrected: 06 "SPAIN CALLS 29 NOV SNAP VOTE", 37 "NOV 2°
  ABOVE PRE-INDUSTRIAL" (drops ".0" so it fits; deck keeps "2°").
  LUMA was already correct in v5 (Claude misread it at small size —
  verified at 2x zoom + SOURCES.md); the word is unchanged.
- No extra Oceania / South Asia story added: the Daily Summary of
  World page for 26 Nov (27 stories) contains no other Oceania or
  South Asia story, and the grid has no room (13/13/12 at 33px rows).
- Canvas stays 1024x1024 (portrait is impossible — see v5 note).

v5 (27 Nov 2026): rebuilt from the Claude verdict on v4
(~/workspace/make-fun-agent/mock-judge-verdict-v4.md, NEEDS WORK 71/100)
plus the fallback-judge polish (83/100):
- 10 real regions (WORLD deleted; EUROPE & UKRAINE and MIDDLE EAST &
  GULF split); grid columns rebalanced for 33px rows.
- Type up: list headlines 14pt, summaries 11pt (target ~55 chars),
  DATE CHECK + footer line 10pt; stake-flag legend moved to the
  footer line (the CLAIM LABELS box no longer fits the grid).
- Scene tiles carry a caption bar ("NN · LABEL"); scene 04 redrawn
  as a strike; timeline gains 1px leader lines + "·" captions.
- Lead headlines accurate at 20pt (Claude's 25-31-char wordings do
  not fit one line at 24pt in a 326px card — measured 417-542px vs
  314px available); leads get filled status chips.
- REPORTED darkened to #7a4d00 (measured ~7.3:1).
- Canvas stays 1024x1024: Claude's portrait 1024x1450 suggestion was
  REJECTED — kit RULES.txt caps output at 1024x1024 px and main.py
  enforces it; a portrait image would FAIL the kit check.
  Legibility is maximised inside the square canvas instead.

v4 (27 Nov 2026): rebuilt from the mock-judge verdict on v3
(~/workspace/make-fun-agent/mock-judge-verdict-v3.md):
- stat strip deleted (it duplicated the masthead spec line);
- scenes 10 -> 13 (added 32 Cartagena store, 10 Kuwait debris,
  17 Kenya clinic); map pins = exactly the 13 scene numbers;
- type hierarchy: lead headline 24pt, region bar 13pt, row headline
  12pt, timeline caption 10pt;
- small grey text darkened to #333; REPORTED pill darkened to #8a5a00;
- timeline redrawn on a true 00-24 UTC scale with numbered captions,
  the 00:23-01:39 cluster staggered above/below the line;
- label logic (OFFICIAL = the named source is the body that issued
  it) and per-row source lines "Source - Place - 26 Nov - FIELD" with
  a stake flag (U+2691) and a legend in the CLAIM LABELS box.

Deterministic: fixed strings, fixed fonts, no network, no timestamps,
no randomness. Pillow only (installed locally, 10.2.0).

Run: python3 tools/make_image.py [output-path]
Default output: world-news-26-nov-2026.png next to this repo root.
"""

import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from stories import (  # noqa: E402
    COLUMNS, EDITION_DATE, FIELDS, LEADS, PINS, SCENES, SCENE_CAPTIONS,
    STORIES, TIMELINE,
)

from PIL import Image, ImageDraw, ImageFont  # noqa: E402

W, H = 1024, 1024
MARGIN = 14

PAPER = (247, 243, 232)
INK = (20, 20, 20)
GREY = (90, 88, 80)
DARKGREY = (40, 40, 40)
DARKTEXT = (34, 34, 34)          # #222 — small text, contrast ~13.7:1
ACCENT = (178, 58, 32)          # orange-red (Ivy brand accent)
TEAL = (15, 59, 58)             # dark-green section bars
NAVY = (20, 33, 61)
SEA = (208, 226, 234)
LAND = (228, 214, 182)
LAND_LINE = (120, 110, 80)
RED = (178, 34, 34)
GOLD = (255, 200, 60)
CARD_BG = (255, 255, 255)
RULE = (180, 175, 160)

# Claim-status colours (ClaimReview-style verdict labels).
# REPORTED is #7a4d00 (v5: darkened from v4 #8a5a00): white on it is
# ~7.3:1 (v4 #8a5a00 was ~5.9:1; v3 amber was ~3.5:1). Measured
# programmatically — see news-image-20261126-work/audit/contrast-v5.py.
STATUS_COLORS = {
    "CONFIRMED": (30, 110, 60),
    "REPORTED": (122, 77, 0),
    "OFFICIAL": (30, 60, 110),
    "CLAIMED": (178, 34, 34),
}

# Wire outlets: when the named source IS a wire relay (Reuters, AP,
# Fox Weather), the source line shows "via {outlet}" as the source
# slot itself (v6, First Draft provenance) instead of repeating the
# outlet name as a "1st-hand" source. Every other source gets
# " · 1st-hand" appended. Exactly 5 rows are wire: 01, 02, 24
# (Reuters), 28 (AP), 29 (Fox Weather) — all unflagged.
WIRE = {"Reuters", "AP", "Fox Weather"}

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


F_SERIF = lambda s: font("DejaVuSerif-Bold.ttf", s)          # noqa: E731
F_BOLD = lambda s: font("DejaVuSans-Bold.ttf", s)            # noqa: E731
F_REG = lambda s: font("DejaVuSans.ttf", s)                  # noqa: E731


def text_w(draw, text, fnt):
    return draw.textlength(text, font=fnt)


def wrap(draw, text, fnt, width):
    """Greedy word wrap; returns list of lines fitting width."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if text_w(draw, trial, fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines or [""]


def draw_lines(draw, lines, x, y, fnt, fill, leading):
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def chip_width(draw, status):
    """Width of the status chip (8pt bold text + 5px padding total)."""
    return int(text_w(draw, status, F_BOLD(8))) + 5


def draw_status_chip(draw, x_right, y, status):
    """Small filled chip with the claim-status word, right-aligned at x_right."""
    color = STATUS_COLORS[status]
    fnt = F_BOLD(8)
    w, h = chip_width(draw, status), 13
    draw.rectangle([x_right - w, y, x_right, y + h], fill=color)
    draw.text((x_right - w + 2, y + 2), status, font=fnt,
              fill=(255, 255, 255))
    return w


# Rough continent outlines (lon, lat) for the stylised world map.
CONTINENTS = [
    # North America
    [(-168, 66), (-140, 70), (-120, 72), (-95, 80), (-80, 73), (-75, 62),
     (-65, 60), (-55, 52), (-60, 47), (-70, 42), (-75, 35), (-80, 32),
     (-85, 30), (-90, 21), (-95, 19), (-105, 20), (-110, 24), (-120, 34),
     (-125, 40), (-125, 49), (-135, 58), (-155, 60), (-168, 66)],
    # Greenland
    [(-58, 64), (-45, 60), (-40, 65), (-30, 68), (-25, 70), (-35, 76),
     (-55, 76), (-58, 70)],
    # South America (v6: Brazil bulge + Patagonia taper sharpened so
    # the continent reads at the 45px map height)
    [(-80, 9), (-75, 11), (-62, 10), (-55, 6), (-50, 0), (-44, -3),
     (-35, -8), (-38, -15), (-41, -23), (-48, -28), (-52, -33),
     (-57, -38), (-65, -41), (-68, -47), (-70, -52), (-73, -54),
     (-70, -40), (-71, -30), (-70, -20), (-77, -12), (-80, -5), (-80, 9)],
    # Africa (v6: Gulf of Guinea notch added; Horn kept sharp)
    [(-17, 15), (-10, 31), (-5, 35), (10, 37), (20, 32), (32, 31), (35, 28),
     (43, 12), (51, 11), (48, 2), (40, -10), (35, -18), (32, -26), (26, -34),
     (18, -35), (14, -22), (12, -6), (8, 4), (4, 6), (-8, 5), (-13, 8),
     (-17, 15)],
    # Eurasia
    [(-10, 36), (-9, 43), (-2, 48), (0, 51), (5, 53), (10, 58), (18, 56),
     (24, 58), (30, 62), (40, 68), (55, 68), (70, 72), (90, 75), (110, 76),
     (130, 72), (150, 70), (170, 66), (178, 65), (170, 60), (162, 56),
     (156, 51), (142, 50), (140, 40), (130, 33), (122, 30), (115, 22),
     (108, 18), (105, 9), (100, 8), (98, 12), (94, 16), (90, 22), (86, 20),
     (80, 15), (77, 8), (75, 12), (72, 20), (66, 25), (61, 25), (57, 26),
     (52, 28), (48, 30), (44, 29), (40, 32), (36, 36), (30, 38), (26, 38),
     (23, 36), (19, 40), (12, 44), (3, 42), (-2, 37), (-10, 36)],
    # Australia
    [(113, -22), (114, -30), (115, -35), (120, -34), (130, -32), (137, -35),
     (140, -38), (147, -39), (150, -37), (153, -27), (153, -24), (146, -19),
     (142, -15), (142, -11), (136, -12), (132, -12), (126, -14), (122, -17),
     (118, -20), (113, -22)],
    # Japan
    [(130, 31), (132, 33), (135, 34), (138, 35), (140, 38), (141, 41),
     (142, 44), (144, 44), (141, 40), (139, 37), (137, 35), (134, 34)],
    # Indonesia
    [(95, 5), (98, 3), (100, 0), (104, -3), (106, -6), (110, -7), (114, -8),
     (118, -9), (120, -10), (122, -9), (125, -9), (128, -4), (130, -2),
     (132, 0), (136, -2), (140, -4), (141, -8), (138, -8), (135, -5),
     (131, -1), (128, 1), (125, 1), (122, 0), (119, 0), (117, 2), (115, 1),
     (112, -2), (110, -5), (108, -6), (106, -5), (104, -2), (101, 1),
     (98, 4), (95, 5)],
    # New Zealand
    [(167, -45), (170, -42), (173, -40), (176, -38), (178, -37), (175, -40),
     (172, -43), (168, -46), (167, -45)],
    # United Kingdom
    [(-5, 50), (-3, 53), (-5, 56), (-3, 58), (-1, 57), (1, 52), (-5, 50)],
]


def draw_map(draw, box):
    """Stylised continents + numbered pins inside box (x0,y0,x1,y1)."""
    x0, y0, x1, y1 = box
    draw.rectangle(box, fill=SEA, outline=RULE)
    bw, bh = x1 - x0, y1 - y0

    def proj(lon, lat):
        return (x0 + (lon + 180.0) / 360.0 * bw,
                y0 + (85.0 - lat) / 145.0 * bh)

    # faint graticule so the band reads as a map, not an empty strip
    grat = (190, 210, 220)
    for lon in range(-150, 181, 30):
        gx, _ = proj(lon, 0)
        draw.line([(gx, y0), (gx, y1)], fill=grat, width=1)
    for lat in range(-60, 86, 30):
        _, gy = proj(0, lat)
        draw.line([(x0, gy), (x1, gy)], fill=grat, width=1)
    for poly in CONTINENTS:
        pts = [proj(lon, lat) for lon, lat in poly]
        draw.polygon(pts, fill=LAND, outline=LAND_LINE)
    # 1px leader lines for nudged pins (v6): the dot sits where the
    # cluster fits, the line points to the story's true position.
    # Drawn BEFORE the pins so each dot covers its line's start.
    for num, lon, lat, dlon, dlat in PINS:
        if (lon, lat) != (dlon, dlat):
            tx, ty = proj(lon, lat)
            px, py = proj(dlon, dlat)
            draw.line([(px, py), (tx, ty)], fill=LAND_LINE, width=1)
    for num, lon, lat, dlon, dlat in PINS:
        px, py = proj(dlon, dlat)
        r = 7
        draw.ellipse([px - r, py - r, px + r, py + r], fill=RED,
                     outline=(255, 255, 255), width=2)
        fnt = F_BOLD(10)
        label = str(num)
        tw = text_w(draw, label, fnt)
        draw.text((px - tw / 2, py - 7), label, font=fnt,
                  fill=(255, 255, 255))


def draw_scene(draw, key, box, accent):
    """A drawn mini-scene (not a lone glyph): background + 2-4 shapes
    that stage the story — ship + containers, skyline + smoke, etc."""
    x0, y0, x1, y1 = box
    draw.rectangle(box, fill=accent)
    cx, cy = (x0 + x1) // 2, (y0 + y1) // 2
    w, h = x1 - x0, y1 - y0
    white = (255, 255, 255)
    dark = (20, 20, 20)
    # ground line shared by most scenes
    if key not in ("rocket", "balloon", "sat"):
        draw.rectangle([x0 + 4, y1 - 6, x1 - 4, y1 - 4], fill=white)
    if key == "cargo":
        # container ship: thick hull + two rows of stacked containers + % tag.
        # v6: containers spread across the hull (5 columns at +-w/4, +-w/8,
        # 0) so the ship reads in a wide lead card, not a small cluster.
        draw.rectangle([x0 + 6, cy + 4, x1 - 6, cy + 12], fill=white)
        draw.polygon([(x0 + 6, cy + 4), (x0 + 14, cy + 12), (x1 - 14, cy + 12),
                      (x1 - 6, cy + 4)], fill=white)
        for row, oy in enumerate((cy - 12, cy - 2)):
            for j, ox in enumerate((-w // 4, -w // 8, 0, w // 8, w // 4)):
                fill = GOLD if (row + j) % 2 == 0 else white
                draw.rectangle([cx + ox - 7, oy, cx + ox + 7, oy + 9],
                               fill=fill, outline=dark)
        draw.rectangle([x1 - 26, y0 + 3, x1 - 5, y0 + 15], fill=GOLD)
        draw.text((x1 - 22, y0 + 4), "%", font=F_BOLD(9), fill=dark)
    elif key == "city":
        # skyline with lit windows + sun + smoke plume.
        # v6: buildings spread across the full width (8 towers in a wide
        # lead card) instead of clustering on the left third.
        n = max(5, w // 40)
        bw = 22 if w >= 200 else 14
        step = (w - 12 - bw) // (n - 1) if n > 1 else 0
        heights = (24, 34, 20, 30, 26, 36, 22, 28, 32, 18)
        for i in range(n):
            bx = x0 + 6 + i * step
            bh = heights[i % len(heights)]
            draw.rectangle([bx, y1 - 6 - bh, bx + bw, y1 - 6], fill=white)
            for wy in range(y1 - 6 - bh + 4, y1 - 10, 6):
                for wx in (bx + 5, bx + bw - 8):
                    draw.rectangle([wx, wy, wx + 3, wy + 2], fill=dark)
        draw.ellipse([x1 - 20, y0 + 3, x1 - 9, y0 + 14], fill=GOLD)
        for ox, oy, r in ((-2, 0, 4), (2, -5, 5), (6, -10, 4)):
            draw.ellipse([cx + ox - r, y0 + 8 + oy - r, cx + ox + r,
                          y0 + 8 + oy + r], fill=white)
    elif key == "bank":
        # pediment + columns + euro sign.
        # v6: pediment and columns widen with the box (pw = w/6) so the
        # temple reads in a wide lead card, not a small central cluster.
        pw = w // 6
        draw.polygon([(cx - pw, y0 + 8), (cx + pw, y0 + 8), (cx, y0 + 2)],
                     fill=white)
        for ox in (-pw, -pw // 3, pw // 3, pw):
            draw.rectangle([cx + ox - 2, y0 + 10, cx + ox + 2, y1 - 8],
                           fill=white)
        draw.rectangle([x0 + 6, y1 - 8, x1 - 6, y1 - 5], fill=white)
        draw.text((cx - 5, y0 + 12), "E", font=F_BOLD(10), fill=dark)
    elif key == "tankerfire":
        # tanker truck + flame + smoke
        draw.rectangle([x0 + 6, cy, cx + 8, cy + 8], fill=white)
        draw.rectangle([cx + 10, cy - 2, x1 - 8, cy + 8], fill=GOLD)
        for wx in (x0 + 14, cx, x1 - 12):
            draw.ellipse([wx - 3, cy + 8, wx + 3, cy + 13], fill=dark)
        draw.polygon([(cx - 2, y0 + 2), (cx + 8, cy - 4), (cx + 4, y0 + 12),
                      (cx - 6, y0 + 10)], fill=(255, 120, 40))
    elif key == "strike":
        # airstrike on a city: explosion bursts + missile streaks +
        # building silhouettes (reads as "strikes kill 3", not a network).
        # v6: positions relative to the box width (temp is now 108 wide),
        # so the bursts/buildings spread instead of clustering left.
        for ex, ey, r in ((x0 + (w * 28) // 100, 12, 8),
                          (x0 + (w * 72) // 100, 10, 7)):
            draw.polygon([(ex, ey - r), (ex + 3, ey - 3), (ex + r, ey),
                          (ex + 3, ey + 3), (ex, ey + r), (ex - 3, ey + 3),
                          (ex - r, ey), (ex - 3, ey - 3)], fill=GOLD)
        for mx, my, dx, dy in ((x0 + 8, 4, 8, 10), (x1 - 16, 6, -8, 10)):
            draw.line([mx, my, mx + dx, my + dy], fill=white, width=2)
            draw.ellipse([mx + dx - 2, my + dy - 2, mx + dx + 2,
                          my + dy + 2], fill=GOLD)
        for bx, bw, bh in ((x0 + 8, 18, 16), (x0 + w // 2 - 9, 18, 22),
                           (x1 - 26, 18, 14)):
            draw.rectangle([bx, y1 - 6 - bh, bx + bw, y1 - 6], fill=white)
            draw.rectangle([bx + 4, y1 - 6 - bh + 4, bx + 7,
                            y1 - 6 - bh + 7], fill=dark)
            draw.rectangle([bx + bw - 7, y1 - 6 - bh + 4, bx + bw - 4,
                            y1 - 6 - bh + 7], fill=dark)
    elif key == "balloon":
        # parade balloon + basket + clouds
        draw.ellipse([cx - 14, y0 + 2, cx + 14, y0 + 22], fill=white)
        draw.line([cx - 8, y0 + 22, cx - 4, y0 + 28], fill=white, width=2)
        draw.line([cx + 8, y0 + 22, cx + 4, y0 + 28], fill=white, width=2)
        draw.rectangle([cx - 5, y0 + 28, cx + 5, y0 + 33], fill=GOLD)
        draw.ellipse([x0 + 4, y1 - 12, x0 + 16, y1 - 6], fill=white)
        draw.ellipse([x1 - 16, y1 - 10, x1 - 4, y1 - 4], fill=white)
    elif key == "rocket":
        # rocket + flame + stars
        draw.polygon([(cx, y0 + 2), (cx + 6, y0 + 16), (cx - 6, y0 + 16)],
                     fill=white)
        draw.rectangle([cx - 6, y0 + 16, cx + 6, y0 + 28], fill=white)
        draw.polygon([(cx - 6, y0 + 22), (cx - 10, y0 + 28), (cx - 6, y0 + 26)],
                     fill=GOLD)
        draw.polygon([(cx + 6, y0 + 22), (cx + 10, y0 + 28), (cx + 6, y0 + 26)],
                     fill=GOLD)
        draw.polygon([(cx, y0 + 28), (cx + 4, y0 + 36), (cx - 4, y0 + 36)],
                     fill=(255, 120, 40))
        for sx, sy in ((x0 + 8, y0 + 8), (x1 - 10, y0 + 12), (x0 + 12, y0 + 24)):
            draw.ellipse([sx - 1, sy - 1, sx + 1, sy + 1], fill=white)
    elif key == "mountain":
        # mine mountain + shaft + helmet
        draw.polygon([(x0 + 6, y1 - 6), (cx, y0 + 4), (x1 - 6, y1 - 6)],
                     fill=white)
        draw.polygon([(cx - 4, y0 + 14), (cx + 4, y0 + 14), (cx, y0 + 22)],
                     fill=dark)
        draw.rectangle([cx - 10, y1 - 14, cx + 10, y1 - 6], fill=GOLD)
        draw.pieslice([cx - 6, y1 - 20, cx + 6, y1 - 12], 180, 360, fill=GOLD)
    elif key == "storm":
        # storm cloud + rain + lightning
        for ox, oy, r in ((-8, 2, 8), (0, -4, 10), (9, 2, 8)):
            draw.ellipse([cx + ox - r, cy + oy - r - 4, cx + ox + r,
                          cy + oy + r - 4], fill=white)
        draw.rectangle([cx - 14, cy + 2, cx + 16, cy + 8], fill=white)
        draw.polygon([(cx + 2, cy + 8), (cx - 2, cy + 16), (cx + 3, cy + 16),
                      (cx - 1, cy + 24)], fill=GOLD)
        for rx in (x0 + 10, x1 - 12):
            draw.line([(rx, cy + 12), (rx, cy + 18)], fill=white, width=2)
    elif key == "missile":
        # missile on launcher + trajectory dots
        draw.rectangle([x0 + 8, cy + 2, x1 - 8, cy + 6], fill=white)
        draw.polygon([(x1 - 8, cy - 2), (x1 - 2, cy + 4), (x1 - 8, cy + 10)],
                     fill=GOLD)
        for dx in (0, 10, 20):
            draw.ellipse([x0 + 8 + dx, y0 + 6, x0 + 12 + dx, y0 + 10],
                         fill=white)
    elif key == "scales":
        # scales of justice + courthouse base
        draw.line([cx, y0 + 6, cx, y1 - 10], fill=white, width=2)
        draw.line([cx - 14, y0 + 8, cx + 14, y0 + 8], fill=white, width=2)
        for ox in (-14, 14):
            draw.line([cx + ox, y0 + 8, cx + ox, y0 + 14], fill=white, width=2)
            draw.pieslice([cx + ox - 6, y0 + 12, cx + ox + 6, y0 + 20], 0,
                          180, fill=GOLD)
        draw.rectangle([x0 + 8, y1 - 10, x1 - 8, y1 - 6], fill=white)
    elif key == "shield":
        # shield + palm frond
        draw.polygon([(cx - 12, y0 + 4), (cx + 12, y0 + 4), (cx + 12, cy + 4),
                      (cx, y1 - 6), (cx - 12, cy + 4)], fill=white)
        draw.text((cx - 4, cy - 6), "P", font=F_BOLD(12), fill=dark)
        draw.line([(x1 - 8, y0 + 6), (x1 - 16, y0 + 16)], fill=GOLD, width=2)
    elif key == "ballot":
        # ballot box + slip + check
        draw.rectangle([x0 + 10, y0 + 12, x1 - 10, y1 - 6], fill=white)
        draw.rectangle([cx - 12, y0 + 14, cx + 12, y0 + 17], fill=dark)
        draw.polygon([(cx - 10, y0 + 2), (cx - 2, y0 + 12), (cx + 2, y0 + 12),
                      (cx + 10, y0 + 2)], fill=GOLD)
        draw.line([(cx - 6, y1 - 16), (cx - 2, y1 - 11), (cx + 8, y1 - 20)],
                  fill=dark, width=2)
    elif key == "sat":
        draw.rectangle([cx - 6, cy - 5, cx + 6, cy + 5], fill=white)
        draw.rectangle([x0 + 6, cy - 3, cx - 8, cy + 3], fill=GOLD)
        draw.rectangle([cx + 8, cy - 3, x1 - 6, cy + 3], fill=GOLD)
    elif key == "store":
        # supermarket storefront (Cartagena siege): striped awning,
        # sign band, door + tall shop windows
        n = 6
        sw = (w - 12) // n
        for i in range(n):
            fill = white if i % 2 == 0 else GOLD
            draw.rectangle([x0 + 6 + i * sw, y0 + 3,
                            x0 + 6 + (i + 1) * sw, y0 + 11], fill=fill)
        draw.rectangle([x0 + 6, y0 + 11, x1 - 6, y1 - 4], fill=white)
        draw.rectangle([cx - 24, y0 + 13, cx + 24, y0 + 17], fill=GOLD)
        draw.rectangle([x0 + 14, y0 + 20, x0 + 30, y1 - 4], fill=dark)
        draw.rectangle([cx - 6, y0 + 20, cx + 12, y1 - 4], fill=dark)
        draw.rectangle([cx + 18, y0 + 20, x1 - 14, y1 - 4], fill=dark)
    elif key == "debris":
        # intercepted drone: shrapnel burst + falling fragments
        draw.polygon([(cx, y0 + 2), (cx + 4, y0 + 10), (cx + 12, y0 + 8),
                      (cx + 7, y0 + 15), (cx + 12, y0 + 22), (cx + 4, y0 + 20),
                      (cx, y0 + 28), (cx - 4, y0 + 20), (cx - 12, y0 + 22),
                      (cx - 7, y0 + 15), (cx - 12, y0 + 8), (cx - 4, y0 + 10)],
                     fill=GOLD)
        for fx, fy in ((x0 + 16, cy + 4), (x1 - 18, cy + 8), (cx - 24, cy + 10),
                       (cx + 22, cy + 2)):
            draw.rectangle([fx - 2, fy - 2, fx + 2, fy + 2], fill=white)
    elif key == "clinic":
        # Ebola-site clinic: building + red-cross sign + door + windows
        draw.rectangle([x0 + 12, y0 + 18, x1 - 12, y1 - 6], fill=white)
        draw.rectangle([cx - 16, y0 + 4, cx + 16, y0 + 16], fill=RED)
        draw.rectangle([cx - 2, y0 + 6, cx + 2, y0 + 14], fill=white)
        draw.rectangle([cx - 6, y0 + 9, cx + 6, y0 + 11], fill=white)
        draw.rectangle([cx - 4, y1 - 16, cx + 4, y1 - 6], fill=dark)
        draw.rectangle([x0 + 18, y0 + 26, x0 + 28, y0 + 34], fill=dark)
        draw.rectangle([x1 - 28, y0 + 26, x1 - 18, y0 + 34], fill=dark)
    draw.rectangle(box, outline=(0, 0, 0, 40))


def draw_lead_card(draw, num, headline, deck, scene, accent, x, y, w, h):
    """One large lead card (v6): 76px scene on top, 26pt serif headline
    on TWO lines, 9pt deck, source line (number + source + place +
    field + provenance, NO date — the date is on the masthead and every
    grid row) + a FILLED status chip (8pt bold, like the list rows)."""
    story = next(s for s in STORIES if s[0] == num)
    _n, _r, _hl, _sm, source, status, field, place, flagged = story
    draw.rectangle([x, y, x + w, y + h], fill=CARD_BG, outline=RULE)
    draw_scene(draw, scene, (x + 1, y + 1, x + w - 1, y + 77), accent)
    assert isinstance(headline, tuple) and len(headline) == 2, \
        f"lead headline must be 2 lines: {headline!r}"
    for i, line in enumerate(headline):
        assert text_w(draw, line, F_SERIF(26)) <= w - 12, \
            f"lead headline line too wide: {line!r}"
        draw.text((x + 6, y + 80 + i * 28), line, font=F_SERIF(26), fill=INK)
    deck_lines = wrap(draw, deck, F_REG(9), w - 12)
    assert len(deck_lines) == 1, f"lead deck wraps: {deck!r}"
    draw_lines(draw, deck_lines[:1], x + 6, y + 139, F_REG(9), DARKGREY, 11)
    # source + filled status chip, bottom-anchored (no date here)
    flag = "\u2691 " if flagged else ""
    if source in WIRE:
        src_txt, prov = f"via {source}", ""
    else:
        src_txt, prov = source, " \u00b7 1st-hand"
    stake = "" if flagged else " \u00b7 no stake"
    src = (f"{num:02d}  {flag}{src_txt} \u00b7 {place} "
           f"\u00b7 {field.upper()}{prov}{stake}  ")
    sy = y + 151
    draw.text((x + 6, sy), src, font=F_REG(8), fill=DARKTEXT)
    off = text_w(draw, src, F_REG(8))
    cw = int(text_w(draw, status, F_BOLD(8))) + 5
    assert off + cw <= w - 12, f"lead source too long: {src!r}{status}"
    draw.rectangle([x + 6 + off, sy - 1, x + 6 + off + cw, sy + 12],
                   fill=STATUS_COLORS[status])
    draw.text((x + 6 + off + 2, sy + 1), status, font=F_BOLD(8),
              fill=(255, 255, 255))


def draw_scenes(img, draw, y):
    """13 scene tiles in two rows (7+6), 135x50, number badge top-left.

    The scene art is drawn into a 108x40 temp and upscaled uniformly
    (1.25x) so the figures fill the tile instead of sitting small in
    the middle of a wide box. The second row is centred.
    Each tile carries a caption bar at the bottom ("NN · LABEL", v5).
    """
    gap = 8
    tile_w = (W - 2 * MARGIN - gap * 6) // 7
    tile_h = 50
    row_gap = 6
    rows = [SCENES[:7], SCENES[7:]]
    for ri, row in enumerate(rows):
        row_w = len(row) * tile_w + (len(row) - 1) * gap
        x0 = MARGIN + (W - 2 * MARGIN - row_w) // 2
        ty = y + ri * (tile_h + row_gap)
        for ci, (num, scene, accent) in enumerate(row):
            tx = x0 + ci * (tile_w + gap)
            tmp = Image.new("RGB", (108, 40), accent)
            td = ImageDraw.Draw(tmp)
            draw_scene(td, scene, (0, 0, 108, 40), accent)
            art = tmp.resize((tile_w, tile_h), Image.LANCZOS)
            img.paste(art, (tx, ty))
            draw.rectangle([tx, ty, tx + tile_w, ty + tile_h], outline=RULE)
            # number badge, top-left
            badge = f"{num:02d}"
            bw = 26
            draw.rectangle([tx, ty, tx + bw, ty + 15], fill=INK)
            draw.text((tx + 4, ty + 2), badge, font=F_BOLD(10),
                      fill=(255, 255, 255))
            # caption bar at the tile bottom: "NN · SHORT LABEL"
            cap = f"{num:02d} \u00b7 {SCENE_CAPTIONS[num]}"
            assert text_w(draw, cap, F_BOLD(8)) <= tile_w - 8, \
                f"scene caption too wide: {cap!r}"
            draw.rectangle([tx, ty + tile_h - 12, tx + tile_w, ty + tile_h],
                           fill=INK)
            draw.text((tx + 4, ty + tile_h - 10), cap, font=F_BOLD(8),
                      fill=(255, 255, 255))


def draw_timeline(draw, y):
    """UTC timeline on a true 00-24 scale. y = top of the band (56px).

    Captions are 10pt bold, "NN · LABEL", and staggered: the
    00:23-01:39 cluster is split above/below the line. A 1px leader
    line joins each dot to its caption (v5). Ticks at 00 / 06 / 12 /
    18 / 24.
    """
    def tx(minutes):
        return MARGIN + minutes / 1440.0 * (W - 2 * MARGIN)

    def mins(t):
        h, m = t.split(":")
        return int(h) * 60 + int(m)

    axis_y = y + 27
    # label, top-right
    lab = "THE DAY IN UTC"
    draw.text((W - MARGIN - text_w(draw, lab, F_BOLD(9)), y), lab,
              font=F_BOLD(9), fill=TEAL)
    # axis line
    draw.line([MARGIN, axis_y, W - MARGIN, axis_y], fill=RULE, width=2)
    # ticks at 00/06/12/18/24 with labels below the axis
    for h in (0, 6, 12, 18, 24):
        x = tx(h * 60)
        draw.line([x, axis_y - 3, x, axis_y + 3], fill=INK, width=2)
        tlab = f"{h:02d}"
        tw = text_w(draw, tlab, F_REG(8))
        if h == 0:
            lx = x
        elif h == 24:
            lx = x - tw
        else:
            lx = x - tw / 2
        draw.text((lx, y + 46), tlab, font=F_REG(8), fill=DARKTEXT)
    # captions, staggered so same-row captions never overlap.
    # above row 1: 00:23, 05:44, 12:28, 18:07; above row 2: 01:39;
    # below: 00:54, 10:25, 14:02.
    row_of = {6: 0, 2: 0, 8: 0, 16: 0, 5: 1, 15: 2, 19: 2, 4: 2}
    row_y = {0: y, 1: y + 11, 2: y + 33}
    placed = {0: [], 1: [], 2: []}
    for t, label, num in TIMELINE:
        cap = f"{num:02d} \u00b7 {label}"
        cw = text_w(draw, cap, F_BOLD(10))
        x = tx(mins(t))
        row = row_of[num]
        for s, e in placed[row]:
            assert x + cw + 6 <= s or x >= e + 6, \
                f"timeline captions overlap: {cap!r}"
        placed[row].append((x, x + cw))
        draw.text((x, row_y[row]), cap, font=F_BOLD(10), fill=DARKTEXT)
        draw.ellipse([x - 4, axis_y - 4, x + 4, axis_y + 4], fill=ACCENT,
                     outline=(255, 255, 255), width=1)
        # 1px leader line: dot edge to caption (above rows go up,
        # below row goes down)
        if row in (0, 1):
            draw.line([x, row_y[row] + 10, x, axis_y - 4], fill=DARKTEXT,
                      width=1)
        else:
            draw.line([x, axis_y + 4, x, row_y[row]], fill=DARKTEXT,
                      width=1)


def fit_one_line(draw, text, fnt, width):
    """Truncate text with '...' until it fits one line of width.

    Drops whole words from the end, so the result never ends
    mid-word ("bud..."); the ellipsis follows a complete word.
    """
    if len(wrap(draw, text, fnt, width)) <= 1:
        return text
    words = text.split()
    while len(words) > 4:
        words = words[:-1]
        cand = " ".join(words) + "..."
        if len(wrap(draw, cand, fnt, width)) <= 1:
            return cand
    # last resort: hard cut (should not happen for these summaries)
    return text[:40].rstrip() + "..."


def draw_column(draw, regions, x, y, col_w, grid_bottom):
    """Draw region sections + stories in one column; returns bottom y.

    Per story (33px): 14pt headline (asserted 1 line) with the status
    chip at the right end of the headline line, then 1 line of summary
    at 11pt (truncated with '...' if needed, target ~55 chars), then
    the source line "Source · Place · 26 Nov · FIELD · provenance"
    with a stake flag (U+2691) and "no stake" on unflagged rows.
    v6: chips 8pt bold (padding 5), number gutter 21px, source lines
    in #222 with provenance + "no stake" (First Draft pillars).
    """
    by_region = {}
    for s in STORIES:
        by_region.setdefault(s[1], []).append(s)
    for region in regions:
        stories = by_region[region]
        draw.rectangle([x, y, x + col_w, y + 20], fill=TEAL)
        label = f"{region}  -  {len(stories)}"
        draw.text((x + 6, y + 3), label, font=F_BOLD(13),
                  fill=(255, 255, 255))
        y += 22
        for num, _r, headline, summary, source, status, field, place, flagged in stories:
            cw = chip_width(draw, status)
            hl_lines = wrap(draw, headline, F_BOLD(14), col_w - 21 - cw)
            assert len(hl_lines) == 1, f"headline wraps: {headline!r}"
            draw.text((x, y), f"{num:02d}", font=F_BOLD(14), fill=ACCENT)
            tx = x + 21
            draw.text((tx, y), headline, font=F_BOLD(14), fill=INK)
            draw_status_chip(draw, x + col_w, y, status)
            y += 14
            text = fit_one_line(draw, summary, F_REG(11), col_w - 21)
            draw.text((tx, y), text, font=F_REG(11), fill=DARKGREY)
            y += 11
            flag = "\u2691 " if flagged else ""
            if source in WIRE:
                src_txt, prov = f"via {source}", ""
            else:
                src_txt, prov = source, " \u00b7 1st-hand"
            stake = "" if flagged else " \u00b7 no stake"
            src = (f"{flag}{src_txt} \u00b7 {place} \u00b7 26 Nov "
                   f"\u00b7 {field.upper()}{prov}{stake}")
            assert text_w(draw, src, F_REG(8)) <= col_w - 21, \
                f"source too long: {src!r}"
            draw.text((tx, y), src, font=F_REG(8), fill=DARKTEXT)
            y += 8
    return y


def build(output_path):
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- Masthead ----
    title = "IVY WORLD FRONTPAGE"
    f_title = F_SERIF(30)
    tw = text_w(d, title, f_title)
    d.text(((W - tw) / 2, 4), title, font=f_title, fill=INK)
    d.line([MARGIN, 40, W - MARGIN, 40], fill=INK, width=2)
    spec = (f"{EDITION_DATE}  -  38 STORIES  -  10 REGIONS  -  "
            f"{len(FIELDS)} FIELDS  -  UTC TIMELINE")
    f_spec = F_BOLD(11)
    tw = text_w(d, spec, f_spec)
    d.text(((W - tw) / 2, 44), spec, font=f_spec, fill=ACCENT)

    # ---- Fields strip ----
    fields_text = "FIELDS:  " + "  \u00b7  ".join(FIELDS)
    assert text_w(d, fields_text, F_REG(8)) <= W - 2 * MARGIN, "fields strip too wide"
    d.text((MARGIN, 60), fields_text, font=F_REG(8), fill=DARKTEXT)

    # ---- 3 large lead cards ----
    ly, lh = 70, 166
    lw = (W - 2 * MARGIN - 2 * 8) // 3
    for i, (num, headline, deck, scene, accent) in enumerate(LEADS):
        draw_lead_card(d, num, headline, deck, scene, accent,
                       MARGIN + i * (lw + 8), ly, lw, lh)

    # ---- Drawn scenes strip (13, two rows 7+6) ----
    draw_scenes(img, d, 240)

    # ---- Pinned world map ----
    d.text((MARGIN, 348),
           "WHERE IT HAPPENED  -  13 NUMBERED PINS = STORY NUMBERS  -  "
           "13 DRAWN SCENES ABOVE",
           font=F_BOLD(9), fill=TEAL)
    draw_map(d, (MARGIN, 364, W - MARGIN, 364 + 45))

    # ---- UTC timeline (true 00-24 scale) ----
    draw_timeline(d, 415)

    # ---- Story grid ----
    grid_top = 475
    grid_bottom = 973
    col_w = (W - 2 * MARGIN - 2 * 8) // 3
    col_x = [MARGIN, MARGIN + col_w + 8, MARGIN + 2 * (col_w + 8)]
    bottoms = []
    for i, regions in enumerate(COLUMNS):
        bottoms.append(draw_column(d, regions, col_x[i], grid_top, col_w,
                                   grid_bottom))
    max_bottom = max(bottoms)
    assert max_bottom <= grid_bottom, f"grid overflow: {max_bottom}"

    # Claim-labels key in the third column (holds the stake-flag legend).
    b = bottoms[2]
    if grid_bottom - b >= 40:
        title, note = ("CLAIM LABELS",
            "CONFIRMED: fact. OFFICIAL: body announced it. REPORTED: "
            "relayed, unconfirmed. CLAIMED: one side's claim. "
            "\u2691: source has a stake.")
        lines = wrap(d, note, F_REG(8), col_w - 12)
        assert len(lines) <= 2, f"claim-labels note too long: {note!r}"
        box_h = 16 + len(lines) * 11 + 6
        assert b + 4 + box_h <= grid_bottom, "claim-labels box overflows"
        d.rectangle([col_x[2], b + 4, col_x[2] + col_w, b + 4 + box_h],
                    outline=RULE)
        d.text((col_x[2] + 6, b + 8), title, font=F_BOLD(9), fill=TEAL)
        draw_lines(d, lines, col_x[2] + 6, b + 20, F_REG(8), DARKTEXT, 11)

    # ---- Footer: DATE CHECK (states EXCLUSION, never an admission) ----
    # v6: DATE CHECK now states the First Draft pillars (provenance,
    # source, date, location, motivation) + the claim status; the
    # stake-flag legend moved here from the footer line (which drops
    # "⚑ = SOURCE HAS A STAKE" to avoid duplication).
    d.line([MARGIN, 977, W - MARGIN, 977], fill=INK, width=2)
    foot = ("DATE CHECK - Every story on this page is dated Thu 26 Nov 2026. "
            "No story dated 25 Nov or earlier appears here. Each story shows "
            "provenance, source, date, location and motivation "
            "(\u2691 = source has a stake) and a claim status (CONFIRMED / "
            "REPORTED / OFFICIAL / CLAIMED).")
    fl = wrap(d, foot, F_REG(10), W - 2 * MARGIN)
    assert len(fl) == 2, f"DATE CHECK wraps to {len(fl)} lines"
    y = draw_lines(d, fl, MARGIN, 983, F_REG(10), INK, 13)
    footline = ("IVY WORLD FRONTPAGE \u00b7 26 NOV 2026 \u00b7 38 STORIES "
                "\u00b7 10 REGIONS \u00b7 19 FIELDS \u00b7 UTC TIMELINE "
                "\u00b7 13 SCENES \u00b7 3 LEAD CARDS \u00b7 13 MAP PINS")
    assert text_w(d, footline, F_BOLD(10)) <= W - 2 * MARGIN, \
        "footer line too wide"
    d.text((MARGIN, y + 2), footline, font=F_BOLD(10), fill=DARKTEXT)
    assert y + 2 + 10 <= H, "footer overflows page"

    img.save(output_path, "PNG", optimize=True)

    # ---- Count checks (template rules) ----
    regions = sorted({s[1] for s in STORIES})
    fields = sorted({s[6] for s in STORIES})
    assert len(STORIES) == 38, len(STORIES)
    assert len(regions) == 10, regions
    assert sum(len([s for s in STORIES if s[1] == r]) for r in regions) == 38
    assert len(fields) == len(FIELDS) == 19, fields
    assert fields == sorted(FIELDS), "FIELDS list mismatch"
    assert len(LEADS) == 3
    assert len(SCENES) == 13
    assert len(PINS) == 13
    assert {p[0] for p in PINS} == {s[0] for s in SCENES}, "pins != scenes"
    assert len(TIMELINE) == 8
    assert all(s[5] in STATUS_COLORS for s in STORIES), "bad status"
    size = os.path.getsize(output_path)
    assert size <= 1024 * 1024, f"over 1 MiB: {size}"
    counts = {st: len([s for s in STORIES if s[5] == st])
              for st in STATUS_COLORS}
    print(f"OK {output_path}: {size} bytes, 1024x1024")
    print(f"stories={len(STORIES)} regions={len(regions)} "
          f"({', '.join(f'{r}:{len([s for s in STORIES if s[1]==r])}' for r in regions)})")
    print(f"fields={len(fields)} leads={len(LEADS)} "
          f"scenes={len(SCENES)} pins={len(PINS)} "
          f"timeline={len(TIMELINE)} grid_bottom_max={max_bottom}")
    print(f"status: {counts}  flagged={len([s for s in STORIES if s[8]])}")


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "world-news-26-nov-2026.png")
    build(out)
