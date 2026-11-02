from render import *
import numpy as np
W,H=round(mm2px(251)),round(mm2px(95))   # tour estimé π×80 mm, hauteur 95 mm (CMP, estimé)
M=round(mm2px(6)); ANSE=round(mm2px(30))  # marges et bande d'anse, valeurs de test
panel=( (ANSE//2+M, M, W//2-ANSE//2-M, H-M) )   # panneau gauche
TESTS=[["Léa"],["Léa","Inès","Noé"],["Léa","Inès","Noé","Maëlle","Jean-François","Œuvre"],
       ["Marie-Bérénice","Jean-Christophe","Anne-Gaëlle","François-Xavier","Héloïse","Zoé"]]
def lines_for(names):  # gabarit simple : 1 à 3 par ligne
    k=3 if len(names)>4 else 2 if len(names)>1 else 1
    return [", ".join(names[i:i+k]) for i in range(0,len(names),k)]
def fit(p,lines,bw,bh,lh=1.2):
    for s in range(400,10,-1):
        f=ImageFont.truetype(p,s,layout_engine=ImageFont.Layout.RAQM)
        w=max(f.getlength(l,features=["kern","liga"]) for l in lines)
        asc,desc=f.getmetrics(); h=s*lh*(len(lines)-1)+asc+desc
        if w<=bw and h<=bh: return s
def svg_multi(fam,s,lines,box,lh=1.2,color="#1B4D3E"):
    x0,y0,x1,y1=box; cx=(x0+x1)/2; bh=y1-y0
    asc=s*0.96; tot=s*lh*(len(lines)-1)
    y=y0+(bh-tot)/2 + s*0.3
    spans="".join(f'<tspan x="{cx}" dy="{0 if i==0 else s*lh}">{escape(l)}</tspan>' for i,l in enumerate(lines))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}"><rect width="100%" height="100%" fill="white"/>'
            f'<rect x="{x0}" y="{y0}" width="{x1-x0}" height="{y1-y0}" fill="none" stroke="#ddd"/>'
            f'<text y="{y}" font-family="{fam}" font-size="{s}" fill="{color}" text-anchor="middle">{spans}</text></svg>')
res=[]
for n,(p,fam) in F.items():
    for ti,names in enumerate(TESTS):
        L=lines_for(names); x0,y0,x1,y1=panel
        s=fit(p,L,x1-x0,y1-y0)
        t0=time.perf_counter()
        b=resvg_py.svg_to_bytes(svg_string=svg_multi(fam,s,L,panel),font_files=[p],skip_system_fonts=True)
        dt=time.perf_counter()-t0
        im=Image.open(io.BytesIO(bytes(b))).convert("RGB"); save(im,f"out/mug/{n}_cas{ti}.png")
        a=np.asarray(im.convert("L")); ys,xs=np.where(a<100)
        inside = xs.min()>=x0 and xs.max()<=x1 and ys.min()>=y0 and ys.max()<=y1
        capmm=round(s*capH(p)[0]/1000/11.811,2)
        res.append((n,ti,len(names),s,capmm,inside,int(xs.min()-x0),int(x1-xs.max()),int(ys.min()-y0),int(y1-ys.max()),round(dt*1000)))
print("W,H",W,H,"panneau",panel)
for r in res: print(r)
