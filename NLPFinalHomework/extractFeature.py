# -*- coding:utf-8 -*-

"""
create on July 6,2016
@author:Wayne
Function:对已经做好中文分词的文本进行特征提取

方案一：

SMSLen,SPNumber,PhoneNumber,BankNumber,URL,【Classification】

方案二：

SMSLen,SPNumber,PhoneNumber,BankNumber,URL,SpamWord,【Classification】
"""
import time


def extract_feature_5(input_file, output_file):
    time_start = time.clock()
    sms_len, sp_number, phone_number, bank_number, url = '0', '0', '0', '0', '0'
    # sms_len, number, url = 'short', '0', '0'
    fr = open(input_file, 'r')
    fw = open(output_file, 'w')
    for line in fr.readlines():
        line = line.split('\t')
        classification = 'no'
        if line[1] == '1':
            classification = 'yes'
        sms_content = line[2]
        if len(sms_content.decode('utf8')) > 65:
            sms_len = '1'
        if "xxxxxxxx" in sms_content:
            sp_number = '1'
        if "xxxxxxxxxxx" in sms_content:
            phone_number = '1'
        if "xxxxxxxxxxxxxxxxxxx" in sms_content:
            bank_number = '1'
        if "www" in sms_content:
            print sms_content
            url = '1'
        fw.write(sp_number+"\t"+phone_number+"\t"+bank_number+"\t"+url+"\t"+sms_len+"\t"+classification+"\t"+"\n")
        sms_len, sp_number, phone_number, bank_number, url = '0', '0', '0', '0', '0'
    fw.close()
    fr.close()
    time_end = time.clock()
    return time_end - time_start

if __name__ == "__main__":
    print "- - - - - - - - - - - - - - - - - - - - - - - - - - - "
    file_for_input = 'data\\8w_cut_train.txt'
    file_for_output = 'data\\8w_cut_train.txt_feature.txt'
    time_consuming = extract_feature_5(file_for_input,file_for_output)
    print "Task 1:\n" \
          "input:%s \n" \
          "output: %s" % (file_for_input, file_for_output)
    print "Task had done!Time consuming is : %f s" % time_consuming
    print "- - - - - - - - - - - - - - - - - - - - - - - - - - - "
    file_for_input = 'data\\2w_cut_test.txt'
    file_for_output = 'data\\2w_cut_test.txt_feature.txt'
    time_consuming = extract_feature_5(file_for_input,file_for_output)
    print "Task 2:\n" \
          "input:%s \n" \
          "output: %s" % (file_for_input, file_for_output)
    print "Task had done!Time consuming is : %f s" % time_consuming
    print "- - - - - - - - - - - - - - - - - - - - - - - - - - - "
    file_for_input = 'data\\80w_train.txt'
    file_for_output = 'data\\80w_train.txt_feature.txt'
    time_consuming = extract_feature_5(file_for_input,file_for_output)
    print "Task 3:\n" \
          "input:%s \n" \
          "output: %s" % (file_for_input, file_for_output)
    print "Task had done!Time consuming is : %f s" % time_consuming
    print "- - - - - - - - - - - - - - - - - - - - - - - - - - - "
