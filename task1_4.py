#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pandas as pd


df = pd.read_csv('task1_1.csv', encoding='gb2312')

# 2-1 calculate profits of each categorie
# 按商品类型 ，销售日期分组并按销售金额求和
df_Types_date = df.groupby(by=['商品类型', '销售日期']).agg({'销售金额':sum}).reset_index()
print(df_Types_date)
data1 = df_Types_date.loc[df_Types_date['商品类型'] == '生鲜']
data2 = df_Types_date.loc[df_Types_date['商品类型'] == '一般商品']
print(data1)
print(data2)


import re
import time as ti
import datetime
#today=int(time.strftime("%w"));

#判断起始日期的星期几，并是time等于第一个周一
anyday=datetime.datetime(2015, 1, 1).strftime("%w");
print("anyday", anyday)
if anyday == 0:
    time = datetime.datetime(2015,1,1)
else:
    time = datetime.datetime(2015,1,1)+datetime.timedelta(days=(7-int(anyday)))
time = ti.strftime('%Y,%m,%d')
print("time", time)

#计算7天后的日期
def getday(time0):
    y = int(time0[0:4])
    m = int(time0[5:7])
    d = int(time0[8:-1])
    the_date = datetime.datetime(y, m, d)
    result_date = the_date + datetime.timedelta(days=7)
    d = result_date.strftime('%Y,%m,%d')
    return d
#print(getday(time)) #8月15日后21天

#计算2015年1-4月一共有多少周
Week = 0
print("time+getday(time)", ti.strptime(time, "%Y,%m,%d")+getday(time))
while(ti.strptime(int(ti.mktime(time))+int(ti.mktime(getday(time))), "%Y,%m,%d") <= datetime.datetime(2015, 4, 30)):
    Week +=1

#统计生鲜每周的销售金额
Week_sum = []
for i in range(Week):
    week_sum_sales = 0
    for data in data1.ix['销售日期']:
        if time<= data< getday(time):
            week_sum_sales = week_sum_sales+ data1.ix[data1.index[data],'销售金额']
    time += getday(time)
    Week_sum.append(week_sum_sales)
