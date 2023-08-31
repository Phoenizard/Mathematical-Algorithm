% 多项式回归
t = 1/30:1/30:14/30;
s = [11.86 15.67 20.60 26.69 33.71 41.93 51.13 61.49 72.90 85.44 99.08 113.77 129.54 146.48];

% (2 代表次数为2)
[p, S] = polyfit(t, s, 2); 

% 多元二项式回归
% rstool(x,y,model,alpha)
% 线性：linear
% 纯二次: purequadratic
% 交叉: interaction
% 完全二次: quadratic
