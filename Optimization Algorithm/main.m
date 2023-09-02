maxgen = 300; % 最大迭代次数
sizepop = 100; 
pcross = 0.6; % 交叉参数
pmutation = 0.01; % 变异参数

lenchrom = [1, 1, 1]; % 定义个体为三位编码
bound = [-5, 5; -5, 5; -5, 5]; % 定义域

% 构造个体与初始化
individuals = struct('fitness', zeros(1, sizepop), 'chrom', []);
avgfitness = [];
bestfitness = [];
bestchrom = [];

for i = 1 : sizepop
    individuals.chrom(i, :) = Code(lenchrom, bound);
    x = individuals.chrom(i, :);
    individuals.chrom(i, :) = fun(x);
end

[bestfitness, bestindex] = min(individuals.fitness);
bestchrom = individuals.chrom(bestindex, :);
avgfitness = sum(individuals.fitness) / sizepop;

trace = [];
for i = 1: maxgen
    individuals = Select(individuals, sizepop);
    individuals.chrom = Cross(pcross, lenchrom, individuals.chrom, sizepop, bound);
    individuals.chrom = Mutation(pmutation, lenchrom, individuals.chrom, sizepop, [i, maxgen], bound);
    for j = 1 : sizepop
        x = individuals.chrom(i, :);
        individuals.chrom(i, :) = fun(x);
    end
    [newbestfitness, newbestindex] = min(individuals.fitness);
    if newbestfitness < bestfitness
        bestfitness = newbestfitness;
        bestchrom = individuals.chrom(newbestindex, :);
    end
    avgfitness = sum(individuals.fitness) / sizepop;
    trace = [trace; bestfitness];
end
