__author__ = 'liyuanpeng'

import re

sj=re.compile(r"hello wsdas")

#print str(sj)

mat=sj.match("hello world in my sentence")

if mat:

    print mat.group()
print "type a=:\b"
a =input("a=:")
print a+7


name = input("what is your name ?")

print "Hello, " +name +"!"


#print sj