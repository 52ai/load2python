# -*- coding:utf-8 -*-

# <。)#)))≦
# Author:Wayne
# Date：20160704
# function: data cutting
"""
现有100万条短信，80万条标注好的训练集，20万条没有标注的测试集。初步将80万训练集分出切分10万条，将前8万条作为训练集用于训练模型，后2万条作为测试集，用于测试分类效果。

input: 80w_train.txt
output:10w_cut.txt

input:10w_cut.txt
output:8w_train_cut.txt 2w_test_cut.txt

"""
import time


def data_cut(input_filename, output_filename, start_line, cut_number_of_lines):
    time_start = time.clock()  # 计时开始
    fr = open(input_filename, 'r')
    fw = open(output_filename, 'w')
    line_count = 1
    while True:
        line = fr.readline()
        if line_count < start_line:
            line_count += 1
            continue
        elif line_count < (start_line + cut_number_of_lines):
            fw.write(line)
            line_count += 1
        else:
            break
    fw.close()
    fr.close()
    time_end = time.clock()  # 计时结束
    return time_end - time_start

if __name__ == "__main__":
    print "- - - - - - - - - - - - - - - - - - - - - - - - - - - "
    file_for_input = 'data\\80w_train.txt'
    file_for_output = 'data\\10w_cut.txt'
    time_consuming = data_cut(file_for_input, file_for_output, 1, 100000)
    print "Task 1:\n" \
          "input:%s \n" \
          "output: %s" % (file_for_input, file_for_output)
    print "Task had done!Time consuming is : %f s" % time_consuming
    print "- - - - - - - - - - - - - - - - - - - - - - - - - - - "

    file_for_input = 'data\\10w_cut.txt'
    file_for_output = 'data\\8w_cut_train.txt'
    time_consuming = data_cut(file_for_input, file_for_output, 1, 80000)
    print "Task 2:\n" \
          "input:%s \n" \
          "output: %s" % (file_for_input, file_for_output)
    print "Task had done!Time consuming is : %f" % time_consuming
    print "- - - - - - - - - - - - - - - - - - - - - - - - - - - "

    file_for_input = 'data\\10w_cut.txt'
    file_for_output = 'data\\2w_cut_test.txt'
    time_consuming = data_cut(file_for_input, file_for_output, 80001, 20000)
    print "Task 3:\n" \
          "input:%s \n" \
          "output: %s" % (file_for_input, file_for_output)
    print "Task had done!Time consuming is : %f" % time_consuming
    print "- - - - - - - - - - - - - - - - - - - - - - - - - - - "

