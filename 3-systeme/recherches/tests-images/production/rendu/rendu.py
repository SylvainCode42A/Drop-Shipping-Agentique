"""Module de rendu NolaPrint, Noël 2026 : le fichier d'impression d'une commande.

Décisions 10, 13, 14 et 15 ; données de placement : CMP - Gabarits de support (gabarits.json).
Tout est en millimètres jusqu'à l'export ; la conversion en pixels vient du placeholder de chaque
support. Aucune image n'est redimensionnée d'un support à l'autre : chaque rendu repart des éléments
de production/valides/ et des scènes recolorées.

Usage :
    from rendu import rendre, enregistrer
    image, alertes = rendre(commande)
    enregistrer(image, "sortie.png")

    python rendu.py --essai      # quatre rendus de contrôle avec les zones tracées (étapes 1 à 4)

Une commande est un dict :
    support       "mug" | "boule" | "bois"
    forme         pour le bois : "ovale", "chaussette", "sapin", "cloche", "coeur", "etoile"
    gabarit       "A" (un symbole par prénom) | "B" (scène fixe)
    destinataire  "mamie", "papy", "maman", "papa", "couple", "famille"
    saison        "base" (fleurs, sol) | "noel" (ornements, branche, calque d'hiver)
    surnom        "Mamie", "Mémé"... (titre du gabarit)
    prenoms       liste de 0 à 6 {"prenom": "Léa", "symbole": "rose", "mois": "juin"}
    phrase        texte libre, peut être vide
    couleur_texte une des quatre couleurs de texte de la palette du destinataire

rendre() renvoie l'image RGBA et la liste des alertes (texte réduit, zone dépassée, zone estimée).
Une impossibilité (prénom illisible même réduit, symbole inconnu, N trop grand) lève TacheHumaine.
"""
from __future__ import annotations

import io
import json
import math
import sys
import unicodedata
from xml.sax.saxutils import escape
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path

import numpy as np
from PIL import Image, ImageCms, ImageDraw, ImageFont, features

ICI = Path(__file__).resolve().parent
PROD = ICI.parent
VALIDES = PROD / "valides"
G = json.loads((PROD / "gabarits.json").read_text())
sys.path.insert(0, str(PROD))
import brief  # noqa: E402  palettes (fond, accents)

DPI = 300
PX_PAR_MM_300 = DPI / 25.4

# Couleurs de texte par destinataire : CMP - Brief de génération, section 2 (absentes de brief.py,
# qui ne porte que les prompts). Fond et accents viennent de brief.PALETTES.
TEXTE = {
    "mamie":   ["#6B4430", "#C8453C", "#5E8A6E", "#2B3A67"],
    "papy":    ["#2B3A67", "#B5533C", "#2E5E4E", "#6B4430"],
    "maman":   ["#7B3F61", "#6B4430", "#5E8A6E", "#2B3A67"],
    "papa":    ["#2B3A67", "#8A5A3B", "#2F4FA8", "#1A1A1A"],
    "couple":  ["#7A1E2E", "#6B4430", "#5E8A6E", "#2B3A67"],
    "famille": ["#2E5E4E", "#6B4430", "#C8623C", "#2B3A67"],
}
# Choix validés en chat le 02/11/2026, absents de gabarits.json (à reporter dans CMP - Gabarits de support) :
# ornements du mug descendus de 4 mm à Noël, pour que la branche sorte de la zone du titre ;
# capitale minimale de la phrase à 2,5 mm (texte minimal de CMP - Personnalisation par produit).
MUG_NOEL_DECALAGE_MM = 4
PHRASE_CAP_MIN_MM = 2.5
MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre",
        "octobre", "novembre", "décembre"]


class TacheHumaine(Exception):
    """Le rendu automatique est impossible : la commande part en tâche humaine (FLOW - Personnalisation)."""


# ---------- toile ----------

@dataclass
class Toile:
    """Une image RGBA avec son repère en millimètres (origine en haut à gauche, ou au centre pour la boule)."""
    support: str
    w_mm: float
    h_mm: float
    w_px: int
    h_px: int
    centre: bool = False
    img: Image.Image = None
    alertes: list = field(default_factory=list)
    infos: list = field(default_factory=list)
    textes: list = field(default_factory=list)

    @property
    def ppm(self) -> float:  # pixels par millimètre, d'après le placeholder
        return self.w_px / self.w_mm

    def px(self, x_mm: float, y_mm: float) -> tuple[int, int]:
        if self.centre:
            x_mm, y_mm = x_mm + self.w_mm / 2, y_mm + self.h_mm / 2
        return round(x_mm * self.ppm), round(y_mm * self.ppm)

    def mm(self, v: float) -> int:
        return round(v * self.ppm)

    def coller(self, im: Image.Image, x_mm: float, y_mm: float) -> None:
        self.img.alpha_composite(im, self.px(x_mm, y_mm))

    def alerte(self, texte: str, genre: str = "autre") -> None:
        """Alerte typée : « réduction » (texte réduit), « omission » (zone omise par une règle),
        « dépassement » (dessin réel hors d'une zone), « autre » (donnée estimée, décision à prendre)."""
        ligne = f"{genre} : {texte}"
        if ligne not in self.alertes:
            self.alertes.append(ligne)

    def info(self, texte: str) -> None:
        """Ce que le module ajuste comme prévu (zone ramenée dans le cercle, grille descendue) : pas une alerte."""
        if texte not in self.infos:
            self.infos.append(texte)


def nouvelle_toile(cmd: dict, echelle: float = 1.0) -> Toile:
    """La toile à la taille du placeholder, multipliée par echelle (1 pour l'impression, 0,25 pour l'aperçu).
    Tout le reste du module travaille en millimètres : seul le nombre de pixels par millimètre change."""
    t = _toile_impression(cmd)
    if echelle != 1.0:
        t.w_px, t.h_px = max(1, round(t.w_px * echelle)), max(1, round(t.h_px * echelle))
        t.img = t.img.resize((t.w_px, t.h_px))
    return t


def _toile_impression(cmd: dict) -> Toile:
    s = cmd["support"]
    if s == "mug":
        w_mm, h_mm = G["mug"]["panneau_mm"]
        w_px, h_px = G["mug"]["placeholder_px"]
        t = Toile(s, w_mm, h_mm, w_px, h_px)
        fond = brief.PALETTES[cmd["destinataire"]]["fond"]
        t.img = Image.new("RGBA", (w_px, h_px), fond)
    elif s == "boule":
        d = G["boule"]["disque_mm"]
        w_px, h_px = G["boule"]["placeholder_px"]
        t = Toile(s, d, d, w_px, h_px, centre=True)
        t.img = Image.new("RGBA", (w_px, h_px), (0, 0, 0, 0))
    elif s == "bois":
        forme = cmd["forme"]
        w_mm, h_mm = G["bois"]["formes"][forme]["fichier_mm"]
        connu = G["bois"]["placeholder_px_estime"].get(forme)
        if connu:
            w_px, h_px = connu
        else:  # placeholder non relevé : 300 DPI sur les dimensions du fichier
            w_px, h_px = round(w_mm * PX_PAR_MM_300), round(h_mm * PX_PAR_MM_300)
        t = Toile(s, w_mm, h_mm, w_px, h_px)
        t.img = Image.new("RGBA", (w_px, h_px), (0, 0, 0, 0))
        if not connu:
            t.alerte(f"bois {forme} : placeholder non relevé, {w_px} × {h_px} px calculés à 300 DPI", "autre")
    else:
        raise TacheHumaine(f"support inconnu : {s}")
    return t


# ---------- commande ----------

def nfc(texte) -> str:
    return unicodedata.normalize("NFC", (texte or "").strip())


def mois_texte(m) -> str:
    if m in (None, ""):
        return ""
    if isinstance(m, int) or str(m).isdigit():
        return MOIS[int(m) - 1]
    return nfc(m).lower()


def valider(cmd: dict) -> dict:
    """Normalise la commande (NFC partout) et refuse ce que la fiche n'aurait pas dû permettre."""
    c = dict(cmd)
    for k in ("surnom", "phrase"):
        c[k] = nfc(c.get(k))
    c["prenoms"] = [{"prenom": nfc(p.get("prenom")), "symbole": p.get("symbole"), "mois": mois_texte(p.get("mois"))}
                    for p in (c.get("prenoms") or [])]
    n = len(c["prenoms"])
    if c["destinataire"] not in brief.PALETTES:
        raise TacheHumaine(f"destinataire inconnu : {c['destinataire']}")
    if c.get("couleur_texte", "").upper() not in [x.upper() for x in TEXTE[c["destinataire"]]]:
        raise TacheHumaine(f"couleur {c.get('couleur_texte')} hors de la palette {c['destinataire']}")
    if c["saison"] not in ("base", "noel"):
        raise TacheHumaine(f"saison inconnue : {c['saison']}")
    n_max = 6
    if c["support"] == "bois":
        f = G["bois"]["formes"].get(c.get("forme"))
        if not f:
            raise TacheHumaine(f"forme de bois inconnue : {c.get('forme')}")
        n_max = f["n_max"]
        if c["gabarit"] == "B" and not f["B"]:
            raise TacheHumaine(f"le gabarit B n'existe pas sur la forme {c['forme']}")
    if n > n_max:
        raise TacheHumaine(f"{n} prénoms pour {n_max} au plus sur ce support")
    if c["gabarit"] == "A":
        famille = brief.FLEURS if c["saison"] == "base" else brief.ORNEMENTS
        for p in c["prenoms"]:
            if p["symbole"] not in famille:
                genre = "une fleur" if c["saison"] == "base" else "un ornement"
                raise TacheHumaine(f"symbole {p['symbole']} : il faut {genre} du brief en saison {c['saison']}")
            if not (VALIDES / f"{p['symbole']}.png").exists():
                raise TacheHumaine(f"symbole {p['symbole']} absent de valides/")
    return c


# ---------- symboles ----------

@lru_cache(maxsize=64)
def _source(nom: str) -> Image.Image:
    return Image.open(VALIDES / f"{nom}.png").convert("RGBA")


def symbole(nom: str, taille_px: int) -> Image.Image:
    """Le symbole contenu dans un carré de taille_px, proportions gardées, réduit en Lanczos."""
    src = _source(nom)
    k = taille_px / max(src.size)
    return src.resize((max(1, round(src.width * k)), max(1, round(src.height * k))), Image.LANCZOS)


# ---------- grilles du gabarit A ----------

@dataclass
class Case:
    """Emplacement d'un symbole : carré de côté s (mm), coin haut gauche (x, y) dans le repère de la toile."""
    x: float
    y: float
    s: float
    rangee: int


def _cap(nom: str, support: str) -> float:
    return G["communs"]["cap_mm"][nom][support]


def hauteur_support(s: float) -> float:
    return G["communs"]["support_symboles"]["hauteur_fraction"] * s


def hauteur_bloc_texte(support: str, avec_mois: bool) -> float:
    """Hauteur réservée sous le symbole pour le prénom et le mois : interligne de 1,4 capitale (estimé)."""
    h = 1.4 * _cap("prenom", support)
    if avec_mois:
        h += 1.4 * G["communs"]["mois"]["cap_mm"][support]
    return h


def mois_affiche(cmd: dict) -> bool:
    n = len(cmd["prenoms"])
    return not (cmd["support"] == "boule" and n > G["communs"]["mois"]["omis_boule_si_n_sup"])


def repartir(n: int, colonnes: int, rangees: int) -> list[int]:
    """Nombre de symboles par rangée, réparti au plus juste (5 sur 2 rangées de 3 : 3 puis 2)."""
    out, reste = [], n
    for r in range(rangees):
        k = min(colonnes, math.ceil(reste / (rangees - r)))
        out.append(k)
        reste -= k
    return [k for k in out if k]


def _rangees(par_rangee: list[int], s: float, e: float, cx: float, y0: float, pas: float) -> list[Case]:
    cases = []
    for r, k in enumerate(par_rangee):
        largeur = k * s + (k - 1) * e
        x0 = cx - largeur / 2
        for i in range(k):
            cases.append(Case(x0 + i * (s + e), y0 + r * pas, s, r))
    return cases


def grille_A(t: Toile, cmd: dict) -> list[Case]:
    n = len(cmd["prenoms"])
    if n == 0:
        return []
    sup, noel = cmd["support"], cmd["saison"] == "noel"
    e = G["communs"]["espace_symboles_mm"][sup]
    bloc = hauteur_bloc_texte(sup, mois_affiche(cmd))
    if sup == "mug":
        a = G["mug"]["A"]
        s = a["symboles"]["taille_par_n"][str(n)]
        y = a["symboles"]["y"] + (MUG_NOEL_DECALAGE_MM if noel else 0)
        return _rangees([n], s, e, a["symboles"]["centre_x"], y, 0)
    if sup == "boule":
        a = G["boule"]["A"]["symboles"]
        if n <= a["n_max_rangee"]:
            s = a["une_rangee"]["taille"]
            return _rangees([n], s, e, 0, a["une_rangee"]["y"] - s / 2, 0)
        s = a["deux_rangees"]["taille"]
        haut, bas = a["deux_rangees"]["y"]
        return _rangees(repartir(n, 3, 2), s, e, 0, haut - s / 2, bas - haut)
    # bois
    f = G["bois"]["formes"][cmd["forme"]]
    saison = f["A"].get("noel", {}) if noel else {}   # réglage propre à Noël (ovale à 5 et 6)
    disposition = saison.get("disposition", {}).get(str(n)) or f["A"]["disposition"][str(n)]
    s, colonnes, rangees = disposition[0]
    par_rangee = repartir(n, colonnes, rangees)
    pas_impose = saison.get("pas_par_n", {}).get(str(n)) or f["A"].get("pas_par_n", {}).get(str(n))
    if pas_impose:  # pas imposé par le gabarit (ovale à 5 et 6)
        pas = pas_impose
    elif noel:  # la branche de la rangée suivante passe sous le bloc de texte, pas dessus
        ss = G["communs"]["support_symboles"]
        pas = s + 0.5 + bloc + e + ss["branche_decalage_mm"] + hauteur_support(s) / 2
    else:
        pas = s + hauteur_support(s) + 0.5 + bloc + e
    u = f["utile"]["jambe"] if "jambe" in f["utile"] else f["utile"]
    hauteur = len(par_rangee) * pas - e
    if "grille_y" in f["A"]:
        cx, y0 = f["A"]["centre_x"], f["A"]["grille_y"]
    else:  # centrée dans le rectangle utile (chaussette : la jambe)
        cx, y0 = u["x"] + u["l"] / 2, u["y"] + (u["h"] - hauteur) / 2
    if noel:  # la branche et la ficelle passent au-dessus de la première rangée
        y0 += G["communs"]["support_symboles"]["branche_decalage_mm"]
    cases = _rangees(par_rangee, s, e, cx, y0, pas)
    return cases


def _boite_opaque(im: Image.Image) -> tuple[int, int, int, int]:
    return im.getchannel("A").point(lambda v: 255 if v > 128 else 0).getbbox() or (0, 0, im.width, im.height)


def _accroche(im: Image.Image) -> int:
    """Rangée du premier pixel opaque près de l'axe vertical : là où la ficelle s'attache."""
    a = np.asarray(im.getchannel("A"))
    c, demi = im.width // 2, max(2, im.width // 20)
    lignes = np.where((a[:, c - demi:c + demi + 1] > 128).any(axis=1))[0]
    return int(lignes[0]) if len(lignes) else _boite_opaque(im)[1]


@lru_cache(maxsize=32)
def _morceau(support: str, partie: str) -> Image.Image:
    return Image.open(VALIDES / f"{support}-{partie}.png").convert("RGBA")


def bande_support(nom: str, largeur_px: int, hauteur_px: int) -> Image.Image:
    """Sol ou branche à la largeur demandée : bout gauche, tuile répétée k fois, bout droit.

    Les trois morceaux sont mis à la hauteur voulue en Lanczos. Le nombre de tuiles est arrondi au
    plus proche, puis la tuile est étirée ou tassée (au plus de moitié d'une tuile) pour tomber juste :
    on ne coupe jamais une tuile, car la jonction avec le bout droit ne se raccorde qu'en fin de tuile."""
    g, tu, d = (_morceau(nom, p) for p in ("gauche", "tuile", "droite"))

    def h(im, w=None):
        k = hauteur_px / im.height
        return im.resize((w or max(1, round(im.width * k)), hauteur_px), Image.LANCZOS)

    g, d, tu = h(g), h(d), h(tu)
    reste = largeur_px - g.width - d.width
    if reste <= 0:  # rangée très courte : les deux bouts seuls, tassés
        g, d = h(_morceau(nom, "gauche"), largeur_px // 2), h(_morceau(nom, "droite"), largeur_px - largeur_px // 2)
        k, tu = 0, None
    else:
        k = max(1, round(reste / tu.width))
        largeurs = [reste // k + (1 if i < reste % k else 0) for i in range(k)]
        tu = h(_morceau(nom, "tuile"), largeurs[0]) if len(set(largeurs)) == 1 else None
    out = Image.new("RGBA", (largeur_px, hauteur_px), (0, 0, 0, 0))
    x = 0
    out.alpha_composite(g, (0, 0))
    x += g.width
    for i in range(k):
        w = reste // k + (1 if i < reste % k else 0)
        tuile = tu if tu is not None and tu.width == w else h(_morceau(nom, "tuile"), w)
        out.alpha_composite(tuile, (x, 0))
        x += w
    out.alpha_composite(d, (x, 0))
    return out


def poser_symboles(t: Toile, cmd: dict, cases: list[Case]) -> list[float]:
    """Sol puis fleurs (plantées, base des tiges enfoncée dans le sol), ou branche, ficelles puis ornements.

    Renvoie, pour chaque case, la hauteur (mm) où commence le bloc de texte en dessous."""
    noel = cmd["saison"] == "noel"
    ss = G["communs"]["support_symboles"]
    nom_support = ss["noel"] if noel else ss["base"]
    sous = []
    for r in sorted({c.rangee for c in cases}):
        rangee = [c for c in cases if c.rangee == r]
        s = rangee[0].s
        h_sup = ss["hauteur_fraction"] * s
        gauche, droite = rangee[0].x, rangee[-1].x + s
        largeur = droite - gauche + ss["marge_largeur_symboles"] * s
        x_sup = (gauche + droite) / 2 - largeur / 2
        haut = rangee[0].y
        if noel:  # axe de la branche à 6 mm au-dessus du haut des ornements
            y_axe = haut - ss["branche_decalage_mm"]
            y_sup = y_axe - h_sup / 2
        else:  # la base des tiges entre de 15 % dans la bande de sol
            y_sup = haut + s - ss["sol_enfoncement_fraction"] * h_sup
        bande = bande_support(nom_support, t.mm(largeur), t.mm(h_sup))
        t.img.alpha_composite(bande, t.px(x_sup, y_sup))
        if noel and y_sup < (G["mug"]["A"]["titre"]["y"] + G["mug"]["A"]["titre"]["h"]) and t.support == "mug":
            t.alerte(f"mug, Noël : la branche (haut à {y_sup:.1f} mm) entre dans la zone du titre (bas à "
                     f"{G['mug']['A']['titre']['y'] + G['mug']['A']['titre']['h']} mm)", "dépassement")
        fic = ss["ficelle"]
        for case in rangee:
            p = cmd["prenoms"][cases.index(case)]
            im = symbole(p["symbole"], t.mm(s))
            bx0, by0, bx1, by1 = _boite_opaque(im)
            x, y = t.px(case.x, case.y)
            dx = (t.mm(s) - (bx0 + bx1)) // 2           # centre de la partie opaque sur la case
            if noel:
                dy = -by0                                 # haut opaque sur le haut de la case
                cx = x + t.mm(s) // 2
                y_fil0 = t.px(0, y_axe)[1]
                y_fil1 = y + dy + _accroche(im) + max(1, t.mm(0.3))
                ImageDraw.Draw(t.img).line([(cx, y_fil0), (cx, y_fil1)], fill=fic["couleur"],
                                           width=max(1, t.mm(fic["epaisseur_mm"])))
            else:
                dy = t.mm(s) - by1                        # bas opaque sur le bas de la case
            t.img.alpha_composite(im, (x + dx, y + dy))
        bas = haut + s + (0 if noel else h_sup * (1 - ss["sol_enfoncement_fraction"]))
        sous += [bas] * len(rangee)
    return sous


# ---------- textes du gabarit A ----------

@dataclass
class Texte:
    """Un texte à poser : contenu, zone (x, y, l, h en mm) ou arc, capitale visée et minimale, police."""
    role: str
    contenu: list            # [(texte, échelle de capitale, opacité)] : morceaux d'une même ligne
    zone: tuple | None
    cap: float
    cap_min: float
    police: str
    arc: dict | None = None
    lignes: int = 1
    aligne: str = "centre"     # "centre" (titre, phrase) ou "haut" (prénom collé sous son symbole)
    cap_retenue: float | None = None
    nb_lignes: int = 1
    bas: float | None = None


def titre_gabarit(t: "Toile", cmd: dict, cle: str) -> str:
    surnom = cmd["surnom"]
    titre = G["communs"]["titre_phrase"][cle].format(surnom=surnom)
    if surnom.lower().startswith("famille") or surnom.lower() in ("chez nous", "notre tribu"):
        t.alerte(f"titre « {titre} » : tournure à décider pour les titres de famille", "autre")
    return titre


def titre_A_omis(cmd: dict) -> bool:
    """Boule, gabarit A : pas de titre à Noël (la branche croise l'arc, même à 3 ornements), ni au-delà
    de N = 3 en base."""
    if cmd["support"] != "boule":
        return False
    a = G["boule"]["A"]
    return (cmd["saison"] == "noel" and a.get("titre_omis_noel", False)) or \
        len(cmd["prenoms"]) > a.get("titre_si_n_max", 6)


def titre_A(t: "Toile", cmd: dict) -> str:
    return titre_gabarit(t, cmd, "A_noel" if cmd["saison"] == "noel" else "A_base")


def textes_A(t: Toile, cmd: dict, cases: list[Case], sous: list[float]) -> list[Texte]:
    sup = cmd["support"]
    police = G["communs"]["police"]["A"]
    caps, mins = G["communs"]["cap_mm"], G["communs"]["cap_min_mm"]
    mois = G["communs"]["mois"]
    out = []
    if cmd["surnom"] and titre_A_omis(cmd):
        raison = "à Noël" if cmd["saison"] == "noel" else f"N > {G['boule']['A']['titre_si_n_max']}"
        t.alerte(f"boule, N = {len(cmd['prenoms'])} : titre omis (règle du gabarit, {raison})", "omission")
    elif cmd["surnom"]:
        if sup == "mug":
            z = G["mug"]["A"]["titre"]
            out.append(Texte("titre", [(titre_A(t, cmd), 1, 1)], (z["x"], z["y"], z["l"], z["h"]),
                             caps["titre"]["mug"], mins["titre"]["mug"], police))
        elif sup == "boule":
            out.append(Texte("titre", [(titre_A(t, cmd), 1, 1)], None, caps["titre"]["boule"], mins["titre"]["boule"],
                             police, arc=G["boule"]["A"]["titre_arc"]))
        else:
            z = zone_bois(t, cmd, "titre")
            if z:
                cap = G["bois"]["formes"][cmd["forme"]]["A"].get("titre_cap", caps["titre"]["bois"])
                out.append(Texte("titre", [(titre_A(t, cmd), 1, 1)], z, cap, mins["titre"]["bois"], police,
                                 lignes=2))
    decal = {"mug": G["mug"]["A"]["prenom"]["decalage_y"], "boule": G["boule"]["A"]["prenom"]["decalage_y"]}.get(sup, 0.5)
    cap_p = G["bois"]["formes"][cmd["forme"]]["A"].get("prenom_cap", caps["prenom"][sup]) if sup == "bois" else caps["prenom"][sup]
    avec_mois = mois_affiche(cmd)
    for case, y_bas, p in zip(cases, sous, cmd["prenoms"]):
        if not p["prenom"]:
            continue
        morceaux = [(p["prenom"], 1, 1)]
        if avec_mois and p["mois"]:
            morceaux.append((mois["separateur"] + p["mois"], mois["cap_mm"][sup] / cap_p, mois["opacite"]))
        e = G["communs"]["espace_symboles_mm"][sup]
        out.append(Texte("prenom", morceaux, (case.x - e / 2, y_bas + decal, case.s + e,
                                              hauteur_bloc_texte(sup, avec_mois)),
                         cap_p, mins["prenom"][sup], police, aligne="haut"))
    if cmd["phrase"]:
        n = len(cmd["prenoms"])
        if sup == "mug":
            z = G["mug"]["A"]["phrase"]
            out.append(Texte("phrase", [(cmd["phrase"], 1, 1)], (z["x"], z["y"], z["l"], z["h"]),
                             caps["phrase"]["mug"], PHRASE_CAP_MIN_MM, police, lignes=z.get("lignes", 1)))
        elif sup == "boule":
            arc = G["boule"]["A"]["phrase_arc"]
            if n <= arc["si_n_max"]:
                out.append(Texte("phrase", [(cmd["phrase"], 1, 1)], None, caps["phrase"]["boule"],
                                 PHRASE_CAP_MIN_MM, police, arc=arc))
            else:
                t.alerte(f"boule, N = {n} : phrase omise (règle du gabarit, N > {arc['si_n_max']})", "omission")
        elif n > G["bois"]["formes"][cmd["forme"]]["A"].get("phrase_si_n_max", 6):
            t.alerte(f"bois {cmd['forme']}, N = {n} : phrase omise (règle du gabarit, N > "
                     f"{G['bois']['formes'][cmd['forme']]['A']['phrase_si_n_max']})", "omission")
        else:
            z = zone_bois(t, cmd, "phrase")
            if z:
                out.append(Texte("phrase", [(cmd["phrase"], 1, 1)], z, caps["phrase"]["bois"],
                                 PHRASE_CAP_MIN_MM, police))
    return out


def zone_bois(t: Toile, cmd: dict, role: str) -> tuple | None:
    """Zone de titre ou de phrase sur le bois : celle du gabarit, sinon une estimation signalée."""
    f = G["bois"]["formes"][cmd["forme"]]
    if role in f["A"]:
        z = f["A"][role]
        return (z["x"], z["y"], z["l"], z["h"])
    u = f["utile"]
    if role == "titre":
        if "jambe" in u:
            j = u["jambe"]
            z = (j["x"], j["y"], j["l"], 11)
        elif cmd["forme"] == "sapin":  # « dans la pointe », au-dessus du rectangle utile
            z = (u["x"], u["y"] - 13, u["l"], 11)
        else:                          # au-dessus du rectangle utile, deux lignes à 4 mm
            z = (u["x"], u["y"] - 13, u["l"], 11)
    else:
        if "pied" in u:
            p = u["pied"]
            z = (p["x"], p["y"] + p["h"] - 10, p["l"], 7)
        else:
            z = (u["x"], u["y"] + u["h"] + 2, u["l"], 6)
    t.alerte(f"bois {cmd['forme']} : zone de {role} absente de gabarits.json, estimée à "
             f"x {z[0]:.0f}, y {z[1]:.0f}, {z[2]:.0f} × {z[3]:.0f} mm", "autre")
    return z


# ---------- gabarit B : la scène de goûter ----------

def _fichier_scene(cmd: dict) -> Path:
    d = cmd["destinataire"]
    nom = f"scene-{d}-hiver-recolle-recolor.png" if cmd["saison"] == "noel" else f"scene-{d}-seed1-recolor.png"
    chemin = PROD / nom
    if not chemin.exists():
        raise TacheHumaine(f"scène absente : {nom} (recolorer.py)")
    return chemin


@lru_cache(maxsize=16)
def scene_preparee(chemin: str) -> tuple[Image.Image, float, float, Image.Image]:
    """La scène, la position du bord du panneau de texte et du haut du sol (fractions de la largeur et de
    la hauteur), et un carré de sol sans objet, qui sert à prolonger le sol sous la zone de texte."""
    im = Image.open(chemin).convert("RGB")
    a = np.asarray(im).astype(np.float32)
    h, w, _ = a.shape
    bas = a[int(0.75 * h):]
    saut = np.abs(np.diff(bas.mean(axis=2), axis=1)).mean(axis=0)
    x_pan = int(np.argmax(saut[w // 2:]) + w // 2)          # bord vertical du panneau, sol coupé net
    colonne = a[:, x_pan - 30].mean(axis=1)
    y_sol = int(np.argmax(np.abs(np.diff(colonne[h // 3:]))) + h // 3)   # ligne mur / sol
    # morceau de sol libre : un carré dont presque aucun pixel ne s'écarte de la couleur du sol (pas de
    # nappe, de pied de table ni de jouet), cherché partout sous la ligne du sol
    sol = np.median(a[int(0.95 * h):, x_pan - 300:x_pan - 10].reshape(-1, 3), axis=0)
    cote = max(96, w // 15)
    meilleur = None
    for y0 in range(y_sol + 6, h - cote, 24):
        for x0 in range(int(0.02 * w), x_pan - cote - 8, 24):
            bloc = a[y0:y0 + cote, x0:x0 + cote]
            ecart = np.linalg.norm(bloc - sol, axis=2)
            if (ecart > 40).mean() > 0.005:
                continue
            v = float(ecart.mean() + bloc.std(axis=(0, 1)).mean())
            if meilleur is None or v < meilleur[0]:
                meilleur = (v, x0, y0)
    if meilleur is None:
        raise TacheHumaine(f"scène {Path(chemin).name} : aucun morceau de sol libre pour prolonger le sol")
    _, x0, y0 = meilleur
    motif = im.crop((x0, y0, x0 + cote, y0 + cote))
    return im, x_pan / w, y_sol / h, motif


def bande_sol(motif: Image.Image, largeur: int, hauteur: int, echelle: float) -> Image.Image:
    """Le morceau de sol répété en miroir dans les deux sens (ni couture ni motif qui saute), à l'échelle
    de la scène posée."""
    c = max(8, round(motif.width * echelle))
    m = motif.resize((c, c), Image.LANCZOS)
    quad = Image.new("RGB", (2 * c, 2 * c))
    quad.paste(m, (0, 0))
    quad.paste(m.transpose(Image.FLIP_LEFT_RIGHT), (c, 0))
    quad.paste(m.transpose(Image.FLIP_TOP_BOTTOM), (0, c))
    quad.paste(m.transpose(Image.ROTATE_180), (c, c))
    out = Image.new("RGB", (largeur, hauteur))
    for y in range(0, hauteur, 2 * c):
        for x in range(0, largeur, 2 * c):
            out.paste(quad, (x, y))
    return out.convert("RGBA")


def poser_scene(t: Toile, cmd: dict, zone: tuple, recadrage: dict, sol_jusqua_mm: float | None) -> float:
    """Recadre la scène au rapport de la zone, la pose, puis prolonge le sol vers la droite, sous la zone
    de texte, de la coupe nette du panneau jusqu'à sol_jusqua_mm (abscisse dans le repère de la toile).
    Renvoie la hauteur (mm) de la ligne du sol dans le repère de la toile."""
    im, f_pan, f_sol, motif = scene_preparee(str(_fichier_scene(cmd)))
    W, H = im.size
    ch = recadrage["hauteur_fraction"] * H
    cw = recadrage["ratio"] * ch
    if cw > W:  # zone plus large que la scène : pleine largeur, hauteur réduite d'autant
        cw, ch = W, W / recadrage["ratio"]
    cx = recadrage["centre_x_fraction"] * W
    x0 = min(max(0, cx - cw / 2), W - cw)
    y0 = (H - ch) * recadrage.get("haut_fraction", 0.5)   # 0 : on garde le haut de la scène, 0,5 : centré
    crop = im.crop((round(x0), round(y0), round(x0 + cw), round(y0 + ch)))
    x, y, l, h = zone
    w_px, h_px = t.mm(l), t.mm(h)
    t.img.alpha_composite(crop.resize((w_px, h_px), Image.LANCZOS).convert("RGBA"), t.px(x, y))
    k = w_px / cw                                    # pixels de toile par pixel de scène
    y_sol = y + (f_sol * H - y0) * k / t.ppm         # ligne du sol, en mm de toile
    if sol_jusqua_mm is None:
        return y_sol
    x_pan = x + (f_pan * W - x0) * k / t.ppm         # coupe du sol, en mm de toile
    if x_pan >= sol_jusqua_mm or not (y < y_sol < y + h):
        return y_sol
    debut = x_pan - 2                                # recouvre le liseré clair de la coupe
    largeur, hauteur = t.mm(sol_jusqua_mm - debut), t.mm(y + h - y_sol)
    bande = bande_sol(motif, largeur, hauteur, k)
    # fondu de 1 mm au début, pour que le sol prolongé reprenne celui de la scène sans trait
    f = min(t.mm(1), bande.width)
    alpha = np.full((bande.height, bande.width), 255, np.uint8)
    alpha[:, :f] = np.linspace(0, 255, f, dtype=np.uint8)[None, :]
    bande.putalpha(Image.fromarray(alpha))
    t.img.alpha_composite(bande, t.px(debut, y_sol))
    return y_sol


def _prenoms_liste(cmd: dict) -> list[str]:
    return [p["prenom"] for p in cmd["prenoms"] if p["prenom"]]


def _liste_en_texte(noms: list[str]) -> str:
    return noms[0] if len(noms) == 1 else ", ".join(noms[:-1]) + " et " + noms[-1]


def textes_B(t: Toile, cmd: dict, y_sol: float | None = None) -> list[Texte]:
    sup = cmd["support"]
    police = G["communs"]["police"]["B"]
    caps, mins = G["communs"]["cap_mm"], G["communs"]["cap_min_mm"]
    cle_sup = "bois" if sup == "bois" else sup
    titre = titre_gabarit(t, cmd, "B") if cmd["surnom"] else ""
    noms = _prenoms_liste(cmd)
    n = len(noms)
    out = []
    if sup == "bois":
        z = G["bois"]["formes"][cmd["forme"]]["B_zones"]
        if titre:
            zt = z["titre"]
            out.append(Texte("titre", [(titre, 1, 1)], (zt["x"], zt["y"], zt["l"], zt["h"]),
                             zt.get("cap", caps["titre"]["bois"]), zt.get("cap_min", mins["titre"]["bois"]), police,
                             lignes=zt.get("lignes", 1)))
        if noms:
            zp = z["prenoms"]
            out.append(Texte("prenom", [(_liste_en_texte(noms), 1, 1)], (zp["x"], zp["y"], zp["l"], zp["h"]),
                             caps["prenom"]["bois"], mins["prenom"]["bois"], police, lignes=zp.get("lignes", 1)))
        if cmd["phrase"]:
            if n > z.get("phrase_si_n_max", 6):
                t.alerte(f"bois {cmd['forme']} B, N = {n} : phrase omise (règle du gabarit)", "omission")
            else:
                zs = z["scene"]
                zp = (zs["x"], zs["y"] + zs["h"] + 0.5, zs["l"], G["bois"]["formes"][cmd["forme"]]["fichier_mm"][1] - 5 - (zs["y"] + zs["h"] + 0.5))
                if zp[3] < PHRASE_CAP_MIN_MM:
                    raise TacheHumaine(f"bois {cmd['forme']} B : le gabarit ne prévoit pas de zone de phrase et il "
                                       f"ne reste que {max(zp[3], 0):.1f} mm sous la scène (tâche humaine)")
                t.alerte(f"bois {cmd['forme']} B : zone de phrase absente de gabarits.json, estimée sous la scène "
                         f"(y {zp[1]:.1f}, {zp[3]:.1f} mm de haut)", "autre")
                out.append(Texte("phrase", [(cmd["phrase"], 1, 1)], zp, caps["phrase"]["bois"], PHRASE_CAP_MIN_MM, police))
        return out
    b = G[sup]["B"]
    if titre:
        if "titre_arc" in b:   # boule : titre sur l'arc du haut
            out.append(Texte("titre", [(titre, 1, 1)], None, b["titre_arc"].get("cap", caps["titre"][cle_sup]),
                             b["titre_arc"].get("cap_min", mins["titre"][cle_sup]), police, arc=b["titre_arc"]))
        else:
            zt = b["titre"]
            out.append(Texte("titre", [(titre, 1, 1)], (zt["x"], zt["y"], zt["l"], zt["h"]),
                             zt.get("cap", caps["titre"][cle_sup]), zt.get("cap_min", mins["titre"][cle_sup]), police,
                             lignes=zt.get("lignes", 1)))
    zp = b["prenoms"]
    deux_col = n >= zp.get("deux_colonnes_si_n_min", 99)
    rangs = (n + 1) // 2 if deux_col else n
    for i, nom in enumerate(noms):
        col, rang = (i // rangs, i % rangs) if deux_col else (0, i)
        l = zp["l"] / 2 if deux_col else zp["l"]
        out.append(Texte("prenom", [(nom, 1, 1)], (zp["x"] + col * l, zp["y0"] + rang * zp["pas"], l, zp["h"]),
                         caps["prenom"][cle_sup], mins["prenom"][cle_sup], police))
    bas_prenoms = zp["y0"] + (rangs - 1) * zp["pas"] + zp["h"] if n else zp["y0"]
    if cmd["phrase"]:
        zs = b["phrase"]
        if sup == "boule" and n > 3:
            t.alerte(f"boule B, N = {n} : phrase omise (règle du gabarit, N > 3)", "omission")
        elif "au_dessus_du_sol_mm" in zs and y_sol is not None:
            # mug B : la phrase se pose sur le mur, entre le dernier prénom et la ligne du sol
            bas = y_sol - zs["au_dessus_du_sol_mm"]
            haut = max(bas - zs["h"], bas_prenoms + 1)
            if bas - haut < PHRASE_CAP_MIN_MM:
                raise TacheHumaine(f"mug B, N = {n} : plus de place pour la phrase entre les prénoms "
                                   f"({bas_prenoms:.1f} mm) et le sol ({y_sol:.1f} mm) (tâche humaine)")
            out.append(Texte("phrase", [(cmd["phrase"], 1, 1)], (zs["x"], haut, zs["l"], bas - haut),
                             caps["phrase"][cle_sup], PHRASE_CAP_MIN_MM, police, lignes=zs.get("lignes", 1)))
        else:
            out.append(Texte("phrase", [(cmd["phrase"], 1, 1)], (zs["x"], zs["y"], zs["l"], zs["h"]),
                             caps["phrase"][cle_sup], PHRASE_CAP_MIN_MM, police, lignes=zs.get("lignes", 1)))
    return out


def composer_B(t: Toile, cmd: dict) -> list[Texte]:
    sup = cmd["support"]
    if sup == "mug":
        s = G["mug"]["B"]["scene"]
        zs = G["mug"]["zone_sure"]
        y_sol = poser_scene(t, cmd, (s["x"], s["y"], s["l"], s["h"]), s["recadrage"], zs["x"] + zs["l"])
        return textes_B(t, cmd, y_sol)
    elif sup == "boule":
        d = G["boule"]["disque_mm"]
        poser_scene(t, cmd, (-d / 2, -d / 2, d, d), G["boule"]["B"]["scene"]["recadrage"], d / 2)
    else:
        f = G["bois"]["formes"][cmd["forme"]]
        z = f.get("B_zones", {})
        if z.get("a_dessiner") or "scene" not in z:
            raise TacheHumaine(f"gabarit B de la forme {cmd['forme']} pas encore dessiné (CMP - Gabarits de support)")
        s = z["scene"]
        poser_scene(t, cmd, (s["x"], s["y"], s["l"], s["h"]), s["recadrage"], s["x"] + s["l"])
    return textes_B(t, cmd)


# ---------- règles de place validées le 02/11/2026 (étape 5) ----------

def _zone_titre_A(t: Toile, cmd: dict):
    """Zone du titre du gabarit A : ("rect", (x, y, l, h)) ou ("arc", arc, capitale)."""
    if not cmd["surnom"] or titre_A_omis(cmd):
        return None
    sup = cmd["support"]
    if sup == "mug":
        z = G["mug"]["A"]["titre"]
        return "rect", (z["x"], z["y"], z["l"], z["h"])
    if sup == "boule":
        return "arc", G["boule"]["A"]["titre_arc"], G["communs"]["cap_mm"]["titre"]["boule"]
    z = zone_bois(t, cmd, "titre")
    return ("rect", z) if z else None


def _branche_dans_titre(titre, x0: float, x1: float, y_haut: float) -> bool:
    if titre is None:
        return False
    if titre[0] == "rect":
        zx, zy, zl, zh = titre[1]
        return x1 > zx and x0 < zx + zl and y_haut < zy + zh + 0.5
    arc, cap = titre[1], titre[2]
    r_int = arc["rayon"] - cap - 0.5            # bas des lettres de l'arc du haut, avec 0,5 mm de garde
    for x in np.arange(x0, x1 + 0.01, 0.5):
        d = math.hypot(x, y_haut)
        ang = math.degrees(math.atan2(y_haut, x)) % 360
        if r_int <= d <= arc["rayon"] + 1 and arc["deg_debut"] <= ang <= arc["deg_fin"]:
            return True
    return False


def eviter_titre(t: Toile, cmd: dict, cases: list[Case]) -> list[Case]:
    """À Noël, descend toute la grille jusqu'à ce que la branche de la première rangée sorte du titre
    (mug et bois ; sur la boule, signale seulement le conflit)."""
    if cmd["saison"] != "noel" or not cases:
        return cases
    titre = _zone_titre_A(t, cmd)
    ss = G["communs"]["support_symboles"]
    rangee = [c for c in cases if c.rangee == 0]
    s = rangee[0].s
    h_sup = ss["hauteur_fraction"] * s
    largeur = rangee[-1].x + s - rangee[0].x + ss["marge_largeur_symboles"] * s
    cx = (rangee[0].x + rangee[-1].x + s) / 2
    x0, x1 = cx - largeur / 2, cx + largeur / 2
    y_haut = rangee[0].y - ss["branche_decalage_mm"] - h_sup / 2
    if t.support == "boule":
        # sur la boule, descendre la grille la sortirait du cercle : le conflit reste au gabarit.
        # La branche est rognée au disque : seule sa partie visible compte.
        r = G["boule"]["disque_mm"] / 2
        if _branche_dans_titre(titre, max(x0, -r), min(x1, r), y_haut):
            t.alerte("boule, Noël : la branche croise le titre en arc (gabarit à revoir, A VERIFIER)", "dépassement")
        return cases
    dy = 0.0
    while _branche_dans_titre(titre, x0, x1, y_haut + dy) and dy < 25:
        dy += 0.5
    if dy:
        t.info(f"{t.support}, Noël : grille descendue de {dy:.1f} mm pour que la branche sorte du titre")
        cases = [Case(c.x, c.y + dy, c.s, c.rangee) for c in cases]
    return cases


def rogner_au_cercle(t: Toile, textes: list) -> None:
    """Boule : chaque zone de texte rectangulaire est ramenée dans le cercle utile. Les prénoms, posés côte
    à côte, sont réduits à la corde du cercle à leur hauteur ; les autres zones glissent d'abord vers le
    centre sans changer de largeur, puis sont réduites si besoin. Le texte se réduit ensuite tout seul."""
    if t.support != "boule":
        return
    r = G["boule"]["rayon_utile"]
    for tx in textes:
        if not tx.zone:
            continue
        x, y, l, h = tx.zone
        loin = max(abs(y), abs(y + h))
        if loin >= r:
            t.alerte(f"boule : zone de {tx.role} hors du cercle utile (y {y:.1f} à {y + h:.1f} mm)", "dépassement")
            continue
        c = math.sqrt(r * r - loin * loin)
        nx0, nx1 = x, x + l
        if tx.role == "prenom":          # prénoms côte à côte : glisser les ferait se chevaucher
            nx0, nx1 = max(nx0, -c), min(nx1, c)
        elif nx1 > c:                      # d'abord glisser vers le centre, sans changer la largeur
            nx0, nx1 = max(-c, nx0 - (nx1 - c)), c
        if nx0 < -c:
            nx0, nx1 = -c, min(c, nx1 + (-c - nx0))
        nx0, nx1 = max(nx0, -c), min(nx1, c)
        if (nx0, nx1) != (x, x + l):
            tx.zone = (nx0, y, nx1 - nx0, h)
            t.info(f"boule : zone de {tx.role} ramenée dans le cercle utile "
                     f"(x {x:.1f} à {x + l:.1f} mm devient {nx0:.1f} à {nx1:.1f} mm)")


# ---------- texte : mesure par Pillow, rendu par resvg (RCH - Rendu du texte, 02/11/2026) ----------

FONTS = ICI / "fonts"
POLICES = {  # fichier : (famille SVG, graisse, instance de la police variable pour la mesure)
    "CaveatBrush-Regular.ttf": ("Caveat Brush", 400, None),
    "Nunito[wght].ttf": ("Nunito", 600, b"SemiBold"),   # demi-grasse : CMP - Personnalisation par produit
}
MESURE_PX = 1000  # corps de mesure


@lru_cache(maxsize=8)
def _police_mesure(fichier: str) -> ImageFont.FreeTypeFont:
    if not (FONTS / fichier).exists():
        raise RuntimeError(f"police absente : {FONTS / fichier} (voir rendu/fonts/, dépôt google/fonts)")
    if not features.check("raqm"):
        raise RuntimeError("Pillow sans libraqm : les prénoms en Unicode décomposé seraient mal mesurés "
                           "(RCH - Rendu du texte). Installer une version de Pillow avec raqm.")
    f = ImageFont.truetype(str(FONTS / fichier), MESURE_PX, layout_engine=ImageFont.Layout.RAQM)
    instance = POLICES[fichier][2]
    if instance:
        f.set_variation_by_name(instance)
    return f


@lru_cache(maxsize=8)
def capitale_par_corps(fichier: str) -> float:
    """Hauteur du H mesurée sur le glyphe, rapportée au corps (Caveat Brush 0,661 ; Nunito demi-grasse 0,719)."""
    x0, y0, x1, y1 = _police_mesure(fichier).getbbox("H")
    return (y1 - y0) / MESURE_PX


def largeur_mm(fichier: str, texte: str, cap_mm: float) -> float:
    corps_mm = cap_mm / capitale_par_corps(fichier)
    return _police_mesure(fichier).getlength(texte) * corps_mm / MESURE_PX


def largeur_ligne(tx: "Texte", cap: float, morceaux=None) -> float:
    return sum(largeur_mm(tx.police, m[0], cap * m[1]) for m in (morceaux or tx.contenu))


def _couper(texte: str, n: int) -> list[str]:
    """Coupe une phrase en deux lignes à l'espace qui équilibre le mieux les longueurs."""
    mots = texte.split()
    if n <= 1 or len(mots) < 2:
        return [texte]
    meilleur = None
    for i in range(1, len(mots)):
        a, b = " ".join(mots[:i]), " ".join(mots[i:])
        ecart = abs(len(a) - len(b))
        if meilleur is None or ecart < meilleur[0]:
            meilleur = (ecart, [a, b])
    return meilleur[1]


def ajuster(t: "Toile", tx: "Texte") -> tuple[float, list[list]]:
    """Capitale retenue et lignes (listes de morceaux). Réduit par pas de 0,1 mm jusqu'au minimum,
    essaie deux lignes si la zone en prévoit deux, sinon lève TacheHumaine."""
    texte_entier = "".join(m[0] for m in tx.contenu)
    if tx.arc:
        haut = tx.arc["deg_debut"] >= 180
        cap = tx.cap

        def longueur(c):  # longueur utile de l'arc à la ligne de base (rayon intérieur sur l'arc du haut)
            r = tx.arc["rayon"] - (c if haut else 0)
            return math.radians(tx.arc["deg_fin"] - tx.arc["deg_debut"]) * r * 0.96

        while largeur_ligne(tx, cap) > longueur(cap) and cap > tx.cap_min + 1e-9:
            cap = round(cap - 0.1, 2)
        if largeur_ligne(tx, cap) > longueur(cap):
            raise TacheHumaine(f"{tx.role} « {texte_entier} » : ne tient pas sur l'arc même à {tx.cap_min} mm "
                               "de capitale (tâche humaine)")
        if cap < tx.cap:
            t.alerte(f"{tx.role} « {texte_entier} » réduit de {tx.cap} à {cap} mm de capitale", "réduction")
        return cap, [tx.contenu]
    x, y, l, h = tx.zone
    essais = [[tx.contenu]]
    if tx.role == "prenom" and len(tx.contenu) == 2:  # « Léa · juin » trop large : le mois passe dessous
        mois_seul = tx.contenu[1][0].replace(G["communs"]["mois"]["separateur"], "")
        essais.append([[tx.contenu[0]], [(mois_seul, tx.contenu[1][1], tx.contenu[1][2])]])
    if tx.lignes >= 2 and len(tx.contenu) == 1:
        essais.append([[(ligne, 1, 1)] for ligne in _couper(tx.contenu[0][0], 2)])
    for lignes in essais:
        def tient(c):
            return max(largeur_ligne(tx, c, li) for li in lignes) <= l and hauteur_lignes(lignes, c) <= h + 1e-6
        cap = tx.cap
        while not tient(cap) and cap > tx.cap_min + 1e-9:
            cap = round(cap - 0.1, 2)
        if tient(cap):
            if cap < tx.cap:
                t.alerte(f"{tx.role} « {texte_entier} » réduit de {tx.cap} à {cap} mm de capitale", "réduction")
            return cap, lignes
    raise TacheHumaine(f"{tx.role} « {texte_entier} » : dépasse sa zone de {l:.1f} × {h:.1f} mm même à "
                       f"{tx.cap_min} mm de capitale (tâche humaine)")


def _echelle(ligne: list) -> float:
    return max(m[1] for m in ligne)


def hauteur_lignes(lignes: list, cap: float) -> float:
    """Hauteur du bloc : capitale de la première ligne, puis 1,45 capitale par ligne suivante."""
    return cap * _echelle(lignes[0]) + sum(1.45 * cap * _echelle(li) for li in lignes[1:])


def _tspans(t: "Toile", tx: "Texte", cap: float, morceaux: list) -> str:
    out = []
    for texte, echelle, opacite in morceaux:
        corps = t.ppm * cap * echelle / capitale_par_corps(tx.police)
        op = f' fill-opacity="{opacite}"' if opacite < 1 else ""
        out.append(f'<tspan font-size="{corps:.2f}"{op}>{escape(texte)}</tspan>')
    return "".join(out)


def svg_textes(t: "Toile", textes: list, couleur: str) -> str:
    """Tous les textes de la toile dans un seul SVG à la taille du placeholder."""
    defs, corps = [], []
    for i, tx in enumerate(textes):
        cap, lignes = ajuster(t, tx)
        tx.cap_retenue, tx.nb_lignes = cap, len(lignes)
        if tx.zone:  # bas réel du texte, pour le contrôle de dépassement après rendu
            x_, y_, l_, h_ = tx.zone
            haut_bloc = hauteur_lignes(lignes, cap)
            tx.bas = y_ + (haut_bloc if tx.aligne == "haut" else (h_ + haut_bloc) / 2) + 0.3 * cap
        famille, graisse, _ = POLICES[tx.police]
        style = f'font-family="{famille}" font-weight="{graisse}" fill="{couleur}"'
        if tx.arc:
            a = tx.arc
            haut = a["deg_debut"] >= 180   # arc du haut : lettres vers l'extérieur, capitales sous le rayon
            r = t.ppm * (a["rayon"] - (cap if haut else 0))
            cx, cy = t.px(0, 0)
            d0, d1 = (a["deg_debut"], a["deg_fin"]) if haut else (a["deg_fin"], a["deg_debut"])
            p0 = (cx + r * math.cos(math.radians(d0)), cy + r * math.sin(math.radians(d0)))
            p1 = (cx + r * math.cos(math.radians(d1)), cy + r * math.sin(math.radians(d1)))
            sens = 1 if haut else 0          # arc du bas parcouru de gauche à droite : texte à l'endroit
            grand = 1 if abs(d1 - d0) > 180 else 0
            defs.append(f'<path id="arc{i}" d="M {p0[0]:.1f},{p0[1]:.1f} A {r:.1f},{r:.1f} 0 {grand} {sens} '
                        f'{p1[0]:.1f},{p1[1]:.1f}"/>')
            corps.append(f'<text {style}><textPath href="#arc{i}" xlink:href="#arc{i}" startOffset="50%" '
                         f'text-anchor="middle">{_tspans(t, tx, cap, tx.contenu)}</textPath></text>')
            continue
        x, y, l, h = tx.zone
        bloc = hauteur_lignes(lignes, cap)
        base = y + (0 if tx.aligne == "haut" else (h - bloc) / 2) + cap * _echelle(lignes[0])
        for k, li in enumerate(lignes):
            if k:
                base += 1.45 * cap * _echelle(li)
            bx, by = t.px(x + l / 2, base)
            corps.append(f'<text {style} x="{bx}" y="{by}" text-anchor="middle">{_tspans(t, tx, cap, li)}</text>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
            f'width="{t.w_px}" height="{t.h_px}" viewBox="0 0 {t.w_px} {t.h_px}">'
            f'<defs>{"".join(defs)}</defs>{"".join(corps)}</svg>')


def poser_textes(t: "Toile", textes: list, couleur: str) -> None:
    if not textes:
        return
    import resvg_py
    polices = sorted({str(FONTS / tx.police) for tx in textes})
    png = resvg_py.svg_to_bytes(svg_string=svg_textes(t, textes, couleur), font_files=polices,
                                skip_system_fonts=True)
    calque = Image.open(io.BytesIO(bytes(png))).convert("RGBA")
    t.img.alpha_composite(calque)


# ---------- zones de contrôle ----------

def tracer_zones(t: Toile, cmd: dict, cases: list[Case], textes: list[Texte]) -> None:
    """Trace les zones en traits fins : rouge = symboles, bleu = texte, vert = zone sûre."""
    d = ImageDraw.Draw(t.img)
    w = max(1, t.mm(0.25))

    def rect(x, y, l, h, c):
        x0, y0 = t.px(x, y)
        x1, y1 = t.px(x + l, y + h)
        d.rectangle([x0, y0, x1, y1], outline=c, width=w)

    for c in cases:
        rect(c.x, c.y, c.s, c.s, (220, 0, 0, 255))
    for tx in textes:
        if tx.zone:
            rect(*tx.zone, (0, 70, 220, 255))
        elif tx.arc:
            ra = tx.arc["rayon"]
            x0, y0 = t.px(-ra, -ra)
            x1, y1 = t.px(ra, ra)
            d.arc([x0, y0, x1, y1], tx.arc["deg_debut"], tx.arc["deg_fin"], fill=(0, 70, 220, 255), width=w)
    if cmd["support"] == "mug":
        z = G["mug"]["zone_sure"]
        rect(z["x"], z["y"], z["l"], z["h"], (0, 160, 0, 255))
    elif cmd["support"] == "boule":
        r = G["boule"]["rayon_utile"]
        x0, y0 = t.px(-r, -r)
        x1, y1 = t.px(r, r)
        d.ellipse([x0, y0, x1, y1], outline=(0, 160, 0, 255), width=w)
    else:
        f = G["bois"]["formes"][cmd["forme"]]
        for u in (f["utile"].values() if "jambe" in f["utile"] else [f["utile"]]):
            rect(u["x"], u["y"], u["l"], u["h"], (0, 160, 0, 255))


# ---------- contrôles après rendu ----------

def verifier_bois(t: Toile, cmd: dict, cases: list) -> None:
    """Bois, gabarit A : compare le bas réel des prénoms (et des symboles) au bas du rectangle utile."""
    if t.support != "bois" or cmd["gabarit"] != "A" or not cases:
        return
    f = G["bois"]["formes"][cmd["forme"]]
    u = f["utile"]["jambe"] if "jambe" in f["utile"] else f["utile"]
    limite = u["y"] + u["h"]
    bas = max([c.y + c.s for c in cases] + [tx.bas for tx in t.textes if tx.role == "prenom" and tx.bas])
    if bas > limite + 0.5:
        t.alerte(f"bois {cmd['forme']}, N = {len(cases)} : le dessin descend à {bas:.1f} mm, sous le rectangle "
                 f"utile ({limite:.1f} mm)", "dépassement")


def contour_forme(forme: str) -> tuple[list, bool]:
    """Contour de la forme de bois en mm : (points, exact). L'ovale est l'ellipse inscrite dans le fichier ;
    les autres formes sont des polygones estimés à partir du fichier et des rectangles utiles."""
    f = G["bois"]["formes"][forme]
    w, h = f["fichier_mm"]
    if forme == "ovale":
        return [(w / 2 + (w / 2 - 0.5) * math.cos(a), h / 2 + (h / 2 - 0.5) * math.sin(a))
                for a in np.linspace(0, 2 * math.pi, 180)], True
    if forme == "etoile":
        cx, cy, R = w / 2, h / 2 + 2, min(w, h) / 2 - 1
        return [(cx + (R if k % 2 == 0 else 0.42 * R) * math.cos(math.radians(-90 + 36 * k)),
                 cy + (R if k % 2 == 0 else 0.42 * R) * math.sin(math.radians(-90 + 36 * k))) for k in range(10)], False
    if forme == "coeur":
        pts = []
        for a in np.linspace(0, 2 * math.pi, 180):
            x = 16 * math.sin(a) ** 3
            y = -(13 * math.cos(a) - 5 * math.cos(2 * a) - 2 * math.cos(3 * a) - math.cos(4 * a))
            pts.append((x, y))
        xs, ys = [p[0] for p in pts], [p[1] for p in pts]
        kx, ky = (w - 2) / (max(xs) - min(xs)), (h - 2) / (max(ys) - min(ys))
        return [(1 + (x - min(xs)) * kx, 1 + (y - min(ys)) * ky) for x, y in pts], False
    if forme == "cloche":
        return [(w * 0.38, 3), (w * 0.62, 3), (w * 0.75, h * 0.22), (w * 0.80, h * 0.62), (w - 2, h * 0.86),
                (w - 2, h * 0.93), (2, h * 0.93), (2, h * 0.86), (w * 0.20, h * 0.62), (w * 0.25, h * 0.22)], False
    if forme == "sapin":
        c = w / 2
        return [(c, 2), (c + 22, 40), (c + 15, 40), (c + 34, 80), (c + 26, 80), (w - 2, 118), (c + 7, 118),
                (c + 7, h - 2), (c - 7, h - 2), (c - 7, 118), (2, 118), (c - 26, 80), (c - 34, 80), (c - 15, 40),
                (c - 22, 40)], False
    if forme == "chaussette":
        j, p = f["utile"]["jambe"], f["utile"]["pied"]
        return [(j["x"] - 4, 2), (j["x"] + j["l"] + 4, 2), (j["x"] + j["l"] + 4, p["y"] + p["h"] - 6),
                (j["x"] + j["l"] - 4, h - 2), (p["x"] + 6, h - 2), (2, p["y"] + p["h"] - 8), (2, p["y"] + 8),
                (p["x"] + 6, p["y"] - 3), (j["x"] - 4, p["y"] - 4)], False
    return [(0, 0), (w, 0), (w, h), (0, h)], False


def tracer_contour(t: Toile, cmd: dict) -> None:
    """Calque de contrôle : le contour de la forme de bois, en tirets magenta. Jamais imprimé."""
    if t.support != "bois":
        return
    pts, exact = contour_forme(cmd["forme"])
    d = ImageDraw.Draw(t.img)
    xy = [t.px(x, y) for x, y in pts] + [t.px(*pts[0])]
    epais = max(1, t.mm(0.4))
    for i in range(len(xy) - 1):  # tirets
        (x0, y0), (x1, y1) = xy[i], xy[i + 1]
        n = max(1, int(math.hypot(x1 - x0, y1 - y0) / max(2, t.mm(1.5))))
        for k in range(0, n, 2):
            a, b = k / n, min(1, (k + 1) / n)
            d.line([(x0 + (x1 - x0) * a, y0 + (y1 - y0) * a), (x0 + (x1 - x0) * b, y0 + (y1 - y0) * b)],
                   fill=(230, 0, 140, 255), width=epais)
    if not exact:
        d.text(t.px(1.5, 1.5), "contour estimé", fill=(230, 0, 140, 255))


# ---------- rendu ----------

def rendre(commande: dict, zones: bool = False, echelle: float = 1.0,
           contour: bool = False) -> tuple[Image.Image, list[str]]:
    """Le fichier d'impression (ou l'aperçu, avec echelle) et ses alertes typées.
    zones=True et contour=True ajoutent des calques de contrôle, jamais imprimés."""
    cmd = valider(commande)
    t = nouvelle_toile(cmd, echelle)
    if cmd["gabarit"] == "A":
        cases = eviter_titre(t, cmd, grille_A(t, cmd))
        sous = poser_symboles(t, cmd, cases)
        textes = textes_A(t, cmd, cases, sous)
    elif cmd["gabarit"] == "B":
        cases = []
        textes = composer_B(t, cmd)
    else:
        raise TacheHumaine(f"gabarit inconnu : {cmd['gabarit']}")
    rogner_au_cercle(t, textes)
    t.textes = textes
    poser_textes(t, textes, cmd["couleur_texte"])
    verifier_bois(t, cmd, cases)
    if zones:
        tracer_zones(t, cmd, cases, textes)
    if contour:
        tracer_contour(t, cmd)
    if t.support == "boule":  # rien hors du disque
        masque = Image.new("L", t.img.size, 0)
        ImageDraw.Draw(masque).ellipse([0, 0, t.w_px - 1, t.h_px - 1], fill=255)
        t.img.putalpha(Image.fromarray(np.minimum(np.asarray(t.img.getchannel("A")), np.asarray(masque))))
    DERNIERS_TEXTES[:] = t.textes
    DERNIERES_INFOS[:] = t.infos
    return t.img, t.alertes


DERNIERS_TEXTES: list = []  # textes du dernier rendu, pour l'affichage des essais
DERNIERES_INFOS: list = []  # ajustements prévus du dernier rendu (zone ramenée, grille descendue)
SRGB = ImageCms.ImageCmsProfile(ImageCms.createProfile("sRGB")).tobytes()


def enregistrer(img: Image.Image, chemin) -> None:
    """PNG sRGB 300 DPI ; le mug est opaque (fond crème), boule et bois gardent leur alpha."""
    if img.getchannel("A").getextrema() == (255, 255):
        img = img.convert("RGB")
    img.save(chemin, dpi=(DPI, DPI), icc_profile=SRGB)


if __name__ == "__main__" and "--essai" in sys.argv:
    sortie = ICI / "essais"
    sortie.mkdir(exist_ok=True)
    essais = {
        "etape4-mug-A-mamie-3": dict(support="mug", gabarit="A", destinataire="mamie", saison="base", surnom="Mamie",
                                     couleur_texte="#6B4430", phrase="",
                                     prenoms=[{"prenom": "Léa", "symbole": "rose", "mois": "juin"},
                                              {"prenom": "Noé", "symbole": "muguet", "mois": "mai"},
                                              {"prenom": "Maëlle", "symbole": "houx", "mois": "décembre"}]),
        "etape4-boule-A-famille-6": dict(support="boule", gabarit="A", destinataire="famille", saison="noel",
                                         surnom="Famille", couleur_texte="#2E5E4E", phrase="",
                                         prenoms=[{"prenom": p, "symbole": s, "mois": 1} for p, s in
                                                  zip(["Léa", "Noé", "Inès", "Tom", "Zoé", "Jules"],
                                                      ["boule", "etoile", "sapin", "flocon", "coeur", "boule"])]),
        "etape4-mug-A-papy-6-noel": dict(support="mug", gabarit="A", destinataire="papy", saison="noel", surnom="Papy",
                                         couleur_texte="#2B3A67", phrase="Joyeux Noël Papy",
                                         prenoms=[{"prenom": p, "symbole": s, "mois": m} for p, s, m in
                                                  zip(["Léa", "Noé", "Inès", "Tom", "Zoé", "Jules"],
                                                      ["boule", "etoile", "sapin", "flocon", "coeur", "pain-epice"],
                                                      [6, 5, 12, 8, 1, 3])]),
        "etape4-mug-B-maman-2": dict(support="mug", gabarit="B", destinataire="maman", saison="base", surnom="Maman",
                                     couleur_texte="#7B3F61", phrase="Merci pour tous ces goûters",
                                     prenoms=[{"prenom": "Léa"}, {"prenom": "Noé"}]),
        "etape4-boule-B-papa-3": dict(support="boule", gabarit="B", destinataire="papa", saison="noel", surnom="Papa",
                                      couleur_texte="#2B3A67", phrase="Noël 2026",
                                      prenoms=[{"prenom": "Léa"}, {"prenom": "Noé"}, {"prenom": "Inès"}]),
        "etape4-bois-ovale-B-famille-2": dict(support="bois", forme="ovale", gabarit="B", destinataire="famille",
                                              saison="base", surnom="Mamie", couleur_texte="#2E5E4E", phrase="",
                                              prenoms=[{"prenom": "Léa"}, {"prenom": "Noé"}]),
        "etape4-bois-ovale-A-mamie-6": dict(support="bois", forme="ovale", gabarit="A", destinataire="mamie",
                                            saison="base", surnom="Mamie", couleur_texte="#6B4430", phrase="",
                                            prenoms=[{"prenom": p, "symbole": s, "mois": m} for p, s, m in
                                                     zip(["Léa", "Noé", "Inès", "Tom", "Zoé", "Jules"],
                                                         ["rose", "muguet", "houx", "tournesol", "oeillet", "rose"],
                                                         [6, 5, 12, 8, 1, 6])]),
    }
    for nom, cmd in essais.items():
        try:
            img, alertes = rendre(cmd, zones=True)
        except TacheHumaine as e:
            print(f"{nom} : TÂCHE HUMAINE : {e}")
            continue
        enregistrer(img, sortie / f"{nom}.png")
        print(f"{nom}.png : {img.width} × {img.height} px" + "".join(f"\n  alerte : {a}" for a in alertes))
        for tx in DERNIERS_TEXTES:
            print(f"  {tx.role} : " + "".join(m[0] for m in tx.contenu)
                  + f"  (capitale {tx.cap_retenue} mm, {tx.nb_lignes} ligne{'s' if tx.nb_lignes > 1 else ''})")
