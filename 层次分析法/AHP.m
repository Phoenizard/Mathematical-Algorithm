%输入判断矩阵
A = [1 2 3 5
    1/2 1 1/2 2
    1/3 2 1 2
    1/5 1/2 1/2 1];

%一致性检验
maxlam = max(eig(A));
[~, n] = size(A);
RI = [0,0,0.58,0.9,1.12,1.24,1.32,1.41,1.45, 1.49, 1.52, 1.54, 1.56, 1.58, 1.59];
CI = (maxlam - n) / (n-1);
CR = CI / RI(n);
if CR < 0.10
    disp('通过一致性检验')
else
    disp('不通过一致性检验')
    return  % 终止运行 
end


%计算权重向量
[n,~] = size(A);
Asum = sum(A,1);    % 按列求和
Aprogress = A./(ones(n,1)*Asum);

W = sum(Aprogress, 2)./n;