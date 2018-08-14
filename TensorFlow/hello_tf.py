# coding:utf-8
"""
create on April 19,2018 by Wayne
"""
import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))