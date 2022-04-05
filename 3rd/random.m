%%
clc;
clear;

%计算对应比例
data = csvread('1.csv',1,0);
data(:,5) = data(:,1) * (1/10);%添加时间维度
x = mean(data(:,3));
y = mean(data(:,4));%计算圆心
data(:,3) = data(:,3) - x;
data(:,4) = data(:,4) - y;%转换为相对圆心的向量
[theta,rho] = cart2pol(data(:,3),data(:,4)) ;
v_theta = mean(abs(diff(theta) ./ 0.1))
T = 2*pi / v_theta