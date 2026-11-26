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
# Headlines are ALL CAPS and must fit ONE line at 12pt bold in a 300px
# column with the status chip on the same line (the generator asserts
# this). Summaries fit ONE line at 8pt (truncated with "..." if needed).
# Counts: 38 stories, 9 regions, 19 fields.

STORIES = [
    # EUROPE & UKRAINE (7)
    (1, "EUROPE & UKRAINE",
     "DE COS PICKED TO RUN THE ECB",
     "Euro leaders pick Spain's de Cos to succeed Lagarde in February.",
     "Reuters", "REPORTED", "central banking", "Frankfurt", False),
    (2, "EUROPE & UKRAINE",
     "EU SPLIT OVER UKRAINE LOAN",
     "Leaders clash over a big Kyiv loan and the 2028-34 budget.",
     "Reuters", "REPORTED", "diplomacy", "Brussels", False),
    (3, "EUROPE & UKRAINE",
     "NATO WATCHES POLAND BY AIR",
     "AWACS radar jet deployed after three Russian missiles crashed in Poland.",
     "NATO", "OFFICIAL", "security", "Poland", False),
    (4, "EUROPE & UKRAINE",
     "RUSSIAN STRIKES KILL 3 IN UKRAINE",
     "Ballistic missiles and 113 drones hit Kyiv and Kharkiv; 87 shot down.",
     "Ukrainian officials", "REPORTED", "war", "Kyiv", False),
    (5, "EUROPE & UKRAINE",
     "UKRAINE CLAIMS 5 JETS HIT",
     "Kyiv says drones hit three MiG-31s and two Su-34s in Russia.",
     "Ukraine General Staff", "CLAIMED", "war", "Savasleyka", True),
    (6, "EUROPE & UKRAINE",
     "SPAIN TO VOTE EARLY ON 29 NOV",
     "Sanchez calls a snap election; polls put the PP narrowly ahead.",
     "Spanish PM's office", "OFFICIAL", "elections", "Madrid", False),
    (7, "EUROPE & UKRAINE",
     "UK-EU TREATY TEXTS DUE OUT",
     "Food and emissions deals carry a 10-year exit clause.",
     "UK government", "OFFICIAL", "diplomacy", "London", False),

    # MIDDLE EAST & GULF (7)
    (8, "MIDDLE EAST & GULF",
     "ISRAEL THREATENS 1M IN GAZA",
     "Katz: one million Palestinians displaced unless Hamas disarms.",
     "Israel defence ministry", "OFFICIAL", "war", "Gaza", True),
    (9, "MIDDLE EAST & GULF",
     "8 KILLED IN GAZA STRIKES",
     "Strikes hit Deir al-Balah for a third straight night despite the ceasefire.",
     "Gaza Health Ministry", "REPORTED", "war", "Deir al-Balah", True),
    (10, "MIDDLE EAST & GULF",
     "2 KILLED BY DRONE SHRAPNEL",
     "Two Italian technicians die after Iranian drones are intercepted over Kuwait.",
     "Kuwait ministry", "OFFICIAL", "security", "Kuwait", False),
    (11, "MIDDLE EAST & GULF",
     "UK SANCTIONS HOUTHIS",
     "London freezes assets as Houthis claim strikes on Jeddah and Jazan ports.",
     "UK government", "OFFICIAL", "security", "London", False),
    (12, "MIDDLE EAST & GULF",
     "BLAST HITS SANAA",
     "Coalition says it intercepted missiles over Riyadh and drones in the east.",
     "Saudi coalition", "CLAIMED", "war", "Sanaa", True),
    (13, "MIDDLE EAST & GULF",
     "ISIL ATTACK KILLS 2 IN HASAKAH",
     "Suicide bombers hit a checkpoint in north-east Syria.",
     "Syrian officials", "REPORTED", "war", "Hasakah", False),
    (14, "MIDDLE EAST & GULF",
     "IRAQ JAILS 8 FRENCH IS MEMBERS",
     "Court sentences eight French nationals for joining Islamic State.",
     "Iraqi court", "OFFICIAL", "justice", "Baghdad", False),

    # AFRICA (4)
    (15, "AFRICA",
     "31 KILLED AS TANKER BURNS",
     "Fuel tanker overturns on the Ring Road in Giza; 21 hurt.",
     "Egypt Health Ministry", "CONFIRMED", "disaster", "Cairo", False),
    (16, "AFRICA",
     "GUINEA-BISSAU VOTE DELAYED",
     "Military government postpones elections by two years.",
     "Transitional presidency", "OFFICIAL", "politics", "Bissau", False),
    (17, "AFRICA",
     "KENYA COURT FAULTS US EBOLA SITE",
     "High Court: the US-backed quarantine base breached the constitution.",
     "Kenya High Court", "OFFICIAL", "courts", "Nairobi", False),
    (18, "AFRICA",
     "ZAMBIA BANS TERM-LIMIT PROTEST",
     "Police block a march against a push to scrap presidential term limits.",
     "Zambian police", "REPORTED", "politics", "Lusaka", False),

    # SOUTH ASIA (2)
    (20, "SOUTH ASIA",
     "TALIBAN ERASE WOMEN'S NAMES",
     "Officials told to replace women's names with 'Bibi' in records.",
     "Afghan officials", "REPORTED", "rights", "Balkh", False),
    (21, "SOUTH ASIA",
     "INDIA WOMEN HOCKEY NO. 4",
     "India's women climb to fourth in the world hockey rankings.",
     "FIH", "CONFIRMED", "sport", "India", False),

    # EAST & SOUTHEAST ASIA (5)
    (19, "EAST & SOUTHEAST ASIA",
     "MYANMAR REJECTS ICJ RULING",
     "Junta leader refuses parts of the Rohingya genocide verdict.",
     "Myanmar junta", "OFFICIAL", "justice", "Naypyidaw", False),
    (22, "EAST & SOUTHEAST ASIA",
     "KIM: WIDEN NUCLEAR DEPLOYMENT",
     "North Korea to spread tactical nuclear weapons across domains.",
     "KCNA", "OFFICIAL", "security", "Pyongyang", True),
    (23, "EAST & SOUTHEAST ASIA",
     "BANGKOK DEPOT BLAST INJURES 7",
     "Fireball at the Bangchak depot; four critically hurt, residents evacuated.",
     "Thai officials", "REPORTED", "disaster", "Bangkok", False),
    (24, "EAST & SOUTHEAST ASIA",
     "BOGOR MINE SEARCH RESUMES",
     "Hunt for trapped miners in a flooded gold mine; 13 confirmed dead.",
     "Reuters", "REPORTED", "disaster", "Bogor", False),
    (26, "EAST & SOUTHEAST ASIA",
     "AUSTRALIA HIT CANADA 14-1",
     "Marais scores four as Australia rout Canada in Ipoh, Malaysia.",
     "FIH", "CONFIRMED", "sport", "Ipoh, Malaysia", False),

    # OCEANIA (1)
    (25, "OCEANIA",
     "EX-PM ATTACKS SOLOMONS PACT",
     "Sogavare calls the A$740m treaty a sell-out, signed in Canberra.",
     "AAP", "REPORTED", "diplomacy", "Honiara", True),

    # NORTH AMERICA (5)
    (27, "NORTH AMERICA",
     "US TARIFFS HIT 14 PARTNERS",
     "USTR proposes duties on 14 economies; China capped at 20%.",
     "USTR", "OFFICIAL", "trade", "Washington", False),
    (28, "NORTH AMERICA",
     "PARADE PUSHED TO SATURDAY",
     "The 100th Macy's parade moves off Thanksgiving for the first time.",
     "AP", "CONFIRMED", "culture", "New York", False),
    (29, "NORTH AMERICA",
     "STORM CUTS POWER FOR 600,000",
     "Thanksgiving nor'easter floods the Jersey Shore.",
     "Fox Weather", "REPORTED", "weather", "New Jersey", False),
    (30, "NORTH AMERICA",
     "COURT AXES LUMA CONTRACT",
     "Supreme Court votes 5-4 to cancel the power contract.",
     "Puerto Rico Supreme Court", "OFFICIAL", "energy", "San Juan", False),
    (31, "NORTH AMERICA",
     "US INFLATION RUNS AT 3.8%",
     "October PCE prices rise 3.8% a year; core hits 3.3%, a three-year high.",
     "US Bureau of Economic Analysis", "OFFICIAL", "markets", "Washington", False),

    # SOUTH AMERICA (3)
    (32, "SOUTH AMERICA",
     "76 HOSTAGES FREED IN CARTAGENA",
     "Forces end a 17-hour supermarket siege; hostages freed.",
     "Colombian police", "CONFIRMED", "security", "Cartagena", False),
    (33, "SOUTH AMERICA",
     "BRAZIL, CHINA DENOUNCE TARIFFS",
     "Brasilia calls US sugar and aircraft duties unacceptable; Beijing cries foul.",
     "Brazilian government", "OFFICIAL", "trade", "Brasília", False),
    (34, "SOUTH AMERICA",
     "BRAZIL PROBES SINGER",
     "Singer investigated over illegal cassiterite exports as tin prices surge.",
     "Brazilian police", "REPORTED", "justice", "Brazil", False),

    # WORLD (4)
    (35, "WORLD",
     "SPACEX CLEARED FOR 1M SATELLITES",
     "FCC approves up to a million orbital data-centre satellites.",
     "FCC", "OFFICIAL", "space", "Washington", False),
    (36, "WORLD",
     "EU TO TRIPLE DATA CAPACITY",
     "Brussels wants three times the AI and cloud capacity, but rules lag behind.",
     "European Commission", "OFFICIAL", "tech", "Brussels", False),
    (37, "WORLD",
     "NOVEMBER 2.0° ABOVE NORMAL",
     "Copernicus: this month past 2 degrees above pre-industrial.",
     "Copernicus", "REPORTED", "climate", "Reading", False),
    (38, "WORLD",
     "DEPARDIEU TO FACE TRIAL",
     "Paris court orders the actor to stand trial over a 2018 rape allegation.",
     "Paris appeals court", "OFFICIAL", "courts", "Paris", False),
]

# Lead cards (3 large): (story number, headline, deck, scene key, accent).
# The lead is the day's single most consequential event, stated WITH its
# claim status (template: "what, where, when (UTC), who says so").
# Lead headlines are SHORT display versions (24pt serif, one line);
# the full headline lives in the story grid row for the same number.
LEADS = [
    (27, "US TARIFFS HIT 14",
     "USTR proposes duties on 14 economies; China capped at 20%.",
     "cargo", "#7A1F1F"),
    (8, "MOVE 1M IN GAZA",
     "Katz: one million displaced unless Hamas disarms.",
     "city", "#5B2A1A"),
    (1, "DE COS TO RUN ECB",
     "Euro leaders choose de Cos to succeed Lagarde in February.",
     "bank", "#1E3A5F"),
]

# UTC timeline: (time, short label, story number). First-reported UTC times
# per Daily Summary of World, 26 Nov 2026 (see SOURCES.md).
# The generator prefixes each caption with its story number.
TIMELINE = [
    ("00:23", "SPAIN VOTE", 6),
    ("00:54", "CAIRO CRASH", 15),
    ("01:39", "5 JETS CLAIM", 5),
    ("05:44", "EU LOAN ROW", 2),
    ("10:25", "MYANMAR ICJ", 19),
    ("12:28", "GAZA THREAT", 8),
    ("14:02", "KYIV STRIKES", 4),
    ("18:07", "BISSAU VOTE", 16),
]

# 13 drawn scenes for the scenes strip: (story number, scene key, accent).
# Order = strip order: row 1 (7 tiles), then row 2 (6 tiles).
# Together with the 3 lead scenes = 16 drawn scenes on the page.
SCENES = [
    (15, "tankerfire", "#7A1F1F"),
    (4, "drone", "#3F3F46"),
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

# Map pins: (story number, true lon, true lat, display lon, display lat).
# Display coords are nudged a few degrees where the true spots would
# overlap at this map scale (Cairo/Kyiv, New Jersey/New York, Nairobi);
# the numbered story is unchanged, only the dot is shifted for legibility.
# Pins are EXACTLY the 13 scene numbers.
PINS = [
    (15, 31.2, 30.0, 40.0, 26.0),
    (4, 30.5, 50.5, 30.5, 50.5),
    (28, -74.0, 40.7, -74.0, 40.7),
    (35, -97.2, 25.9, -97.2, 25.9),
    (24, 106.8, -6.6, 106.8, -6.6),
    (29, -74.0, 40.0, -82.0, 34.0),
    (22, 125.8, 39.0, 125.8, 39.0),
    (19, 96.2, 19.8, 96.2, 19.8),
    (25, 160.0, -9.4, 160.0, -9.4),
    (6, -3.7, 40.4, -3.7, 40.4),
    (32, -75.5, 10.4, -75.5, 10.4),
    (10, 47.5, 29.4, 47.5, 29.4),
    (17, 36.8, -1.3, 33.0, -1.3),
]

# Column assignment for the story grid (region order per column).
# Counts: col 1 = 7 + 7 = 14; col 2 = 4 + 2 + 5 + 1 = 12;
# col 3 = 5 + 3 + 4 = 12.
COLUMNS = [
    ["EUROPE & UKRAINE", "MIDDLE EAST & GULF"],
    ["AFRICA", "SOUTH ASIA", "EAST & SOUTHEAST ASIA", "OCEANIA"],
    ["NORTH AMERICA", "SOUTH AMERICA", "WORLD"],
]

EDITION_DATE = "THURSDAY, 26 NOVEMBER 2026"

FIELDS = ["trade", "war", "diplomacy", "central banking", "security",
          "elections", "justice", "courts", "disaster", "politics",
          "rights", "sport", "weather", "energy", "markets", "space",
          "tech", "climate", "culture"]

# Self-checks (run on import by the generator).
assert len(STORIES) == 38, len(STORIES)
assert len({s[1] for s in STORIES}) == 9, sorted({s[1] for s in STORIES})
assert len({s[6] for s in STORIES}) == 19, sorted({s[6] for s in STORIES})
assert len(SCENES) == 13, len(SCENES)
assert len(PINS) == 13, len(PINS)
assert {p[0] for p in PINS} == {s[0] for s in SCENES}, "pins != scenes"
assert len(LEADS) == 3
assert len(TIMELINE) == 8
assert sum(len([s for s in STORIES if s[1] == r])
           for r in {s[1] for s in STORIES}) == 38
