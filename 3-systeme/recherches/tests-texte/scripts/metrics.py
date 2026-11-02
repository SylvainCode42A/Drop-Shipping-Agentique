from fontTools.ttLib import TTFont
F={"CaveatBrush":"fonts/CaveatBrush-Regular.ttf","Kalam":"fonts/Kalam-Regular.ttf","PatrickHand":"fonts/PatrickHand-Regular.ttf","Nunito":"fonts/Nunito-VF.ttf"}
REQ="éèêëàâäçîïôöûùüÿœŒæÆÉÈÊËÀÂÄÇÎÏÔÖÛÙÜŸ-’'"
for n,p in F.items():
    t=TTFont(p); cm=t.getBestCmap(); upm=t["head"].unitsPerEm; os2=t["OS/2"]
    miss=[c for c in REQ if ord(c) not in cm]
    print(n, "UPM",upm,"cap",getattr(os2,"sCapHeight",None),"x",getattr(os2,"sxHeight",None),"asc",t["hhea"].ascent,"desc",t["hhea"].descent,"manquants:","".join(miss) or "aucun", "fvar" in t)
