import numpy as np

# 准则重要性矩阵
A = np.array([[1, 2, 3, 5],
             [1 / 2, 1, 1 / 2, 2],
             [1 / 3, 2, 1, 2],
             [1 / 5, 1 / 2, 1 / 2, 1]])
[n, m] = A.shape

# 一致性检验
V, D = np.linalg.eig(A)

maxlam = np.max(V)
CI = (maxlam - n) / (n - 1)
RI = [0, 0, 0.58, 0.9, 1.12, 1.24, 1.32, 1.41, 1.45, 1.49, 1.52, 1.54, 1.56, 1.58, 1.59]
# 判断是否通过一致性检验
CR = CI / RI[n - 1]
if CR >= 0.1:
    print('没有通过一致性检验\n')
else:
    print('通过一致性检验\n')

# 计算权重
Asum = np.sum(A, axis=0)
Aprogress = A/(np.ones((n, 1), dtype=np.int64) * Asum)

W = np.average(Aprogress, axis=1)
