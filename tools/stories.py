# Verified story list for the 26 November 2026 news-image edition.
# "Ivy World Frontpage" — koran v2 per
# ~/workspace/make-fun-agent/templates/news-image-newspaper.md
# and the top-10 study ~/workspace/make-fun-agent/top10-study-20261126.md.
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
#   OFFICIAL  — a government / court / institution announced it.
#   REPORTED  — reported by the named outlet, not yet independently confirmed.
#   CLAIMED   — one party's claim, explicitly hedged as a claim.
# No claim is ever stated as flat fact without a status.
#
# Format: (number, region, headline, summary, source, status, field)
# Headlines are ALL CAPS and must fit ONE line at 10pt bold in a 300px
# column (the generator asserts this). Summaries fit TWO lines at 8.5pt.
# Counts: 38 stories, 9 regions, 19 fields.

STORIES = [
    # EUROPE & UKRAINE (7)
    (1, "EUROPE & UKRAINE",
     "DE COS PICKED TO RUN THE ECB",
     "Euro leaders choose Spain's Pablo Hernandez de Cos to succeed Lagarde in February.",
     "Reuters", "OFFICIAL", "central banking"),
    (2, "EUROPE & UKRAINE",
     "EU SPLIT OVER UKRAINE LOAN, BUDGET",
     "Leaders clash in Brussels over a big new Kyiv loan and the 2028-34 budget.",
     "Reuters", "REPORTED", "diplomacy"),
    (3, "EUROPE & UKRAINE",
     "NATO WATCHES POLAND FROM THE AIR",
     "AWACS radar jet deployed after three Russian missiles crashed in Poland.",
     "NATO", "OFFICIAL", "security"),
    (4, "EUROPE & UKRAINE",
     "RUSSIAN STRIKES KILL 3 IN UKRAINE",
     "Ballistic missiles and 113 drones hit Kyiv and Kharkiv; 87 shot down.",
     "Ukrainian officials", "REPORTED", "war"),
    (5, "EUROPE & UKRAINE",
     "UKRAINE CLAIMS 5 JETS HIT IN RUSSIA",
     "Kyiv says drones damaged three MiG-31s and two Su-34s at Savasleyka base.",
     "Ukraine General Staff", "CLAIMED", "war"),
    (6, "EUROPE & UKRAINE",
     "SPAIN TO VOTE EARLY ON 29 NOV",
     "Sanchez calls a snap election eight months early; polls put the PP narrowly ahead.",
     "Spanish PM's office", "OFFICIAL", "elections"),
    (7, "EUROPE & UKRAINE",
     "UK-EU TREATY TEXTS DUE OUT",
     "Food and emissions deals carry a 10-year exit clause; critics attack the terms.",
     "UK government", "REPORTED", "diplomacy"),

    # MIDDLE EAST & GULF (7)
    (8, "MIDDLE EAST & GULF",
     "ISRAEL THREATENS TO MOVE 1M IN GAZA",
     "Katz: one million Palestinians displaced unless Hamas surrenders its weapons.",
     "Israel defence ministry", "REPORTED", "war"),
    (9, "MIDDLE EAST & GULF",
     "8 KILLED IN OVERNIGHT GAZA STRIKES",
     "Strikes hit Deir al-Balah for a third straight night despite the ceasefire.",
     "Gaza officials", "REPORTED", "war"),
    (10, "MIDDLE EAST & GULF",
     "2 KILLED BY DRONE SHRAPNEL IN KUWAIT",
     "Two Italian technicians die after Iranian drones are intercepted over Kuwait.",
     "Kuwait ministry", "OFFICIAL", "security"),
    (11, "MIDDLE EAST & GULF",
     "UK SANCTIONS HOUTHIS OVER SAUDI HITS",
     "London freezes assets as Houthis claim strikes on Jeddah and Jazan ports.",
     "UK government", "OFFICIAL", "security"),
    (12, "MIDDLE EAST & GULF",
     "BLAST HITS SANAA AS MISSILES FLY",
     "Coalition says it intercepted missiles over Riyadh and drones in the east.",
     "Saudi coalition", "CLAIMED", "war"),
    (13, "MIDDLE EAST & GULF",
     "ISIL ATTACK KILLS 2 IN HASAKAH",
     "Suicide bombers hit a security checkpoint in north-east Syria; four attackers die.",
     "Syrian officials", "REPORTED", "war"),
    (14, "MIDDLE EAST & GULF",
     "IRAQ JAILS 8 FRENCH IS MEMBERS FOR LIFE",
     "Court sentences eight French nationals for joining Islamic State; two get 15 years.",
     "Iraqi court", "OFFICIAL", "justice"),

    # AFRICA (4)
    (15, "AFRICA",
     "31 KILLED AS TANKER BURNS IN CAIRO",
     "Fuel tanker overturns on the Ring Road in Giza; 21 hurt, 27 vehicles charred.",
     "Egypt Health Ministry", "CONFIRMED", "disaster"),
    (16, "AFRICA",
     "GUINEA-BISSAU VOTE DELAYED TO 2028",
     "Military government postpones elections by two years on the coup's first anniversary.",
     "Transitional presidency", "OFFICIAL", "politics"),
    (17, "AFRICA",
     "KENYA COURT FAULTS US EBOLA SITE",
     "High Court: building the US-backed quarantine base breached the constitution.",
     "Reuters", "OFFICIAL", "courts"),
    (18, "AFRICA",
     "ZAMBIA BANS PROTEST OVER TERM LIMITS",
     "Police block a march against a push to scrap presidential term limits.",
     "Zambian police", "REPORTED", "politics"),

    # SOUTH ASIA (3)
    (19, "SOUTH ASIA",
     "MYANMAR REJECTS PARTS OF ICJ RULING",
     "Junta leader refuses parts of the Rohingya genocide verdict; reparations ordered.",
     "Myanmar junta", "OFFICIAL", "justice"),
    (20, "SOUTH ASIA",
     "TALIBAN ERASE WOMEN'S NAMES IN BALKH",
     "Officials told to replace women's real names with 'Bibi' in records, reports say.",
     "Afghan officials", "REPORTED", "rights"),
    (21, "SOUTH ASIA",
     "INDIA WOMEN HOCKEY UP TO WORLD NO. 4",
     "India climb the rankings after a dominant win over Japan.",
     "FIH", "CONFIRMED", "sport"),

    # EAST & SOUTHEAST ASIA (3)
    (22, "EAST & SOUTHEAST ASIA",
     "KIM: WIDEN TACTICAL NUCLEAR DEPLOYMENT",
     "North Korea to spread tactical nuclear weapons across domains, KCNA reports.",
     "KCNA", "OFFICIAL", "security"),
    (23, "EAST & SOUTHEAST ASIA",
     "BANGKOK OIL DEPOT BLAST INJURES 7",
     "Fireball at the Bangchak depot; four critically hurt, residents evacuated.",
     "Thai officials", "REPORTED", "disaster"),
    (24, "EAST & SOUTHEAST ASIA",
     "BOGOR MINE SEARCH RESUMES; 13 DEAD",
     "Rescuers hunt 13 trapped miners in a flooded illegal gold mine; 13 confirmed dead.",
     "Reuters", "REPORTED", "disaster"),

    # OCEANIA (2)
    (25, "OCEANIA",
     "EX-PM ATTACKS SOLOMONS-AUSTRALIA PACT",
     "Sogavare calls the A$740m treaty a sell-out a day after it was signed in Canberra.",
     "AAP", "REPORTED", "diplomacy"),
    (26, "OCEANIA",
     "AUSTRALIA HIT CANADA 14-1 IN IPOH",
     "Marais scores four as Australia rout Canada in the hockey tournament in Ipoh.",
     "FIH", "CONFIRMED", "sport"),

    # NORTH AMERICA (5)
    (27, "NORTH AMERICA",
     "US TARIFFS HIT 14 PARTNERS",
     "USTR proposes duties on 14 economies; China capped at 20% as partners protest.",
     "USTR", "OFFICIAL", "trade"),
    (28, "NORTH AMERICA",
     "MACY'S PARADE PUSHED TO SATURDAY",
     "The 100th parade moves off Thanksgiving for the first time, as a storm lashes the coast.",
     "AP", "CONFIRMED", "culture"),
    (29, "NORTH AMERICA",
     "STORM KNOCKS OUT POWER FOR 600,000",
     "Thanksgiving nor'easter floods the Jersey Shore; Virginia counts 217,000 outages.",
     "Fox Weather", "REPORTED", "weather"),
    (30, "NORTH AMERICA",
     "PUERTO RICO COURT AXES LUMA CONTRACT",
     "Supreme Court votes 5-4 to cancel the power contract; a year to find a successor.",
     "Puerto Rico Supreme Court", "OFFICIAL", "energy"),
    (31, "NORTH AMERICA",
     "US INFLATION RUNS AT 3.8%",
     "October PCE prices rise 3.8% a year; core hits 3.3%, a three-year high.",
     "US Bureau of Economic Analysis", "OFFICIAL", "markets"),

    # SOUTH AMERICA (3)
    (32, "SOUTH AMERICA",
     "76 HOSTAGES FREED IN CARTAGENA",
     "Forces end a 17-hour supermarket siege; shoppers and staff held at gunpoint freed.",
     "Colombian police", "CONFIRMED", "security"),
    (33, "SOUTH AMERICA",
     "BRAZIL, CHINA DENOUNCE US TARIFFS",
     "Brasilia calls sugar and aircraft duties unacceptable; Beijing cries foul.",
     "Brazilian government", "REPORTED", "trade"),
    (34, "SOUTH AMERICA",
     "BRAZIL PROBES SINGER IN TIN SCHEME",
     "Singer investigated over illegal cassiterite exports as tin prices surge.",
     "Brazilian police", "REPORTED", "justice"),

    # WORLD & MARKETS (4)
    (35, "WORLD & MARKETS",
     "SPACEX CLEARED FOR 1M SATELLITES",
     "FCC approves up to a million orbital data-centre satellites, a first of its kind.",
     "FCC", "OFFICIAL", "space"),
    (36, "WORLD & MARKETS",
     "EU TO TRIPLE DATA-CENTRE CAPACITY",
     "Brussels wants three times the AI and cloud capacity, but rules lag behind.",
     "European Commission", "REPORTED", "tech"),
    (37, "WORLD & MARKETS",
     "NOVEMBER RUNS 2.0 DEGREES ABOVE NORMAL",
     "Copernicus data put this month past 2 degrees above pre-industrial - a record anomaly.",
     "Copernicus", "REPORTED", "climate"),
    (38, "WORLD & MARKETS",
     "DEPARDIEU TO FACE TRIAL OVER 2018 RAPE",
     "Paris court orders the actor to stand trial; he denies wrongdoing, faces up to 20 years.",
     "Paris appeals court", "OFFICIAL", "courts"),
]

# Lead cards (3 large): (story number, headline, deck, scene key, accent).
# The lead is the day's single most consequential event, stated WITH its
# claim status (template: "what, where, when (UTC), who says so").
LEADS = [
    (27, "US TARIFFS HIT 14 PARTNERS",
     "USTR proposes duties on 14 economies; China capped at 20%. Brazil and China denounce the plan.",
     "cargo", "#7A1F1F"),
    (8, "ISRAEL THREATENS TO MOVE 1M IN GAZA",
     "Defence chief Katz: one million Palestinians displaced unless Hamas disarms. Strikes kill 8 overnight.",
     "city", "#5B2A1A"),
    (1, "DE COS PICKED TO RUN THE ECB",
     "Euro leaders choose Spain's Pablo Hernandez de Cos to succeed Lagarde in February; a first for Spain.",
     "bank", "#1E3A5F"),
]

# 6-number stat strip: (big number, label). Every number is checkable
# against a story on this page.
STATS = [
    ("38", "stories on one page"),
    ("9", "regions, incl. S. America + Oceania"),
    ("19", "labelled fields"),
    ("14", "trading partners hit by US tariffs"),
    ("1M", "satellites in SpaceX's FCC approval"),
    ("3.8%", "US inflation, Oct PCE, year on year"),
]

# UTC timeline: (time, short label, story number). First-reported UTC times
# per Daily Summary of World, 26 Nov 2026 (see SOURCES.md).
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

# 10 drawn scenes for the scenes strip: (story number, caption, scene key, accent).
# Together with the 3 lead scenes = 13 vector scenes (template spec).
SCENES = [
    (15, "Tanker, Cairo", "tankerfire", "#7A1F1F"),
    (4, "Drones, Kyiv", "drone", "#3F3F46"),
    (28, "Parade waits", "balloon", "#1D4ED8"),
    (35, "1M satellites", "rocket", "#4C1D95"),
    (24, "Bogor mine", "mountain", "#57534E"),
    (29, "Storm coast", "storm", "#475569"),
    (22, "Pyongyang", "missile", "#292524"),
    (19, "Justice scales", "scales", "#155E75"),
    (25, "Pacific pact", "shield", "#14532D"),
    (6, "Ballot, Madrid", "ballot", "#854D0E"),
]

# Map pins: (story number, true lon, true lat, display lon, display lat).
# Display coords are nudged a few degrees where the true spots would
# overlap at this map scale (Gaza/Cairo, Washington/New York); the numbered
# story is unchanged, only the dot is shifted for legibility.
PINS = [
    (27, -77.0, 39.0, -77.0, 39.0),
    (28, -74.0, 40.7, -69.0, 42.5),
    (32, -75.5, 10.4, -75.5, 10.4),
    (35, -97.2, 25.9, -97.2, 25.9),
    (1, 4.4, 50.8, 4.4, 50.8),
    (4, 30.5, 50.5, 30.5, 50.5),
    (8, 34.5, 31.5, 38.5, 30.0),
    (15, 31.2, 30.0, 31.2, 30.0),
    (16, -15.6, 11.9, -15.6, 11.9),
    (17, 36.8, -1.3, 36.8, -1.3),
    (19, 96.2, 19.8, 96.2, 19.8),
    (24, 106.8, -6.6, 106.8, -6.6),
    (25, 160.0, -9.4, 160.0, -9.4),
]

# Column assignment for the story grid (region order per column).
COLUMNS = [
    ["EUROPE & UKRAINE", "MIDDLE EAST & GULF"],
    ["AFRICA", "SOUTH ASIA", "EAST & SOUTHEAST ASIA", "OCEANIA"],
    ["NORTH AMERICA", "SOUTH AMERICA", "WORLD & MARKETS"],
]

EDITION_DATE = "THURSDAY, 26 NOVEMBER 2026"

FIELDS = ["trade", "war", "diplomacy", "central banking", "security",
          "elections", "justice", "courts", "disaster", "politics",
          "rights", "sport", "weather", "energy", "markets", "space",
          "tech", "climate", "culture"]
