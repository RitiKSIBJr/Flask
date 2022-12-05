from PIL import Image
import numpy as np

w, h = 50, 100


with open('img', mode='rb') as f:
    d = np.fromfile(f,dtype=np.uint8,count=w*h).reshape(h,w)


PILimage = Image.fromarray(d)
PILimage.show()