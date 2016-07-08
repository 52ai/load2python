# -*- coding:utf-8 -*-

"""
create on July 7,2016
@author:Wayne
Function: create decision tree for sms classification
"""

from treeModel.trees import *
from treeModel.treePlotter_new import *
import time

if __name__ == "__main__":
    time_start = time.clock()  # 计时开始
    # my_dat, labels = create_data_set()
    # my_dat, labels = create_data_set_sms('data\\8w_cut_train.txt_feature.txt')
    my_dat, labels = create_data_set_sms('data\\80w_train.txt_feature.txt')
    # my_dat, labels = create_data_set_sms('data\\lenses.txt')
    # print labels
    # print my_dat

    my_tree = create_tree(my_dat, labels)
    print my_tree
    store_tree(my_tree, 'data\\classifierStorage_sms.txt')
    time_end = time.clock()  # 计时结束
    print "Task had done!Time consuming is:%f s" % (time_end - time_start)
    createPlot(my_tree)

