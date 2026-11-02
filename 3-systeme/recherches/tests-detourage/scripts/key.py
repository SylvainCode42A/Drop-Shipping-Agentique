import numpy as np,cv2
def lab(i): return cv2.cvtColor(np.ascontiguousarray(i),cv2.COLOR_BGR2LAB).astype(np.float32)*[100/255,1,1]-[0,128,128]
def bg_color(img):
    b=np.concatenate([img[:8].reshape(-1,3),img[-8:].reshape(-1,3),img[:,:8].reshape(-1,3),img[:,-8:].reshape(-1,3)])
    return np.median(b,0)
def dist(img,bg=None):
    bg=bg_color(img) if bg is None else bg
    return np.linalg.norm(lab(img)-lab(np.uint8(bg)[None,None]),axis=2)
def key_alpha(img,t0=10,t1=60,bg=None):
    return np.clip((dist(img,bg)-t0)/(t1-t0),0,1)
