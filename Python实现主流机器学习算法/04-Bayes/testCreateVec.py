# -*- coding:utf-8 -*-

"""
create on July 27,2016 by Wayne
function: test for create vector
"""

import bayes


list_of_posts, list_classes = bayes.load_data_set()
my_vocab_list = bayes.create_vocab_list(list_of_posts)

print list_of_posts
print list_classes
print my_vocab_list

# print bayes.set_of_words_to_vec(my_vocab_list, list_of_posts[0])
# print bayes.set_of_words_to_vec(my_vocab_list, list_of_posts[3])

train_mat = []
for post_in_doc in list_of_posts:
    train_mat.append(bayes.set_of_words_to_vec(my_vocab_list, post_in_doc))

p0v, p1v, pab = bayes.train_bayes0(train_mat, list_classes)
print "pab:",pab
print "p0v:",p0v
print "p1v:",p1v





