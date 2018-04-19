# -*- coding:utf-8 -*-

"""
create on July 27,2016 by Wayne
"""
from bayes import *


def spam_test():
    doc_list = []
    class_list =[]
    full_text = []
    for i in range(1, 26):
        word_list = text_parse(open('email/spam/%d.txt' % i).read())
        doc_list.append(word_list)
        full_text.extend(word_list)
        class_list.append(1)
        word_list = text_parse(open('email/ham/%d.txt' % i).read())
        doc_list.append(word_list)
        full_text.extend(word_list)
        class_list.append(0)
    vocab_list = create_vocab_list(doc_list)
    training_set = range(50)
    test_set = []
    for i in range(10):
        rand_index = int(random.uniform(0, len(training_set)))
        test_set.append(training_set[rand_index])
        del(training_set[rand_index])
    train_mat = []
    train_classes = []
    for doc_index in training_set:
        train_mat.append(set_of_words_to_vec(vocab_list, doc_list[doc_index]))
        train_classes.append(class_list[doc_index])
    p0v, p1v, pspam = train_bayes0(array(train_mat), array(train_classes))
    error_count = 0
    for doc_index in test_set:
        word_vector = set_of_words_to_vec(vocab_list, doc_list[doc_index])
        if classify_bayes(array(word_vector), p0v, p1v, pspam) != class_list[doc_index]:
            error_count += 1
    print "the error rate is: ", float(error_count)/len(test_set)


if __name__ == "__main__":
    spam_test()


