# -*- coding:utf-8 -*-

"""
create on July 7,2016
@author:Wayne
Function: create decision tree for sms classification
"""

from treeModel.trees import *
from treeModel.treePlotter_new import *

if __name__ == "__main__":
    # my_dat, labels = create_data_set()
    my_dat, labels = create_data_set_sms('data\\8w_cut_train.txt_feature.txt')
    # my_dat, labels = create_data_set_sms('data\\lenses.txt')
   # print labels
    # print my_dat

    my_tree = create_tree(my_dat, labels)
    print my_tree
    store_tree(my_tree, 'data\\classifierStorage_sms.txt')
    createPlot(my_tree)

