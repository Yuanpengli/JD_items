__author__ = 'liyuanpeng'

import urllib
import json
import re


class JdPrice(object):

    def __init__(self, url):
        self.url = url
        self._response = urllib.urlopen(self.url)
        self.html = self._response.read()

    def get_product(self):

        product_re = re.compile(r'compatible: true,(.*?)};', re.S)
        product_info = re.findall(product_re, self.html)[0]
        return product_info

    def get_product_skuid(self):

        product_info = self.get_product()
        skuid_re = re.compile(r'skuid: (.*?),')
        skuid = re.findall(skuid_re, product_info)[0]
        return skuid

    def get_product_name(self):


        product_info = self.get_product()

        name_re = re.compile(r"name: '(.*?)',")
        name = re.findall(name_re, product_info)[0]
        return name.decode('unicode-escape')

    def get_product_price(self):

        price = None

        skuid = self.get_product_skuid()
        name = self.get_product_name()
        print name


        url = 'http://p.3.cn/prices/mgets?skuIds=J_' + skuid + '&type=1'

        price_json = json.load(urllib.urlopen(url))[0]


        if price_json['p']:
            price = price_json['p']
        return price


if __name__ == '__main__':

    url = 'http://item.jd.com/11461683.html'
    jp = JdPrice(url)
    print jp.get_product_price()
