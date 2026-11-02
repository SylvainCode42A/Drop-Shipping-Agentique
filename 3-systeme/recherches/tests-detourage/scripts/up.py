import torch,spandrel,numpy as np,cv2,time
torch.set_num_threads(1)
_cache={}
def load(name):
    if name in _cache: return _cache[name]
    if name.startswith('general-dn'):
        dn=float(name[10:]); a=torch.load('w/realesr-general-x4v3.pth',map_location='cpu'); b=torch.load('w/realesr-general-wdn-x4v3.pth',map_location='cpu')
        ka='params' if 'params' in a else 'params_ema'; kb='params' if 'params' in b else 'params_ema'
        sd={k:dn*a[ka][k]+(1-dn)*b[kb][k] for k in a[ka]}
        m=spandrel.ModelLoader().load_from_state_dict(sd)
    else:
        f={'x4plus':'RealESRGAN_x4plus','x2plus':'RealESRGAN_x2plus','anime6B':'RealESRGAN_x4plus_anime_6B','swinir':'003_realSR_BSRGAN_DFO_s64w8_SwinIR-M_x4_GAN'}[name]
        m=spandrel.ModelLoader().load_from_file(f'w/{f}.pth')
    m.eval(); _cache[name]=m; return m
def upscale(img,name,out_scale):
    """img BGR uint8 ; renvoie BGR uint8 agrandi de out_scale, et le temps"""
    h,w=img.shape[:2]; t=time.time()
    if name=='lanczos':
        return cv2.resize(img,(w*out_scale,h*out_scale),interpolation=cv2.INTER_LANCZOS4),time.time()-t
    m=load(name); x=torch.from_numpy(img[...,::-1].copy()).permute(2,0,1)[None].float()/255
    pad=0
    if name=='swinir':
        pad=(8-h%8)%8
    with torch.no_grad(): y=m(x)
    y=(y[0].permute(1,2,0).clamp(0,1).numpy()[...,::-1]*255).round().astype(np.uint8)
    if y.shape[0]!=h*out_scale: y=cv2.resize(y,(w*out_scale,h*out_scale),interpolation=cv2.INTER_LANCZOS4)
    return y,time.time()-t
