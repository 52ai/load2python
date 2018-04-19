# -*- coding:utf-8 -*-

"""
create on July 27,2016  by Wayne
function : bayes model
"""

from numpy import *


def load_data_set():
    posting_list = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                    ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                    ['my', 'dal', 'is', 'so', 'cute', 'I', 'love', 'him'],
                    ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                    ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                    ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    class_vec = [0, 1, 0, 1, 0, 1]    # 1 is abusive, 0 not
    return posting_list, class_vec


def create_vocab_list(data_set):
    vocab_set = set([])  # 创建一个空集
    for document in data_set:
        vocab_set = vocab_set | set(document)  # 创建两个集合的并集
    return list(vocab_set)


def set_of_words_to_vec(vocab_list, input_set):
    return_vec = [0] * len(vocab_list)
    for word in input_set:
        if word in vocab_list:
            return_vec[vocab_list.index(word)] = 1
        else:
            print "the word: %s is not in my vocabulary! " % word
    return return_vec


def bag_of_words_to_vec(vocab_list, input_set):
    return_vec = [0] * len(vocab_list)
    for word in input_set:
        if word in vocab_list:
            return_vec[vocab_list.index(word)] += 1
    return return_vec


def train_bayes0(train_matrix, train_category):
    num_of_train_docs = len(train_matrix)
    num_of_words = len(train_matrix[0])
    p_abusive = sum(train_category) / float(num_of_train_docs)
    # p0_num = zeros(num_of_words)
    # p1_num = zeros(num_of_words)
    # p0_denom = 0.0
    # p1_denom = 0.0
    '''
    为解决概率为零对计算多个概率乘积所带来的影响,将概率初始化做如下改变
    '''
    p0_num = ones(num_of_words)
    p1_num = ones(num_of_words)
    p0_denom = 2.0
    p1_denom = 2.0

    for i in range(num_of_train_docs):
        if train_category[i] == 1:
            p1_num += train_matrix[i]
            p1_denom += sum(train_matrix[i])
        else:
            p0_num += train_matrix[i]
            p0_denom += sum(train_matrix[i])

    '''
    为解决多个很小的数相乘造成的数据下溢出问题,对乘积取自然对数。
    通过求对数可以避免下溢出或者浮点数舍入导致的错误。
    在数学上讲,采用自然对数进行处理不会有任何的函数损失。
    '''
    p1_vec = log(p1_num / p1_denom)  # change to log
    p0_vec = log(p0_num / p0_denom)  # change to log

    return p0_vec, p1_vec, p_abusive


def classify_bayes(vec_to_classify, p0_vec, p1_vec, p_class1):
    p1 = sum(vec_to_classify * p1_vec) + log(p_class1)
    p0 = sum(vec_to_classify * p0_vec) + log(1.0 - p_class1)
    if p1 > p0:
        return 1
    else:
        return 0


def text_parse(big_string):
    import re
    list_of_tokens = re.split(r'\\W*', big_string)
    return [tok.lower() for tok in list_of_tokens if len(tok) > 2]


# 下面是RSS源分类器及高频词去除函数


def calc_most_freq(vocablist, full_text):
    import operator
    freq_dict = {}
    for token in vocablist:
        freq_dict[token] = full_text.count(token)
    sorted_freq = sorted(freq_dict.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sorted_freq[:30]


def local_words(feed1, feed0):
    import feedparser
    doc_list = []
    class_list = []
    full_text = []
    min_len = min((len(feed1['entries'])), len(feed0['entries']))
    print "min_len",min_len
    for i in range(min_len):
        word_list = text_parse(feed1['entries'][i]['summary'])
        doc_list.append(word_list)
        full_text.extend(word_list)
        class_list.append(1)
        word_list = text_parse(feed0['entries'][i]['summary'])
        doc_list.append(word_list)
        full_text.extend(word_list)
        class_list.append(0)
    vocab_list = create_vocab_list(doc_list)
    print vocab_list
    top30_words = calc_most_freq(vocab_list, full_text)
    for pairw in top30_words:
        if pairw[0] in vocab_list:
            vocab_list.remove(pairw[0])
    training_set = range(2*min_len)
    test_set = []
    for i in range(20):
        rand_index = int(random.uniform(0, len(training_set)))
        test_set.append(training_set[rand_index])
        del(training_set[rand_index])
    train_mat = []
    train_classes = []
    for doc_index in training_set:
        train_mat.append(bag_of_words_to_vec(vocab_list, doc_list[doc_index]))
        train_classes.append(class_list[doc_index])
    p0v, p1v, pspam = train_bayes0(array(train_mat), array(train_classes))
    error_cnt = 0
    for doc_index in test_set:
        word_vector = bag_of_words_to_vec(vocab_list, doc_list[doc_index])
        if classify_bayes(array(word_vector), p0v,p1v, pspam) != class_list[doc_index]:
            error_cnt += 1
    print "The error rate is:", float(error_cnt) / len(test_set)
    return vocab_list, p0v, p1v


def get_top_words(ny, sf):
    import operator
    vocab_list, p0v, p1v = local_words(ny, sf)
    top_nf = []
    top_sf = []
    for i in range(len(p0v)):
        if p0v[i] > -6.0:
            top_sf.append((vocab_list[i], p0v[i]))
        if p1v[i] > -6.0:
            top_nf.append((vocab_list[i], p1v[i]))
    sorted_sf = sorted(top_sf, key=lambda pair:pair[1], reverse=True)
    print "SF*SF*SF*SF*SF*SF*SF"
    for item in sorted_sf:
        print item[0]
    sorted_ny = sorted(top_nf, key=lambda pair:pair[1], reverse=True)
    print "NY*NY*NY*NY*NY*NY*NY"
    for item in sorted_ny:
        print item[0]






