from PIL import Image
im=Image.open(r"C:\Users\86183\Desktop\壁纸.jpeg")
r,g,b=im.split()
om=Image.merge(mode='RGB',bands=(r,b,g))
om.save('new3.jpeg')
import os
os.startfile('new3.jpeg')