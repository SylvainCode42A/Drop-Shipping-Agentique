from render import *
import numpy as np
D=round(mm2px(76.2)); cx=cy=D/2; r=D*0.40
TXT="Joyeux Noël Maëlle et Jean-François"
p,fam=F["CaveatBrush"]; size=round(size_for(p,6))
path=f"M {cx-r},{cy} A {r},{r} 0 0 1 {cx+r},{cy}"
path2=f"M {cx-r*0.86},{cy} A {r*0.86},{r*0.86} 0 0 0 {cx+r*0.86},{cy}"  # bas, lisible
def svg(tr=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{D}" height="{D}" viewBox="0 0 {D} {D}">'
      f'<circle cx="{cx}" cy="{cy}" r="{D/2-2}" fill="#fff7ec" stroke="#ccc"/>'
      f'<defs><path id="h" d="{path}"/><path id="b" d="{path2}"/></defs>'
      f'<text font-family="{fam}" font-size="{size}" fill="#B3122E" {tr}><textPath href="#h" xlink:href="#h" startOffset="50%" text-anchor="middle">{escape(TXT)}</textPath></text>'
      f'<text font-family="{fam}" font-size="{size}" fill="#1B4D3E" dominant-baseline="hanging" {tr}><textPath href="#b" xlink:href="#b" startOffset="50%" text-anchor="middle">Léa · Inès · Noé · Œuvre</textPath></text></svg>')
t0=time.perf_counter(); b=resvg_py.svg_to_bytes(svg_string=svg(),font_files=[p],skip_system_fonts=True); t1=time.perf_counter()
save(Image.open(io.BytesIO(bytes(b))).convert("RGBA"),"out/arc/arc_resvg.png")
b2=cairosvg.svg2png(bytestring=svg('text-rendering="geometricPrecision"').encode()); t2=time.perf_counter()
save(Image.open(io.BytesIO(b2)).convert("RGBA"),"out/arc/arc_cairosvg.png")
# Pillow, glyphe par glyphe
def arc_text(img,text,size,cx,cy,r,fill,center_deg=-90):
    f=ImageFont.truetype(p,size,layout_engine=ImageFont.Layout.RAQM)
    total=f.getlength(text,features=["kern"]); a0=math.radians(center_deg)-(total/r)/2; s=int(size*2.5)
    for i,ch in enumerate(text):
        if ch.isspace(): continue
        mid=f.getlength(text[:i],features=["kern"])+f.getlength(ch)/2; a=a0+mid/r
        tile=Image.new("RGBA",(s,s),(0,0,0,0)); ImageDraw.Draw(tile).text((s/2,s/2),ch,font=f,fill=fill,anchor="ms")
        tile=tile.rotate(-math.degrees(a)-90,resample=Image.Resampling.BICUBIC,center=(s/2,s/2))
        x,y=cx+r*math.cos(a),cy+r*math.sin(a); img.alpha_composite(tile,(round(x-s/2),round(y-s/2)))
t3=time.perf_counter()
im=Image.new("RGBA",(D,D),(0,0,0,0)); ImageDraw.Draw(im).ellipse((2,2,D-2,D-2),fill="#fff7ec",outline="#ccc")
arc_text(im,TXT,size,cx,cy,r,"#B3122E"); t4=time.perf_counter()
save(im,"out/arc/arc_pillow.png")
print("D px",D,"corps px",size,"resvg ms",round((t1-t0)*1000),"cairosvg ms",round((t2-t1)*1000),"pillow ms",round((t4-t3)*1000))
