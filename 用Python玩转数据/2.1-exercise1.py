# coding:utf-8
import os

file= open("Blowing in the wind.txt", "r")
'''
str_body = """
How many roads must a man walk down
Before they call him a man
How many seas must a white dove sail
Before she sleeps in the sand
How many times must the cannon balls fly
Before they're forever banned
The answer my friend is blowing in the wind
The answer is blowing in the wind
"""
'''
str_head = "Blowin’ in the wind\n"
str_singer = "Bob Dylan\n"
str_foot = "\n1962 by Warner Bros. Inc."
str = str_head + str_singer
#file.write(str_body)
for line in file.readlines():
	str = str + line
str = str + str_foot
file.close

file = open("Blowing in the wind.txt", "w")
print str
file.write(str)

file.close()