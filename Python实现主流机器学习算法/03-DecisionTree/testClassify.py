# -*- coding:utf-8 -*-

from trees import *
from treePlotter_new import *

if __name__ == "__main__":
    my_dat, labels = create_data_set()
    print labels
    my_tree = retrieveTree(0)
    print my_tree
    store_tree(my_tree, 'data\\classifierStorage.txt')
    print classify(my_tree, labels, [1, 0])
    print classify(my_tree, labels, [1, 1])
    createPlot(my_tree)

