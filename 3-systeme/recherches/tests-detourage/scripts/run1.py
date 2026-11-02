import numpy as np,cv2,time
from pipe import *; from metr import *
img=cv2.imread('src_1024.png'); bg=bg_color(img)
seg={m:cv2.imread(f'10_alpha_{m}.png',0)/255. for m in ['u2net','isnet-general-use']}
C={'u2net':seg['u2net'],'isnet':seg['isnet-general-use'],'cle-lab':key_alpha(img,bg=bg)}
t=time.time(); C['fusion']=fuse(img,seg['isnet-general-use'],bg=bg); print('t fusion %.2fs'%(time.time()-t))
for k,a in C.items():
    print(k,'brut',fmt(metrics(img,a,1024)))
    t=time.time(); fg,ac=clean(img,a); dt=time.time()-t
    print(k,'nettoye (%.1fs)'%dt,fmt(metrics(fg,ac,1024)))
    cv2.imwrite(f'20_{k}_brut.png',np.dstack([img,(a*255).astype(np.uint8)]))
    cv2.imwrite(f'21_{k}_nettoye.png',np.dstack([fg,(ac*255).round().astype(np.uint8)]))
a=C['fusion']
for name,kw in [('seuil seul',dict(open_=False,min_area=0,hole_area=0,decontam=False)),
                ('decontam seule',dict(lo=0,hi=1,open_=False,min_area=0,hole_area=0)),
                ('complet+erosion1',dict(erode=1)),('complet+erosion2',dict(erode=2))]:
    fg,ac=clean(img,a,**kw); print('fusion',name,fmt(metrics(fg,ac,1024)))
