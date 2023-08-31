% 线性回归主要使用regress()
% [b, bint, r, rint, stats] = regress(Y, X, alpha)
% alpha为置信水平，默认0.05
% b为回归系数; bint为回归系数的区间估计; r残差, rint置信区间
% stats中含有三个数值：相关系数r^2,F值与F值对应的概率P
% r^2越接近1，说明回归方程越显著；F越大说明回归方程越显著
% p < alpha时，回归模型成立
X = [ones(16, 1) table2array(x)];
Y = table2array(y);

[b, bint, r, rint, stats] = regress(Y, X);
b, bint, stats 

% 残差图
rcoplot(r, rint)