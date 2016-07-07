# -*- coding:utf-8 -*-

"""
create on July 7, 2016
@author:Wayne
Function:进行分类
"""


from treeModel.trees import *
from treeModel.treePlotter_new import *

if __name__ == "__main__":
    my_tree = grab_tree('data\\classifierStorage_sms.txt')
    # labels = ['sms_len', 'sp_number', 'phone_number', 'bank_number', 'url']
    labels = ['sp_number', 'phone_number', 'bank_number', 'url', 'sms_len']
    # print my_tree
    #print labels
    print classify_sms(my_tree, labels, [1, 1, 0, 0, 1])
    # createPlot(my_tree)
