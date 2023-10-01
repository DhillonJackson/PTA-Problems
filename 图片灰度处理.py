import numpy
import matplotlib.pyplot as pyp
a=pyp.imread(r"C:\Users\86183\Desktop\作息.jpg")
b=pyp.imshow(a)
c=numpy.array([0.299,0.587,0.114])
d=numpy.dot(a,c)
pyp.imshow(d,cmap='gray')
pyp.show()
