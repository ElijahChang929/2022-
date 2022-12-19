import random,math
import copy
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from scipy import stats

#以下为读区csv数据并进行处理
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
            
            
#分析相关系数部分            
column_num = 4   
control_num_raw = [raw[column_num] for raw in raw_lst if raw[column_num] != 'False']
control_num_raw = control_num_raw[:93]
tmp_lst = copy.deepcopy(control_num_raw)
enforced_data  =[]
tmp = 5000

for i in range(tmp):#打乱
    random.shuffle(tmp_lst)
    enforced_data.append(np.array(tmp_lst))
correlation_coefficient = [np.corrcoef(control_num_raw,x)[0][1] for x in enforced_data]#得到相关系数

plt.hist(correlation_coefficient,bins = 40)
plt.title('Distribution of correlation coefficient')
plt.show()

print('cor',np.percentile(correlation_coefficient, 0.5),np.percentile(correlation_coefficient, 99.5))#99%置信区间


#实验组的相关系数计算
column_num_ex1 = 1       
ex_num1 = [raw[column_num_ex1] for raw in raw_lst if raw[column_num_ex1] != 'False']
column_num_ex2 = 2          
ex_num2 = [raw[column_num_ex2] for raw in raw_lst if raw[column_num_ex2] != 'False']
print(np.corrcoef(ex_num1,ex_num2)[0][1])

#control组
column_num_ex3 = 4          
ex_num3 = [raw[column_num_ex3] for raw in raw_lst if raw[column_num_ex3] != 'False']
ex_num3 = ex_num3[:len(ex_num1)]

#WL的数据
column_num_WL_ex = 10  
column_num_WL_control = 12 
WL_ex_num = [raw[column_num_WL_ex] for raw in raw_lst if raw[column_num_WL_ex] != 'False']
WL_control_num = [raw[column_num_WL_control] for raw in raw_lst if raw[column_num_WL_control] != 'False']
WL_control_num = WL_control_num[:len(WL_ex_num)]

#ZTY的数据

column_num_ZTY_ex = 6 
column_num_ZTY_control = 8 
ZTY_ex_num = [raw[column_num_ZTY_ex] for raw in raw_lst if raw[column_num_ZTY_ex] != 'False']
ZTY_control_num = [raw[column_num_ZTY_control] for raw in raw_lst if raw[column_num_ZTY_control] != 'False']
ZTY_control_num = ZTY_control_num[:len(ZTY_ex_num)]

#TYX的数据

column_num_TYX_ex = 14 
column_num_TYX_control = 16 
TYX_ex_num = [raw[column_num_TYX_ex] for raw in raw_lst if raw[column_num_TYX_ex] != 'False']
TYX_control_num = [raw[column_num_TYX_control] for raw in raw_lst if raw[column_num_TYX_control] != 'False']
TYX_control_num = TYX_control_num[:len(TYX_ex_num)]


#绘图部分

plt.subplot(221)
plt.hist(ex_num1, alpha = 0.5, bins=10,label='experiment1')
plt.hist(ex_num3, alpha = 0.5,bins=10, label='control')
plt.hist(ex_num2, alpha = 0.5, bins=10,label='experiment2')
plt.legend(loc='upper right')
plt.title('ZSJ&ZGX\'s data')
plt.subplot(222)
plt.hist(WL_ex_num, alpha = 0.5, bins=10,label='experiment')
plt.hist(WL_control_num, alpha = 0.5, bins=10,label='control')
plt.legend(loc='upper right')
plt.title('WL\'s data')
plt.subplot(223)
plt.hist(ZTY_ex_num, alpha = 0.5, bins=10,label='experiment')
plt.hist(ZTY_control_num, alpha = 0.5,bins=10, label='control')
plt.legend(loc='upper right')
plt.title('ZTY\'s data')
plt.subplot(224)
plt.hist(TYX_ex_num, alpha = 0.5, bins=10,label='experiment')
plt.hist(TYX_control_num, alpha = 0.5, bins=10,label='control')
plt.legend(loc='upper right')
plt.title('TYX\'s data')
plt.show()

#突变率
a_ZZ_1 = 3.62E-07
a_ZZ_2 = 3.66E-07
a_WL = 7.13E-08
a_ZTY = 7.03E-08
a_TYX = 1.02E-07




#实验数据的方差分析
#ZGX&ZSJ
var_ZZ_ex_1 = np.var(ex_num1)
mean_ZZ_ex_1 = np.mean(ex_num1)
N_t1 = np.mean([raw_lst[0][0],raw_lst[1][0],raw_lst[2][0]])
C_1 = len(ex_num1)
print('N_t1',N_t1)

var_ZZ_ex_2 = np.var(ex_num2)
mean_ZZ_ex_2 = np.mean(ex_num2)
var_ZZ_control = np.var(ex_num3)
mean_ZZ_control = np.mean(ex_num3)

print('ZZ实验数据的方差,均值',var_ZZ_ex_1,mean_ZZ_ex_1,var_ZZ_ex_2,mean_ZZ_ex_2,var_ZZ_control,mean_ZZ_control)
print('理论数据的方差/均值',N_t1*C_1*a_ZZ_1/math.log(N_t1*C_1*a_ZZ_1),N_t1*C_1*a_ZZ_1/math.log(N_t1*C_1*a_ZZ_2))

#WL
WLN_t = np.mean([raw_lst[0][9],raw_lst[1][9],raw_lst[2][9]])
C_WL = len(WL_ex_num)
var_WL_ex = np.var(WL_ex_num)
mean_WL_ex = np.mean(WL_ex_num)
var_WL_control = np.var(WL_control_num)
mean_WL_control = np.mean(WL_control_num)

print("WL",var_WL_ex,mean_WL_ex,var_WL_control,mean_WL_control)
print('WL理论数据的方差/均值',WLN_t*C_WL*a_WL/math.log(WLN_t*C_WL*a_WL))

#ZTY
ZTYN_t = np.mean([raw_lst[0][5],raw_lst[1][5],raw_lst[2][5]])
C_ZTY = len(ZTY_ex_num)
var_ZTY_ex = np.var(ZTY_ex_num)
mean_ZTY_ex = np.mean(ZTY_ex_num)
var_ZTY_control = np.var(ZTY_control_num)
mean_ZTY_control = np.mean(ZTY_control_num)
print('ZTY',var_ZTY_ex,mean_ZTY_ex,var_ZTY_control,mean_ZTY_control)
print('ZTY理论数据的方差/均值',ZTYN_t*C_ZTY*a_ZTY/math.log(ZTYN_t*C_ZTY*a_ZTY))

#TYX
TYXN_t = np.mean([raw_lst[0][13],raw_lst[1][13],raw_lst[2][13]])
C_TYX = len(TYX_ex_num)
var_TYX_ex = np.var(TYX_ex_num)
mean_TYX_ex = np.mean(TYX_ex_num)
var_TYX_control = np.var(TYX_control_num)
mean_TYX_control = np.mean(TYX_control_num)
print('TYX',var_TYX_ex,mean_TYX_ex,var_TYX_control,mean_TYX_control)
print('RTX理论数据的方差/均值',TYXN_t*C_TYX*a_TYX/math.log(TYXN_t*C_TYX*a_TYX))