# Verified story list for the 26 November 2026 news-image edition.
# "Ivy World Frontpage" — koran v2 per
# ~/workspace/make-fun-agent/templates/news-image-newspaper.md
# and the top-10 study ~/workspace/make-fun-agent/top10-study-20261126.md.
#
# v4 (27 Nov 2026): rebuilt from the mock-judge verdict on v3
# (~/workspace/make-fun-agent/mock-judge-verdict-v3.md). Changes:
# - 13 drawn scenes (was 10) in a 2-row strip; map pins = exactly the
#   13 scene numbers; stat strip deleted (it duplicated the masthead).
# - Headlines shortened to fit ONE line at 12pt bold with the status
#   chip on the same line (generator asserts this).
# - Label logic: OFFICIAL = the named source is the body that issued it;
#   REPORTED = relayed by a third party. 01 -> REPORTED; 17 credited to
#   the Kenya High Court (OFFICIAL); 08, 07, 33, 36 -> OFFICIAL; 09's toll
#   sourced to the Gaza Health Ministry.
# - 19 (Myanmar) moved to East & Southeast Asia; 26 (Ipoh) moved to
#   East & Southeast Asia and its text now says "Ipoh, Malaysia".
# - 37 headline fixed: "NOVEMBER 2.0° ABOVE NORMAL".
# - "WORLD & MARKETS" renamed "WORLD" (a place, not a theme).
# - Every story carries a place + a stake flag for the source line
#   "Source · Place · 26 Nov · FIELD" (⚑ = source has a stake).
#
# v5 (27 Nov 2026): rebuilt from the Claude verdict on v4
# (~/workspace/make-fun-agent/mock-judge-verdict-v4.md, NEEDS WORK 71/100)
# plus the fallback-judge polish
# (~/workspace/make-fun-agent/mock-judge-verdict-v4-fallback.md, 83/100).
# Changes:
# - 10 real regions (WORLD deleted): 35 -> North America; 36, 37, 38 ->
#   Europe; EUROPE & UKRAINE split into EUROPE (01, 02, 06, 07, 36, 37,
#   38) + UKRAINE & RUSSIA (03, 04, 05); MIDDLE EAST & GULF split into
#   MIDDLE EAST (08, 09, 13, 14) + GULF (10, 11, 12).
# - Type up: list headlines 14pt, summaries 11pt, source lines 8pt;
#   headlines/summaries shortened to fit one line (generator asserts).
# - Stake flags widened (Claude): source is a party to the matter ->
#   03, 06, 07, 10, 11, 13, 20, 27, 33 added (05, 08, 09, 12, 22 kept);
#   25's source is now the claimant (Sogavare), not the relay (AAP).
# - CONFIRMED -> OFFICIAL for 15, 21, 26, 32 (announcing bodies).
# - Lead headlines made accurate: tariffs PROPOSED (not imposed), Katz
#   THREATENS (not an order), de Cos PICKED (actor named).
# - Prior-day language removed: 03 (deployment only), 09 (26 Nov only),
#   32 (siege ended 26 Nov).
# - Pin 15 moved to Egypt's north coast (was Saudi Arabia); pin 12 does
#   NOT exist (story 12 has no scene; pins = scenes by design — Claude's
#   "pin 12 over America" was a misread of pin 32 Cartagena / pin 10
#   Kuwait, both correctly placed; verified on the v4 map at full zoom).
# - Scene 04 redrawn as a strike (was a drone/network node).
#
# v6 (27 Nov 2026): rebuilt from the Claude verdict on v5
# (~/workspace/make-fun-agent/mock-judge-verdict-v5.md, NEEDS WORK 79/100).
# Changes:
# - Headline 06 "SPAIN CALLS 29 NOV SNAP VOTE" (snap election called
#   29 Nov — SOURCES.md); 37 "NOV 2° ABOVE PRE-INDUSTRIAL" (baseline
#   is pre-industrial; ".0" dropped so the headline fits the column).
# - Lead headlines now two lines at 26pt ("TARIFFS / PROPOSED ON 14",
#   "KATZ THREATENS / 1M IN GAZA", "DE COS PICKED / FOR ECB").
# - Sources 30/31 shortened to "PR Supreme Court" / "US BEA" so their
#   source lines fit at 8pt with the new provenance + "no stake"
#   suffixes (generator format: wire outlets are shown as the source
#   slot "via {outlet}"; every other source gets " · 1st-hand").
# - Timeline: "SPAIN CALLS VOTE", "BISSAU VOTE DELAYED".
# - Pins 15/17/32 nudged further apart with leader lines (15 east to
#   Egypt's east coast, 17 south-west, 32 south-east to (-67, 2) — far
#   enough that its 1px leader line shows outside the pin disc; the
#   first 32 display (-70, 4) hid the whole leader under the pin);
#   29 stays off the US coast. LIMA was never here: story 30's headline was "COURT
#   AXES LUMA CONTRACT" in v5 too — Claude misread it at small size
#   (verified at 2x zoom + SOURCES.md); the word is unchanged, but
#   the misread itself is why the type floor was raised (see v6).
#
# Every story was checked against its named source on 26 Nov 2026 (see
# SOURCES.md for the per-story evidence and first-reported UTC times).
# Dating rule (stated on the page in the DATE CHECK footer): every story
# on the page is dated Thu 26 Nov 2026; no story dated 25 Nov or earlier
# appears. The 26 Nov news cycle carries items whose underlying data was
# released late on 25 Nov (USTR tariffs, BEA inflation, FCC/SpaceX) — those
# are reported here as 26 Nov reports, which is what SOURCES.md records.
#
# Claim status per story (ClaimReview-style reviewRating alternateName):
#   CONFIRMED — the named source states it as established fact.
#   OFFICIAL  — the named source IS the body that issued/announced it.
#   REPORTED  — relayed by a third party, not yet independently confirmed.
#   CLAIMED   — one party's claim, explicitly hedged as a claim.
# No claim is ever stated as flat fact without a status.
#
# Format: (number, region, headline, summary, source, status, field,
#          place, flagged)
#   place   — dateline place for the source line.
#   flagged — True when the source has a stake in the claim (⚑).
# Headlines are ALL CAPS and must fit ONE line at 14pt bold in a 300px
# column with the status chip on the same line (the generator asserts
# this). Summaries fit ONE line at 11pt (truncated with "..." if needed,
# target ~55 characters).
# Counts: 38 stories, 10 regions, 19 fields.

STORIES = [
    # EUROPE (7)
    (1, "EUROPE",
     "DE COS TO RUN THE ECB",
     "Euro leaders pick de Cos to succeed Lagarde.",
     "Reuters", "REPORTED", "central banking", "Frankfurt", False),
    (2, "EUROPE",
     "EU SPLIT OVER UKRAINE LOAN",
     "Leaders clash over Kyiv loan, 2028-34 budget.",
     "Reuters", "REPORTED", "diplomacy", "Brussels", False),
    (6, "EUROPE",
     "SPAIN CALLS 29 NOV SNAP VOTE",
     "Sanchez calls snap election; PP narrowly ahead.",
     "Spanish PM's office", "OFFICIAL", "elections", "Madrid", True),
    (7, "EUROPE",
     "UK-EU TREATY TEXTS DUE OUT",
     "Food and emissions deals carry a 10-year exit clause.",
     "UK government", "OFFICIAL", "diplomacy", "London", True),
    (36, "EUROPE",
     "EU TO TRIPLE DATA CAPACITY",
     "Brussels wants triple AI capacity; rules lag.",
     "European Commission", "OFFICIAL", "tech", "Brussels", False),
    (37, "EUROPE",
     "NOV 2° ABOVE PRE-INDUSTRIAL",
     "Copernicus: this month 2° above pre-industrial.",
     "Copernicus", "REPORTED", "climate", "Reading", False),
    (38, "EUROPE",
     "DEPARDIEU TO FACE TRIAL",
     "Court orders Depardieu to trial over 2018 case.",
     "Paris appeals court", "OFFICIAL", "courts", "Paris", False),

    # UKRAINE & RUSSIA (3)
    (3, "UKRAINE & RUSSIA",
     "NATO WATCHES POLAND BY AIR",
     "AWACS radar jet deployed over Poland on 26 Nov.",
     "NATO", "OFFICIAL", "security", "Poland", True),
    (4, "UKRAINE & RUSSIA",
     "STRIKES KILL 3 IN UKRAINE",
     "Missiles, 113 drones hit Kyiv and Kharkiv.",
     "Ukrainian officials", "REPORTED", "war", "Kyiv", False),
    (5, "UKRAINE & RUSSIA",
     "UKRAINE CLAIMS 5 JETS HIT",
     "Kyiv says drones hit 3 MiG-31s, 2 Su-34s.",
     "Ukraine General Staff", "CLAIMED", "war", "Savasleyka", True),

    # MIDDLE EAST (4)
    (8, "MIDDLE EAST",
     "ISRAEL THREATENS 1M IN GAZA",
     "Katz: one million displaced unless Hamas disarms.",
     "Israel defence ministry", "OFFICIAL", "war", "Gaza", True),
    (9, "MIDDLE EAST",
     "8 KILLED IN GAZA STRIKES",
     "Strikes hit Deir al-Balah on 26 Nov; 8 killed.",
     "Gaza Health Ministry", "REPORTED", "war", "Deir al-Balah", True),
    (13, "MIDDLE EAST",
     "ISIL ATTACK KILLS 2",
     "Suicide bombers hit a checkpoint in north-east Syria.",
     "Syrian officials", "REPORTED", "war", "Hasakah", True),
    (14, "MIDDLE EAST",
     "IRAQ JAILS 8 IS MEMBERS",
     "Court jails eight French nationals for joining IS.",
     "Iraqi court", "OFFICIAL", "justice", "Baghdad", False),

    # GULF (3)
    (10, "GULF",
     "2 KILLED BY DRONE SHRAPNEL",
     "Two Italian technicians die; drones intercepted.",
     "Kuwait ministry", "OFFICIAL", "security", "Kuwait", True),
    (11, "GULF",
     "UK SANCTIONS HOUTHIS",
     "London freezes assets; Houthis claim port strikes.",
     "UK government", "OFFICIAL", "security", "London", True),
    (12, "GULF",
     "BLAST HITS SANAA",
     "Coalition says it intercepted missiles, drones.",
     "Saudi coalition", "CLAIMED", "war", "Sanaa", True),

    # AFRICA (4)
    (15, "AFRICA",
     "31 KILLED AS TANKER BURNS",
     "Tanker overturns on Ring Road in Giza; 21 hurt.",
     "Egypt Health Ministry", "OFFICIAL", "disaster", "Cairo", False),
    (16, "AFRICA",
     "GUINEA-BISSAU VOTE DELAYED",
     "Military government postpones elections 2 years.",
     "Transitional presidency", "OFFICIAL", "politics", "Bissau", False),
    (17, "AFRICA",
     "COURT FAULTS US EBOLA SITE",
     "High Court: US-backed base breached constitution.",
     "Kenya High Court", "OFFICIAL", "courts", "Nairobi", False),
    (18, "AFRICA",
     "ZAMBIA BANS PROTEST",
     "Police block march against scrapping term limits.",
     "Zambian police", "REPORTED", "politics", "Lusaka", False),

    # SOUTH ASIA (2)
    (20, "SOUTH ASIA",
     "TALIBAN AXE WOMEN'S NAMES",
     "Officials: replace women's names with 'Bibi'.",
     "Afghan officials", "REPORTED", "rights", "Balkh", True),
    (21, "SOUTH ASIA",
     "INDIA WOMEN HOCKEY NO. 4",
     "India's women climb to fourth in world hockey.",
     "FIH", "OFFICIAL", "sport", "India", False),

    # EAST & SOUTHEAST ASIA (5)
    (19, "EAST & SOUTHEAST ASIA",
     "MYANMAR REJECTS ICJ RULING",
     "Junta refuses parts of Rohingya genocide verdict.",
     "Myanmar junta", "OFFICIAL", "justice", "Naypyidaw", False),
    (22, "EAST & SOUTHEAST ASIA",
     "KIM SPREADS NUCLEAR ARMS",
     "Pyongyang to widen tactical nuclear deployment.",
     "KCNA", "OFFICIAL", "security", "Pyongyang", True),
    (23, "EAST & SOUTHEAST ASIA",
     "BANGKOK BLAST INJURES 7",
     "Fireball at Bangchak depot; four critically hurt.",
     "Thai officials", "REPORTED", "disaster", "Bangkok", False),
    (24, "EAST & SOUTHEAST ASIA",
     "BOGOR MINE RESCUE RESUMES",
     "Hunt for trapped miners; 13 confirmed dead.",
     "Reuters", "REPORTED", "disaster", "Bogor", False),
    (26, "EAST & SOUTHEAST ASIA",
     "AUSTRALIA HIT CANADA 14-1",
     "Marais scores four as Australia rout Canada.",
     "FIH", "OFFICIAL", "sport", "Ipoh, Malaysia", False),

    # OCEANIA (1)
    (25, "OCEANIA",
     "EX-PM SLAMS SOLOMONS PACT",
     "Sogavare calls A$740m treaty a sell-out.",
     "Sogavare", "REPORTED", "diplomacy", "Honiara", True),

    # NORTH AMERICA (6)
    (27, "NORTH AMERICA",
     "US PROPOSES TARIFFS ON 14",
     "USTR proposes duties; China capped at 20%.",
     "USTR", "OFFICIAL", "trade", "Washington", True),
    (28, "NORTH AMERICA",
     "PARADE MOVED TO SATURDAY",
     "100th parade moves off Thanksgiving, a first.",
     "AP", "CONFIRMED", "culture", "New York", False),
    (29, "NORTH AMERICA",
     "STORM CUTS POWER FOR 600K",
     "Thanksgiving nor'easter floods the Jersey Shore.",
     "Fox Weather", "REPORTED", "weather", "New Jersey", False),
    (30, "NORTH AMERICA",
     "COURT AXES LUMA CONTRACT",
     "Court votes 5-4 to cancel the power contract.",
     "PR Supreme Court", "OFFICIAL", "energy", "San Juan", False),
    (31, "NORTH AMERICA",
     "US INFLATION RUNS AT 3.8%",
     "October PCE up 3.8% a year; core 3.3%.",
     "US BEA", "OFFICIAL", "markets", "Washington", False),
    (35, "NORTH AMERICA",
     "SPACEX GETS 1M SATELLITES",
     "FCC clears a million data-centre satellites.",
     "FCC", "OFFICIAL", "space", "Washington", False),

    # SOUTH AMERICA (3)
    (32, "SOUTH AMERICA",
     "76 HOSTAGES FREED",
     "Siege ends on 26 Nov; 76 hostages freed.",
     "Colombian police", "OFFICIAL", "security", "Cartagena", False),
    (33, "SOUTH AMERICA",
     "BRAZIL, CHINA SLAM TARIFFS",
     "Brasilia, Beijing call US duties unacceptable.",
     "Brazilian government", "OFFICIAL", "trade", "Brasília", True),
    (34, "SOUTH AMERICA",
     "BRAZIL PROBES SINGER",
     "Singer probed over illegal cassiterite exports.",
     "Brazilian police", "REPORTED", "justice", "Brazil", False),
]

# Lead cards (3 large): (story number, (headline line 1, headline line 2),
# deck, scene key, accent).
# The lead is the day's single most consequential event, stated WITH its
# claim status (template: "what, where, when (UTC), who says so").
# Lead headlines are LARGE display versions (26pt serif bold, TWO lines —
# v6, up from 20pt one line; measured to fit a 314px column) of the grid
# headlines for the same number; the full headline lives in the grid row.
# v5: headlines made accurate — tariffs PROPOSED (not imposed), Katz
# THREATENS (not an order), de Cos PICKED (actor named). Claude's
# suggested wordings (25-31 chars) do not fit one line at 24pt in a
# 326px card (measured 417-542px vs 314px available), so v5 uses 20pt
# with shortened-but-accurate headlines (measured to fit).
LEADS = [
    (27, ("TARIFFS", "PROPOSED ON 14"),
     "USTR proposes duties on 14 economies; China capped at 20%.",
     "cargo", "#7A1F1F"),
    (8, ("KATZ THREATENS", "1M IN GAZA"),
     "Katz: one million displaced in Gaza unless Hamas disarms.",
     "city", "#5B2A1A"),
    (1, ("DE COS PICKED", "FOR ECB"),
     "Euro leaders choose de Cos to succeed Lagarde in February.",
     "bank", "#1E3A5F"),
]

# UTC timeline: (time, short label, story number). First-reported UTC times
# per Daily Summary of World, 26 Nov 2026 (see SOURCES.md).
# The generator prefixes each caption with its story number + "·".
TIMELINE = [
    ("00:23", "SPAIN CALLS VOTE", 6),
    ("00:54", "CAIRO CRASH", 15),
    ("01:39", "5 JETS CLAIM", 5),
    ("05:44", "EU LOAN ROW", 2),
    ("10:25", "MYANMAR ICJ", 19),
    ("12:28", "GAZA THREAT", 8),
    ("14:02", "KYIV STRIKES", 4),
    ("18:07", "BISSAU VOTE DELAYED", 16),
]

# 13 drawn scenes for the scenes strip: (story number, scene key, accent).
# Order = strip order: row 1 (7 tiles), then row 2 (6 tiles).
# Together with the 3 lead scenes = 16 drawn scenes on the page.
SCENES = [
    (15, "tankerfire", "#7A1F1F"),
    (4, "strike", "#3F3F46"),
    (28, "balloon", "#1D4ED8"),
    (35, "rocket", "#4C1D95"),
    (24, "mountain", "#57534E"),
    (29, "storm", "#475569"),
    (22, "missile", "#292524"),
    (19, "scales", "#155E75"),
    (25, "shield", "#14532D"),
    (6, "ballot", "#854D0E"),
    (32, "store", "#B45309"),
    (10, "debris", "#9A3412"),
    (17, "clinic", "#0F766E"),
]

# Caption under each scene tile: "NN · SHORT LABEL".
SCENE_CAPTIONS = {
    15: "GIZA TANKER FIRE",
    4: "KYIV STRIKES",
    28: "MACY'S PARADE",
    35: "SPACEX ROCKET",
    24: "BOGOR MINE SEARCH",
    29: "NEW JERSEY STORM",
    22: "PYONGYANG MISSILE",
    19: "MYANMAR ICJ SCALES",
    25: "SOLOMONS PACT",
    6: "SPAIN BALLOT BOX",
    32: "CARTAGENA STORE",
    10: "KUWAIT DRONE DEBRIS",
    17: "KENYA EBOLA CLINIC",
}

# Map pins: (story number, true lon, true lat, display lon, display lat).
# Display coords are nudged a few degrees where the true spots would
# overlap at this map scale (Cairo/Kyiv, New Jersey/New York, Nairobi);
# the numbered story is unchanged, only the dot is shifted for legibility.
# Pins are EXACTLY the 13 scene numbers.
# v5: pin 15 display moved from (40, 26) [Saudi Arabia] to (36, 27)
# [Egypt's north coast, NE Africa] — the v4 spot read as the Gulf, not
# Egypt. Pin 17 stays nudged west (33, -1.3) to clear pin 15.
PINS = [
    (15, 31.2, 30.0, 38.0, 25.0),
    (4, 30.5, 50.5, 30.5, 50.5),
    (28, -74.0, 40.7, -74.0, 40.7),
    (35, -97.2, 25.9, -97.2, 25.9),
    (24, 106.8, -6.6, 106.8, -6.6),
    (29, -74.0, 40.0, -82.0, 34.0),
    (22, 125.8, 39.0, 125.8, 39.0),
    (19, 96.2, 19.8, 96.2, 19.8),
    (25, 160.0, -9.4, 160.0, -9.4),
    (6, -3.7, 40.4, -3.7, 40.4),
    (32, -75.5, 10.4, -67.0, 2.0),
    (10, 47.5, 29.4, 47.5, 29.4),
    (17, 36.8, -1.3, 28.0, -6.0),
]

# Column assignment for the story grid (region order per column).
# Row height 33px (headline 14 + summary 11 + source 8); region bar 22px.
# Grid height 498px (y472-970): col 1 = 13 stories + 3 bars = 495;
# col 2 = 13 stories + 3 bars = 495; col 3 = 12 stories + 4 bars = 484.
COLUMNS = [
    ["EUROPE", "UKRAINE & RUSSIA", "GULF"],
    ["NORTH AMERICA", "SOUTH AMERICA", "AFRICA"],
    ["MIDDLE EAST", "SOUTH ASIA", "EAST & SOUTHEAST ASIA", "OCEANIA"],
]

EDITION_DATE = "THURSDAY, 26 NOVEMBER 2026"

FIELDS = ["trade", "war", "diplomacy", "central banking", "security",
          "elections", "justice", "courts", "disaster", "politics",
          "rights", "sport", "weather", "energy", "markets", "space",
          "tech", "climate", "culture"]

# Self-checks (run on import by the generator).
assert len(STORIES) == 38, len(STORIES)
assert len({s[1] for s in STORIES}) == 10, sorted({s[1] for s in STORIES})
assert len({s[6] for s in STORIES}) == 19, sorted({s[6] for s in STORIES})
assert len(SCENES) == 13, len(SCENES)
assert len(PINS) == 13, len(PINS)
assert {p[0] for p in PINS} == {s[0] for s in SCENES}, "pins != scenes"
assert set(SCENE_CAPTIONS) == {s[0] for s in SCENES}, "captions != scenes"
assert len(LEADS) == 3
assert len(TIMELINE) == 8
assert sum(len([s for s in STORIES if s[1] == r])
           for r in {s[1] for s in STORIES}) == 38
