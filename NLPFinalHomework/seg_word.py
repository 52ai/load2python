# -*- coding:utf-8 -*-

"""
create on July 6,2016
@author:Wayne
Function:对短信样本数据进行分词
"""
import jieba
import time


def seg_word(line):
    seg_list = jieba.cut(line, cut_all=False)
    return_str = "/".join(seg_list).encode("utf8")
    return return_str


def seg_word_file(file_name):
    start_time = time.clock()  # 计时开始
    fr = open(file_name, 'r')
    fw = open(file_name+"_seg.txt", 'w')
    # 两种思路，当文件比较大的时候，适合用思路一，但数据量较小的时候两种思路的所消耗的时间差不多
    # 思路一，读一行，处理一行，写一行
    """
    done = 0
    while not done:
        line = fr.readline()
        if line != '':
            write_str = seg_word(line)
            fw.write(write_str)
        else:
            done = 1
    """
    # 思路二，一次性全部读入，然后处理一行，写一行
    for line in fr.readlines():
        write_str = seg_word(line)
        fw.write(write_str)
    fw.close()
    fr.close()
    end_time = time.clock()  # 计时结束
    return end_time - start_time

if __name__ == "__main__":

    print "- - - - - - - - - - - - - - - - - - - - - - - - - - - "
    file_for_input = 'data\\2w_cut_test.txt'
    file_for_output = 'data\\2w_cut_test.txt_seg.txt'
    time_consuming = seg_word_file(file_for_input)
    print "Task 1:\n" \
          "input:%s \n" \
          "output: %s" % (file_for_input, file_for_output)
    print "Task had done!Time consuming is : %f s" % time_consuming
    print "- - - - - - - - - - - - - - - - - - - - - - - - - - - "
    file_for_input = 'data\\8w_cut_train.txt'
    file_for_output = 'data\\8w_cut_train.txt_seg.txt'
    time_consuming = seg_word_file(file_for_input)
    print "Task 2:\n" \
          "input:%s \n" \
          "output: %s" % (file_for_input, file_for_output)
    print "Task had done!Time consuming is : %f s" % time_consuming
    print "- - - - - - - - - - - - - - - - - - - - - - - - - - - "
