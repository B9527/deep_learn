#!/usr/bin/python
# coding:utf-8

"""
项目名：deep_code - the name of the current project.
文件名：knn_learn - the name of the new file which you specify in the New File dialog box during the file creation.
电脑：Administrator - baiyang
时间：2017/8/26 23:55 
IDE:PyCharm - the name of the IDE in which the file will be created.
"""

from sklearn import neighbors
from sklearn import datasets

knn = neighbors.KNeighborsClassifier()
# sklearn自带的数据集
iris = datasets.load_iris()

print iris
for i in iris['data'][:50]:

    print str(i).replace('[' ,'').replace(']', '').replace('  ',',').strip()+',setosa'
for i in iris['data'][51:100]:
    print str(i).replace('[' ,'').replace(']', '').replace('  ',',').strip()+',versicolor'
for i in iris['data'][100:150]:
    print str(i).replace('[' ,'').replace(']', '').replace('  ',',').strip()+',virginica'


knn.fit(iris.data, iris.target)
# 给定数据分类
predictedLabel = knn.predict([0.1, 0.2, 0.3, 0.4])

# ['setosa', 'versicolor', 'virginica'] 0 1 2
print predictedLabel
