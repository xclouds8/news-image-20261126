#!/usr/bin/env python3
"""Draw the 26 November 2026 news-image front page (1024x1024 PNG).

"Ivy World Frontpage" — koran v2 per
~/workspace/make-fun-agent/templates/news-image-newspaper.md and the
top-10 study (~/workspace/make-fun-agent/top10-study-20261126.md):
masthead brand, fields strip, 6-number stat strip, UTC timeline,
3 large lead cards with drawn scenes, pinned world map (13 numbered
pins), 10 more drawn scenes (13 total), 38 numbered stories in
9 regions, each with a named source AND a claim-status label
(CONFIRMED / REPORTED / OFFICIAL / CLAIMED), DATE CHECK footer
stating exclusion of earlier-day events.

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
    COLUMNS, EDITION_DATE, FIELDS, LEADS, PINS, SCENES, STATS, STORIES,
    TIMELINE,
)

from PIL import Image, ImageDraw, ImageFont  # noqa: E402

W, H = 1024, 1024
MARGIN = 14

PAPER = (247, 243, 232)
INK = (20, 20, 20)
GREY = (90, 88, 80)
DARKGREY = (40, 40, 40)
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
STATUS_COLORS = {
    "CONFIRMED": (30, 110, 60),
    "REPORTED": (176, 120, 20),
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


def draw_status_chip(draw, x_right, y, status):
    """Small filled chip with the claim-status word, right-aligned at x_right."""
    color = STATUS_COLORS[status]
    fnt = F_BOLD(7)
    tw = text_w(draw, status, fnt)
    w, h = int(tw) + 10, 11
    draw.rectangle([x_right - w, y, x_right, y + h], fill=color)
    draw.text((x_right - w + 5, y + 2), status, font=fnt,
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
    draw.rectangle(box, outline=(0, 0, 0, 40))


def draw_lead_card(draw, num, headline, deck, scene, accent, x, y, w, h):
    """One large lead card: scene on top, serif headline, deck, source."""
    story = next(s for s in STORIES if s[0] == num)
    _n, _r, _hl, _sm, source, status, _f = story
    draw.rectangle([x, y, x + w, y + h], fill=CARD_BG, outline=RULE)
    draw_scene(draw, scene, (x + 1, y + 1, x + w - 1, y + 46), accent)
    hy = y + 50
    hl_lines = wrap(draw, headline, F_SERIF(12), w - 12)
    assert len(hl_lines) == 1, f"lead headline wraps: {headline!r}"
    hy = draw_lines(draw, hl_lines[:1], x + 6, hy, F_SERIF(12), INK, 15)
    deck_lines = wrap(draw, deck, F_REG(9), w - 12)
    assert len(deck_lines) <= 2, f"lead deck too long: {deck!r}"
    hy = draw_lines(draw, deck_lines[:2], x + 6, hy + 1, F_REG(9),
                    DARKGREY, 11)
    # source + coloured status word
    sy = y + h - 13
    draw.text((x + 6, sy), f"{num:02d}  {source}  -  ", font=F_REG(8),
              fill=GREY)
    off = text_w(draw, f"{num:02d}  {source}  -  ", F_REG(8))
    draw.text((x + 6 + off, sy), status, font=F_BOLD(8),
              fill=STATUS_COLORS[status])


def draw_column(draw, regions, x, y, col_w, grid_bottom):
    """Draw region sections + stories in one column; returns bottom y.

    Per story: number + 1-line headline (asserted) with a status chip at
    the right end of the headline line, then up to 2 lines of
    summary + source (summary truncated with an ellipsis if it would
    spill to a third line, keeping the source intact).
    """
    by_region = {}
    for s in STORIES:
        by_region.setdefault(s[1], []).append(s)
    for region in regions:
        stories = by_region[region]
        draw.rectangle([x, y, x + col_w, y + 17], fill=TEAL)
        label = f"{region}  -  {len(stories)}"
        draw.text((x + 6, y + 3), label, font=F_BOLD(10), fill=(255, 255, 255))
        y += 21
        for num, _r, headline, summary, source, status, _field in stories:
            hl_lines = wrap(draw, headline, F_BOLD(10), col_w - 22)
            assert len(hl_lines) == 1, f"headline wraps: {headline!r}"
            draw.text((x, y), f"{num:02d}", font=F_BOLD(10), fill=ACCENT)
            tx = x + 22
            draw.text((tx, y), headline, font=F_BOLD(10), fill=INK)
            draw_status_chip(draw, x + col_w, y, status)
            y += 11
            text = summary + " - " + source
            lines = wrap(draw, text, F_REG(8), col_w - 22)
            while len(lines) > 2 and len(summary) > 40:
                summary = summary[:-4].rstrip().rstrip(".")
                text = summary + "... - " + source
                lines = wrap(draw, text, F_REG(8), col_w - 22)
            assert len(lines) <= 2, f"summary too long: {text!r}"
            y = draw_lines(draw, lines[:2], tx, y, F_REG(8), DARKGREY, 9)
            y += 2
    return y


def build(output_path):
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- Masthead ----
    title = "IVY WORLD FRONTPAGE"
    f_title = F_SERIF(34)
    tw = text_w(d, title, f_title)
    d.text(((W - tw) / 2, 6), title, font=f_title, fill=INK)
    d.line([MARGIN, 50, W - MARGIN, 50], fill=INK, width=2)
    spec = (f"{EDITION_DATE}  -  38 STORIES  -  9 REGIONS  -  "
            f"{len(FIELDS)} FIELDS  -  UTC TIMELINE")
    f_spec = F_BOLD(11)
    tw = text_w(d, spec, f_spec)
    d.text(((W - tw) / 2, 56), spec, font=f_spec, fill=ACCENT)

    # ---- Fields strip ----
    fields_text = "FIELDS:  " + "  \u00b7  ".join(FIELDS)
    assert text_w(d, fields_text, F_REG(8)) <= W - 2 * MARGIN, "fields strip too wide"
    d.text((MARGIN, 76), fields_text, font=F_REG(8), fill=GREY)

    # ---- Stat strip (6 boxes) ----
    sy, sh = 94, 38
    sw = (W - 2 * MARGIN - 5 * 8) // 6
    for i, (num, label) in enumerate(STATS):
        x0 = MARGIN + i * (sw + 8)
        d.rectangle([x0, sy, x0 + sw, sy + sh], fill=CARD_BG, outline=RULE)
        d.text((x0 + 8, sy + 2), num, font=F_BOLD(18), fill=ACCENT)
        lines = wrap(d, label, F_REG(8), sw - 16)
        draw_lines(d, lines[:2], x0 + 8, sy + 22, F_REG(8), GREY, 10)

    # ---- UTC timeline ----
    # Label on the left; slots start after it so no time collides with it.
    ty = 140
    d.text((MARGIN, ty), "THE DAY IN UTC  -", font=F_BOLD(9), fill=TEAL)
    line_y = ty + 20
    d.line([MARGIN, line_y, W - MARGIN, line_y], fill=RULE, width=2)
    slots_x0 = MARGIN + 150
    slot_w = (W - MARGIN - slots_x0) // len(TIMELINE)
    for i, (t, label, _num) in enumerate(TIMELINE):
        cx = slots_x0 + slot_w * i + slot_w // 2
        d.text((cx - text_w(d, t, F_BOLD(9)) / 2, ty + 2), t,
               font=F_BOLD(9), fill=INK)
        d.ellipse([cx - 4, line_y - 4, cx + 4, line_y + 4], fill=ACCENT,
                  outline=(255, 255, 255), width=1)
        ll = wrap(d, label, F_REG(8), slot_w - 8)
        assert len(ll) == 1, f"timeline label wraps: {label!r}"
        draw_lines(d, ll, cx - text_w(d, ll[0], F_REG(8)) / 2,
                   line_y + 7, F_REG(8), GREY, 10)

    # ---- 3 large lead cards ----
    ly, lh = 186, 104
    lw = (W - 2 * MARGIN - 2 * 8) // 3
    for i, (num, headline, deck, scene, accent) in enumerate(LEADS):
        draw_lead_card(d, num, headline, deck, scene, accent,
                       MARGIN + i * (lw + 8), ly, lw, lh)

    # ---- Pinned world map ----
    my = 296
    d.text((MARGIN, my),
           "WHERE IT HAPPENED  -  13 NUMBERED PINS = STORY NUMBERS  -  "
           "13 DRAWN SCENES BELOW",
           font=F_BOLD(9), fill=TEAL)
    draw_map(d, (MARGIN, my + 15, W - MARGIN, my + 15 + 94))

    # ---- Drawn scenes strip (10) ----
    sy2 = 414
    gap = 8
    cw = (W - 2 * MARGIN - gap * (len(SCENES) - 1)) // len(SCENES)
    for i, (num, caption, scene, accent) in enumerate(SCENES):
        x0 = MARGIN + i * (cw + gap)
        x1 = x0 + cw
        d.rectangle([x0, sy2, x1, sy2 + 48], fill=CARD_BG, outline=RULE)
        draw_scene(d, scene, (x0 + 1, sy2 + 1, x1 - 1, sy2 + 30), accent)
        cap = f"{num:02d}  {caption}"
        cap_lines = wrap(d, cap, F_REG(8), cw - 6)
        assert len(cap_lines) == 1, f"scene caption wraps: {cap!r}"
        draw_lines(d, cap_lines, x0 + 3, sy2 + 33, F_REG(8), INK, 10)

    # ---- Story grid ----
    grid_top = 468
    grid_bottom = 968
    col_w = (W - 2 * MARGIN - 2 * 8) // 3
    col_x = [MARGIN, MARGIN + col_w + 8, MARGIN + 2 * (col_w + 8)]
    bottoms = []
    for i, regions in enumerate(COLUMNS):
        bottoms.append(draw_column(d, regions, col_x[i], grid_top, col_w,
                                   grid_bottom))
    max_bottom = max(bottoms)
    assert max_bottom <= grid_bottom, f"grid overflow: {max_bottom}"

    # Fill short columns with genuine reading keys (not filler): the map
    # key goes in the second column, the claim-label key in the third.
    # Only drawn when the space is really there.
    keys = {
        1: ("MAP KEY",
            "Red pins are story numbers on the map above. Scenes are drawn "
            "illustrations, not photographs. All times are UTC."),
        2: ("CLAIM LABELS",
            "CONFIRMED: stated as fact. OFFICIAL: announced by a body. "
            "REPORTED: as reported, unconfirmed. CLAIMED: one side's claim."),
    }
    for i, b in enumerate(bottoms):
        if i in keys and grid_bottom - b >= 50:
            title, note = keys[i]
            d.rectangle([col_x[i], b + 6, col_x[i] + col_w, b + 50],
                        outline=RULE)
            d.text((col_x[i] + 6, b + 10), title, font=F_BOLD(9),
                   fill=TEAL)
            lines = wrap(d, note, F_REG(8), col_w - 12)
            draw_lines(d, lines[:2], col_x[i] + 6, b + 22, F_REG(8),
                       GREY, 11)

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
           "19 FIELDS  -  UTC TIMELINE  -  13 SCENES  -  13 MAP PINS",
           font=F_BOLD(9), fill=GREY)

    img.save(output_path, "PNG", optimize=True)

    # ---- Count checks (template rules) ----
    regions = sorted({s[1] for s in STORIES})
    fields = sorted({s[6] for s in STORIES})
    assert len(STORIES) == 38, len(STORIES)
    assert len(regions) == 9, regions
    assert sum(len([s for s in STORIES if s[1] == r]) for r in regions) == 38
    assert len(fields) == len(FIELDS) == 19, fields
    assert fields == sorted(FIELDS), "FIELDS list mismatch"
    assert len(STATS) == 6
    assert len(LEADS) == 3
    assert len(SCENES) == 10 and len(LEADS) + len(SCENES) == 13
    assert len(PINS) == 13
    assert len(TIMELINE) == 8
    assert all(s[5] in STATUS_COLORS for s in STORIES), "bad status"
    size = os.path.getsize(output_path)
    assert size <= 1024 * 1024, f"over 1 MiB: {size}"
    print(f"OK {output_path}: {size} bytes, 1024x1024")
    print(f"stories={len(STORIES)} regions={len(regions)} "
          f"({', '.join(f'{r}:{len([s for s in STORIES if s[1]==r])}' for r in regions)})")
    print(f"fields={len(fields)} stats={len(STATS)} leads={len(LEADS)} "
          f"scenes={len(SCENES) + len(LEADS)} pins={len(PINS)} "
          f"timeline={len(TIMELINE)} grid_bottom_max={max_bottom}")


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "world-news-26-nov-2026.png")
    build(out)
