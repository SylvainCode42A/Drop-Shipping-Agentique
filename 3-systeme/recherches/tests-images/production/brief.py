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
    # Souci et chrysanthème v1 (02/11/2026), têtes sans tige, validés ; régénérés avec une tige courte pour
    # être plantés dans la bande de sol (décision 15, précision du 02/11).
    # "souci":        ("a single marigold flower", "dense round head with tightly packed petals", "bright orange", True),
    # "chrysantheme": ("a single chrysanthemum flower", "very full round pompom head", "yellow or bronze", True),
    "souci":         ("a single marigold flower", "dense round head with tightly packed petals, on a short straight stem ending in a clean blunt cut", "bright orange, green stem", True),
    "chrysantheme":  ("a single chrysanthemum flower", "very full round pompom head, on a short straight stem ending in a clean blunt cut", "yellow or bronze, green stem", True),
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

# Supports des symboles (ajoutés le 02/11/2026, brief section 4 bis) : générés en 16:9, découpés par le code
# en trois morceaux (15 % gauche, milieu répété, 15 % droite) pour tenir toute largeur.
SUPPORTS = {
    "sol":     ("a horizontal strip of short green grass with a thin band of brown earth below it", "soft rounded ends, no marked pattern so that the middle can be repeated, height about one fifth of the width", "bright green grass, brown earth", True),
    "branche": ("a horizontal fir tree branch", "bold needles, two natural ends, no marked pattern so that the middle can be repeated, height about one fifth of the width", "dark green needles, brown twig", True),
    # Lot Papa et Papy (04/11/2026, brief section 9).
    "branche-nue": ("a horizontal bare wooden branch with a few small leaves", "two natural ends, no marked pattern so that the middle can be repeated, height about one fifth of the width", "brown, a little green", True),
    "panneau":     ("a horizontal wooden pegboard strip with evenly spaced holes", "rounded ends, no marked pattern so that the middle can be repeated, height about one fifth of the width", "light wood", False),
    "eau":         ("a horizontal strip of water with simple rounded waves", "rounded ends, no marked pattern so that the middle can be repeated, height about one fifth of the width", "blue, light blue", False),
}
ASPECT_SUPPORTS = "16:9"

# Lot Maman (03/11/2026, brief section 8) : quatre familles de symboles de plus et une couronne.
PAPILLONS = {
    "papillon-rouge":  ("a single butterfly", "open wings seen from above, two large upper wings and two small lower wings, thin body, two thick antennae", "red and orange", False),
    "papillon-bleu":   ("a single butterfly", "open wings seen from above, two large upper wings and two small lower wings, thin body, two thick antennae", "blue and navy", False),
    "papillon-jaune":  ("a single butterfly", "open wings seen from above, two large upper wings and two small lower wings, thin body, two thick antennae", "yellow and ochre", False),
    "papillon-rose":   ("a single butterfly", "open wings seen from above, two large upper wings and two small lower wings, thin body, two thick antennae", "pink and plum", False),
    "papillon-vert":   ("a single butterfly", "open wings seen from above, two large upper wings and two small lower wings, thin body, two thick antennae", "green and bottle green", True),
    "papillon-violet": ("a single butterfly", "open wings seen from above, two large upper wings and two small lower wings, thin body, two thick antennae", "violet and lavender", False),
}

COEURS = {
    "coeur-rouge":  ("a single heart", "full heart with rounded lobes, one simple flat highlight", "red #C8453C", False),
    "coeur-corail": ("a single heart", "full heart with rounded lobes, one simple flat highlight", "coral #E07A5F", False),
    "coeur-rose":   ("a single heart", "full heart with rounded lobes, one simple flat highlight", "pink #D98BA6", False),
    "coeur-prune":  ("a single heart", "full heart with rounded lobes, one simple flat highlight", "plum #7B3F61", False),
    "coeur-bleu":   ("a single heart", "full heart with rounded lobes, one simple flat highlight", "blue #4A7FC1", False),
    "coeur-vert":   ("a single heart", "full heart with rounded lobes, one simple flat highlight", "sage green #5E8A6E", True),
}

# Oiseaux posés v1 (03/11/2026), complétés avant la graine 3 : seeds 1 et 2 avec des pattes sous 12 px, des plumes
# rayées détaillées (rouge-gorge, chardonneret, moineau) et une branche ajoutée (mésange 1, moineau 2).
# "mesange":      ("a single blue tit bird", "small round bird in profile, perched, blue head, white cheeks, yellow belly", "blue, yellow, white", False),
# "rouge-gorge":  ("a single robin bird", "small round bird in profile, perched, orange breast", "brown and orange", False),
# "chardonneret": ("a single goldfinch bird", "small bird in profile, red face, yellow bar on the wing", "red, yellow, brown", False),
# "moineau":      ("a single sparrow bird", "small round bird in profile, perched, streaked brown", "brown and beige", False),
OISEAUX_SANS_PATTES = ", legs hidden under the round body, simple flat color areas, no feather detail, no branch"
OISEAUX = {
    "mesange":      ("a single blue tit bird", "small round bird in profile, perched, blue head, white cheeks, yellow belly" + OISEAUX_SANS_PATTES, "blue, yellow, white", False),
    "rouge-gorge":  ("a single robin bird", "small round bird in profile, perched, orange breast" + OISEAUX_SANS_PATTES, "brown and orange", False),
    "hirondelle":   ("a single swallow bird", "slim bird in flight, pointed wings, forked tail", "navy blue and white", False),
    "chardonneret": ("a single goldfinch bird", "small bird in profile, red face, yellow bar on the wing" + OISEAUX_SANS_PATTES, "red, yellow, brown", False),
    "moineau":      ("a single sparrow bird", "small round bird in profile, perched, streaked brown" + OISEAUX_SANS_PATTES, "brown and beige", False),
    "bouvreuil":    ("a single bullfinch bird", "small round bird in profile, perched, pink breast, black cap", "pink, black, grey", False),
}

# Texte commun v1 (03/11/2026), remplacé le même jour avant la graine 3 : cinq images sur seize peintes sur une
# carte à bordure blanche (garcon-blond 1, fille-brune 1, fille-chatain-mate 2, garcon-frise 1 et 2). Les six
# figurines validées en graine 2 (et fille-blonde 1 et 2) sont gardées.
# ENFANT_COMMUN_V1 = ("a single small child character, standing, front view, big round head and short body, two dot "
#                     "eyes and a small smile, no realistic face, no nose detail, plain one-color clothes, no logo, "
#                     "no pattern, arms slightly open, same character design for the whole set")
ENFANT_COMMUN = ("a single small child character, standing, front view, big round head and short body, two dot "
                 "eyes and a small smile, no realistic face, no nose detail, plain one-color clothes, no logo, "
                 "no pattern, arms slightly open, same character design for the whole set, painted directly "
                 "on the background, no card, no paper sheet, no frame, no white border")
ENFANTS = {
    "fille-blonde":       (ENFANT_COMMUN, "girl, light blonde hair in two short pigtails, light skin, yellow dress", "", False),
    "garcon-blond":       (ENFANT_COMMUN, "boy, short light blonde hair, light skin, blue t-shirt and shorts", "", False),
    "fille-brune":        (ENFANT_COMMUN, "girl, brown hair in a ponytail, light skin, red dress", "", False),
    "garcon-brun":        (ENFANT_COMMUN, "boy, short brown hair, light skin, green t-shirt and shorts", "", True),
    "fille-chatain-mate": (ENFANT_COMMUN, "girl, dark brown hair in a braid, medium tan skin, coral dress", "", False),
    "garcon-chatain-mat": (ENFANT_COMMUN, "boy, short dark brown hair, medium tan skin, ochre t-shirt and shorts", "", False),
    "fille-frisee":       (ENFANT_COMMUN, "girl, black curly hair, dark brown skin, violet dress", "", False),
    # Variante v1 (03/11/2026), remplacée avant la graine 4 : seeds 1 et 2 sur carte, seed 3 avec les boucles
    # peintes en S qui se lisent comme des lettres.
    # "garcon-frise":     (ENFANT_COMMUN, "boy, short black curly hair, dark brown skin, teal t-shirt and shorts", "", True),
    "garcon-frise":       (ENFANT_COMMUN, "boy, short black curly hair forming one full rounded cap that covers the top of the head, dark brown skin, teal t-shirt and shorts", "", True),
    # Bébé et chat v1 (03/11/2026), complétés avant la graine 1 par la phrase contre la carte à bordure blanche
    # du texte commun v2.
    # "bebe":             ("a single swaddled baby in a white blanket", "big round head, two dot eyes and a small smile, no realistic face, same character design as the child set", "white, light skin", False),
    # "chat":             ("a single small sitting cat", "simple rounded shape, two dot eyes, same painting style as the child set", "ginger and white", False),
    "bebe":               ("a single swaddled baby in a white blanket", "big round head, two dot eyes and a small smile, no realistic face, same character design as the child set, painted directly on the background, no card, no paper sheet, no frame, no white border", "white, light skin", False),
    "chat":               ("a single small sitting cat", "simple rounded shape, two dot eyes, same painting style as the child set, painted directly on the background, no card, no paper sheet, no frame, no white border", "ginger and white", False),
}

COURONNE = {
    "couronne": ("a single round floral wreath", "ring of small flowers and leaves, empty center, ring thickness about one fifth of the diameter, perfectly round", "green leaves, pink, coral and yellow flowers", True),
}

# Lot Papa et Papy (04/11/2026, brief section 9) : trois familles de symboles de plus.
# « every part fully opaque » repris de la jonquille : les fanes et les feuilles partaient en lavis.
POTAGER_COMMUN = ", every part fully opaque"
POTAGER = {
    "tomate":  ("a single tomato", "on a short vine stem with two leaves" + POTAGER_COMMUN, "red, green", True),
    "carotte": ("a single carrot", "standing upright with its green tops" + POTAGER_COMMUN, "orange, green", True),
    "potiron": ("a single round pumpkin", "with a short stem" + POTAGER_COMMUN, "orange, green stem", True),
    "radis":   ("a single radish", "with green leaves" + POTAGER_COMMUN, "pink-red, white tip, green", True),
    "poireau": ("a single leek", "standing upright" + POTAGER_COMMUN, "white base, green leaves", True),
    "chou":    ("a single round cabbage", "compact round head" + POTAGER_COMMUN, "pale and dark green", True),
}

OUTILS_ACCROCHE = "shown flat, slightly tilted, as if hanging on a wall, no numbers, no brand, no inscription"
OUTILS = {
    "marteau":   ("a single claw hammer", OUTILS_ACCROCHE, "wooden handle, grey head", False),
    "cle":       ("a single open-end wrench", OUTILS_ACCROCHE, "grey steel", False),
    "tournevis": ("a single screwdriver", OUTILS_ACCROCHE, "red or yellow handle, grey shaft", False),
    "scie":      ("a single hand saw", "teeth as one bold zigzag edge, no fine teeth, " + OUTILS_ACCROCHE, "wooden handle, grey blade", False),
    "pince":     ("a single pair of pliers", OUTILS_ACCROCHE, "red handles, grey jaws", False),
    "metre":     ("a single folding carpenter's ruler", "partly unfolded, no text, " + OUTILS_ACCROCHE, "yellow", False),
}

POISSONS_COMMUN = "simple fish in side view, one dot eye, no realistic scale detail, "
POISSONS = {
    "truite":         ("a single trout", POISSONS_COMMUN + "long slim body with a few bold dark spots", "silver grey, dark spots, pink side stripe", False),
    "poisson-rouge":  ("a single goldfish", POISSONS_COMMUN + "round body, fan-shaped tail", "orange-red", False),
    "maquereau":      ("a single mackerel", POISSONS_COMMUN + "slim pointed body, forked tail, a few bold dark wavy stripes on the back", "blue and green back, silver belly", True),
    "perche":         ("a single perch", POISSONS_COMMUN + "deep body, spiky back fin, a few bold dark vertical stripes", "yellow-ochre, dark stripes, orange fins", False),
    "poisson-lune":   ("a single sunfish", POISSONS_COMMUN + "round flat body like a disc, small fins", "yellow", False),
    "poisson-orange": ("a single small fish", POISSONS_COMMUN + "small body with long flowing fins and a long tail", "orange", False),
}

FAMILLES = {"fleurs": FLEURS, "ornements": ORNEMENTS, "supports": SUPPORTS, "papillons": PAPILLONS,
            "coeurs": COEURS, "oiseaux": OISEAUX, "enfants": ENFANTS, "couronne": COURONNE,
            "potager": POTAGER, "outils": OUTILS, "poissons": POISSONS}

SCENE = ("a cozy afternoon tea table seen from the front, slightly from above: a round table with a "
         "tablecloth in {ACCENT1}, a teapot and three cups in {ACCENT2}, a cake on a stand, a small "
         "vase, a few wooden toys on the floor, a chair on the left, warm interior, wall color {FOND}, "
         "floor in {ACCENT3}")

HIVER = ("add a window on the left wall showing falling snow outside, and a small decorated Christmas "
         "tree in the left corner; keep everything else exactly the same")

# Scène B de Papa et Papy (04/11/2026, brief section 9), qui s'ajoute au goûter.
ATELIER = ("a cozy home workshop seen from the front: a wooden workbench, a few tools hanging on the wall "
           "on the left, a small wooden toy car on the bench, a stool, warm interior, wall color {FOND}, "
           "floor in {ACCENT3}, accents in {ACCENT1} and {ACCENT2}")

HIVER_ATELIER = ("add a window on the left wall showing falling snow outside, and a small decorated "
                 "Christmas tree on the workbench; keep everything else exactly the same")

# Phrase de référence v1 (02/11/2026), remplacée avant l'essai 5 de la jonquille et du glaïeul : la rose de
# référence déteignait sur les sorties (sa paire de feuilles en lavis sur jonquille, glaïeul, pied-d'alouette,
# violette ; une rose fantôme derrière le glaïeul seed 4). « same contour thickness » n'avait plus de sens
# sans contour noir.
# REFERENCE_STYLE_V1 = ("Same painting style, same contour thickness, same opaque gouache material as the "
#                       "reference image. ")
REFERENCE_STYLE = ("Use the reference image only for its painting style and its opaque gouache material. "
                   "Do not copy its subject, its leaves, its stem or its composition. ")


def prompt_element(nom):
    """Prompt complet d'un élément de n'importe quelle famille, et le fond à utiliser."""
    tous = {}
    for fam in FAMILLES.values():
        tous.update(fam)
    sujet, silhouette, couleurs, vert = tous[nom]
    fond = FOND_MAGENTA if vert else FOND_VERT
    corps = f"{sujet}, {silhouette}" + (f", {couleurs}" if couleurs else "")
    return (f"{PREFIXE}. {corps}. "
            f"{SUFFIXE_ELEMENT.format(FOND=fond)}"), fond


def prompt_scene(destinataire, modele=SCENE):
    p = PALETTES[destinataire]
    a1, a2, a3 = p["accents"]
    corps = modele.format(FOND=p["fond"], ACCENT1=a1, ACCENT2=a2, ACCENT3=a3)
    return f"{PREFIXE}. {corps}. {SUFFIXE_SCENE.format(FOND=p['fond'])}", p["fond"]
