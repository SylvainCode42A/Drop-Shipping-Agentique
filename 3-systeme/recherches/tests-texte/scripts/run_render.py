from render import *
import numpy as np
NAMES=["Léa","Inès","Noé","Maëlle","Jean-François","Œuvre"]
LINE=", ".join(NAMES)
stats=[]
for n,(p,fam) in F.items():
    for mm in (3,8):
        s=size_for(p,mm)
        # ligne complète, Pillow, pour le vault
        im=pil_line(p,s,LINE); save(im,f"out/line/{n}_{mm}mm_pillow.png")
        # même ligne en resvg et cairosvg, même canevas
        f=ImageFont.truetype(p,round(s),layout_engine=ImageFont.Layout.RAQM)
        l,t,r,b=f.getbbox(LINE,anchor="ls"); W,H=im.size; base=30-t
        for eng,fn in (("resvg",lambda:resvg_line(p,fam,round(s),LINE,W+200,H,base)),("cairosvg",lambda:cairo_line(fam,round(s),LINE,W+200,H,base))):
            t0=time.perf_counter(); im2=fn(); dt=time.perf_counter()-t0
            save(im2,f"out/line/{n}_{mm}mm_{eng}.png")
            a=np.asarray(im2.convert("L")); ink=np.where(a<128)
            stats.append((n,mm,eng,int(ink[1].max()-ink[1].min()),len(np.unique(a)),round(dt*1000,1)))
        a=np.asarray(im.convert("L")); ink=np.where(a<128)
        stats.append((n,mm,"pillow",int(ink[1].max()-ink[1].min()),len(np.unique(a)),None))
        for i,nm in enumerate(NAMES):
            for eng in ("pillow","resvg","cairosvg"):
                if eng=="pillow": x=pil_line(p,s,nm)
                else:
                    ff=ImageFont.truetype(p,round(s),layout_engine=ImageFont.Layout.RAQM); l,t,r,b=ff.getbbox(nm,anchor="ls")
                    w=r-l+60; h=b-t+60
                    x=(resvg_line if eng=="resvg" else (lambda P,Fa,S,T,W_,H_,B: cairo_line(Fa,S,T,W_,H_,B)))(p,fam,round(s),nm,w+40,h,30-t)
                save(x,f"out/names/{n}_{mm}mm_{eng}_{i}.png")
for r in stats: print(r)
