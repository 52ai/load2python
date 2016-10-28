# coding:utf-8

import urllib
r = urllib.urlopen("http://mryu.top/")
html = r.read()
print html
