x = [10 11 8 3 2 1]';
y = [6 4 5 3 2.8 1]';

x_a = mean(x);
y_a = mean(y);

x_delta = ones(6, 1) * mean(x);
y_delta = ones(6, 1) * mean(y);

X = x - x_delta;
Y = y - y_delta;

scatter(X, Y)

a = [0.2235 -1]';  % 2 * 1 
k = sqrt(0.2235^2 + 1);
p = [X Y]; % 6 * 2 

