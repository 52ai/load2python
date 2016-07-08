# -*- coding:utf-8 -*-

"""
create on July 7, 2016
@author:Wayne
Function:进行分类
"""

from treeModel.trees import *
from treeModel.treePlotter_new import *
from extractFeature import extract_feature


def classify_and_score(filename):
    my_tree = grab_tree('data\\classifierStorage_sms.txt')  # 载入决策树模型
    labels = ['sp_number', 'phone_number', 'bank_number', 'url', 'sms_len']  # 定义好分类使用的标签
    correct = 0
    error = 0
    line_count = 0
    sms_class = 'no'
    fr = open(filename, 'r')
    for line in fr.readlines():
        line = line.split('\t')
        sms_content = line[2]
        if line[1] == 1:
            sms_class = 'yes'
        sms_feature = extract_feature(sms_content)
        print sms_feature
        sms_class_predict = classify_sms(my_tree, labels, sms_feature)
        if sms_class_predict == sms_class:
            correct += 1
        elif sms_class_predict != sms_class:
            error += 1
        else:
            print "classify error!"
        line_count += 1
    return (correct * 100) / (line_count * 100)

if __name__ == "__main__":
    """
    # test_file = 'data\\2w_cut_test.txt'
    test_file = 'data\\8w_cut_train.txt'
    correct_rate = classify_and_score(test_file)
    print "分类准确率为： %f" % correct_rate
    """
    my_tree = grab_tree('data\\classifierStorage_sms.txt')  # 载入决策树模型
    # labels = ['sms_len', 'sp_number', 'phone_number', 'bank_number', 'url']
    labels = ['sp_number', 'phone_number', 'bank_number', 'url', 'sms_len']  # 定义好分类使用的标签
    # print my_tree
    # print labels
    # sms_text = "它是由AlexanderStepanov、MengLee和DavidRMusser在惠普实验室工作时所开发出来的"
    sms_text = "庆x'x节本会所优惠活动，为答谢新老顾客的支持与厚爱，，面部特卡:xxx元/xx次，身体活动，带脉减小肚腩:xxxx元/xx次，，肠胃"
    sms_feature = extract_feature(sms_text)
    print sms_feature
    print classify_sms(my_tree, labels, sms_feature)
    # createPlot(my_tree)
