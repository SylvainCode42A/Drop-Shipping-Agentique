"""Planches de test NolaPrint — mug, boule en verre, décoration en bois.
Spécification : RCH - Rendu des trois procédés d'impression et planche de test (02-11-2026).
Sortie : PNG sRGB 300 DPI, dimensions exactes des placeholders Printify `front`
(API variants.json, 01/11 et 02/11/2026) : mug 2244 × 945, boule 900 × 900, bois ovale 1085 × 1545.
Échelle : 300 DPI fixes (choix d'Antoine, 02/11/2026) ; la mire mesurera l'échelle réelle.
"""
import math, datetime, os
from PIL import Image, ImageDraw, ImageFont, ImageCms
import numpy as np
import cv2

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("PLANCHE_OUT", HERE)
os.makedirs(OUT, exist_ok=True)
PX = 300 / 25.4
DATE = datetime.date.today().strftime("%d-%m-%Y")
FONTS = os.environ.get("PLANCHE_FONTS", os.path.join(HERE, "fonts"))
CAVEAT, NUNITO = f"{FONTS}/CaveatBrush-Regular.ttf", f"{FONTS}/Nunito.ttf"
CAP = {CAVEAT: 660.5, NUNITO: 712.0}   # hauteur réelle du H, mesurée (RCH polices)
SRGB = ImageCms.ImageCmsProfile(ImageCms.createProfile("sRGB")).tobytes()

def mm(v): return int(round(v * PX))

def font(path, cap_mm, weight=600):
    size = cap_mm * PX * 1000 / CAP[path]
    f = ImageFont.truetype(path, int(round(size)))
    if path == NUNITO:
        f.set_variation_by_axes([weight])
    return f

def hexrgb(h): return tuple(int(h[i:i+2], 16) for i in (1, 3, 5))

PASTELS = ["#F4C2C2", "#FFD8B1", "#FFF1A8", "#BDE8C9", "#BFDDF2", "#D9C8EE", "#EADBC8", "#D9D9D9"]
MOYENNES = ["#C8453C", "#E08A3C", "#D4A537", "#5E9E6E", "#4A7FC1", "#2F4FA8", "#7B5AA6", "#8A5A3B"]
SOUTENUES = ["#D0021B", "#C2185B", "#F57C00", "#FFD400", "#00A651", "#0098D8", "#0033A0", "#000000"]
CHAIR = ["#F6D7C3", "#E8B896", "#C98E6B", "#A0694A", "#6B4430"]
QUASI = ["#FFFFFF", "#FAFAFA", "#F0F0F0"]
GRIS = [(int(255 * (1 - p)),) * 3 for p in (0.1, 0.3, 0.5, 0.7, 0.9)]
BLEU_MOYEN, BLEU_ROI, PECHE, BRUN, ROUGE, VERT = "#4A7FC1", "#2F4FA8", "#FFD8B1", "#8A5A3B", "#C8453C", "#5E9E6E"
BLACK, WHITE = (0, 0, 0, 255), (255, 255, 255, 255)

def save(img, name):
    img.save(f"{OUT}/{name}", dpi=(300, 300), icc_profile=SRGB)
    print(name, img.size)

# ---------- briques ----------
def pastilles(d, x, y, colors, diam, gap=2, label=True, lab_col=BLACK, fsize=1.3):
    """Rangée de pastilles rondes. x, y, diam, gap en mm. Retourne la largeur en mm."""
    f = font(NUNITO, fsize, 500)
    for i, c in enumerate(colors):
        cx = x + i * (diam + gap)
        col = hexrgb(c) if isinstance(c, str) else c
        d.ellipse([mm(cx), mm(y), mm(cx + diam), mm(y + diam)], fill=col + (255,))
        if label:
            txt = c if isinstance(c, str) else f"{int(round(100 - col[0] / 2.55))}%"
            d.text((mm(cx + diam / 2), mm(y + diam + 0.4)), txt.replace("#", ""), font=f, fill=lab_col, anchor="ma")
    return len(colors) * (diam + gap) - gap

def traits(d, x, y, widths, length, color, vertical=False, pitch=2.2, label_col=None):
    """Traits de largeurs données (mm), espacés de pitch mm. Retourne la hauteur (ou largeur) occupée."""
    f = font(NUNITO, 1.3, 500)
    for i, w in enumerate(widths):
        if vertical:
            cx = x + i * pitch
            d.rectangle([mm(cx), mm(y), mm(cx) + max(1, mm(w)), mm(y + length)], fill=color)
        else:
            cy = y + i * pitch
            d.rectangle([mm(x), mm(cy), mm(x + length), mm(cy) + max(1, mm(w))], fill=color)
            if label_col:
                d.text((mm(x + length + 1), mm(cy)), f"{w} mm", font=f, fill=label_col, anchor="lm")
    return len(widths) * pitch

def text_sizes(d, x, y, sizes, path, color, text="Mamie Josette 0123", pitch=1.6):
    """Lignes de texte à hauteurs de capitale données (mm). Retourne la hauteur occupée."""
    cy = y
    for s in sizes:
        f = font(path, s)
        d.text((mm(x), mm(cy)), text, font=f, fill=color, anchor="la")
        asc, desc = f.getmetrics()
        cy += (asc + desc) / PX * 0.85 + pitch
    return cy - y

def gradient(img, box, c1, c2):
    x0, y0, x1, y1 = box
    arr = np.zeros((y1 - y0, x1 - x0, 4), np.uint8)
    for i in range(x1 - x0):
        t = i / max(1, x1 - x0 - 1)
        arr[:, i, :3] = [int(c1[k] + (c2[k] - c1[k]) * t) for k in range(3)]
    arr[:, :, 3] = 255
    img.paste(Image.fromarray(arr), (x0, y0))

def header(d, x, y, name, size=3):
    f = font(NUNITO, size, 700)
    d.text((mm(x), mm(y)), f"{name}  {DATE}  HAUT ^", font=f, fill=BLACK, anchor="la")

def rulers(d, W, H, depth=6):
    """Lignes parallèles à chaque bord, de 1 à depth mm, pour lire la perte au bord."""
    f = font(NUNITO, 1.2, 600)
    for k in range(1, depth + 1):
        p = mm(k)
        col = (0, 0, 0, 255) if k in (3, 6) else (120, 120, 120, 255)
        d.line([(0, p), (W, p)], fill=col, width=2)
        d.line([(0, H - p), (W, H - p)], fill=col, width=2)
        d.line([(p, 0), (p, H)], fill=col, width=2)
        d.line([(W - p, 0), (W - p, H)], fill=col, width=2)
    for k in (3, 6):
        d.text((mm(10), mm(k) + 2), f"{k} mm", font=f, fill=BLACK, anchor="la")
        d.text((mm(k) + 2, mm(20)), f"{k}", font=f, fill=BLACK, anchor="la")

def fleur(img, cx, cy, size):
    """Motif gouache de synthèse : fleur à aplats, petits blancs de 1 à 2 mm entre pétales, cœur, feuilles."""
    d = ImageDraw.Draw(img)
    r = mm(size / 2)
    cxp, cyp = mm(cx), mm(cy)
    # feuilles
    for ang in (200, 340):
        a = math.radians(ang)
        ex, ey = cxp + int(r * 0.75 * math.cos(a)), cyp + int(r * 0.75 * math.sin(a))
        d.ellipse([ex - r * 0.35, ey - r * 0.2, ex + r * 0.35, ey + r * 0.2], fill=hexrgb(VERT) + (255,))
        d.line([(cxp, cyp), (ex, ey)], fill=hexrgb("#3E7A4E") + (255,), width=mm(0.8))
    # pétales séparés par des blancs de 1,5 mm
    gap = mm(1.5)
    for i in range(6):
        a = math.radians(i * 60 - 90)
        px_, py_ = cxp + int(r * 0.55 * math.cos(a)), cyp + int(r * 0.55 * math.sin(a))
        d.ellipse([px_ - r * 0.42, py_ - r * 0.42, px_ + r * 0.42, py_ + r * 0.42], fill=hexrgb("#C8453C") + (255,))
    for i in range(6):   # blancs entre pétales
        a = math.radians(i * 60 - 60)
        d.line([(cxp, cyp), (cxp + int(r * 1.05 * math.cos(a)), cyp + int(r * 1.05 * math.sin(a)))], fill=WHITE, width=gap)
    d.ellipse([cxp - r * 0.3, cyp - r * 0.3, cxp + r * 0.3, cyp + r * 0.3], fill=hexrgb("#D4A537") + (255,))
    # petits blancs de 1 mm dans le cœur
    for i in range(5):
        a = math.radians(i * 72)
        qx, qy = cxp + int(r * 0.18 * math.cos(a)), cyp + int(r * 0.18 * math.sin(a))
        d.ellipse([qx - mm(0.5), qy - mm(0.5), qx + mm(0.5), qy + mm(0.5)], fill=WHITE)

def ombre(img, box, alpha=128):
    """Aplat gris à alpha partiel : témoin de la transparence partielle."""
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(layer).ellipse(box, fill=(60, 60, 60, alpha))
    img.alpha_composite(layer)

def aruco(img, x, y, size_px, idx):
    dic = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
    m = cv2.aruco.generateImageMarker(dic, idx, size_px)
    img.paste(Image.fromarray(m).convert("RGBA"), (x, y))

def damier(img, box, case_mm=5):
    d = ImageDraw.Draw(img)
    x0, y0, x1, y1 = box
    c = mm(case_mm)
    for j, yy in enumerate(range(y0, y1, c)):
        for i, xx in enumerate(range(x0, x1, c)):
            if (i + j) % 2 == 0:
                d.rectangle([xx, yy, min(xx + c, x1) - 1, min(yy + c, y1) - 1], fill=BLACK)


BOIS_W, BOIS_H = 1085, 1545
BOIS_OX = (BOIS_W / PX - 85) / 2                  # 3,4 mm
BOIS_OY = (BOIS_H / PX - 125) / 2                 # 2,9 mm

# ---------- MUG : zone 2244 × 945 px (190 × 80 mm à 300 DPI) ----------
def mug():
    W, H = 2244, 945
    img = Image.new("RGBA", (W, H), WHITE)
    d = ImageDraw.Draw(img)
    rulers(d, W, H)
    d.rectangle([0, mm(8.6), W, mm(11.6)], fill=hexrgb(BLEU_MOYEN) + (255,))  # bande de couture
    header(d, 8, 12.6, "mug-test")
    # --- gauche : traits et texte (x 8 -> 58) ---
    y = 17.5
    widths = [0.2, 0.3, 0.5, 0.7, 1.0]
    h = traits(d, 8, y, widths, 30, BLACK, pitch=1.7, label_col=BLACK); y += h + 0.4
    d.rectangle([mm(8), mm(y), mm(50), mm(y + 8.2)], fill=hexrgb(BLEU_ROI) + (255,))
    traits(d, 10, y + 0.7, widths, 30, WHITE, pitch=1.5); y += 8.8
    y += text_sizes(d, 8, y, [2, 3, 5], CAVEAT, BLACK, pitch=0.2)
    y += text_sizes(d, 8, y, [2, 4], NUNITO, BLACK, pitch=0.2)
    d.rectangle([mm(8), mm(y), mm(58), mm(y + 4.8)], fill=hexrgb(BLEU_ROI) + (255,))
    text_sizes(d, 9, y + 0.35, [3], NUNITO, WHITE); y += 5.3
    d.rectangle([mm(8), mm(y), mm(58), mm(y + 4.8)], fill=hexrgb(PECHE) + (255,))
    text_sizes(d, 9, y + 0.35, [3], CAVEAT, hexrgb(BRUN) + (255,)); y += 4.8
    print("mug : bas de la colonne gauche =", round(y, 1), "mm sur 74 (réglets à partir de 74)")
    # --- centre : nuancier, pastilles de 8 mm (x 62 -> 140) ---
    y = 17.5
    for row in (PASTELS, MOYENNES, SOUTENUES, CHAIR + QUASI):
        pastilles(d, 62, y, row, 8); y += 10.8
    pastilles(d, 62, y, GRIS, 8)
    print("mug : bas du nuancier =", round(y + 8 + 2, 1), "mm")
    # --- droite : dégradés et motif (x 143 -> 183) ---
    gradient(img, (mm(143), mm(17.5), mm(183), mm(22.5)), (0, 0, 0), (255, 255, 255))
    gradient(img, (mm(143), mm(23.5), mm(183), mm(28.5)), hexrgb("#BFDDF2"), hexrgb("#0033A0"))
    d.rectangle([mm(143), mm(17.5), mm(183), mm(28.5)], outline=BLACK, width=1)
    ombre(img, [mm(148), mm(56), mm(178), mm(70)])                              # ombre à 50 % d'alpha
    fleur(img, 163, 50, 34)
    f = font(NUNITO, 1.3, 500)
    d.text((mm(143), mm(71)), "motif ~38 mm, blancs 1-2 mm, ombre alpha 50 %", font=f, fill=BLACK, anchor="la")
    save(img, "mug-test-2244x945.png")

# ---------- BOULE : disque 900 px (76,2 mm) ----------
def boule(variant):
    S = 900
    img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    C = 38.1
    if variant == "B":
        d.ellipse([0, 0, S - 1, S - 1], fill=hexrgb(BLEU_MOYEN) + (255,))
    ink = WHITE if variant == "B" else BLACK
    # cercle de centrage à 3 mm du bord, 0,5 mm
    r = mm(C - 3); d.ellipse([mm(C) - r, mm(C) - r, mm(C) + r, mm(C) + r], outline=ink, width=mm(0.5))
    # 18 pastilles de 6 mm en couronne (r = 31 mm) sur 300°, le haut reste libre pour l'en-tête
    for i, c in enumerate(PASTELS[:6] + MOYENNES[:6] + SOUTENUES[:6]):
        a = math.radians(-50 + i * 280 / 17)
        cx, cy = C + 31 * math.cos(a), C + 31 * math.sin(a)
        d.ellipse([mm(cx - 3), mm(cy - 3), mm(cx + 3), mm(cy + 3)], fill=hexrgb(c) + (255,))
    d.text((mm(C), mm(C - 29)), f"boule-{variant} {DATE} HAUT ^", font=font(NUNITO, 1.4, 700), fill=ink, anchor="mm")
    # 3 tons chair de 6 mm
    pastilles(d, C - 16.5, C - 17, CHAIR[1:4], 6, gap=1.5, label=False)
    if variant == "B":
        text_sizes(d, C - 13, C - 25, [4], NUNITO, WHITE, text="Mamie Josette")   # prénom blanc réservé 4 mm
        d.rectangle([mm(C + 8), mm(C - 18), mm(C + 18), mm(C - 8)], fill=WHITE)   # aplat blanc 10 mm
    # témoins 12 mm : alpha 0 dans un anneau rouge, blanc pur, bleu à 50 % d'alpha
    f = font(NUNITO, 1.1, 500)
    for k, (dx, kind) in enumerate(((-14, "alpha0"), (0, "blanc"), (14, "alpha50"))):
        x0, y0 = mm(C + dx - 6), mm(C - 7)
        box = [x0, y0, x0 + mm(12), y0 + mm(12)]
        if kind == "alpha0":
            d.ellipse([x0 - mm(1.5), y0 - mm(1.5), x0 + mm(13.5), y0 + mm(13.5)], fill=hexrgb(ROUGE) + (255,))
            d.ellipse(box, fill=(0, 0, 0, 0))
        elif kind == "blanc":
            d.ellipse(box, fill=WHITE)
        else:
            layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
            ImageDraw.Draw(layer).ellipse(box, fill=hexrgb("#0033A0") + (128,))
            img.alpha_composite(layer); d = ImageDraw.Draw(img)
        d.text((x0 + mm(6), y0 + mm(12.3)), kind, font=f, fill=ink, anchor="ma")
    # traits 0,2 à 1 mm (longueur 24 mm) et texte 2 et 3 mm
    traits(d, C - 12, C + 7.5, [0.2, 0.3, 0.5, 0.7, 1.0], 24, ink, pitch=1.5)
    text_sizes(d, C - 11, C + 15, [2], CAVEAT, ink, pitch=0.2)
    text_sizes(d, C - 11.5, C + 19, [3], CAVEAT, ink, text="Mamie Josette")
    save(img, f"boule-{variant}-900x900.png")

# ---------- BOIS : zone 1085 × 1545 px (91,9 × 130,8 mm à 300 DPI), pièce ovale 85 × 125 mm centrée ----------
def bois():
    W, H = BOIS_W, BOIS_H
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    ox, oy = BOIS_OX, BOIS_OY                     # décalage de la pièce dans la zone, en mm
    cx = ox + 42.5
    # hors de la pièce (fond perdu supposé) : bleu soutenu ; bord de la pièce : bande verte 3 mm
    d.rectangle([0, 0, W - 1, H - 1], fill=hexrgb("#0033A0") + (255,))
    d.ellipse([mm(ox), mm(oy), mm(ox + 85), mm(oy + 125)], fill=hexrgb("#00A651") + (255,))
    d.ellipse([mm(ox + 3), mm(oy + 3), mm(ox + 82), mm(oy + 122)], fill=(0, 0, 0, 0))
    d.ellipse([mm(ox), mm(oy), mm(ox + 85), mm(oy + 125)], outline=BLACK, width=2)   # contour 85 × 125
    ink = hexrgb(BRUN) + (255,)
    d.text((mm(cx), mm(oy + 8)), f"bois-ovale {DATE} HAUT ^", font=font(NUNITO, 1.4, 700), fill=ink, anchor="ma")
    # 18 pastilles de 7 mm, trois rangées de 6, puis 5 tons chair
    y = oy + 14
    for row in (PASTELS[:6], MOYENNES[:6], SOUTENUES[:6]):
        w = 6 * 7 + 5 * 1.5
        pastilles(d, cx - w / 2, y, row, 7, gap=1.5, lab_col=ink, fsize=1.0); y += 9.5
    w = 5 * 7 + 4 * 1.5
    pastilles(d, cx - w / 2, y, CHAIR, 7, gap=1.5, lab_col=ink, fsize=1.0); y += 10
    # témoins 10 mm : blanc, alpha 0 dans un anneau brun, noir
    for k, (dx, kind) in enumerate(((-13, "blanc"), (0, "alpha0"), (13, "noir"))):
        x0, y0 = mm(cx + dx - 5), mm(y)
        box = [x0, y0, x0 + mm(10), y0 + mm(10)]
        if kind == "alpha0":
            d.ellipse([x0 - mm(1.5), y0 - mm(1.5), x0 + mm(11.5), y0 + mm(11.5)], fill=ink)
            d.ellipse(box, fill=(0, 0, 0, 0))
        else:
            d.ellipse(box, fill=WHITE if kind == "blanc" else BLACK)
        d.text((x0 + mm(5), y0 + mm(10.5)), kind, font=font(NUNITO, 1.0, 500), fill=ink, anchor="ma")
    y += 13
    # gris 10 à 90 % et dégradé ocre
    w = 5 * 5 + 4 * 1.5
    pastilles(d, cx - w / 2, y, GRIS, 5, gap=1.5, lab_col=ink, fsize=1.0); y += 7.5
    gradient(img, (mm(cx - 15), mm(y), mm(cx + 15), mm(y + 4)), hexrgb("#EADBC8"), hexrgb("#8A5A3B")); y += 5.5
    # traits horizontaux et verticaux (sens du fil), puis en réserve dans un aplat vert
    widths = [0.3, 0.5, 0.7, 1.0]
    traits(d, cx - 24, y, widths, 12, BLACK, pitch=2)
    traits(d, cx - 9, y, widths, 7, BLACK, vertical=True, pitch=2)
    d.rectangle([mm(cx + 1), mm(y - 0.5), mm(cx + 24), mm(y + 8)], fill=hexrgb(VERT) + (255,))
    traits(d, cx + 2, y + 0.5, widths, 12, WHITE, pitch=1.8)
    traits(d, cx + 17, y + 0.5, widths, 7, WHITE, vertical=True, pitch=1.4); y += 9.5
    # texte brun sur bois nu, puis blanc réservé sur rouge
    y += text_sizes(d, cx - 16, y, [2, 3], CAVEAT, ink, pitch=0.3) + 0.5
    d.rectangle([mm(cx - 21), mm(y), mm(cx + 21), mm(y + 6)], fill=hexrgb(ROUGE) + (255,))
    text_sizes(d, cx - 20, y + 1, [3.2], NUNITO, WHITE, text="Mamie Josette 0123"); y += 7
    # aplat moyen 28 × 9 mm pour voir le grain
    d.rectangle([mm(cx - 14), mm(y), mm(cx + 14), mm(y + 9)], fill=hexrgb("#4A7FC1") + (255,))
    d.text((mm(cx), mm(y + 9.3)), "aplat : grain", font=font(NUNITO, 1.0, 500), fill=ink, anchor="ma")
    print("bois : dernier y =", round(y + 11 - oy, 1), "mm sur 125 dans la pièce")
    save(img, "bois-ovale-1085x1545.png")

# ---------- MIRES (calibration des mockups) ----------
def mires():
    # mug
    W, H = 2244, 945
    img = Image.new("RGBA", (W, H), WHITE)
    damier(img, (0, 0, W, H))
    s = mm(15)
    for k, (x, y) in enumerate(((mm(2), mm(2)), (W - s - mm(2), mm(2)), (mm(2), H - s - mm(2)), (W - s - mm(2), H - s - mm(2)))):
        ImageDraw.Draw(img).rectangle([x - mm(1), y - mm(1), x + s + mm(1), y + s + mm(1)], fill=WHITE)
        aruco(img, x, y, s, k)
    d = ImageDraw.Draw(img)
    d.rectangle([mm(68), mm(31), mm(122), mm(49)], fill=WHITE)
    d.text((mm(95), mm(40)), "HAUT ^   anse >", font=font(NUNITO, 4, 800), fill=BLACK, anchor="mm")
    save(img, "mire-mug-2244x945.png")
    # boule
    S = 900
    img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    mask = Image.new("L", (S, S), 0); ImageDraw.Draw(mask).ellipse([0, 0, S - 1, S - 1], fill=255)
    tmp = Image.new("RGBA", (S, S), WHITE); damier(tmp, (0, 0, S, S))
    img.paste(tmp, (0, 0), mask)
    s = mm(12)
    for k, (x, y) in enumerate(((mm(12), mm(12)), (S - s - mm(12), mm(12)), (mm(12), S - s - mm(12)), (S - s - mm(12), S - s - mm(12)))):
        ImageDraw.Draw(img).rectangle([x - mm(1), y - mm(1), x + s + mm(1), y + s + mm(1)], fill=WHITE)
        aruco(img, x, y, s, k)
    d = ImageDraw.Draw(img)
    d.rectangle([mm(28), mm(33), mm(48), mm(43)], fill=WHITE)
    d.text((mm(38.1), mm(38)), "HAUT ^", font=font(NUNITO, 3.5, 800), fill=BLACK, anchor="mm")
    save(img, "mire-boule-900x900.png")
    # bois ovale : damier sur toute la zone (fond perdu compris), contour de la pièce en rouge
    W, H = BOIS_W, BOIS_H
    ox, oy = BOIS_OX, BOIS_OY
    img = Image.new("RGBA", (W, H), WHITE)
    damier(img, (0, 0, W, H))
    ImageDraw.Draw(img).ellipse([mm(ox), mm(oy), mm(ox + 85), mm(oy + 125)], outline=hexrgb(ROUGE) + (255,), width=mm(0.5))
    s = mm(12)
    pw, ph = mm(ox + 85), mm(oy + 125)
    for k, (x, y) in enumerate(((mm(ox + 14), mm(oy + 22)), (pw - s - mm(14), mm(oy + 22)), (mm(ox + 14), ph - s - mm(22)), (pw - s - mm(14), ph - s - mm(22)))):
        ImageDraw.Draw(img).rectangle([x - mm(1), y - mm(1), x + s + mm(1), y + s + mm(1)], fill=WHITE)
        aruco(img, x, y, s, k)
    d = ImageDraw.Draw(img)
    d.rectangle([mm(ox + 32), mm(oy + 57), mm(ox + 53), mm(oy + 67)], fill=WHITE)
    d.text((mm(ox + 42.5), mm(oy + 62)), "HAUT ^", font=font(NUNITO, 3.5, 800), fill=BLACK, anchor="mm")
    save(img, "mire-bois-ovale-1085x1545.png")

if __name__ == "__main__":
    mug(); boule("A"); boule("B"); bois(); mires()
