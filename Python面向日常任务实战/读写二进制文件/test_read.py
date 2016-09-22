# coding:utf-8

f = open('..//README.md', 'r')
lines = f.readlines()

for line in lines:
    print line

f.close()
