import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris     #从sklearn库中导入鸢尾花数据集

iris = load_iris()
X = iris.data
Y = iris.target
petalLength = []
petalWidth = []
colors_r = []
data = []

for i in X:
    data.append([i[2],i[3]])
    petalLength.append(i[2])
    petalWidth.append(i[3])
for i in Y:
    if i == 0:
        colors_r.append("red")
    elif i == 1:
        colors_r.append("blue")
    else:
        colors_r.append("green")

plt.xlabel('petal length')
plt.ylabel('petal width')
plt.scatter(petalLength,petalWidth, c=colors_r)
plt.title("Iris")

estimator = KMeans(n_clusters=3, n_init='auto').fit(data)                       #聚类
label_pred = estimator.labels_         #获取聚类标签
colors_p = []

for i in label_pred:
    if i == 0:
        colors_p.append("red")
    elif i == 1:
        colors_p.append("blue")
    else:
        colors_p.append("green")

plt.title("Predicted")
plt.xlabel('petal length')
plt.ylabel('petal width')
plt.scatter(petalLength,petalWidth, c=colors_p)

plt.show()