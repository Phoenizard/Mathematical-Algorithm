function [fitresult, gof] = createFit(x, y)
%CREATEFIT(X,Y)
%  创建一个拟合。
%
%  要进行 'demo' 拟合的数据:
%      X 输入: x
%      Y 输出: y
%      验证 X: x
%      验证 Y: y
%  输出:
%      fitresult: 表示拟合的拟合对象。
%      gof: 带有拟合优度信息的结构体。
%
%  另请参阅 FIT, CFIT, SFIT.

%  由 MATLAB 于 27-Aug-2023 20:41:11 自动生成


%% 拟合: 'demo'。
[xData, yData] = prepareCurveData( x, y );

% 设置 fittype 和选项。
ft = fittype( 'poly7' );

% 对数据进行模型拟合。
[fitresult, gof] = fit( xData, yData, ft );

% 对照验证数据进行比较。
[xValidation, yValidation] = prepareCurveData( x, y );
residual = yValidation - fitresult( xValidation );
nNaN = nnz( isnan( residual ) );
residual(isnan( residual )) = [];
sse = norm( residual )^2;
rmse = sqrt( sse/length( residual ) );
fprintf( '''%s'' 拟合的验证优度:\n', 'demo' );
fprintf( '    SSE : %f\n', sse );
fprintf( '    RMSE : %f\n', rmse );
fprintf( '    %i 个点在数据域之外。\n', nNaN );

% 绘制数据拟合图。
figure( 'Name', 'demo' );
h = plot( fitresult, xData, yData );
% 向绘图中添加验证数据。
hold on
h(end+1) = plot( xValidation, yValidation, 'bo', 'MarkerFaceColor', 'w' );
hold off
legend( h, 'y vs. x', 'demo', 'y vs. x', 'Location', 'NorthEast', 'Interpreter', 'none' );
% 为坐标区加标签
xlabel( 'x', 'Interpreter', 'none' );
ylabel( 'y', 'Interpreter', 'none' );
grid on


