% 奇偶法则：
% 如果邻居之和为奇数则更新为1
% 如果邻居之和为偶数则更新为0

% 元胞空间
n = 200;
Se = zeros(n);
z = zeros(n);
% 初始化
Se(n/2-2:n/2+2, n/2-2:n/2+2) = 1;
p = imagesc(cat(3, Se, z, z));
axis square;
Sd = zeros(n + 2);
while(true)
   Sd(2:n+1, 2:n+1) = Se;
   sum = Sd(1:n,2:n+1) + Sd(3:n+2,2:n+1) + Sd(2:n+1,1:n) + Sd(2:n+1,3:n+2);
   % 生成新元胞
   Se = mod(sum, 2);
   set(p,'cdata',cat(3, Se, z, z))
   pause(0.03)
end