# coding:utf-8

import sys
import time
'''
create on 2016 Sep.21 by Wayne

处理要求：

对每132个字节进行如下操作：

操作1：删除这132个字节后面的8个字节
操作2：在操作1的基础上再在后面添加16个字节，每个字节都是FF 

'''

# f_in_name = '20160528夜班-处理前1032数据.dat'

f_in_name = sys.argv[1] # 获取需要处理的文件名

temp = f_in_name.split('.') # 将输入的文件名按照.进行切分
f_out_name_1 = temp[0][0:15]+"处理后1032数据-1."+temp[1]
f_out_name_2 = temp[0][0:15]+"处理后1032数据-2."+temp[1]

f_in = open(f_in_name, 'rb')
f_out_1 = open(f_out_name_1, 'wb') # 输出文件1 操作1
f_out_2 = open(f_out_name_2, 'wb') # 输出文件2 操作1+操作2 

print "开始处理数据："
print "--------------------------------"
print "数据处理中......"
startTime = time.time()

buf = f_in.read(1024)

# 行计数
buf_count = 0

while (buf):
	
	# print "开始读取1024个字节的数据并存入文件"
	f_out_1.write(buf) 
	f_out_2.write(buf)

	# 操作1：利用读取操作进行删除末尾8个字节
	f_in.read(8)
	# print "删除接下来8个字节"

        # 操作2：在末尾添加16个字节FF补足140位 
	for i in range(0, 16): # write 16 bytes FF
		f_out_2.write(chr(255))
	#print "写入16个字节的FF"
	#print "--------------------------------"
	buf = f_in.read(1024)
	'''
	buf_count += 1
	if buf_count == 2:
		break
	'''
print "--------------------------------"
endTime = time.time()
print "数据处理完成！程序运行耗时：%s s" %(endTime - startTime)
f_out_1.close()
f_out_2.close()
f_in.close()	


