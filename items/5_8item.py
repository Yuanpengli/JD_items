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
a=(numpy.asarray(im))
l=len(a)
print l
f=open("geodesic.txt",'w')
for i in range(l):
    t=a[i]
    f.write(str(t)+ "\n")
f.close()

#print a.shape()
#print numpy.asarray(im)[9]
#im.show()

# class JdPrice(object):
#
#     def __init__(self, url):
#         self.url = url
#         self._response = urllib.urlopen(self.url)
#         self.html = self._response.read()

