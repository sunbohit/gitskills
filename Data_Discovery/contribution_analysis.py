'''
贡献度分析，又称帕累托分析。
'''

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

read_file = "catering_dish_profit.xls" #数据集
cdp_data = pd.read_excel(read_file,index_col = "菜品名") #菜品名作为索引

print(cdp_data['盈利']) #打印盈利列与索引

'''
菜品名
A1     9173
A2     5729
A3     4811
A4     3594
A5     3195
A6     3026
A7     2378
A8     1970
A9     1877
A10    1782
Name: 盈利, dtype: int64
'''
cdp_data = cdp_data['盈利'].copy()

plt.figure()

cdp_data.plot(kind='bar') #绘制盈利条形图
plt.ylabel('盈利（元）',fontproperties="SimHei") 

p = 1.0 * cdp_data.cumsum()/cdp_data.sum()
p.plot(color = 'r', secondary_y = True, style = '-o', linewidth = 2)
plt.ylabel('盈利比例') #绘制盈利累计比例曲线

plt.show() #结果保存在contribution_analysis.png
