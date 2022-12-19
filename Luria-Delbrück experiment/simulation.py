import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import poisson
from tqdm import tqdm
import math,copy,random
import pandas as pd
from scipy import stats

#数据格式处理
fileName = './Counting_results_1.tsv'
text = ''
lines = []
raw_lst = []

with open(fileName, 'r') as f:
    text = f.read()
lines = text.split('\n')
for l in lines:
    raw_lst.append(l.split('\t'))
raw_lst.pop()
raw_lst.pop(0)

columns = len(raw_lst[0])
for line in range(len(raw_lst)):
    for num in range(columns):
        if 'E' in raw_lst[line][num]:
            raw_lst[line][num] = int(float(raw_lst[line][num][:raw_lst[line][num].find('E')])*1e5)
        elif raw_lst[line][num] == '':
            raw_lst[line][num] ='False'
        else:
            raw_lst[line][num] = int(raw_lst[line][num])
    
    
#关于报告中讨论的各种模拟，只用修改框架中的部分细节就可重复使用，这里其展示基本功能
column_num_ex1 = 1       
ex_num1 = [raw[column_num_ex1] for raw in raw_lst if raw[column_num_ex1] != 'False']   
     
N_0 = 188.75;
generations = int(math.log2(3.596666666666667e+07/N_0));
groups = 93;
wild = N_0;
mutant = 0;
mutant_rate =4.73E-08;#方法1得到的突变率
cof= []
populations = [[N_0,N_0,mutant] for i in range(groups)]#total number, wild number, mutant number

for generation in tqdm(range(generations)):#每一代
    for culture in range(groups): #每个culture
        populations[culture] = [2 * num for num in populations[culture]]#分裂
        mu = populations[culture][1] * mutant_rate#突变均值
        new_mutation_num = poisson.rvs(mu)#确定突变数
        populations[culture][1] -= new_mutation_num#wild减少
        populations[culture][2] += new_mutation_num#突变型增加
mutant_bac = [culture[2]*(50e-6/(1e-3)) for culture in populations]#观察到的突变数，也考虑了取样的比例
  
plt.hist(mutant_bac,alpha = 0.5,label='simulation1')
plt.hist(ex_num1, alpha = 0.5,label='experiment')

mutant = 0;
mutant_rate =2.51E-07;#方法2得到的突变率
populations = [[N_0,N_0,mutant] for i in range(groups)]#total number, wild number, mutant number

for generation in tqdm(range(generations)):
  for culture in range(groups): 
    populations[culture] = [2 * num for num in populations[culture]]
    mu = populations[culture][1] * mutant_rate
    new_mutation_num = poisson.rvs(mu)
    populations[culture][1] -= new_mutation_num
    populations[culture][2] += new_mutation_num
mutant_bac = [culture[2]*(50e-6/(1e-3)) for culture in populations]
plt.hist(mutant_bac,alpha = 0.5,label='simulation2')
plt.title('simulation&experiment')
plt.legend(loc='upper right')
plt.show()



