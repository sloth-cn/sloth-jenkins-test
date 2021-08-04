# -*- coding:utf-8 -*-
'''
Author: sloth-cn  sloth-cn@outlook.com
Date: 2021-08-04 20:13:51
LastEditTime: 2021-08-04 20:22:22
LastEditors: sloth-cn  sloth-cn@outlook.com
Description:
'''

import time

file = time.asctime(time.localtime(time.time()))
time_info = time.asctime(time.localtime(time.time()))

with open(file, 'a') as file_io:
    file_io.write(time_info)
