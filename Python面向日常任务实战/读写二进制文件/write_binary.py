# coding:utf-8

import struct
import binascii

a = 1024000000
a_bytes = struct.pack('i', a)
a, = struct.unpack('i', a_bytes)
print a

print binascii.b2a_hex(u"你好啊！".encode("utf-8"))
print binascii.b2a_hex(u"你好啊！".encode("gbk"))


print binascii.a2b_hex("e4bda0e5a5bde5958aefbc81")






