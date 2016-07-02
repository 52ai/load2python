# coding = utf-8

from trees import *


if __name__ == "__main__":
    my_data, labels = create_data_set()
    print my_data
    print split_data_set(my_data, 0, 1)
    print split_data_set(my_data, 0, 0)