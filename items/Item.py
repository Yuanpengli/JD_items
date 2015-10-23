__author__ = 'liyuanpeng'

import urllib
import json
import re

#get the price for JD_website items

class JdPrice(object):

    def __init__(self, url):
        self.url = url
        self._response = urllib.urlopen(self.url)
        self.html = self._response.read()

    def get_product(self):

        product_re = re.compile(r'compatible: true,(.*?)};', re.S)
        #print product_re
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


        url = 'http://p.3.cn/prices/mgets?skuIds=J_' + skuid + '&type=1'

        price_json = json.load(urllib.urlopen(url))[0]


        if price_json['p']:
            price = price_json['p']
        return price

    def get_product_comments(self):

        number_of_comments = None

        skuid = self.get_product_skuid()

        url = 'http://club.jd.com/clubservice.aspx?method=GetCommentsCount&referenceIds=' + skuid

        self._response = urllib.urlopen(url)

        self.html = self._response.read()

        CommentCount_re = re.compile(r'"CommentCount":(.*?),')

        CommentCount = re.findall(CommentCount_re, self.html)[0]

        return CommentCount

   # def maijiayingxiang(self):


class geturl(object):

    def __init__(self,url):
        self.url = url
        self._response = urllib.urlopen(self.url)
        self.html = self._response.read()

    def get(self):
        product_re = re.compile(r'href="(.*?)"', re.S)
        product_info = re.findall(product_re, self.html)

        info = []
        for url in product_info:
            if url.startswith('//item') & url.endswith('html'):
                info.append(url)
        return info

# class get_number_of_comments(object):
#
#     def __init__(self,url):
#         self.url = url
#         self._response = urllib.urlopen(self.url)
#         self.html = self._response.read()


if __name__ == '__main__':

    # url = 'http://item.jd.com/11461683.html'
    # jp = JdPrice(url)
    # print jp.get_product_price()


    dict = {}
    page = 1

    while True:
        ob = geturl('http://search.jd.com/search?keyword=python&enc=utf-8&qrst=1&rt=1&stop=1&book=y&vt=2&page='+str(page))
        if ob==None:
            break
        print '***********print    '+str(page)+'    page************'
        page=page+1
        for url in ob.get():
            if not dict.has_key(url):
                dict[url]=1
                jp = JdPrice('http:'+url)
                print jp.get_product_name()+'\t'+jp.get_product_price()+'\t'+jp.get_product_comments()
