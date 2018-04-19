# -*- coding:utf-8 -*-

"""
create on July 29, 2016 by Wayne
"""

from logRegres import *

data_arr, label_mat = load_data_set()
weights = grad_ascent(data_arr, label_mat)
print weights
plot_best_fit(weights.getA())

