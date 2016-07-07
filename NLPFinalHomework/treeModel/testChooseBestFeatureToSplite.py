# coding = utf-8

from trees import *


if __name__ == "__main__":
    my_data, labels = create_data_set()
    print my_data
    print choose_best_feature_to_split(my_data)

