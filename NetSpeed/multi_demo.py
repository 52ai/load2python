# coding:utf-8

import threading
from time import sleep, ctime
cnt = 10


def loop(flag, i):
    while 1:
        file_w = open("demo.txt", 'a+')
        # print "this is ", flag
        str_w = "this is " + str(flag)+"\n"
        file_w.writelines(str_w)
        file_w.close()
        sleep(1)


def main():
    threads = []
    for i in range(cnt):
        flag = i
        t = threading.Thread(target=loop, args=(flag, i))
        threads.append(t)

    for i in range(cnt):
        threads[i].start()
    while 1:
        pass


if __name__ == '__main__':
    main()