"""US English check shared by check_edition.py and the Markets Desk's check_desk.py.

find(text) returns (what was found, the US form) for British spellings and day-before-month dates. Only lower-case
words are matched, so proper names that keep their own spelling (the Labour Party, Egypt Aluminium, the Ministry
of Defence) pass; quotes are the caller's to strip.
"""
import re

MONTHS = "January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sept|Sep|Oct|Nov|Dec"
DATE = re.compile(rf"\b(\d{{1,2}}) ({MONTHS})\b")

# British form (regex, lower case) -> US form
WORDS = [
    (r"colour", "color"), (r"favour", "favor"), (r"behaviour", "behavior"), (r"labour", "labor"), (r"honour", "honor"),
    (r"neighbour", "neighbor"), (r"rumour", "rumor"), (r"harbour", "harbor"), (r"flavour", "flavor"), (r"humour", "humor"),
    (r"endeavour", "endeavor"), (r"vapour", "vapor"), (r"centre", "center"), (r"metre", "meter"), (r"litre", "liter"),
    (r"theatre", "theater"), (r"fibre", "fiber"), (r"calibre", "caliber"), (r"defence", "defense"), (r"offence", "offense"),
    (r"licence", "license"), (r"programme", "program"), (r"catalogue", "catalog"), (r"cheque", "check"), (r"tyre", "tire"),
    (r"jewellery", "jewelry"), (r"sceptic", "skeptic"), (r"aluminium", "aluminum"), (r"tonnes?", "metric tons"),
    (r"grey", "gray"), (r"whilst", "while"), (r"amongst", "among"), (r"per cent", "percent"), (r"judgement", "judgment"),
    (r"ageing", "aging"), (r"learnt", "learned"), (r"fulfil(?!l)", "fulfill"), (r"instalment", "installment"),
    (r"enrolment", "enrollment"), (r"manoeuvre", "maneuver"), (r"paediatric", "pediatric"), (r"anaemi", "anemi"),
    (r"haemo", "hemo"), (r"oestrogen", "estrogen"), (r"storey", "story"), (r"mould", "mold"), (r"plough", "plow"),
    (r"(travel|cancel|model|label|fuel|signal|channel|total|equal|tunnel)l(ed|ing|er)", r"\1\2"),
    (r"analys(e|ed|es|ing)\b", r"analyz\1"),
    (r"(organ|recogn|real|priorit|stabil|privat|subsid|critic|apolog|character|minim|maxim|util|mobil|normal|capital|"
     r"author|final|summar|liberal|industrial|categor|monet|harmon|standard|fertil|special|optim|emphas|central|"
     r"legal|modern|neutral|penal|global|visual|maxim|revital|jeopard|patron|sympath|scrutin|synchron|incentiv)"
     r"is(e|ed|es|ing|ation|ations|er|ers)\b", r"\1iz\2"),
]
COMPILED = [(re.compile(rf"\b{b}"), us) for b, us in WORDS]


def find(text):
    out = []
    for rx, us in COMPILED:
        for m in rx.finditer(text):
            out.append((m.group(0), m.expand(us)))
    for m in DATE.finditer(text):
        out.append((m.group(0), f"{m.group(2)} {m.group(1)}"))
    return out


def report(errors, warnings, full=False):
    """Print a checker's findings compactly (shared by check_edition.py and check_desk.py): every error in full;
    warnings grouped by their opening words, the first two of a group in full and the rest cut to their first
    100 characters, which name the item (a ticker, a link, a section). The run keeps this output open to the end,
    so it is kept short. --all prints everything in full."""
    for e in errors:
        print("ERROR:", e)
    groups = {}
    for w in warnings:
        groups.setdefault(w.split(":")[0][:40], []).append(w)
    for k, ws in groups.items():
        for i, w in enumerate(ws):
            print("WARNING:", w if full or i < 2 or len(w) <= 110 else w[:100] + " …")
