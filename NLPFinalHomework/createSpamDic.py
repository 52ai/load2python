# -*- coding:utf-8 -*-

"""
create on July 6,2016
@author:Wayne
Function: 基于TF-IDF算法构建垃圾词汇库

步骤：

一，先对所有的垃圾短信采用TF-IDF算法，进行主题词提取，组成S_Dic词库。
二，再对所有的正常短信采用TF-IDF算法，进行主题词体术，组成N_Dic词库。
三，垃圾词汇库Spam_Dic = S_Dic - S_Dic intersection N_Dic

jieba.analyse.extract_tags(sentence, topK=20, withWeight=False, allowPOS=())
    1.sentence 为待提取的文本
    2.topK 为返回几个 TF/IDF 权重最大的关键词，默认值为 20
    3.withWeight 为是否一并返回关键词权重值，默认值为 False
    4.allowPOS 仅包括指定词性的词，默认值为空，即不筛选

"""

import jieba.analyse
import time


"""
inputStr = "我在写自然语言处理大作业！"
tags = jieba.analyse.extract_tags(inputStr, topK=2)
print ",".join(tags).encode('utf8')
"""


def extract_topic_words(content, top_k):
    topic_words = jieba.analyse.extract_tags(content, topK=top_k)
    return_str = ",".join(topic_words).encode('utf8')
    return return_str


def extract_topic_words_sms(filename, line_num, top_k):
    fr = open(filename, 'r')
    line_count = 0
    spam_sms_content = ""
    normal_sms_content = ""
    for line in fr.readlines():
        line_array = line.split('\t')
        if line_array[1] == '1':
            spam_sms_content += line_array[2]
        elif line_array[1] == '0':
            normal_sms_content += line_array[2]
        else:
            print "该行格式不对，为无效行！"
        if line_count == line_num:  # 参与提取主题词的最大行数
            break
        line_count += 1
    # print sms_content
    topic_words_spam = extract_topic_words(spam_sms_content, top_k)
    topic_words_normal = extract_topic_words(normal_sms_content, top_k)
    return topic_words_spam, topic_words_normal

if __name__ == "__main__":
    time_start = time.clock()  # 开始计时
    print "采用TF-IDF算法开始构建垃圾词汇库..."
    input_file = "data\\8w_cut_train.txt"
    # 参数含义(样本文件， 参与提取主题词的最大行， 需要提取主题词的个数)
    s_dic, n_dic = extract_topic_words_sms(input_file, 80000, top_k=100)
    print "垃圾短信主题词库：\n", s_dic, "\n"
    print "正常短信主题词库：\n", n_dic, "\n"
    s_dic = set(s_dic.split(','))
    n_dic = set(n_dic.split(','))
    spam_dic = s_dic - (s_dic & n_dic)
    print "垃圾短信主题词库：\n", s_dic, "\n"
    print "正常短信主题词库：\n", n_dic, "\n"
    print "垃圾词汇库：\n", spam_dic, "\n"
    fw = open("data\\spam_dic.txt", 'w')
    for value in spam_dic:
        fw.write(value+" ")
    fw.close()
    time_end = time.clock()  # 计时结束
    print "Task had done!Time consuming is :%f s" %(time_end - time_start)
