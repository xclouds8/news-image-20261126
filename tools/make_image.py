#!/usr/bin/env python3
"""Draw the 26 November 2026 news-image front page (1024x1024 PNG).

"Ivy World Frontpage" — koran v2 per
~/workspace/make-fun-agent/templates/news-image-newspaper.md and the
top-10 study (~/workspace/make-fun-agent/top10-study-20261126.md):
masthead brand, fields strip, UTC timeline on a true 00-24 scale,
3 large lead cards with drawn scenes, pinned world map (13 numbered
pins = the 13 scene numbers), 13 drawn scenes in two rows (7+6),
38 numbered stories in 9 regions, each with a named source, a place,
a date and a claim-status label (CONFIRMED / REPORTED / OFFICIAL /
CLAIMED), DATE CHECK footer stating exclusion of earlier-day events.

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
    COLUMNS, EDITION_DATE, FIELDS, LEADS, PINS, SCENES, STORIES,
    TIMELINE,
)

from PIL import Image, ImageDraw, ImageFont  # noqa: E402

W, H = 1024, 1024
MARGIN = 14

PAPER = (247, 243, 232)
INK = (20, 20, 20)
GREY = (90, 88, 80)
DARKGREY = (40, 40, 40)
DARKTEXT = (51, 51, 51)          # #333 — small text, contrast ~11.4:1
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
# REPORTED is #8a5a00: white on it is ~5.9:1 (v3 amber was ~3.5:1).
STATUS_COLORS = {
    "CONFIRMED": (30, 110, 60),
    "REPORTED": (138, 90, 0),
    "OFFICIAL": (30, 60, 110),
    "CLAIMED": (178, 34, 34),
}

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
    """Width of the status chip (7pt bold text + 4px padding each side)."""
    return int(text_w(draw, status, F_BOLD(7))) + 8


def draw_status_chip(draw, x_right, y, status):
    """Small filled chip with the claim-status word, right-aligned at x_right."""
    color = STATUS_COLORS[status]
    fnt = F_BOLD(7)
    w, h = chip_width(draw, status), 11
    draw.rectangle([x_right - w, y, x_right, y + h], fill=color)
    draw.text((x_right - w + 4, y + 2), status, font=fnt,
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
    # South America
    [(-80, 9), (-75, 11), (-62, 10), (-55, 6), (-50, 0), (-44, -3),
     (-35, -8), (-40, -20), (-48, -28), (-55, -35), (-65, -41), (-70, -50),
     (-73, -54), (-70, -40), (-72, -20), (-77, -12), (-80, -5), (-80, 9)],
    # Africa
    [(-17, 15), (-10, 31), (-5, 35), (10, 37), (20, 32), (32, 31), (35, 28),
     (43, 12), (51, 11), (48, 2), (40, -10), (35, -18), (32, -26), (26, -34),
     (18, -35), (14, -22), (12, -6), (8, 4), (-8, 5), (-13, 8), (-17, 15)],
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
    for num, _lon, _lat, dlon, dlat in PINS:
        px, py = proj(dlon, dlat)
        r = 7
        draw.ellipse([px - r, py - r, px + r, py + r], fill=RED,
                     outline=(255, 255, 255), width=2)
        fnt = F_BOLD(9)
        label = str(num)
        tw = text_w(draw, label, fnt)
        draw.text((px - tw / 2, py - 6), label, font=fnt,
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
    if key not in ("drone", "rocket", "balloon", "sat"):
        draw.rectangle([x0 + 4, y1 - 6, x1 - 4, y1 - 4], fill=white)
    if key == "cargo":
        # container ship: thick hull + two rows of stacked containers + % tag
        draw.rectangle([x0 + 6, cy + 4, x1 - 6, cy + 12], fill=white)
        draw.polygon([(x0 + 6, cy + 4), (x0 + 14, cy + 12), (x1 - 14, cy + 12),
                      (x1 - 6, cy + 4)], fill=white)
        for row, oy in enumerate((cy - 12, cy - 2)):
            for j, ox in enumerate((-24, -8, 8)):
                fill = GOLD if (row + j) % 2 == 0 else white
                draw.rectangle([cx + ox - 7, oy, cx + ox + 7, oy + 9],
                               fill=fill, outline=dark)
        draw.rectangle([x1 - 26, y0 + 3, x1 - 5, y0 + 15], fill=GOLD)
        draw.text((x1 - 22, y0 + 4), "%", font=F_BOLD(9), fill=dark)
    elif key == "city":
        # skyline with lit windows + sun + smoke plume
        for bx, bh in ((x0 + 8, 20), (x0 + 24, 30), (x0 + 42, 16),
                       (x0 + 58, 26), (x0 + 76, 18)):
            draw.rectangle([bx, y1 - 6 - bh, bx + 14, y1 - 6], fill=white)
            for wy in range(y1 - 6 - bh + 4, y1 - 10, 6):
                draw.rectangle([bx + 3, wy, bx + 5, wy + 2], fill=dark)
                draw.rectangle([bx + 9, wy, bx + 11, wy + 2], fill=dark)
        draw.ellipse([x1 - 20, y0 + 3, x1 - 9, y0 + 14], fill=GOLD)
        for ox, oy, r in ((-2, 0, 4), (2, -5, 5), (6, -10, 4)):
            draw.ellipse([cx + ox - r, y0 + 8 + oy - r, cx + ox + r,
                          y0 + 8 + oy + r], fill=white)
    elif key == "bank":
        # pediment + columns + euro sign
        draw.polygon([(cx - 26, y0 + 8), (cx + 26, y0 + 8), (cx, y0 + 2)],
                     fill=white)
        for ox in (-20, -7, 6, 19):
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
    elif key == "drone":
        draw.line([x0 + 10, y0 + 8, x1 - 10, y1 - 8], fill=white, width=2)
        draw.line([x1 - 10, y0 + 8, x0 + 10, y1 - 8], fill=white, width=2)
        for px, py in ((x0 + 10, y0 + 8), (x1 - 10, y0 + 8),
                       (x0 + 10, y1 - 8), (x1 - 10, y1 - 8)):
            draw.ellipse([px - 4, py - 4, px + 4, py + 4], fill=white)
        draw.rectangle([cx - 5, cy - 4, cx + 5, cy + 4], fill=GOLD)
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
    """One large lead card: scene on top, 24pt serif headline, deck,
    source line (number + source + place + date + field) + status word."""
    story = next(s for s in STORIES if s[0] == num)
    _n, _r, _hl, _sm, source, status, field, place, flagged = story
    draw.rectangle([x, y, x + w, y + h], fill=CARD_BG, outline=RULE)
    draw_scene(draw, scene, (x + 1, y + 1, x + w - 1, y + 51), accent)
    hl_lines = wrap(draw, headline, F_SERIF(24), w - 12)
    assert len(hl_lines) == 1, f"lead headline wraps: {headline!r}"
    draw_lines(draw, hl_lines[:1], x + 6, y + 54, F_SERIF(24), INK, 28)
    deck_lines = wrap(draw, deck, F_REG(9), w - 12)
    assert len(deck_lines) == 1, f"lead deck wraps: {deck!r}"
    draw_lines(draw, deck_lines[:1], x + 6, y + 84, F_REG(9), DARKGREY, 11)
    # source + coloured status word, bottom-anchored
    flag = "\u2691 " if flagged else ""
    src = (f"{num:02d}  {flag}{source} \u00b7 {place} \u00b7 26 Nov "
           f"\u00b7 {field.upper()}  ")
    sy = y + 99
    draw.text((x + 6, sy), src, font=F_REG(8), fill=DARKTEXT)
    off = text_w(draw, src, F_REG(8))
    total = off + text_w(draw, status, F_BOLD(8))
    assert total <= w - 12, f"lead source too long: {src!r}{status}"
    draw.text((x + 6 + off, sy), status, font=F_BOLD(8),
              fill=STATUS_COLORS[status])


def draw_scenes(img, draw, y):
    """13 scene tiles in two rows (7+6), 135x60, number badge top-left.

    The scene art is drawn into a 90x40 temp and upscaled uniformly
    (1.5x) so the figures fill the tile instead of sitting small in
    the middle of a wide box. The second row is centred.
    """
    gap = 8
    tile_w = (W - 2 * MARGIN - gap * 6) // 7
    tile_h = 60
    row_gap = 6
    rows = [SCENES[:7], SCENES[7:]]
    for ri, row in enumerate(rows):
        row_w = len(row) * tile_w + (len(row) - 1) * gap
        x0 = MARGIN + (W - 2 * MARGIN - row_w) // 2
        ty = y + ri * (tile_h + row_gap)
        for ci, (num, scene, accent) in enumerate(row):
            tx = x0 + ci * (tile_w + gap)
            tmp = Image.new("RGB", (90, 40), accent)
            td = ImageDraw.Draw(tmp)
            draw_scene(td, scene, (0, 0, 90, 40), accent)
            art = tmp.resize((tile_w, tile_h), Image.LANCZOS)
            img.paste(art, (tx, ty))
            draw.rectangle([tx, ty, tx + tile_w, ty + tile_h], outline=RULE)
            # number badge, top-left
            badge = f"{num:02d}"
            bw = 26
            draw.rectangle([tx, ty, tx + bw, ty + 15], fill=INK)
            draw.text((tx + 4, ty + 2), badge, font=F_BOLD(10),
                      fill=(255, 255, 255))


def draw_timeline(draw, y):
    """UTC timeline on a true 00-24 scale. y = top of the band (56px).

    Captions are 10pt bold, prefixed with the story number, and
    staggered: the 00:23-01:39 cluster is split above/below the line.
    Ticks at 00 / 06 / 12 / 18 / 24.
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
        cap = f"{num:02d} {label}"
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

    Per story (31px): 12pt headline (asserted 1 line) with the status
    chip at the right end of the headline line, then 1 line of summary
    (truncated with '...' if needed), then the source line
    "Source - Place - 26 Nov - FIELD" with a stake flag (U+2691).
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
            hl_lines = wrap(draw, headline, F_BOLD(12), col_w - 22 - cw)
            assert len(hl_lines) == 1, f"headline wraps: {headline!r}"
            draw.text((x, y), f"{num:02d}", font=F_BOLD(12), fill=ACCENT)
            tx = x + 22
            draw.text((tx, y), headline, font=F_BOLD(12), fill=INK)
            draw_status_chip(draw, x + col_w, y, status)
            y += 12
            text = fit_one_line(draw, summary, F_REG(8), col_w - 22)
            draw.text((tx, y), text, font=F_REG(8), fill=DARKGREY)
            y += 9
            flag = "\u2691 " if flagged else ""
            src = (f"{flag}{source} \u00b7 {place} \u00b7 26 Nov "
                   f"\u00b7 {field.upper()}")
            assert text_w(draw, src, F_REG(8)) <= col_w - 22, \
                f"source too long: {src!r}"
            draw.text((tx, y), src, font=F_REG(8), fill=DARKTEXT)
            y += 9
            y += 1  # gap between rows
    return y


def build(output_path):
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- Masthead ----
    title = "IVY WORLD FRONTPAGE"
    f_title = F_SERIF(30)
    tw = text_w(d, title, f_title)
    d.text(((W - tw) / 2, 6), title, font=f_title, fill=INK)
    d.line([MARGIN, 42, W - MARGIN, 42], fill=INK, width=2)
    spec = (f"{EDITION_DATE}  -  38 STORIES  -  9 REGIONS  -  "
            f"{len(FIELDS)} FIELDS  -  UTC TIMELINE")
    f_spec = F_BOLD(11)
    tw = text_w(d, spec, f_spec)
    d.text(((W - tw) / 2, 46), spec, font=f_spec, fill=ACCENT)

    # ---- Fields strip ----
    fields_text = "FIELDS:  " + "  \u00b7  ".join(FIELDS)
    assert text_w(d, fields_text, F_REG(8)) <= W - 2 * MARGIN, "fields strip too wide"
    d.text((MARGIN, 62), fields_text, font=F_REG(8), fill=DARKTEXT)

    # ---- 3 large lead cards ----
    ly, lh = 80, 112
    lw = (W - 2 * MARGIN - 2 * 8) // 3
    for i, (num, headline, deck, scene, accent) in enumerate(LEADS):
        draw_lead_card(d, num, headline, deck, scene, accent,
                       MARGIN + i * (lw + 8), ly, lw, lh)

    # ---- Drawn scenes strip (13, two rows 7+6) ----
    draw_scenes(img, d, 198)

    # ---- Pinned world map ----
    d.text((MARGIN, 330),
           "WHERE IT HAPPENED  -  13 NUMBERED PINS = STORY NUMBERS  -  "
           "13 DRAWN SCENES BELOW",
           font=F_BOLD(9), fill=TEAL)
    draw_map(d, (MARGIN, 344, W - MARGIN, 344 + 68))

    # ---- UTC timeline (true 00-24 scale) ----
    draw_timeline(d, 418)

    # ---- Story grid ----
    grid_top = 480
    grid_bottom = 968
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
    d.line([MARGIN, 972, W - MARGIN, 972], fill=INK, width=2)
    foot = ("DATE CHECK - Every story on this page is dated Thu 26 Nov 2026. "
            "No story dated 25 Nov or earlier appears here; each story carries "
            "its named source and a claim status (CONFIRMED / REPORTED / "
            "OFFICIAL / CLAIMED). Figures are those reported on 26 Nov; later "
            "reporting may revise them.")
    fl = wrap(d, foot, F_REG(9), W - 2 * MARGIN)
    y = draw_lines(d, fl, MARGIN, 978, F_REG(9), INK, 12)
    d.text((MARGIN, y + 2),
           "IVY WORLD FRONTPAGE  -  26 NOV 2026  -  38 STORIES  -  9 REGIONS  -  "
           "19 FIELDS  -  UTC TIMELINE  -  13 SCENES  -  3 LEAD CARDS  -  13 MAP PINS",
           font=F_BOLD(9), fill=DARKTEXT)

    img.save(output_path, "PNG", optimize=True)

    # ---- Count checks (template rules) ----
    regions = sorted({s[1] for s in STORIES})
    fields = sorted({s[6] for s in STORIES})
    assert len(STORIES) == 38, len(STORIES)
    assert len(regions) == 9, regions
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
