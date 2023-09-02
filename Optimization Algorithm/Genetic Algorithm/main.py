from config import maxgen, sizepop, pcross, pmutation, bound
from Individual import Individuals
import operation as op
import matplotlib.pyplot as plt

individuals = []

avg_fitness = 0
best_fitness = 0
best_chrom = []
process = []


def show(set):
    for s in set:
        print(s.chrom, s.fitness)
    print("-----------------------")


if __name__ == '__main__':
    # 种群初始化
    for i in range(sizepop):
        newIndividual = Individuals()
        individuals.append(newIndividual)
    best_fitness = 0
    for i in individuals:
        avg_fitness += i.fitness
        if best_fitness < i.fitness:
            best_fitness = i.fitness
            best_chrom = i.chrom
    avg_fitness = avg_fitness / sizepop
    process.append(avg_fitness)

    # 遗传迭代器
    for cnt in range(maxgen):
        newIndividuals = op.ReStruct(individuals=individuals, sum_fitness=avg_fitness * sizepop)
        for n in newIndividuals:
            n.GetFitness()
        # show(newIndividuals)
        newIndividuals = op.Cross(individuals=newIndividuals)
        for n in newIndividuals:
            n.GetFitness()
        # show(newIndividuals)
        newIndividuals = op.Mutation(individuals=newIndividuals, gen=cnt)
        for n in newIndividuals:
            n.GetFitness()
        # show(newIndividuals)
        avg_fitness = 0

        for n in newIndividuals:
            avg_fitness += n.fitness
            if best_fitness < n.fitness:
                best_fitness = n.fitness
                best_chrom = n.chrom

        avg_fitness = avg_fitness / sizepop
        process.append(avg_fitness)
        individuals = newIndividuals
        print(avg_fitness)

x = []
for i in range(maxgen + 1):
    x.append(i + 1)

plt.plot(x, process)
plt.show()

print("结果为：")
print(best_fitness, best_chrom)
