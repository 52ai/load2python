# -*- coding:utf-8 -*-

"""
create on July 6,2016
@author:Wayne
Function:test createTree

<。)#)))≦
"""

from trees import *

if __name__ == "__main__":
    my_data, labels = create_data_set()
    my_tree = create_tree(my_data, labels)
    print my_data
    print labels
    print my_tree
