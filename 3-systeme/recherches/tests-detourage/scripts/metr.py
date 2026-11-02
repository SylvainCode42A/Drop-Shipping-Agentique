import numpy as np,cv2
from key import lab
BG={'blanc':(255,255,255),'bois':(95,150,200),'bleu':(160,80,30)}
def comp(fg,a,c): return (fg.astype(np.float32)*a[...,None]+np.array(c,np.float32)*(1-a[...,None])).clip(0,255).astype(np.uint8)
def load_gt(n):
    return cv2.imread(f'gt_alpha_{n}.png',0)/255., cv2.imread(f'gt_fg_{n}.png'), np.load(f'masks_{n}.npy')
def metrics(fg,a,n,box=None):
    gt,gfg,ms=load_gt(n)
    if box:
        x0,y0,w=[int(v*n/1024) for v in box]; sl=(slice(y0,y0+w),slice(x0,x0+w)); gt,gfg=gt[sl],gfg[sl]; ms=[q[sl] for q in ms]
    spl,hole,dry,hl=ms; r={}
    band=cv2.dilate(((gt>0.02)&(gt<0.98)).astype(np.uint8),np.ones((7,7)))>0
    r['MAE%']=np.abs(a-gt).mean()*100
    r['IoU']=((a>.5)&(gt>.5)).sum()/((a>.5)|(gt>.5)).sum()
    nn,l=cv2.connectedComponents(spl.astype(np.uint8))
    r['eclab']=f"{sum((a[l==i]>.5).mean()>.5 for i in range(1,nn))}/{nn-1}"
    n2,_=cv2.connectedComponents(((a>.5)&(cv2.dilate((gt>.02).astype(np.uint8),np.ones((5,5)))==0)).astype(np.uint8)); r['ilots']=n2-1
    f=lambda x: float(x.mean()) if x.size else float('nan')
    r['trou']=f(a[hole&(gt<.02)]); r['seche']=f(a[dry&(gt<.02)]); r['reflet']=f(a[hl])
    for k,c in BG.items():
        r['dE_'+k]=np.linalg.norm(lab(comp(fg,a,c))-lab(comp(gfg,gt,c)),axis=2)[band].mean()
    return r
def fmt(r): return {k:(round(float(v),3) if not isinstance(v,str) else v) for k,v in r.items()}
