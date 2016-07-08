# -*- coding:utf-8 -*-

"""
create on July 7, 2016
@author:Wayne
Function:进行分类
"""

from treeModel.trees import *
from treeModel.treePlotter_new import *
from extractFeature import extract_feature

if __name__ == "__main__":
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
