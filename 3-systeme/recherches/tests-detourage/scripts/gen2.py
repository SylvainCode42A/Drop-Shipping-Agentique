import numpy as np, cv2
rng=np.random.default_rng(7); N=4096; s=N/1024
yy,xx=np.mgrid[0:N,0:N].astype(np.float32); xx/=s; yy/=s   # coordonnées en unités 1024
def noise(scale,amp,seed):
    r=np.random.default_rng(seed); n=r.normal(0,1,(int(1024//scale)+2,)*2).astype(np.float32)
    return cv2.resize(n,(N,N),interpolation=cv2.INTER_CUBIC)*amp
d_apple=np.sqrt(((xx-500)/300)**2+((yy-560)/280)**2)
d_leaf=np.sqrt((((xx-640)*0.8+(yy-230)*0.6)/150)**2+(((xx-640)*-0.6+(yy-230)*0.8)/60)**2)
edge=noise(24,0.035,1)+noise(6,0.02,2)+noise(1.5,0.008,3)
apple=(d_apple+edge)<1; leaf=(d_leaf+edge*1.5)<1
stri=(noise(3,1,4)+np.sin(yy/3.0)*0.8)>0.6
dry=(d_apple>0.88)&(xx>650)&stri; apple&=~dry
hole=np.sqrt(((xx-380)/40)**2+((yy-470)/28)**2)<1; apple&=~hole
spl=np.zeros((N,N),bool)
for _ in range(25):
    cx,cy=rng.integers(150,900,2); r=rng.integers(2,9)
    if np.hypot(cx-500,cy-560)<450 and np.hypot(cx-500,cy-560)>310 and not leaf[int(cy*s),int(cx*s)]:
        spl|=np.hypot(xx-cx,yy-cy)<r
bg=np.array([218,232,238],np.float32)  # BGR, fond pâle bleuté
img=np.ones((N,N,3),np.float32)*bg+noise(0.5,2.0,5)[...,None]
tex=noise(4,14,6)+noise(16,10,7)+noise(1,6,8)+np.sin((xx+yy)/5)*4
red=np.stack([40+tex*.5,45+tex,200+tex],-1); grn=np.stack([60+tex*.6,150+tex,70+tex*.5],-1)
hl=(np.sqrt(((xx-600)/60)**2+((yy-450)/40)**2)<1)&apple
ms=[cv2.GaussianBlur(m.astype(np.float32),(0,0),0.6*s) for m in (apple,leaf,spl)]
fg=np.zeros((N,N,3),np.float32)
for m,c in zip(ms,[red,grn,red]):
    img=img*(1-m[...,None])+c*m[...,None]; fg=np.where(m[...,None]>0,c,fg)
hlm=cv2.GaussianBlur(hl.astype(np.float32),(0,0),6*s)[...,None]
cream=np.array([225,235,245],np.float32)
img=img*(1-hlm)+cream*hlm; fg=fg*(1-hlm)+cream*hlm
gt=np.clip(np.maximum.reduce(ms),0,1)
for n in (4096,2048,1024):
    f=lambda a: cv2.resize(a,(n,n),interpolation=cv2.INTER_AREA)
    cv2.imwrite(f'src_{n}.png',np.clip(f(img),0,255).astype(np.uint8))
    cv2.imwrite(f'gt_alpha_{n}.png',(f(gt)*255).astype(np.uint8))
    cv2.imwrite(f'gt_fg_{n}.png',np.clip(f(fg),0,255).astype(np.uint8))
    np.save(f'masks_{n}.npy',np.stack([cv2.resize(m.astype(np.uint8),(n,n),interpolation=cv2.INTER_NEAREST)>0 for m in (spl,hole,dry,hl)]))
print('ok', int(cv2.connectedComponents(spl.astype(np.uint8))[0]-1),'eclaboussures')
