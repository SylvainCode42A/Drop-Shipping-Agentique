import numpy as np,cv2
from pymatting import estimate_foreground_ml
from key import *
def disk(r): return cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(2*r+1,)*2)
def fuse(img,seg,t0=10,t1=60,t_core=None,zone_px=25,far_px=200,min_area=8,bg=None,k=None):
    """seg : masque du réseau (0..1), à la taille de img. Tailles en pixels de l'image 1024 ; mises à l'échelle."""
    k=img.shape[0]/1024 if k is None else k; d=dist(img,bg)
    if t_core is None: t_core=max(1.5,1.7*np.percentile(np.concatenate([d[:8].ravel(),d[-8:].ravel()]),99))
    a=np.clip((d-t0)/(t1-t0),0,1)
    s=(seg>0.5).astype(np.uint8)
    zone=cv2.dilate(s,disk(int(zone_px*k)))>0
    a=np.where((seg>0.9)&(d>t_core),1.0,a)        # cœur sûr : sauve les reflets proches du fond
    out=np.where(zone,a,0.0)
    far=cv2.dilate(s,disk(int(far_px*k)))>0
    n,l,st,_=cv2.connectedComponentsWithStats(((a>0.5)&~zone&far).astype(np.uint8))
    for i in range(1,n):
        if st[i,4]>=min_area*k*k:
            m=cv2.dilate((l==i).astype(np.uint8),np.ones((5,5)))>0; out[m]=a[m]
    return out
def clean(img,a,lo=0.04,hi=0.96,erode=0,open_=True,min_area=8,hole_area=8,decontam=True,k=None):
    k=img.shape[0]/1024 if k is None else k; a=a.astype(np.float32).copy(); a[a<lo]=0; a[a>hi]=1
    if open_: a=cv2.morphologyEx(a,cv2.MORPH_OPEN,np.ones((3,3)))
    if erode: a=cv2.erode(a,disk(erode))
    b=(a>0.5).astype(np.uint8); n,l,st,_=cv2.connectedComponentsWithStats(b)
    for i in range(1,n):
        if st[i,4]<min_area*k*k: a[l==i]=0
    n,l,st,_=cv2.connectedComponentsWithStats(1-b)
    for i in range(1,n):
        if st[i,4]<hole_area*k*k: a[l==i]=1
    if not decontam: return img.copy(),a
    fg=estimate_foreground_ml(img[...,::-1]/255.0,a.astype(np.float64))[...,::-1]*255
    return np.clip(fg,0,255).astype(np.uint8),a
