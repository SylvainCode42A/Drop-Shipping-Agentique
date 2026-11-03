"""Quatorze rendus de contrôle du module de rendu et leur planche contact (étape 5).

Usage, depuis production/rendu/ :
    python exemples.py              # fichiers d'impression et planche
    python exemples.py --contour    # planche seule, avec le contour des formes de bois (calque de contrôle)
Sorties : exemples/<nom>.png (fichiers d'impression, 300 DPI), exemples/planche-exemples.png et
exemples/planche-exemples-contour.png. Les alertes sont typées : réduction, omission, dépassement, autre.
Les boules et les décorations en bois portent la déclinaison de Noël (décision 15) : ornements,
branche, calque d'hiver. Le mug Mamie reste en base (fleurs, sol).
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from rendu import ICI, TacheHumaine, enregistrer, rendre

SORTIE = ICI / "exemples"


def p(prenom, symbole=None, mois=None):
    return {"prenom": prenom, "symbole": symbole, "mois": mois}


EXEMPLES = {
    "01-mug-A-mamie-3": dict(
        support="mug", gabarit="A", destinataire="mamie", saison="base", surnom="Mamie", couleur_texte="#6B4430",
        phrase="Avec tout notre amour",
        prenoms=[p("Léa", "rose", "juin"), p("Noé", "muguet", "mai"), p("Maëlle", "houx", "décembre")]),
    "02-mug-A-papy-6-noel": dict(
        support="mug", gabarit="A", destinataire="papy", saison="noel", surnom="Papy", couleur_texte="#2B3A67",
        phrase="Joyeux Noël Papy",
        prenoms=[p("Léa", "boule", 6), p("Noé", "etoile", 5), p("Inès", "sapin", 12), p("Tom", "flocon", 8),
                 p("Zoé", "coeur", 1), p("Jules", "pain-epice", 3)]),
    "03-mug-B-maman-2": dict(
        support="mug", gabarit="B", destinataire="maman", saison="base", surnom="Maman", couleur_texte="#7B3F61",
        phrase="Merci pour tous ces goûters", prenoms=[p("Léa"), p("Noé")]),
    "04-boule-A-couple-3": dict(
        support="boule", gabarit="A", destinataire="couple", saison="noel", surnom="Papy et Mamie",
        couleur_texte="#7A1E2E", phrase="Noël 2026",
        prenoms=[p("Léa", "etoile", 6), p("Noé", "boule", 5), p("Maëlle", "flocon", 12)]),
    "05-boule-A-famille-6": dict(
        support="boule", gabarit="A", destinataire="famille", saison="noel", surnom="Famille",
        couleur_texte="#2E5E4E", phrase="",
        prenoms=[p("Léa", "boule", 1), p("Noé", "etoile", 2), p("Inès", "sapin", 3), p("Tom", "flocon", 4),
                 p("Zoé", "coeur", 5), p("Jules", "pain-epice", 6)]),
    "06-boule-B-papa-3": dict(
        support="boule", gabarit="B", destinataire="papa", saison="noel", surnom="Papa", couleur_texte="#2B3A67",
        phrase="Noël 2026", prenoms=[p("Léa"), p("Noé"), p("Inès")]),
    "07-bois-ovale-A-mamie-6": dict(
        support="bois", forme="ovale", gabarit="A", destinataire="mamie", saison="noel", surnom="Mamie",
        couleur_texte="#6B4430", phrase="",
        prenoms=[p("Léa", "boule", 6), p("Noé", "etoile", 5), p("Inès", "sapin", 12), p("Tom", "flocon", 8),
                 p("Zoé", "coeur", 1), p("Jules", "pain-epice", 3)]),
    "08-bois-ovale-B-famille-2": dict(
        support="bois", forme="ovale", gabarit="B", destinataire="famille", saison="noel", surnom="Famille",
        couleur_texte="#2E5E4E", phrase="", prenoms=[p("Léa"), p("Noé")]),
    "09-bois-etoile-A-papy-4": dict(
        support="bois", forme="etoile", gabarit="A", destinataire="papy", saison="noel", surnom="Papy",
        couleur_texte="#2B3A67", phrase="",
        prenoms=[p("Léa", "boule", 6), p("Noé", "etoile", 5), p("Inès", "sapin", 12), p("Tom", "flocon", 8)]),
    "10-bois-coeur-A-maman-1": dict(
        support="bois", forme="coeur", gabarit="A", destinataire="maman", saison="noel", surnom="Maman",
        couleur_texte="#7B3F61", phrase="Je t'aime", prenoms=[p("Léa", "coeur", 6)]),
    "11-bois-cloche-A-couple-2": dict(
        support="bois", forme="cloche", gabarit="A", destinataire="couple", saison="noel", surnom="Papy et Mamie",
        couleur_texte="#7A1E2E", phrase="", prenoms=[p("Léa", "boule", 6), p("Noé", "sapin", 5)]),
    "12-bois-chaussette-A-mamie-5": dict(
        support="bois", forme="chaussette", gabarit="A", destinataire="mamie", saison="noel", surnom="Mamie",
        couleur_texte="#6B4430", phrase="Joyeux Noël",
        prenoms=[p("Léa", "boule", 6), p("Noé", "etoile", 5), p("Inès", "sapin", 12), p("Tom", "flocon", 8),
                 p("Zoé", "pain-epice", 1)]),
    "13-bois-ovale-A-mamie-3": dict(
        support="bois", forme="ovale", gabarit="A", destinataire="mamie", saison="base", surnom="Mamie",
        couleur_texte="#6B4430", phrase="",
        prenoms=[p("Léa", "rose", "juin"), p("Noé", "muguet", "mai"), p("Maëlle", "houx", "décembre")]),
    "14-boule-A-mamie-3": dict(
        support="boule", gabarit="A", destinataire="mamie", saison="base", surnom="Mamie", couleur_texte="#6B4430",
        phrase="",
        prenoms=[p("Léa", "rose", "juin"), p("Noé", "muguet", "mai"), p("Maëlle", "houx", "décembre")]),
}


def planche(images: dict, chemin: Path, case: int = 640, colonnes: int = 4) -> None:
    """Vignettes sur fond gris clair (la transparence se voit), nom et état sous chacune."""
    lignes = (len(images) + colonnes - 1) // colonnes
    out = Image.new("RGB", (colonnes * case, lignes * (case + 40)), "white")
    d = ImageDraw.Draw(out)
    try:
        police = ImageFont.truetype(str(ICI / "fonts" / "Nunito[wght].ttf"), 20)
    except OSError:
        police = ImageFont.load_default()
    for i, (nom, (im, etat)) in enumerate(images.items()):
        x, y = (i % colonnes) * case, (i // colonnes) * (case + 40)
        fond = Image.new("RGBA", (case - 16, case - 16), (215, 215, 215, 255))
        if im is not None:
            v = im.copy()
            v.thumbnail((case - 16, case - 16), Image.LANCZOS)
            fond.alpha_composite(v, ((fond.width - v.width) // 2, (fond.height - v.height) // 2))
        out.paste(fond.convert("RGB"), (x + 8, y + 8))
        d.text((x + 10, y + case - 4), f"{nom} {etat}", fill="black", font=police)
    out.save(chemin)


if __name__ == "__main__":
    SORTIE.mkdir(exist_ok=True)
    contour = "--contour" in sys.argv
    rendus = {}
    for nom, cmd in EXEMPLES.items():
        try:
            img, alertes = rendre(cmd, contour=contour)
        except TacheHumaine as e:
            print(f"{nom} : TÂCHE HUMAINE : {e}")
            rendus[nom] = (None, "(tâche humaine)")
            continue
        if not contour:  # le calque de contour n'entre jamais dans un fichier d'impression
            enregistrer(img, SORTIE / f"{nom}.png")
        rendus[nom] = (img, f"({len(alertes)} alerte{'s' if len(alertes) > 1 else ''})" if alertes else "")
        print(f"{nom} : {img.width} × {img.height} px" + "".join(f"\n  {a}" for a in alertes))
    nom_planche = "planche-exemples-contour.png" if contour else "planche-exemples.png"
    planche(rendus, SORTIE / nom_planche)
    print("planche :", SORTIE / nom_planche)
    sys.exit(0)
