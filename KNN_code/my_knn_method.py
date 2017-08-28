#!/usr/bin/python
# coding:utf-8

"""
项目名：deep_code - the name of the current project.
文件名：my_knn_method - the name of the new file which you specify in the New File dialog box during the file creation.
电脑：Administrator - baiyang
时间：2017/8/27 0:11 
IDE:PyCharm - the name of the IDE in which the file will be created.
"""
import csv
import math
import random
import operator


# 加载数据集方法
def loadDataset(filename, split, trainingSet=[], testSet=[]):
    with open(filename, 'rb') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset) - 1):
            for y in range(4):
                dataset[x][y] = float(dataset[x][y])
            if random.random() < split:
                trainingSet.append(dataset[x])
            else:
                testSet.append(dataset[x])


# 计算距离
def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += pow((instance1[x] - instance2[x]), 2)
    return math.sqrt(distance)


# 获取临近
def getNeighbors(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance) - 1
    for x in range(len(trainingSet)):
        dist = euclideanDistance(testInstance, trainingSet[x], length)
        distances.append((trainingSet[x], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors


# 获取结果
def getRespose(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        respose = neighbors[x][-1]
        if respose in classVotes:
            classVotes[respose] += 1
        else:
            classVotes[respose] = 1
    sortedVotes = sorted(classVotes.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]


# 计算准确率
def getAccuracy(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][-1] == predictions[x]:
            correct += 1
    return (correct / float(len(testSet))) * 100.0


def main():
    trainingSet = []
    testSet = []
    split = 0.67
    loadDataset(r'dataset', split, trainingSet, testSet)
    print ('Train set:' + repr(len(trainingSet)))
    print ('Test set:' + repr(testSet))

    predictions = []
    k = 3

    for x in range(len(testSet)):
        neighbors = getNeighbors(trainingSet, testSet[x], k)
        result = getRespose(neighbors)
        predictions.append(result)
        print ('> predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1]))
    accuracy = getAccuracy(testSet, predictions)
    print ('accuracy:' + repr(accuracy) + '%')


main()
