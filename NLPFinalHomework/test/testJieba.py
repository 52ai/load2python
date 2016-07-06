# -*- coding:utf-8 -*-

"""
create on July 6,2016
@author:Wayne
Function: test jieba word segmentation
"""

import jieba

seg_list1 = jieba.cut("我在写自然语言处理大作业。", cut_all=True)
seg_list2 = jieba.cut("我在写自然语言处理大作业。", cut_all=False)

"""
for word in seg_list:
    print word.encode('utf8')
"""

print "Full Mode："+"/".join(seg_list1).encode('utf8')
print "Default Mode："+"/".join(seg_list2).encode('utf8')

seg_list3 = jieba.cut("我在写自然语言处理大作业。", cut_all=False)
out_str = "/".join(seg_list3).encode('utf8')+"\n"
fw = open("..\\data\\test_jieba.txt", 'w')
for i in range(100):
    fw.write(out_str)
fw.close()
