import cv2,numpy as np,json; from up import *; from key import lab
B=(600,380,256); x0,y0,w=B
src=cv2.imread('src_1024.png')[y0:y0+w,x0:x0+w]; cv2.imwrite('30_crop_source.png',src)
res={}
def q(y,S):
    n=1024*S; g=cv2.imread(f'src_{n}.png')[y0*S:(y0+w)*S,x0*S:(x0+w)*S]
    ga=cv2.imread(f'gt_alpha_{n}.png',0)[y0*S:(y0+w)*S,x0*S:(x0+w)*S]/255.
    hl=np.load(f'masks_{n}.npy')[3][y0*S:(y0+w)*S,x0*S:(x0+w)*S]
    inner=(cv2.erode((ga>0.99).astype(np.uint8),np.ones((9,9)))>0)&~cv2.dilate(hl.astype(np.uint8),np.ones((15,15))).astype(bool)
    band=cv2.dilate(((ga>0.02)&(ga<0.98)).astype(np.uint8),np.ones((3*S+1,)*2))>0
    dE=np.linalg.norm(lab(y)-lab(g),axis=2)
    L=lambda im: cv2.Laplacian(np.ascontiguousarray(lab(im)[...,0]).astype(np.float32),cv2.CV_32F)
    tex=L(y)[inner].std()/L(g)[inner].std()
    return dict(dE=float(dE.mean()),dE_bord=float(dE[band].mean()),texture=float(tex))
for S in (2,4):
    for n in ['lanczos','x4plus','general-dn0.0','general-dn0.2','general-dn0.5','general-dn1.0','anime6B','swinir']+(['x2plus'] if S==2 else []):
        y,t=upscale(src,n,S); r=q(y,S); r['t_s']=t; r['s_par_MP_sortie']=t/(y.shape[0]*y.shape[1]/1e6)
        res[f'x{S} {n}']=r; cv2.imwrite(f'31_x{S}_{n}.png',y); print(f'x{S} {n}',{k:round(v,3) for k,v in r.items()},flush=True)
json.dump(res,open('res_up.json','w'),indent=1)
