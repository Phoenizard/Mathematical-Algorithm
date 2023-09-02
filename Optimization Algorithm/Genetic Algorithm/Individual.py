import random
from config import lenchrom, bound, myfunction, maxgen


class Individuals:
    chrom = []  # 存放基因序列
    fitness = 0  # 适应度

    def __init__(self):
        self.chrom = []
        for i in range(lenchrom):
            r = abs(bound[i][1] - bound[i][0]) * random.random() + bound[i][0]
            self.chrom.append(r)
        self.fitness = myfunction(self.chrom)

    def check(self):
        flag = True
        for i in range(lenchrom):
            if bound[i][0] <= self.chrom[i] <= bound[i][1]:
                continue
            else:
                flag = False
                return flag
        return flag

    def mutation(self, chrom_index, gen):
        flag = True
        a = self.chrom[chrom_index]
        while flag:
            p = random.random()
            g = 0.02
            if p < 0.5:
                if a + g < 5:
                    self.chrom[chrom_index] += g
                    break
            else:
                if a - g >= -5:
                    self.chrom[chrom_index] -= g
                    break

    def GetFitness(self):
        self.fitness = myfunction(self.chrom)
