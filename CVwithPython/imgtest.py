# coding:utf-8

"""
create on Mar 8, 2018 by Wayne using python 2.7.2
"""

from PIL import Image
image_file = Image.open("test.png")  # open colour image
image_file = image_file.convert('1')  # convert image to black and white
image_file.save('result.png')