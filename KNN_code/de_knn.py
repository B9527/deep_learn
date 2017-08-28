#!/usr/bin/python
# coding:utf-8

"""
项目名：deep_code - the name of the current project.
文件名：de_knn - the name of the new file which you specify in the New File dialog box during the file creation.
电脑：Administrator - baiyang
时间：2017/8/26 23:34 
IDE:PyCharm - the name of the IDE in which the file will be created.
"""
import math


def ComputerEuclideanDistance(x1, y1, x2, y2):
    d = math.sqrt(math.pow((x1 - x2), 2) + math.pow((y1 - y2), 2))
    return d

d_ag = ComputerEuclideanDistance(3,104,18,89)
print ("d_ag:" + str(d_ag))
