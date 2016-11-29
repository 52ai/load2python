# coding:utf-8

"""
Python 在人文学科的应用

自然语言处理方面nltk
"""

from nltk.corpus import gutenberg
print gutenberg.fileids()

allwords = gutenberg.words(u'shakespeare-hamlet.txt')

print len(allwords) # 莎士比亚的哈姆莱特全书总的词数 37360
print len(set(allwords)) # 其中不重复的也就是说词汇量 5447

print allwords.count(u'Hamlet') # 全书出现Hamlet的次数为99

# 统计书中单词长度大于12的长单词
A = set(allwords)
longwords = [w for w in A if len(w) > 12]
print sorted(longwords)

from nltk.probability import *
fd2 = FreqDist([sx.lower() for sx in allwords if sx.isalpha()])
print fd2.B()
print fd2.N()

fd2.tabulate(20) # 统计全书前20个出现次数最多的单词书

import matplotlib.pyplot as plt

#fd2.plot(20)
#fd2.plot(20, cumulative=True)

"""
美国总统就职演说预料库

"""
from nltk.corpus import inaugural
import nltk

# nltk.download()  先下载inaugural 语料库

fd3 = FreqDist([s for s in inaugural.words()])
print fd3.freq('freedom') # 在整个语料库中freedom出现的频率

# 用词习惯
cfd = ConditionalFreqDist(# 条件频率统计
	(fileid, len(w))
	for fileid in inaugural.fileids()
	for w in inaugural.words(fileid)
	if fileid > '1960'
	)
print cfd.items()[:40]
cfd.plot()