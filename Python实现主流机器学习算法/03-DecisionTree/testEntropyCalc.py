# coding = utf-8

from trees import *

if __name__ == "__main__":
    my_data, labels = create_data_set()
    print my_data
    print calc_shannon_ent(my_data)
    my_data[0][-1] = 'maybe'
    print my_data
    print calc_shannon_ent(my_data)
