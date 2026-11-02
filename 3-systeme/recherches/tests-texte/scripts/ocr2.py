from ocr import *
rows=[]
for n,(p,fam) in F.items():
    c,u=capH(p)
    for cap in (24,32,40,48):
        s=cap*u/c
        for nm in ALL:
            im=pil_line(p,s,nm,pad=20)
            for ck,(psm,td) in (("fra_psm7",(7,None)),("best_psm7",(7,"/home/claude/tt/tessbest"))):
                got=ocr(im,psm,td); ok,tot=accent_ok(nm,got)
                rows.append(dict(font=n,cap=cap,conf=ck,ref=nm,got=got,exact=got==nm,acc_ok=ok,acc_tot=tot))
json.dump(rows,open("out/ocr/tesseract_vignette.json","w"),ensure_ascii=False)
import collections
for ck in ("fra_psm7","best_psm7"):
  for n in F:
    line=[]
    for cap in (24,32,40,48):
        r=[x for x in rows if x["font"]==n and x["cap"]==cap and x["conf"]==ck]
        e=sum(x["exact"] for x in r); ao=sum(x["acc_ok"] for x in r); at=sum(x["acc_tot"] for x in r)
        line.append(f"{cap}px {e}/{len(r)} acc {ao}/{at}")
    print(ck,n," | ".join(line))
print("erreurs best_psm7 32px:")
for x in rows:
    if x["conf"]=="best_psm7" and x["cap"]==32 and not x["exact"]: print(x["font"],repr(x["ref"]),"->",repr(x["got"]))
