# coding = utf-8

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
    return best_feature

