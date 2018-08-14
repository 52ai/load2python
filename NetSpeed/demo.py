# coding:utf-8

a = [1, 2, 3, 4, 5]
b = [10, 10, 10, 10, 10]
c = [0.1, 0.2, 0.3, 0.4, 0.5]

list_queue_a = [1.0, 1.0]
list_queue_b = [1, 2400]

cnt = 0
flag = 0
while cnt <10000:
    pro1 =  list_queue_a[0]/list_queue_b[0]
    pro2 =  list_queue_a[1]/list_queue_b[1]
    if pro1 < pro2:
        list_queue_a[0] += 1
        list_queue_a[1] += 6
        list_queue_b[1] += 6
        flag = 1
    else:
        list_queue_b[0] += 1
        list_queue_b[1] += 6
        list_queue_a[1] += 6
        flag = 0

    if flag == 1:
        print "输出优先级", "a=", pro1, " b=", pro2, "cnt=", cnt

    cnt += 1