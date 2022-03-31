%%
clc;
clear;

%计算对应比例
diameter=csvread('diameter.csv',1,0);
mean_diameter_pixels = mean(diameter(:,6));
pixel2length = 1 / mean_diameter_pixels ;


%处理数据

num_files = 10;
for i = 1:num_files;
    data{i}=readmatrix([num2str(i) '.csv']);
    data{i}(:,5) = data{i}(:,1) * (1/15);%添加时间维度
    data{i}(:,2) = [];
    data{i}(:,2) = data{i}(:,2)-data{i}(1,2);
    data{i}(:,3) = data{i}(:,3)-data{i}(1,3);
    data{i}(:,2) = data{i}(:,2)*pixel2length;%将像素转换成微米
    data{i}(:,3) = data{i}(:,3)*pixel2length;
    data{i}(:,5) = sqrt(data{i}(:,2).^2 + data{i}(:,3).^2);%计算离原点的距离的平方
end;

MSD = [];
for j = 1:400;
    tmp = 0;
    for i = 1:4;
        tmp = (data{i}(j,5))^2+tmp;%将10组数据对应的平方数值求出
    end;
    MSD = [MSD tmp/4];     
end

t = data{2}(:,4);
scatter(t,MSD,'.');
xlabel('t(s)');
ylabel('MSD(微米^2)');
title('微球的均方位移随时间的变化');
mdl = fitlm(t,MSD)
text(1,50,'R-squared: 0.869')
k_b_1 = 1.81 / 4 * 6 *pi *1e-3 *5e-7* 1e-12 / 298.15 
R = 8.32432;
N_a_1 = R / k_b_1
%%

step = [];
for i = 1:4;
    step = [step diff(data{i}(:,5)')];
end;
%bins_width = 0.09979976607;

%nbins = max(step)-min(step)/bins_width 
histfit(step)
xlabel('步长');
ylabel('数量');
title('位移步长直方图');

pd = fitdist(step','Normal')   

sigma = 0.200885 ;
D = sigma^2 / (2 * 1/15);
k_b_2 = D * 6 *pi *1e-3 *5e-7* 1e-12 / 298.15 
R = 8.32432;
N_a_2 = R / k_b_2

%%
clc;
clear;


a = randomwalk(100000);
%a=csvread('randomdata.csv');
MSD = [];
for i = 1:500000;
    MSD = [MSD mean(a(1:i)'.^2)];
end;

t = [1:500000];
scatter(t,MSD,'.');
title('模拟一维随机运动');
xlabel('t');
ylabel('<x^2>');
%%
%csvwrite('randomdata.csv',a)
step = diff(abs(a));
%step= step/max(step); 
histfit(step)
pd = fitdist(step','Normal')  
%%
sigma =  2.99632  ;
D = sigma^2;
k_b_2 = D * 6 *pi *1e-3 *5e-7* 1e-12 / 298.15 
R = 8.32432;
N_a_2 = R / k_b_2

%%


clc;
clear;
%匀速直线运动
v = 0.001;
dis = linspace(1,10,10000);
t = [1:10000];
scatter(t,dis,'.');
title('模拟匀速直线运动');
xlabel('t');
ylabel('<x^2>');
%%


SD=[];
for t = 1:10000;
    SD = [SD (v*t)^2];
end;


t = [1:10000];
scatter(t,SD,'.');
title('模拟匀速直线运动');
xlabel('t');
ylabel('<x^2>');


%%
clc;
clear;
groups = 10000;
walknum = 10000;

for i = 1:groups;
    mod_data{i}=randomwalk(walknum);
end;

MSD = [];
for j = 1:walknum;
    tmp = 0;
    for i = 1:groups;
        tmp = mod_data{i}(1,j)^2 + tmp;
    end;
    MSD = [MSD tmp/groups];     
end

t = [1:walknum];
scatter(t,MSD,'.');
title('模拟一维随机运动');
xlabel('t');
ylabel('<x^2>');

mdl = fitlm(t,MSD)
text(500,8500,'R-squared: 1')
