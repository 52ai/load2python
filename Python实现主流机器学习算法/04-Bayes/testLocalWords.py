# -*- coding:utf-8 -*-

"""
create on July 27,2016 by Wayne
"""

import feedparser
from bayes import *

'''
ny = feedparser.parse('http://newyork.craigslist.org/stp/index.rss')
print len(ny['entries'])

for (k, v) in ny.items():
    print k, ":", v

'''
ny = feedparser.parse('http://newyork.craigslist.org/stp/index.rss')
sf = feedparser.parse('http://sfbay.craigslist.org/stp/index.rss')

# vocab_list, psf, pnf = local_words(ny, sf)
# vocab_list, psf, pnf = local_words(ny, sf)

get_top_words(ny, sf)