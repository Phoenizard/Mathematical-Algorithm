from config import sizepop, pmutation, lenchrom, pcross, bound
from Individual import Individuals
import random


def ReStruct(individuals: [Individuals], sum_fitness):
    sign = []
    res = []
    for i in range(sizepop):
        sign.append(individuals[i].fitness / sum_fitness)
    for i in range(sizepop):
        r = random.random()
        select = -1
        while r >= 0:
            select += 1
            r = r - sign[select]
        res.append(individuals[select])
    return res


def Mutation(individuals: [Individuals], gen):
    src = individuals
    for i in range(sizepop):
        r = random.random()
        if r < pmutation:
            index = random.randint(0, lenchrom - 1)
            p = random.random()
            s = src[i].chrom[index]
            if p > 0.5:
                if s + 0.05 >= 5:
                    continue
                else:
                    src[i].chrom[index] += 0.05
            else:
                if s - 0.05 <= -5:
                    continue
                else:
                    src[i].chrom[index] -= 0.05
    return src


def Cross(individuals: [Individuals]):
    src = individuals
    for cnt in range(5):
        x = random.sample(range(0, sizepop), 2)
        index = random.randint(0, lenchrom - 1)
        s = src[x[0]].chrom[index]
        t = src[x[1]].chrom[index]
        src[x[0]].chrom[index] = t
        src[x[1]].chrom[index] = s
        # while True:
        #     s = src[x[0]].chrom[index]
        #     t = src[x[1]].chrom[index]
        #     if bound[index][0] <= s * (1 - pcross) + t * pcross <= bound[index][1] and bound[index][0] <= s * pcross + t * (1 - pcross) <= bound[index][1]:
        #         src[x[0]].chrom[index] = s * (1 - pcross) + t * pcross
        #         src[x[1]].chrom[index] = s * pcross + t * (1 - pcross)
        #         break
    return src
