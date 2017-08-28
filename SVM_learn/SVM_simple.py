#!/usr/bin/python
# coding:utf-8

"""
项目名：deep_code - the name of the current project.
文件名：SVN_simple - the name of the new file which you specify in the New File dialog box during the file creation.
电脑：Administrator - baiyang
时间：2017/8/27 12:59 
IDE:PyCharm - the name of the IDE in which the file will be created.
"""
from sklearn import svm
x = [[2, 0], [1, 1],[2, 0.5], [2, 3]]
y = [0, 0, 0, 1]
clf = svm.SVC(kernel='linear')
clf.fit(x, y)

print clf
# 支持向量
print clf.support_vectors_
# 原数据支持向量的索引
print clf.support_

# 各分类中支持向量的个数
print clf.n_support_
