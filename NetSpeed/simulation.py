# coding:utf-8
"""
create on Aug 14, 2018 by Wayne
Description:
部门宽带测速排队仿真任务
仿真目的：通过仿真，优化测试策略，使得一段时间内的服务器带宽利用率最高，测试用户最多

#宽带仿真任务编程实现流程梳理#
1）初始化客户端数据，生成服务器端等待队列线程及等待队列、执行队列线程及执行队列。

客户端表（模拟1000个客户端）client_table：0 u_id, 1 demand_width, 2 sum_test_times, 3 login_time, 4 next_request_time, 5 (execute_order_num)
其中
u_id，随机生成0001~1000的字符串，
sum_test_times初始化均为0，
login_time随机初始化为时间戳，
next_request_time则是当返回执行序列号execute_order_num 为0或-1时，将当前时间加上间隔时间interval（测试约定为60s），初始为NULL

等待队列线程中的等待队列waiting_queue:task_id, priority_dic, task_order_num, bandwidth, ttl
其中
task_id指的是任务的唯一标识，由u_id+当前时间戳组成
priority_dic包括test_times_per_time, sum_online_time, time_of_request，按此三者优先级依次递减顺序进行优先级计算排列
task_order_num指的是任务序列号，亦即在队列中的位置，亦即时间片的信息，用于计算执行序列号
bandwidth指的是用户测速带宽，在实际中服务器可知，在测试的时候可以从客户端表中去查
ttl指的是任务的生存时间，可以设为2个时间单位（比如在测试中时间间隔为60s,那么ttl可以设置为120s）

执行队列线程中的执行队列execute_queue:task_id, bandwidth, ttl
其中
task_id用于唯一标识任务，和等待队列中的task_id一致
bandwidth为用户需求带宽
ttl为任务在执行队列中的生存时间，可以设为两个时间单位（同等待队列中的ttl）
执行队列线程中的remain_bandwidth变量，用于标识当前执行池中的剩余的带宽，初始值为1000M,每次入队出队都需要更新这个值

2）循环读取客户端列表，向服务器中的的等待队列发起测试请求，每一次请求作为一个独立线程。
请求接口：u_id, sum_online_time, sum_test_times
其中
u_id亦即用以唯一确定发起请求的客户端，可在客户端列表中直接读取信息。后面任务唯一标识也需要用到它。
sum_online_time使用当前时间减去客户端表中的login_time获得
sum_test_times直接读取客户端列表中的信息即可

响应接口：execute_order_num
服务器端返回execute_order_num执行序列号，其中0标识允许，-1标识禁止或异常，1~max_waiting_queue则标识正在等待

3）服务器端等待队列处理客户端发起的测试请求

Add: 如果该请求，由新发起的测试任务（new_task），则将新任务插入到队列的合适位置
执行该操作与此任务后的所有任务序列号都增加
队尾任务如果超出队列允许的范围则可能被移除

插入位置为最优先且此时有充足带宽可执行，任务被直接移入执行环境中（给客户端返回0标识）
插入位置为最后且已经超出了等待队列允许的长度。（给客户端返回-1标识）

Confirm：如果该请求，由等待中的任务发起（confirm）,则需要确认是否轮到自己执行
任务已经最优先，任务可以被执行
任务需要等待， 则更新任务的生存时间，保证被再次确认前不会被自动清理
任务已经被移除，则需要通知终端终止本次任务

Remove：现阶段移除操作，主要是由于其他操作产生的附加操作
终端主动放弃（暂不实现）
任务超过生存周期被服务器自动清理
由于其他新增任务导致该任务顺位延后超出上限被移除
任务允许执行
排在此任务后的所有任务的序列号减小

4）服务器端执行队列（资源池）执行测试任务

当允许执行时，将任务移入执行队列
测试完成后，需要将任务移出执行队列
执行队列不规定长度，执行队列的本质是一个资源池，任务根据自身的带宽需求请求资源池空间。如果允许则执行，如果不允许则等待。
执行队列的任务有生存时间，需要定时清理超期的任务以释放资源。建议生存时间不超过两个单位时间。

"""
from numpy import random
import time
import threading

client_table = []  # 客户端信息表
client_cnt = 1000
remain_bandwidth = 1000  # 初始化剩余带宽数，测试时可设置为1000
waiting_queue = []  # 等待队列 task_id, priority_dic, task_order_num, bandwidth, ttl
max_len = 60  # 等待队列最大的长度
execute_queue = []  # 执行队列 task_id, bandwidth, ttl


def run_server():
    # print "run_server"
    # print remain_bandwidth
    time.sleep(1)
    print 'run_server DONE at:', time.ctime()


def send_request(u_id, sum_online_time, sum_test_times):
    # 开启一个独立的线程，用于处理客户端发出的请求, 并将处理的结果返回到client_table中
    print u_id, sum_online_time, sum_test_times
    # 下面开始处理逻辑

    # 对等待队列的处理
    # 对执行队列的处理


def main():
    # 1)
    # 初始化客户端表信息
    # 定义需要生成的客户端数
    tmp_list = []
    for n in range(1, client_cnt+1):
        # 获得u_id
        prefix_u_id = ''
        for i in range(0, len(str(client_cnt)) - len(str(n))):
            prefix_u_id += '0'
        u_id = prefix_u_id + str(n)
        # 随机产生一个客户端测速带宽，暂定60%为100M, 30%为50M, 10%20M
        demand_width = 0
        rand_p = random.rand()
        if rand_p <= 0.6:
            demand_width = 100
        elif rand_p <= 0.9:
            demand_width = 50
        else:
            demand_width = 10
        # 初始化单位时间内测试次数为0
        sum_test_times = 0

        # 初始化login_time，以时间戳的形式存储
        t1 = time.time()  # 当前时间
        t2 = t1 - 1000  # 往前1000s作为开始时间戳
        t = random.randint(t2, t1)  # 在开始和结束时间戳中随机取出一个
        # print time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(t))  # 将时间戳转换为时间的形式，但实际上，在表里面可以直接存时间戳单位为s

        # 初始化next_request_time, 初始化为0，表示立刻发送请求
        next_request_time = 0

        # print u_id, demand_width, sum_test_times, t, next_request_time
        tmp_list.append(u_id)
        tmp_list.append(demand_width)
        tmp_list.append(sum_test_times)
        tmp_list.append(t)
        tmp_list.append(next_request_time)

        # 考虑需要对客户端的每次请求，返回相应的标识，因此在客户端信息表中添加execute_order_num字段，初始值为-2,代表的是初始状态
        execute_order_num = -2
        tmp_list.append(execute_order_num)

        # 将生成的客户端记录存入client_table中
        client_table.append(tmp_list)
        tmp_list = []  # 将临时list置空

    print client_table  # 输出生成的客户端信息表

    print 'start at:', time.ctime()
    # 创建服务器端队列线程
    ts = threading.Thread(target=run_server)
    ts.start()
    # print ts.is_alive()
    time.sleep(2)
    print 'all DONE at:', time.ctime()

    # 2)循环读取客户端列表，向服务器端的等待队列发起测试请求，每个请求都是独立线程
    threads = []  # 存储客户端请求线程
    cnt = 1
    while cnt <= 1000:
        u_id = client_table[cnt-1][0]
        sum_online_time = time.time() - client_table[cnt-1][3]
        sum_test_times = client_table[cnt-1][2]
        ts = threading.Thread(target=send_request, args=(u_id, sum_online_time, sum_test_times))
        ts.start()
        threads.append(ts)
        # 如果扫描客户端表到了最后则重新执行，发送请求
        cnt += 1
        if cnt == 1000:
            cnt = 1

if __name__ == '__main__':
    main()

