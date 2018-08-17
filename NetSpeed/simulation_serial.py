# coding:utf-8
"""
create on Aug 14, 2018 by Wayne
Description:
部门宽带测速排队仿真任务
仿真目的：通过仿真，优化测试策略，使得一段时间内的服务器带宽利用率最高，测试用户最多

#宽带仿真任务编程实现流程梳理#
1）初始化客户端数据，生成服务器端等待队列线程及等待队列、执行队列线程及执行队列。

客户端表（模拟1000个客户端）client_table：0 u_id, 1 demand_width, 2 sum_test_times, 3 login_time, 4 next_request_time, 5 (execute_order_num)
6（request_times）
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
请求接口：0 u_id, 1 sum_online_time, 2 sum_test_times, 3 (bandwidth)
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
import csv

# client_table：0 u_id, 1 demand_width, 2 sum_test_times, 3 login_time, 4 next_request_time, 5 (execute_order_num)
client_table = []  # 客户端信息表
client_cnt = 10000
total_bandwidth = 1000  # 总的带宽数，测试时可设置为1000
waiting_queue = []  # 等待队列 task_id, priority_dic, task_order_num, bandwidth, ttl

# 等待队列最大的长度，用最长等待时间间隔/单个测试完成时间， 再乘以每个时间片可以执行的任务数（仿真时一个时间片1s）
# 此外这个队列还得按时间片分片，客户端需要知道第几个时间片可以轮到它, 需要设计算法
# 仿真时，可以假设每10个一个时间片即execute_order_num = task_order_num/10
max_len_queue = 20  # 共20个时间片，每个时间片可以大致排10个
execute_queue = []  # 执行队列 task_id, bandwidth, ttl
max_waiting_time = 10  # 最长等待时间间隔20s
per_time = 2  # 单次执行时间

simulation_time = 10  # 仿真时间，单位为min
# 仿真时，需要采集的统计数据，bandwidth_usage_coefficient
bandwidth_usage = []  # [time, usage_rate]

"""
程序已写好，开始控制变量做仿真实验

第一轮公共参数：
max_len_queue = 300  # 等待队列的最大长度
max_waiting_time 20  # 最长等待时间，单位s
per_time = 2  # 单次执行时间，单位s

共测试了
1K用户的1min,2min,10min
1W用户的1min
6W用户的1min
6w用户的10min

第二轮公共参数，需要讨论，针对用户量大的情况下做相应的修改

假如1万个用户（全部执行1次大致需要2000s）

max_len_queue = 3000  # 等待队列的最大长度 < （最长等待时间 / 单次执行时间 ）*单个时间片可执行任务数
max_waiting_time 60   # 最长等待时间，单位s
per_time = 2  # 单次执行时间，单位s
"""


def run_server():
    # print "run_server"
    # print remain_bandwidth
    time.sleep(1)
    print 'run_server DONE at:', time.ctime()


def priority_bigger(cmp_curr, cmp_i):
    # 对任务的优先级进行比较
    # 如果cmp_curr的优先级大于cmp_i则返回True
    if cmp_curr[1][0] < cmp_i[1][0]:
        # print "cmp_curr[1][0]:", cmp_curr[1][0]
        # print "cmp_i[1][0]:", cmp_i[1][0]
        return True  # 单位时间内测试次数越少，优先级越高
    elif cmp_curr[1][0] > cmp_i[1][0]:
        # print "cmp_curr[1][0]:", cmp_curr[1][0]
        # print "cmp_i[1][0]:", cmp_i[1][0]
        return False
    else:
        # print "eq_cmp_curr[1][0]:", cmp_curr[1][0]
        # print "eq_cmp_i[1][0]:", cmp_i[1][0]
        # 在线时间越长的，优先级越高
        if cmp_curr[1][1] > cmp_i[1][1]:
            return True
        elif cmp_curr[1][1] < cmp_i[1][1]:
            return False
        else:
            # 先发起请求的，优先级越高
            if cmp_curr[1][2] < cmp_i[1][2]:
                return True
            else:
                return False


def send_request(u_id, sum_online_time, sum_test_times, bandwidth):
    print "log_request:Current waiting queue len is :  %s" % len(waiting_queue)
    # print waiting_queue
    print "log_request:Current executing queue len is :  %s" % len(execute_queue)
    # print execute_queue
    # 本方法处理的事一个新的请求连接
    # 开启一个独立的线程，用于处理客户端发出的请求, 并将处理的结果返回到client_table中
    # print u_id, sum_online_time, sum_test_times
    # 下面开始处理逻辑，主要包含了等待队列的处理逻辑和执行队列的处理逻辑
    task_info = []   # task_info用于存储单条用户信息
    priority_dic = []
    # 生成当前任务信息:0 task_id, 1 priority_dic, 2 task_order_num, 3 bandwidth, 4 ttl
    # 其中priority_dic:test_times_per_time, sum_online_time, time_of_request
    task_id = u_id + str(time.time())
    test_times_per_time = float(sum_test_times) / sum_online_time
    priority_dic.append(test_times_per_time)  # 单位时间内测试次数
    priority_dic.append(sum_online_time)  # 客户端总在线时间
    priority_dic.append(time.time())  # 请求到达时间
    task_order_num = -2  # 任务序列号初始值为-2 ,后面执行插入操作后，需要更新
    ttl = time.time()  # ttl 存的是任务生成时间，建议最大生生存长度为2个时间单位，仿真时使用2个最大等待时间间隔
    # 构造task_info
    task_info.append(task_id)
    task_info.append(priority_dic)
    task_info.append(task_order_num)
    task_info.append(bandwidth)
    task_info.append(ttl)
    # print task_info
    # 对等待队列的处理
    # 如果当前等待队列的长度小于max_queue_len，则修改task_order_num，直接往队列里添加信息
    # task_order_num的确定可以做两次扫队列
    # 第一次扫队列，找到优先级比当前任务大或者等于的任务个数pre_n, 那么task_order_num = pre_n + 1
    # 第二次扫队列，把所有task_order_num 大于当前任务task_order_num的值，都做+1操作（以及优先级的小的序号变大1）
    if len(waiting_queue) < max_len_queue:
        # 第一次扫队列
        pre_n = 0
        for i in xrange(len(waiting_queue)):
            # print i
            if not priority_bigger(task_info, waiting_queue[i]):
                # 找出队列中，不小于当前task_info优先级的任务数
                pre_n += 1
        task_order_num = pre_n + 1
        # print task_order_num
        # 第二次扫描队列
        for i in xrange(len(waiting_queue)):
            if waiting_queue[i][2] >= task_order_num:
                waiting_queue[i][2] += 1
        task_info[2] = task_order_num
        # 将当前任务信息入到等待队列中
        waiting_queue.append(task_info)
        # print waiting_queue
        # 处理完成后，返回测试标识，本次处理应为等待，标识码test_flag = task_order_num / 10
        # 仿真时，测试码的返回直接通过修改client_table中execute_order_num来实现
        # 通过u_id去找到当前请求客户端表中的下标，进而修改execute_order_num的值
        # print int(u_id)
        # 这里有个问题:初始化的时候，前十个测试标识码会一直是0，但是客户端会发起新的请求
        if task_order_num / 10 == 0:
            client_table[int(u_id) - 1][5] = 1
        else:
            client_table[int(u_id) - 1][5] = task_order_num / 10  # 返回测试请求标识码

    # 如果当前等待队列的长度大于等于max_queue_len，则表示队列已满，比较优先级，再判断是否入队，或者丢弃
    else:
        # 用task_info中的priority字段，进行优先级定位
        # 这里做一次队列扫描
        # 扫描队列，找到优先级比当前任务大于或等于的个数pre_n，定位队尾元素的index(即task_order_num为max_len_queue)
        # 判断pre_n
        # 如果pre_n < max_len_queue，那么执行插入操作，并移除队尾的那个任务，插入和移除均返回测试标识码
        # 如果pre >= max_len_queue, 一定是等于，也算是说优先级都比他高或者等于，则丢弃此次任务，并返回标识码-1

        # 扫描队列
        pre_n = 0
        tail_index = 0  # 记录优先级最小那个任务的下标
        for i in xrange(len(waiting_queue)):
            # 只要task_info优先级不比队列中待比较的大，则pre自加1
            if not priority_bigger(task_info, waiting_queue[i]):
                pre_n += 1
            if waiting_queue[i][2] == max_len_queue:
                # 找到优先级最小那个任务的下标
                tail_index = i
                # print "find minimum priority :%s" % waiting_queue[i]
        # 判断pre_n
        if pre_n < max_len_queue:
            task_order_num = pre_n + 1
            # 在执行插入操作之前，先将优先级最小的那个任务移除
            # 通知客户端（task_id前len(client_cnt)个数，获得u_id,进而确定某个客户端），返回标识码为-1
            del_u_id = waiting_queue[tail_index][0][0:len(str(client_cnt))]
            client_table[int(del_u_id) - 1][5] = -1
            # 修改下一次发起请求的时间
            client_table[int(del_u_id) - 1][4] = time.time() + max_waiting_time
            # 移除该任务
            del waiting_queue[tail_index]

            # 扫描队列，将所有序号比当前任务大的（即优先级比当前任务小的）任务的task_order_num的值都自增1
            for i in xrange(len(waiting_queue)):
                if waiting_queue[i][2] >= task_order_num:
                    waiting_queue[i][2] += 1

            # 执行插入操作
            task_info[2] = task_order_num
            waiting_queue.append(task_info)
            # 通知客户端，返回测试请求标识码
            # 等待队列满的时候，此处也有可能优先级排在前面10，使得返回的时间片信息为0
            if task_order_num / 10 == 0:
                client_table[int(u_id) - 1][5] = 1
            else:
                client_table[int(u_id) - 1][5] = task_order_num / 10  # 返回测试请求标识码
        else:
            # 如果第一次请求的时候，队列中所有的任务的优先级均大于当前任务
            pass

    # 对执行队列的处理
    # 判断剩余带宽数，如果剩余且当前任务的返回码为0，则加上时间戳放入到执行队列中
    # 在主线程中，新建一个独立线程，去扫描执行队列，模拟测速的过程，时间到了就清除队列
    execute_queue_item = []  # task_id, bandwidth, ttl
    bandwidth_usge_item = []  # time, usage_rate
    # 扫描执行队列，清理已经执行完的带宽，并计算获得剩余带宽数
    remain_bandwidth = total_bandwidth
    j = 0  # 控制执行队列删除元素
    for i in xrange(len(execute_queue)):
        if (time.time() - execute_queue[i-j][2]) >= per_time:
            # 该任务已执行完成，需要移除队列
            # 任务执行完成，移除执行队列之前，需要修改该对应客户端的成功测试次数
            del_u_id = execute_queue[i-j][0][0:len(str(client_cnt))]
            client_table[int(del_u_id) - 1][2] += 1  # 成功测试此时+1
            client_table[int(del_u_id) - 1][5] = 0  # 修改execute_order_num = 0
            client_table[int(del_u_id) - 1][4] = time.time() + max_waiting_time  # 修改下次执行时间 = 当前时间戳 + 最大等待时间
            print "update test_times_per_time, u_id: %s" % del_u_id
            del execute_queue[i-j]
            j += 1
            # 此处出执行队列需要通知客户端完成执行操作
            # 修改sum_test_times
            # 修改execute_order_num = 0
            # 修改下次执行时间 = 当前时间戳 + 最大等待时间
        else:
            # 否则，计算剩余带宽数
            remain_bandwidth = remain_bandwidth - execute_queue[i-j][1]
            # print "log: remain bandwidth: %s" % remain_bandwidth
    """
    采集带宽利用率
    """
    usage_rate = float(total_bandwidth-remain_bandwidth) / total_bandwidth
    bandwidth_usge_item.append(time.time())
    bandwidth_usge_item.append(usage_rate)
    bandwidth_usage.append(bandwidth_usge_item)
    print "request remain bandwidth: %s usage rate: %s" % (remain_bandwidth, usage_rate)

    if (bandwidth < remain_bandwidth) and (task_info[2]/10 == 0):
        print "Put task from waiting queue to execute queue!"
        # 如果还有剩余带宽，且当前任务执行序列号为0 ，则立即执行
        # 任务入执行队列，并将其从等待队列中删除
        # 任务入执行队列
        execute_queue_item.append(task_id)
        execute_queue_item.append(bandwidth)
        execute_queue_item.append(time.time())
        execute_queue.append(execute_queue_item)  # 入队
        # 将该任务从等待队列中删除
        # 利用task_info中的task_id进行定位当前任务
        # 删除之后需要更新当前等待队列的任务序列号
        for i in xrange(len(waiting_queue)):
            if waiting_queue[i][0] == task_id:
                del_task_order_num = waiting_queue[i][2]
                del waiting_queue[i]
                # 更新当前等待队列的任务序列号,所有号比他大的都需要减1
                for j in xrange(len(waiting_queue)):
                    if waiting_queue[j][2] <= del_task_order_num:
                        waiting_queue[j][2] -= 1
            # 通知客户端，返回测试标识请求码

            break  # 跳出当前循环


def send_confirm(u_id, sum_online_time, sum_test_times, bandwidth):
    print "log_confirm:Current waiting queue len is :  %s" % len(waiting_queue)
    # print waiting_queue
    print "log_confirm:Current executing queue len is :  %s" % len(execute_queue)
    # print execute_queue
    # 本方法用于处理客户端发送的确认请求信息
    # 既然是确认请求信息，那么该请求应该是在等待队列中
    # 第一步根据u_id，找到对应的任务记录，若存在则进行第二步，如不存在则返回测试标识码-1
    # 第二步，判断task_order_num / 10 （即执行序列号）,如果为0，则立即执行，如果不是0，则返回相对应的状态标识码
    # 其中执行操作，需要做入执行队列，并从等待队列中删除，返回状态标识0，修改下一次请求时间，更新等待序列的序列号
    loc = -1
    for i in xrange(len(waiting_queue)):
        if waiting_queue[i][0][0:len(str(client_cnt))] == u_id:
            # 找到了
            loc = i
    # print "find confirm task loc: %s" % loc
    if loc == -1:
        # 没有找到
        # 给客户端返回-1，其且修改下一次访问时间
        # print "not find confirm task, u_id: %s" % u_id
        client_table[int(u_id)-1][5] = -1
        client_table[int(u_id)-1][4] = time.time() + max_waiting_time
    else:
        # print "waiting_queue[loc][2]: %s" % waiting_queue[loc][2]
        # 否则就是找到了
        # 扫描执行队列，获得剩余带宽数
        remain_bandwidth = total_bandwidth

        j = 0  # 控制删除执行队列中的元素
        for i in xrange(len(execute_queue)):
            if (time.time() - execute_queue[i-j][2]) >= per_time:
                # 该任务已执行完成，需要移除队列
                # 任务执行完成，移除执行队列之前，需要修改该对应客户端的成功测试次数
                del_u_id = execute_queue[i-j][0][0:len(str(client_cnt))]
                client_table[int(del_u_id)-1][2] += 1  # 成功测试此时+1
                client_table[int(del_u_id)-1][5] = 0  # 修改execute_order_num = 0
                client_table[int(del_u_id)-1][4] = time.time() + max_waiting_time  # 修改下次执行时间 = 当前时间戳 + 最大等待时间
                print "update confirm execute success, u_id: %s" % del_u_id
                del execute_queue[i-j]
                j += 1
                # 此处出执行队列需要通知客户端完成执行操作
            else:
                # 否则该任务为执行完成，计算剩余带宽数
                remain_bandwidth = remain_bandwidth - execute_queue[i-j][1]
        execute_queue_item = []  # task_id, bandwidth, ttl
        bandwidth_usge_item = []  # time, usage
        """
           采集带宽利用率
           """
        usage_rate = float(total_bandwidth - remain_bandwidth) / total_bandwidth
        bandwidth_usge_item.append(time.time())
        bandwidth_usge_item.append(usage_rate)
        bandwidth_usage.append(bandwidth_usge_item)
        print "request remain bandwidth: %s usage rate: %s" % (remain_bandwidth, usage_rate)

        if (waiting_queue[loc][2] / 10 == 0)and (bandwidth < remain_bandwidth):
            # 条件符合，立即执行
            # 任务入执行队列，并将其从等待队列中删除
            # 任务入执行队列
            execute_queue_item.append(waiting_queue[loc][0])  # 获得任务的task_id
            execute_queue_item.append(bandwidth)
            execute_queue_item.append(time.time())
            execute_queue.append(execute_queue_item)  # 入队
            # 将该任务从等待队列中删除
            # 利用task_id进行定位当前任务
            # 删除之后需要更新当前等待队列的任务序列号
            del_task_order_num = waiting_queue[loc][2]
            del waiting_queue[loc]
            # 更新当前等待队列的任务序列号,所有号比他大的都需要减1
            for i in xrange(len(waiting_queue)):
                if waiting_queue[i][2] >= del_task_order_num:
                    waiting_queue[i][2] -= 1
                # break  # 跳出当前循环
            # 通知客户端，返回测试标识码,并修改下次发请求的时间
            # client_table[int(waiting_queue[loc][0][0:len(str(client_cnt))]) - 1][5] = 0
            # client_table[int(waiting_queue[loc][0][0:len(str(client_cnt))]) - 1][4] = time.time() + max_waiting_time
        else:
            # 应该分两种情况，一种是资源不足，第二种没有在时间片为0的区域
            # 找到了，但仍排着队或资源池不足
            # 直接返回测试标识码，啥也不做，等待客户端发起下一轮请求
            # print int(waiting_queue[loc][0][0:len(str(client_cnt))])
            # client_table[int(waiting_queue[loc][0][0:len(str(client_cnt))]) - 1][5] = waiting_queue[loc][2] / 10

            if (waiting_queue[loc][2]/10) == 0:
                client_table[int(waiting_queue[loc][0][0:len(str(client_cnt))]) - 1][5] = 1
            else:
                client_table[int(waiting_queue[loc][0][0:len(str(client_cnt))]) - 1][5] = waiting_queue[loc][2] / 10

            """
            此处返回的肯定是0，客户端发送的应该是立即确认的请求
            可以暂时返回1，小间隔时间立刻方发送confirm
            """


def write_file(file_name, file_list):
    # 写文件
    with open(file_name, "wb") as fw:
        writer = csv.writer(fw)
        for item in file_list:
            writer.writerow(item)
    print "write file: %s DONE!" % file_name


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
        # print time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(t))  # 将时间戳转换为时间的形式

        # 初始化next_request_time, 初始化为0，表示立刻发送请求
        next_request_time = 0
        # 考虑需要对客户端的每次请求，返回相应的标识，因此在客户端信息表中添加execute_order_num字段，初始值为-2,代表的是初始状态
        execute_order_num = -2
        # 考虑到需要统计，每个客户端在给定时间内发起请求的次数，因此在用户表中加入统计请求的次数的字段,初始为0
        request_times = 0

        tmp_list.append(u_id)
        tmp_list.append(demand_width)
        tmp_list.append(sum_test_times)
        tmp_list.append(t)
        tmp_list.append(next_request_time)
        tmp_list.append(execute_order_num)
        tmp_list.append(request_times)
        # 将生成的客户端记录存入client_table中
        client_table.append(tmp_list)
        tmp_list = []  # 将临时list置空
    # client_table:u_id, demand_width, sum_test_times, login_time, next_request_time, execute_order_num
    print "1.Generation Client Table:\n", client_table  # 输出生成的客户端信息表
    print "client_table:u_id, demand_width, sum_test_times, login_time, next_request_time, execute_order_num"
    """
    print 'start at:', time.ctime()
    # 创建服务器端队列线程
    ts = threading.Thread(target=run_server)
    ts.start()
    # print ts.is_alive()
    time.sleep(2)
    print 'all DONE at:', time.ctime()
    """
    # 2)循环读取客户端列表，向服务器端的等待队列发起测试请求，每个请求都是独立线程
    # 记录程序开始的时间
    start_time = time.time()
    print "2.Loop Read Client and Send Request:"
    # threads = []  # 存储客户端请求线程
    cnt = 1
    while cnt <= (client_cnt + 1):
        # print waiting_queue
        u_id = client_table[cnt-1][0]
        sum_online_time = time.time() - client_table[cnt-1][3]
        sum_test_times = client_table[cnt-1][2]

        band_width = client_table[cnt-1][1]
        next_request_time = client_table[cnt-1][4]
        execute_order_num = client_table[cnt-1][5]
        # 扫描客户端表发起请求
        # 如果客户端表中execute_order_num为-2，则代表初始状态，直接发起测试请求
        if execute_order_num == -2:
            send_request(u_id, sum_online_time, sum_test_times, band_width)
            client_table[cnt-1][6] += 1  # 记录发起请求的次数
            # print "flag :%s ,create client request and send request: %s %s %s %s " % (execute_order_num, u_id, sum_online_time, sum_test_times, band_width)
        # 如果客户端表中execute_order_num为-1,0，则代表测试成功或者测试异常状态，等待下一轮时间开启
        # 可从next_request_time中获取信息
        elif execute_order_num == 0 or execute_order_num == -1:
            # 如果条件成立，则判断是否到了下一轮测试的时间，如果到了，则发起新的测试请求
            if time.time() >= next_request_time:
                send_request(u_id, sum_online_time, sum_test_times, band_width)
                client_table[cnt - 1][6] += 1  # 记录发起请求的次数
                # print "flag :%s ,create client request and send request: %s %s %s %s " % (execute_order_num, u_id, sum_online_time, sum_test_times, band_width)
            else:
                # 否则还没到下一轮测试时间，直接跳过,输出日志
                pass
                # print "flag: %s, Wait to Send Request, u_id: %s" % (execute_order_num, u_id)
        # 如果客户端表中execute_order_num为1~max_len_queue中的数，则表示该客户端已经在排着队
        # 此时发送的应该是确认信息
        # 请求策略为判断next_request_time字段，如果已经到达该时间，则发起请求，并设置下一次请求时间
        # 设置下一次请求时间的策略为：
        # 最长排队时间 = execute_order_num * 单个测试时间（实际约为1min, 测试时刻定义为1s）
        # 为防止可以提前排上队执行，但是没有排的情况，需要缩短这个间隔时间，不必按最长排队时间进行发起请求
        # 可以每次取当前最长排队时间的中间值进行，重新设定下一次请求时间（拍脑袋的，与三等分，六等分实际上意思一样）
        else:
            if time.time() >= next_request_time:
                send_confirm(u_id, sum_online_time, sum_test_times, band_width)
                client_table[cnt - 1][6] += 1  # 记录发起请求的次数
                # print "flag :%s ,create client confirm and send confirm: %s %s %s %s " % (execute_order_num, u_id, sum_online_time, sum_test_times, band_width)
            # 如果还未到达下一次发起请求的时间，则重新设置下一次请求时间为当前最长排队时间的中间值
            else:
                client_table[cnt-1][4] = time.time() + (execute_order_num * 1)/100  # 重新设置下一次请求确认时间
                # print "flag: %s, Set Next Request Time, uid: %s" % (execute_order_num, u_id)

        # 如果扫描客户端表到了最后则重新执行，发送请求
        cnt += 1
        if cnt == (client_cnt + 1):
            cnt = 1
            print "New Scan And Client Table:\n", client_table
            print "Waiting Queue:\n", waiting_queue
            print "Execute Queue:\n", execute_queue
        # 获取系统的当前时间
        curr_time = time.time()
        if (curr_time - start_time) / float(60) >= simulation_time:
            print "Time is over, exit simulation!"
            # print "bandwidth_usage:\n", bandwidth_usage
            write_file("bandwidth_usage.csv", bandwidth_usage)
            # print "client_table:\n", client_table
            write_file("client_table.csv", client_table)
            break


if __name__ == '__main__':
    try:
        main()
    except BaseException as e:
        print "Exit: %s" % e


