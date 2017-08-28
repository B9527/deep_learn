#!/usr/bin/python
# coding:utf-8

"""
dot文件转PDF命令dot -Tpdf all_data.dot -o output.pdf
根据CSV提供的数据使用决策ID3方法生成训练集预测
项目名：deeplearn - the name of the current project.
文件名：de_tree - the name of the new file which you specify in the New File dialog box during the file creation.
电脑：Administrator - baiyang
时间：2017/8/26 20:16 
IDE:PyCharm - the name of the IDE in which the file will be created.
"""
from sklearn.feature_extraction import DictVectorizer
import csv
from sklearn import tree, preprocessing
from sklearn.externals.six import StringIO

# 导入测试数据
all_data = open(r'all_data.csv', 'rb')
reader = csv.reader(all_data)
headers = reader.next()

print headers
feature_list = []
label_list = []

for row in reader:
    label_list.append(row[len(row) - 1])
    row_dict = {}
    for i in range(1, len(row) - 1):
        row_dict[headers[i]] = row[i]
    feature_list.append(row_dict)

print feature_list

vec = DictVectorizer()
dummyX = vec.fit_transform(feature_list).toarray()
print ("dummyX:" + str(dummyX))
print vec.get_feature_names()
print ("label_list:" + str(label_list))

lb = preprocessing.LabelBinarizer()
dummyY = lb.fit_transform(label_list)
print ("dummY:" + str(dummyY))

clf = tree.DecisionTreeClassifier(criterion="entropy")
clf = clf.fit(dummyX, dummyY)

print ("clf:" + str(clf))

with open("all_data.dot", 'w') as f:
    f = tree.export_graphviz(clf, feature_names=vec.get_feature_names(), out_file=f)


# 开始预测
oneRowX = dummyX[0, :]
print ("oneRowX:" + str(oneRowX))
newRowX = oneRowX
# 预测中年人的概率
oneRowX[0] = 0
oneRowX[1] = 1
newRowX[2] = 0
print ("newRowX:" + str(newRowX))

predictedY = clf.predict(newRowX)

print ("predictedY:" + str(predictedY))




