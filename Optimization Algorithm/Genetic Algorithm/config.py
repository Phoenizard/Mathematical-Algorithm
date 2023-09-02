# 定义遗传算法参数
maxgen = 300  # 最大迭代次数
sizepop = 100  # 种群大小
pcross = 0.5  # 交叉操作阈值
pmutation = 0.01  # 变异操作参数
bound = [[-5, 5], [-5, 5]]  # 定义域

lenchrom = 2  # 基因链长度


def myfunction(x):
    return 1 / (x[0] * x[0] + x[1] * x[1])
