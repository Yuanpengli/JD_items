__author__ = 'liyuanpeng'

import numpy
from math import *

f=open("geodesic.txt",'r')

a=[]
i=0
for line in f:
    b=numpy.asarray(line)
    a.append(b)
    i=i+1
f.close()
print matrix(a)
