__author__ = 'liyuanpeng'

import json
import re

data={}

data[123]=12

data["jsadaj"]="sjdaps"

d1=json.dumps(data)

d1_re = re.compile()

skuid_re = re.compile(r'jsadaj: (.*?),')

product_info = re.findall(skuid_re, d1)

print d1
print d1_re

print product_info

format="hello %s. Is is enough %s, is not it  "
value=['lee','cold']
print format % value
