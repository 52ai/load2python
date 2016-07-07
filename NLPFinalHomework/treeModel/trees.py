# -*- coding:utf-8 -*-

from math import log
import operator


def calc_shannon_ent(data_set):
    num_entries = len(data_set)
    labels_counts = {}
    for feature_vector in data_set:
        current_label = feature_vector[-1]
        if current_label not in labels_counts.keys():
            labels_counts[current_label] = 0
        labels_counts[current_label] += 1
    shannon_entropy = 0.0
    for key in labels_counts:
        prob = float(labels_counts[key])/num_entries
        shannon_entropy -= prob * log(prob, 2)
    return shannon_entropy


def create_data_set():
    data_set = [[1, 1, 'yes'],
                [1, 1, 'yes'],
                [1, 0, 'no'],
                [0, 1, 'no'],
                [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']
    return data_set, labels


def create_data_set_sms(filename):
    fr = open(filename, 'r')
    # data_set_list = [line.strip().split('\t') for line in fr.readlines()]
    # labels = ['sms_len', 'sp_number', 'phone_number', 'bank_number', 'url']
    labels = ['sp_number', 'phone_number', 'bank_number', 'url', 'sms_len']
    # labels = ['age', 'prescript', 'astigmatic', 'tearRate']
    data_set_list = []
    line_count = 0
    for line in fr.readlines():
        # print list(line.strip().split('\t'))
        data_set_list.append(list(line.strip().split('\t')))
        # print data_set_list
        if line_count == 800000:
            break
        line_count += 1
    return data_set_list, labels


def split_data_set(data_set, axis, value):
    new_data_set = []
    for feature_vector in data_set:
        if feature_vector[axis] == value:
            reduced_feature_vector = feature_vector[:axis]
            reduced_feature_vector.extend(feature_vector[axis+1:])
            new_data_set.append(reduced_feature_vector)
    return new_data_set


def choose_best_feature_to_split(data_set):
    number_features = len(data_set[0]) - 1
    base_entropy = calc_shannon_ent(data_set)
    best_info_gain = 0.0
    best_feature = -1
    for i in range(number_features):
        feature_lists = [example[i] for example in data_set]
        unique_values = set(feature_lists)
        new_entropy = 0.0
        # print unique_values
        for value in unique_values:
            sub_data_set = split_data_set(data_set, i, value)
            prob = len(sub_data_set)/float(len(data_set))
            new_entropy += prob * calc_shannon_ent(sub_data_set)
        info_gain = base_entropy - new_entropy
        if info_gain > best_info_gain:
            best_info_gain = info_gain
            best_feature = i
    if best_feature == -1:
        best_feature = number_features - 1
    return best_feature


def majority_cnt(class_list):
    class_count = {}
    for vote in class_list:
        if vote not in class_count.keys():
            class_count[vote] = 0
        class_count[vote] += 1
    sorted_class_count = sorted(class_count.iteritems(), key=operator.itemgetter(1), reverse=True)
    """
    sorted(arg1, key=arg1, reverse=True) operator.itemgetter(1) 函数获取的不是值，而是定义了一个函数，通过该函数作用到对象上才能获取值。
    reverse = True 表示降序
    """
    return sorted_class_count[0][0]


def create_tree(data_set, labels):
    class_list = [example[-1] for example in data_set]
    # print "class_list:", class_list

    if class_list.count(class_list[0]) == len(class_list):
        # print "class_list[0]:", class_list[0]
        return class_list[0]
    if len(data_set[0]) == 1:
        # print "majority_cnt(class_list):", majority_cnt(class_list)
        return majority_cnt(class_list)

    best_feature = choose_best_feature_to_split(data_set)
    best_feature_label = labels[best_feature]
    # print "best_feature:", labels[best_feature]

    my_tree = {best_feature_label: {}}
    # print "best_feature_id:", best_feature
    del(labels[best_feature])
    # print "labels:", labels

    feature_values = [example[best_feature] for example in data_set]
    # print "feature_values:", feature_values
    unique_values = set(feature_values)
    # print "unique_value:", unique_values

    for value in unique_values:
        sub_labels = labels[:]
        # print "sub_labels:", sub_labels
        my_tree[best_feature_label][value] = create_tree(split_data_set(data_set, best_feature, value), sub_labels)
    return my_tree


def classify(input_tree, feature_labels, test_vec):
    first_str = input_tree.keys()[0]
    second_dict = input_tree[first_str]
    feature_index = feature_labels.index(first_str)
    for key in second_dict.keys():
        if test_vec[feature_index] == key:
            if type(second_dict[key]).__name__ == 'dict':
                class_label = classify(second_dict[key], feature_labels, test_vec)
            else: class_label = second_dict[key]
            return class_label


def classify_sms(input_tree, feature_labels, test_vec):
    class_label = 'no'
    first_str = input_tree.keys()[0]
    # print first_str
    second_dict = input_tree[first_str]
    # print second_dict
    feature_index = feature_labels.index(first_str)
    # print feature_index
    key = test_vec[feature_index]
    # print "key:", key
    value_of_feature = second_dict[str(key)]
    # print "value_of_feature:", value_of_feature

    if isinstance(value_of_feature, dict):
        class_label = classify_sms(value_of_feature, feature_labels, test_vec)
    else:
        # print "value_of_feature:",value_of_feature
        class_label = value_of_feature
    return class_label


def store_tree(input_tree, filename):
    import pickle
    fw = open(filename, 'w')
    pickle.dump(input_tree, fw)
    fw.close()


def grab_tree(filename):
    import  pickle
    fr = open(filename, 'r')
    return pickle.load(fr)
