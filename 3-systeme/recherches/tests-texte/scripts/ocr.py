from render import *
import pytesseract, unicodedata, json, sys
from unidecode import unidecode
NAMES6=["Léa","Inès","Noé","Maëlle","Jean-François","Œuvre"]
EXT=["Zoé","Anaïs","Hélène","Gaëtan","Joël","Chloé","Céline","Loïc","François","Jérôme","Ève","Élodie","Noël","Maïwenn","Benoît","Thaïs","Raphaël","Cécile","Jérémie","Aimée"]
ALL=NAMES6+EXT
ACC=set("éèêëàâäçîïôöûùüÿœŒæÆÉÈÊËÀÂÄÇÎÏÔÖÛÙÜŸ")
def norm(s): return unicodedata.normalize("NFC",s.strip())
def ocr(im,psm,tessdir=None):
    cfg=f"--oem 1 --psm {psm}"+(f" --tessdata-dir {tessdir}" if tessdir else "")
    return norm(pytesseract.image_to_string(im.convert("L"),lang="fra",config=cfg))
def accent_ok(ref,got):
    # chaque lettre accentuée de ref présente à la même position (alignement simple par difflib)
    import difflib
    sm=difflib.SequenceMatcher(None,ref,got); ok=0; tot=0
    m={}
    for a,b,n in sm.get_matching_blocks():
        for k in range(n): m[a+k]=True
    for i,c in enumerate(ref):
        if c in ACC: tot+=1; ok+= bool(m.get(i))
    return ok,tot
if __name__=="__main__":
  pass
CONF={"fra_psm7":(7,None),"fra_psm8":(8,None),"best_psm7":(7,"/home/claude/tt/tessbest")}
if __name__=='__main__':
    rows=[]
    for n,(p,fam) in F.items():
        for mm in (3,8):
            s=size_for(p,mm)
            for nm in ALL:
                im=pil_line(p,s,nm)
                for ck,(psm,td) in CONF.items():
                    got=ocr(im,psm,td); ok,tot=accent_ok(nm,got)
                    rows.append(dict(font=n,mm=mm,conf=ck,ref=nm,got=got,exact=got==nm,noacc=unidecode(got).lower()==unidecode(nm).lower(),acc_ok=ok,acc_tot=tot,six=nm in NAMES6))
    json.dump(rows,open("out/ocr/tesseract.json","w"),ensure_ascii=False,indent=0)
    print(len(rows))
