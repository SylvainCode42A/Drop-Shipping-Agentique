import cv2,numpy as np,time,json; from up import *; from pipe import *; from metr import *
B=(600,380,256); x0,y0,w=B
full=cv2.imread('src_1024.png'); bg=bg_color(full)
segF=cv2.imread('10_alpha_isnet-general-use.png',0)/255.
aF=fuse(full,segF,bg=bg); fgF,acF=clean(full,aF,lo=0,hi=1,open_=False)   # décontamination seule
cr=lambda x: x[y0:y0+w,x0:x0+w]
img,seg,fg1,a1=cr(full),cr(segF),cr(fgF),cr(acF)
def upa(a,name,S):   # agrandir l'alpha
    if name=='bicubic': return np.clip(cv2.resize(a,(w*S,w*S),interpolation=cv2.INTER_CUBIC),0,1),0
    g=np.repeat((a*255).astype(np.uint8)[...,None],3,2); y,t=upscale(g,name,S); return y[...,0]/255.,t
R={}
for S,ups in [(2,['lanczos','x2plus','general-dn0.2']),(4,['lanczos','general-dn0.2','x4plus'])]:
    n=1024*S
    for u in ups:
        # A : détourer puis agrandir
        for rgb_name,rgb in [('rgb-original',img),('rgb-decontamine',fg1)]:
            y,t1=upscale(rgb,u,S)
            for am in (['bicubic',u] if u!='lanczos' else ['bicubic']):
                au,t2=upa(a1.astype(np.float32),am,S)
                k=f'x{S} {u} | A detourer-puis-agrandir | {rgb_name} | alpha {am}'
                R[k]=fmt(metrics(y,au,n,B)); R[k]['t']=round(t1+t2,1); print(k,R[k],flush=True)
                cv2.imwrite(f'40_x{S}_{u}_A_{rgb_name}_alpha-{am}.png',np.dstack([y,(au*255).round().astype(np.uint8)]))
        # B : agrandir puis détourer
        y,t1=upscale(img,u,S); t=time.time()
        segU=np.clip(cv2.resize(seg.astype(np.float32),(w*S,w*S),interpolation=cv2.INTER_CUBIC),0,1)
        d=dist(y,bg); tc=max(1.5,1.7*np.percentile(d[segU<0.01],99))
        aU=fuse(y,segU,bg=bg,k=S,t_core=tc); fU,acU=clean(y,aU,lo=0,hi=1,open_=False,k=S)
        k=f'x{S} {u} | B agrandir-puis-detourer'
        R[k]=fmt(metrics(fU,acU,n,B)); R[k]['t']=round(t1+time.time()-t,1); R[k]['t_core']=round(tc,1); print(k,R[k],flush=True)
        cv2.imwrite(f'41_x{S}_{u}_B.png',np.dstack([fU,(acU*255).round().astype(np.uint8)]))
json.dump(R,open('res_ordre.json','w'),indent=1)
