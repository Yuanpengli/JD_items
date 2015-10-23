__author__ = 'liyuanpeng'

import urllib
import json
import re
import numpy
from PIL import Image


# info = urllib.urlopen('http://image.58.com/showphone.aspx?t=v55&v=316B3F9B3D0F19D24AF8763A98C725744')
#
# print info.read()

im = Image.open('/Users/liyuanpeng/Downloads/showphone.gif')
im = im.convert("L")
a=numpy.asarray(im)
l=len(a)
p=len(a[15])
print p



f=open("geodesic.txt",'w')


sum=0.0
for i in range(l):
    for j in range(p):

        t=a[i][j]
        sum = sum + t
        if j == p-1:
            f.write(str(t)+'\n')
        else:
            f.write(str(t)+' ')
f.close()

average = sum /float(l*p)

mat= open ("matrix.txt",'w')

for i in range(l):
    for j in range(p):
        if j ==p-1:
            if a[i][j]>average:
                mat.write(str(1)+'\n')
            else:
                mat.write(str(0)+'\n')
        else:
            if a[i][j]>average:
                mat.write(str(1)+' ')
            else:
                mat.write(str(0)+' ')
mat.close()



