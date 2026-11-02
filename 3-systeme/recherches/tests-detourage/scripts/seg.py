import sys,time,cv2,numpy as np
from rembg import new_session, remove
from PIL import Image
img=Image.open('00_source_1024.png').convert('RGB')
for m in sys.argv[1:]:
    t=time.time(); s=new_session(m); t1=time.time()
    a=remove(img,session=s,only_mask=True); t2=time.time()
    a.save(f'10_alpha_{m}.png'); print(m,'load %.1fs'%(t1-t),'infer %.1fs'%(t2-t1),flush=True)
