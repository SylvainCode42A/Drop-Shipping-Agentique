import unicodedata, time, io, math, os, json
from PIL import Image, ImageDraw, ImageFont, ImageCms
import resvg_py, cairosvg
from fontTools.ttLib import TTFont
from xml.sax.saxutils import escape
F={"CaveatBrush":("fonts/CaveatBrush-Regular.ttf","Caveat Brush"),"Kalam":("fonts/Kalam-Regular.ttf","Kalam"),
   "PatrickHand":("fonts/PatrickHand-Regular.ttf","Patrick Hand"),"Nunito":("fonts/Nunito-Regular.ttf","Nunito")}
SRGB=ImageCms.ImageCmsProfile(ImageCms.createProfile("sRGB")).tobytes()
def mm2px(mm): return mm*300/25.4
def capH(path):  # vraie hauteur du glyphe H en unités
    t=TTFont(path); g=t.getGlyphSet(); from fontTools.pens.boundsPen import BoundsPen
    bp=BoundsPen(g); g[t.getBestCmap()[ord("H")]].draw(bp); return bp.bounds[3], t["head"].unitsPerEm
def size_for(path,mm):
    c,u=capH(path); return mm2px(mm)*u/c
def save(img,p): img.save(p,dpi=(300,300),icc_profile=SRGB)
def pil_line(path,size,text,pad=30):
    f=ImageFont.truetype(path,round(size),layout_engine=ImageFont.Layout.RAQM)
    l,t,r,b=f.getbbox(text,anchor="ls",features=["kern","liga"])
    W,H=r-l+2*pad, b-t+2*pad
    im=Image.new("RGB",(W,H),"white"); ImageDraw.Draw(im).text((pad-l,pad-t),text,font=f,fill="black",anchor="ls",features=["kern","liga"])
    return im
def svg_line(fam,size,text,W,H,base):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'
            f'<rect width="100%" height="100%" fill="white"/><text x="30" y="{base}" font-family="{fam}" font-size="{size:.2f}" fill="black">{escape(text)}</text></svg>')
def resvg_line(path,fam,size,text,W,H,base):
    b=resvg_py.svg_to_bytes(svg_string=svg_line(fam,size,text,W,H,base),font_files=[path],skip_system_fonts=True)
    return Image.open(io.BytesIO(bytes(b))).convert("RGB")
def cairo_line(fam,size,text,W,H,base):
    b=cairosvg.svg2png(bytestring=svg_line(fam,size,text,W,H,base).encode())
    return Image.open(io.BytesIO(b)).convert("RGB")
