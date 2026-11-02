import cv2,numpy as np
from pipe import *; from metr import comp
WOOD=(95,150,200); WHITE=(255,255,255); BLUE=(160,80,30)
def rgba(p): x=cv2.imread(p,cv2.IMREAD_UNCHANGED); return x[...,:3],x[...,3]/255.
def lab_(im,t,h=34):
    bar=np.full((h,im.shape[1],3),255,np.uint8)
    cv2.putText(bar,t,(6,h-11),cv2.FONT_HERSHEY_SIMPLEX,0.55,(30,30,30),1,cv2.LINE_AA); return np.vstack([bar,im])
def zoom(im,box,size=300):
    x,y,w=box; return cv2.resize(im[y:y+w,x:x+w],(size,size),interpolation=cv2.INTER_NEAREST)
def grid(rows): 
    W=max(sum(c.shape[1] for c in r)+6*(len(r)-1) for r in rows); out=[]
    for r in rows:
        line=np.hstack(sum([[c,np.full((c.shape[0],6,3),255,np.uint8)] for c in r],[])[:-1])
        line=np.hstack([line,np.full((line.shape[0],W-line.shape[1],3),255,np.uint8)]); out+= [line,np.full((6,W,3),255,np.uint8)]
    return np.vstack(out)
src=cv2.imread('src_1024.png'); Z=(700,520,110)  # bord à brosse sèche + éclaboussure
# 1. détourage
row1=[lab_(cv2.resize(src,(300,300),interpolation=cv2.INTER_AREA),'Source 1024 px'),lab_(zoom(src,Z),'Source, zoom bord sec')]
row2=[];row3=[]
for k,t in [('u2net','rembg u2net'),('isnet','rembg isnet'),('cle-lab','Cle Lab'),('fusion','Fusion isnet + cle')]:
    fg,a=rgba(f'21_{k}_nettoye.png')
    row2.append(lab_(zoom((a*255).astype(np.uint8)[...,None].repeat(3,2),Z),t+' : alpha'))
    row3.append(lab_(zoom(comp(fg,a,WOOD),Z),t+' : sur bois'))
cv2.imwrite('out/01-detourage-comparaison.png',grid([row1,row2,row3]))
# 2. nettoyage
img=src; seg=cv2.imread('10_alpha_isnet-general-use.png',0)/255.; a0=fuse(img,seg)
V=[('Brut',img,a0)]
f,a=clean(img,a0,lo=0,hi=1,open_=False,min_area=0,hole_area=0); V.append(('Decontamination',f,a))
f,a=clean(img,a0,erode=1); V.append(('Complet + erosion 1 px',f,a))
f,a=clean(img,a0,erode=2); V.append(('Complet + erosion 2 px',f,a))
rows=[[lab_(zoom(comp(f,a,c),Z),f'{t} / {n}') for t,f,a in V] for c,n in [(WHITE,'blanc'),(WOOD,'bois'),(BLUE,'bleu')]]
cv2.imwrite('out/02-nettoyage-bords.png',grid(rows))
# 3. agrandissement x4, zone de 64 px source -> 256
gt=cv2.imread('src_4096.png')[380*4:636*4,600*4:856*4]; Zu=(600,360,240)
P=[('Reference 4096',gt)]+[(t,cv2.imread(f'31_x4_{n}.png')) for n,t in [('lanczos','Lanczos'),('x4plus','RealESRGAN x4plus'),('general-dn0.2','general-x4v3 dn 0,2'),('general-dn1.0','general-x4v3 dn 1,0'),('anime6B','anime_6B'),('swinir','SwinIR-M')]]
P=[lab_(zoom(im,Zu,260),t) for t,im in P]
cv2.imwrite('out/03-agrandissement-x4.png',grid([P[:4],P[4:]]))
# 4. ordre, x4, sur bois
gfg=cv2.imread('gt_fg_4096.png')[380*4:636*4,600*4:856*4]; ga=cv2.imread('gt_alpha_4096.png',0)[380*4:636*4,600*4:856*4]/255.
O=[('Reference',gfg,ga)]
for p,t in [('40_x4_lanczos_A_rgb-decontamine_alpha-bicubic.png','A Lanczos, decontamine'),('40_x4_x4plus_A_rgb-decontamine_alpha-bicubic.png','A x4plus, decontamine'),
            ('40_x4_x4plus_A_rgb-original_alpha-bicubic.png','A x4plus, RGB original'),('40_x4_x4plus_A_rgb-decontamine_alpha-x4plus.png','A x4plus, alpha par modele'),
            ('41_x4_x4plus_B.png','B x4plus puis detourage'),('41_x4_lanczos_B.png','B Lanczos puis detourage')]:
    f,a=rgba(p); O.append((t,f,a))
rows=[[lab_(zoom(comp(f,a,WOOD),Zu,260),t) for t,f,a in O[:4]],[lab_(zoom(comp(f,a,WOOD),Zu,260),t) for t,f,a in O[4:]]]
cv2.imwrite('out/04-ordre-operations-x4-bois.png',grid(rows))
# reflet : B perd le reflet
Zr=(0,80,200)
R=[(t,f,a) for t,f,a in O if t in('Reference','A x4plus, decontamine','B x4plus puis detourage')]
cv2.imwrite('out/05-ordre-reflet-perdu.png',grid([[lab_(zoom(comp(f,a,WOOD),(Zr[0]*4,Zr[1]*4,Zr[2]*4) if False else (0,240,560),300),t) for t,f,a in R]]))
cv2.imwrite('out/00-source-1024.png',src)
cv2.imwrite('out/06-resultat-fusion-nettoye.png',cv2.imread('21_fusion_nettoye.png',cv2.IMREAD_UNCHANGED))
