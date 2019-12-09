# -*- encoding: utf-8 -*-
"""
@File    : test.py
@Time    : 2019/12/7 0007 13:56
@Software: PyCharm
"""

import csv
import numpy as np
import matplotlib.pyplot as plt

csv_read=csv.reader(open('./政治倾向调查2014年数据.csv',encoding='utf-8'))

with open('./政治倾向调查2014年数据.csv',encoding='utf-8') as csvfile:
    reader=csv.reader(csvfile)
    column=[row[42] for row in reader]
    title=column[0]
    data=column[1::]

dict = {}
for key in data:
    dict[key] = dict.get(key, 0) + 1
dict_sort={}
# dict_sort=dict
dict_sort['强烈反对']=dict['强烈反对']
dict_sort['反对']=dict['反对']
dict_sort['同意']=dict['同意']
dict_sort['强烈同意']=dict['强烈同意']



plt.bar(dict_sort.keys(), dict_sort.values(), width=0.8)
plt.title(title)
plt.show()
print(dict_sort)













