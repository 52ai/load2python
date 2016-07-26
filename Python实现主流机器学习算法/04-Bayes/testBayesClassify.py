# -*- coding:utf-8 -*-

"""
create on July 27.2016 by Wayne
function : test for Bayes classify
"""

import bayes
from numpy import *


def testing_bayes():
    list_of_posts, list_classes = bayes.load_data_set()
    my_vocab_list = bayes.create_vocab_list(list_of_posts)
    train_mat = []
    for post_in_doc in list_of_posts:
        train_mat.append(bayes.set_of_words_to_vec(my_vocab_list, post_in_doc))
    p0v, p1v, pab = bayes.train_bayes0(array(train_mat), array(list_classes))

    test_entry = ['love', 'my', 'dal']
    this_doc = array(bayes.set_of_words_to_vec(my_vocab_list, test_entry))
    print test_entry, 'classified as: ', bayes.classify_bayes(this_doc, p0v, p1v, pab)

    test_entry = ['stupid', 'my', 'garbage']
    this_doc = array(bayes.set_of_words_to_vec(my_vocab_list, test_entry))
    print test_entry, 'classified as: ', bayes.classify_bayes(this_doc, p0v, p1v, pab)

if __name__ == "__main__":
    testing_bayes()

