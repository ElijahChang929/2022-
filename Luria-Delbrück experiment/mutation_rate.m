clear;clc;
data = table2array(tsvread('Counting_results.tsv'));
data(2:3,1)=data(2:3,1)*1e5;
column = 2;%所要读区的列
%%
%first approach
all_data = [];%目标列的所有数据
for i = 1 : length((data(:,column)))
    if ~isnan(data(i,column))
        all_data = [all_data data(i,column)];
    end
end
N_t = mean(data(1:3,column - 1))*100;%稀释100倍
ct_0 = 0;%数0
for i  = 1:length(all_data)
    if all_data(i) == 0
        ct_0 = ct_0 + 1;
    end
end
p_0 = ct_0/length(all_data);
m = -log(p_0);
a = m/N_t
%%
%second approach
all_data = [];
for i = 1 : length((data(:,column)))
    if ~isnan(data(i,column))
        all_data = [all_data data(i,column)];
    end
end
N_t = mean(data(1:3,column - 2))*100;
C = length(all_data);
r = mean(all_data)*20;
syms a;
equ = (r == a * N_t *log(N_t * C * a));%解论文中的方程
mutation_rate = double(solve(equ,a))


