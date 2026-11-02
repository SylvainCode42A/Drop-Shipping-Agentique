"""Le brief de génération en données (CMP - Brief de génération des illustrations de Noël 2026).
Toute modification de prompt se fait ici, jamais dans generer.py.
"""

# Préfixe v2 (02/11/2026, après les roses seed 1 et 2 : le v1 donnait du vecteur à contour noir, pas de
# la gouache). Le v1 est gardé en commentaire pour comparaison.
# PREFIXE_V1 = ("gouache illustration, opaque flat pigment, no wash, no gradient, closed bold contours, "
#               "medium to saturated colors, simple bold shapes, no fine detail, no drop shadow, "
#               "no paper texture, no text, no letters, no watermark, children's book illustration style, "
#               "no realistic face, no recognizable character or brand")
# Préfixe v2 (02/11/2026), remplacé le même jour par le v3 : il a réglé la matière (rose seed 4 validée)
# mais, sans « no wash » ni « opaque flat pigment », il a ramené du lavis sur les fleurs seed 1 et 2 :
# fonds en dégradé ou avec halo (8 sur 22) et feuilles semi-transparentes (jonquille, muguet,
# pied-d'alouette, violette). Les éléments validés en v2 sont gardés.
# PREFIXE_V2 = ("gouache painting, hand-painted with visible brush strokes, slightly uneven opaque paint, "
#               "thick painterly shapes, no black outline, no vector look, no gradient, medium to saturated "
#               "colors, simple bold shapes, no fine detail, no drop shadow, no text, no letters, "
#               "no watermark, children's book illustration, no realistic face, "
#               "no recognizable character or brand")
PREFIXE = ("gouache painting, hand-painted with visible brush strokes inside the shapes, fully opaque paint, "
           "no wash, no watercolor, no transparency, no faded or ghosted parts, every shape ends with a "
           "clean crisp edge, thick painterly shapes, no black outline, no vector look, no gradient, "
           "medium to saturated colors, simple bold shapes, no fine detail, no drop shadow, no text, "
           "no letters, no watermark, children's book illustration, no realistic face, "
           "no recognizable character or brand")

FOND_VERT = "#00C853"
FOND_MAGENTA = "#E600E6"

# Suffixe des éléments v1 (02/11/2026), remplacé le même jour par le v2 : 8 fonds sur 22 non unis
# (dégradé, halo, deux tons) sur les fleurs seed 1 et 2.
# SUFFIXE_ELEMENT_V1 = ("single object, centered, fully inside the frame with wide margins, "
#                       "flat uniform background color {FOND}, nothing else in the image")
SUFFIXE_ELEMENT = ("single object, centered, fully inside the frame with wide margins, "
                   "the background is one single flat color {FOND} with no gradient, no vignette, "
                   "no halo, no glow, nothing else in the image")

SUFFIXE_SCENE = ("cozy family scene, no people, no animals, the right third of the image is a plain "
                 "uniform wall in color {FOND} with nothing on it, soft even lighting")

PALETTES = {
    "mamie":   {"fond": "#F3E6D3", "accents": ["#E07A5F", "#8AA587", "#D4A537"]},
    "papy":    {"fond": "#D6DEE6", "accents": ["#D4A537", "#2E5E4E", "#B5533C"]},
    "maman":   {"fond": "#F2D9DC", "accents": ["#7B3F61", "#D8A62A", "#5E8A6E"]},
    "papa":    {"fond": "#E3DED6", "accents": ["#2F4FA8", "#8A5A3B", "#D8A62A"]},
    "couple":  {"fond": "#F5EFE0", "accents": ["#7A1E2E", "#B8923E", "#5E8A6E"]},
    "famille": {"fond": "#F5EFE0", "accents": ["#5E8A6E", "#C8623C", "#D4A537"]},
}

# nom : (sujet, silhouette, couleurs, contient_du_vert)
FLEURS = {
    "oeillet":       ("a single carnation flower", "round ruffled head with jagged petals, one stem", "bright pink, grey-green leaves", True),
    "violette":      ("a single violet flower", "five rounded petals, two on top and three below, one heart-shaped leaf", "violet purple, yellow center", True),
    # Jonquille v1 (02/11/2026), remplacée avant l'essai 4 : seeds 1, 2 et 3 avec la base de tige fondue en lavis.
    # "jonquille":   ("a single daffodil flower", "central trumpet surrounded by six petals, straight stem", "yellow, orange trumpet", True),
    "jonquille":     ("a single daffodil flower", "central trumpet surrounded by six petals, straight stem ending in a clean blunt cut, two narrow leaves, every part fully opaque", "yellow, orange trumpet", True),
    "marguerite":    ("a single daisy flower", "many thin white petals around a round center", "white petals, yellow center", True),
    "muguet":        ("a single lily of the valley stem", "curved stem carrying small white bell flowers, one large leaf", "white bells, bright green leaf", True),
    "rose":          ("a single rose", "open bud with rolled petals, one stem with two leaves", "red to coral petals, green leaves", True),
    "pied-alouette": ("a single larkspur flower spike", "vertical spike of small tightly packed flowers", "blue and violet", True),
    # Glaïeul v1 (02/11/2026), remplacé avant l'essai 4 : seeds 1, 2 et 3 avec fond en dégradé, feuilles latérales
    # en lavis et tige coupée par le cadre (seed 3).
    # "glaieul":     ("a single gladiolus stem", "straight stem with several trumpet flowers stacked along it", "orange to red", True),
    "glaieul":       ("a single gladiolus stem", "straight stem with several trumpet flowers stacked along it, no leaves, the stem ends in a clean blunt cut well above the bottom edge", "orange to red", True),
    "aster":         ("a single aster flower", "small daisy-like flower with many thin purple petals", "purple petals, yellow center", True),
    "souci":         ("a single marigold flower", "dense round head with tightly packed petals", "bright orange", True),
    "chrysantheme":  ("a single chrysanthemum flower", "very full round pompom head", "yellow or bronze", True),
    "houx":          ("a sprig of holly", "three glossy jagged leaves and a cluster of berries", "dark green leaves, red berries", True),
    # Fleurs de repli (02/11/2026) : la jonquille (mars) et le glaïeul (août) refusés après cinq essais, la rose de
    # référence déteignant sur leurs tiges et leurs feuilles. Silhouettes écrites pour ce brief, sans feuille large.
    "tulipe":        ("a single tulip flower", "closed cup-shaped head of rounded petals, straight stem, one long narrow leaf, every part fully opaque", "bright red petals, green stem and leaf", True),
    "tournesol":     ("a single sunflower", "large round head with a wide dark brown center and one ring of yellow petals, short straight stem, no leaves, every part fully opaque", "yellow petals, dark brown center", True),
}

ORNEMENTS = {
    "boule":      ("a single Christmas bauble", "sphere with a cap and a small ribbon, one simple flat highlight", "red and gold", False),
    "etoile":     ("a single Christmas star", "five-pointed star with crisp edges, slightly thick", "gold and yellow", False),
    "sapin":      ("a single small Christmas tree", "triangle in three tiers with a short trunk and three baubles", "green, red and gold", True),
    "flocon":     ("a single snowflake", "six symmetric thick branches, no fine detail", "off-white and light blue", False),
    "pain-epice": ("a single gingerbread man", "rounded brown silhouette, three buttons, simple icing smile, no realistic face", "brown, white and red", False),
    "coeur":      ("a single Christmas heart", "red heart with a simple white knitted border", "red and white", False),
}

SCENE = ("a cozy afternoon tea table seen from the front, slightly from above: a round table with a "
         "tablecloth in {ACCENT1}, a teapot and three cups in {ACCENT2}, a cake on a stand, a small "
         "vase, a few wooden toys on the floor, a chair on the left, warm interior, wall color {FOND}, "
         "floor in {ACCENT3}")

HIVER = ("add a window on the left wall showing falling snow outside, and a small decorated Christmas "
         "tree in the left corner; keep everything else exactly the same")

# Phrase de référence v1 (02/11/2026), remplacée avant l'essai 5 de la jonquille et du glaïeul : la rose de
# référence déteignait sur les sorties (sa paire de feuilles en lavis sur jonquille, glaïeul, pied-d'alouette,
# violette ; une rose fantôme derrière le glaïeul seed 4). « same contour thickness » n'avait plus de sens
# sans contour noir.
# REFERENCE_STYLE_V1 = ("Same painting style, same contour thickness, same opaque gouache material as the "
#                       "reference image. ")
REFERENCE_STYLE = ("Use the reference image only for its painting style and its opaque gouache material. "
                   "Do not copy its subject, its leaves, its stem or its composition. ")


def prompt_element(nom):
    """Prompt complet d'une fleur ou d'un ornement, et le fond à utiliser."""
    sujet, silhouette, couleurs, vert = (FLEURS | ORNEMENTS)[nom]
    fond = FOND_MAGENTA if vert else FOND_VERT
    return (f"{PREFIXE}. {sujet}, {silhouette}, {couleurs}. "
            f"{SUFFIXE_ELEMENT.format(FOND=fond)}"), fond


def prompt_scene(destinataire):
    p = PALETTES[destinataire]
    a1, a2, a3 = p["accents"]
    corps = SCENE.format(FOND=p["fond"], ACCENT1=a1, ACCENT2=a2, ACCENT3=a3)
    return f"{PREFIXE}. {corps}. {SUFFIXE_SCENE.format(FOND=p['fond'])}", p["fond"]
