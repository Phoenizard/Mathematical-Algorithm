from iris import data, petalWidth, petalLength
import matplotlib.pyplot as plt
import numpy as np
import random
import math

def eucliDist(A, B):
    # 多维欧拉距离
    return '{:.10f}'.format(math.sqrt(sum([(a - b)**2 for (a,b) in zip(A,B)])))


def centerPoint(point_set):
    # 获取点的维度
    dim = len(point_set[0])
    res = []
    for i in range(dim):
        res.append(0)
    for i in range(dim):
        for j in point_set:
            res[i] += j[i]
    for i in range(dim):
        res[i] = res[i] / len(point_set)
    return res


def myKMeans(n_clusters):
    # key_index = random.sample(range(1, len(data)), n_clusters)
    key_index = [20, 80, 140]
    is_change = True
    key_point = []
    group = [[] for _ in range(n_clusters)]
    cmp = 0
    # 以n个关键点分组
    for i in range(n_clusters):
        group[i].append(data[key_index[i]])
        # i同时对应group与key
        key_point.append(data[key_index[i]])
    while is_change:
        # 遍历其余点
        for i in range(len(data)):
            # 与n个目标点比较
            tmp_dis = []
            for j in range(n_clusters):
                tmp_dis.append(eucliDist(key_point[j], data[i]))
            min_index = np.argmin(np.array(tmp_dis))
            group[min_index].append(data[i])

        # 计算每组的中心对象
        tmp_key_point = []
        for i in range(n_clusters):
            new_center = centerPoint(group[i])
            tmp_key_point.append(new_center)
            cmp += float(eucliDist(new_center, key_point[i]))
        # 比较中心点与目标点差异
        if cmp < 0.00002:
            is_change = False
            key_point = tmp_key_point
        else:
            is_change = True
            key_point = tmp_key_point
            cmp = 0
            for i in range(n_clusters):
                group[i][0] = key_point[i]
    return group, key_point


if __name__ == '__main__':
    n = 3
    g, k = myKMeans(n)
    predicted = []
    for i in data:
        for j in range(n):
            if i in g[j]:
                predicted.append(j)
                break
    print(len(data))
    print(len(predicted))

    colors_p = []
    for i in predicted:
        if i == 0:
            colors_p.append("red")
        elif i == 1:
            colors_p.append("blue")
        else:
            colors_p.append("green")

    plt.title("MyPredicted")
    plt.xlabel('petal length')
    plt.ylabel('petal width')
    plt.scatter(petalLength, petalWidth, c=colors_p)
    plt.show()
