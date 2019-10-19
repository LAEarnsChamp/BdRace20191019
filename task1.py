#!/usr/bin/env python
# coding: utf-8

# In[94]:


import pandas as pd

df = pd.read_csv('附件.csv', encoding='gb2312')
# replace unit "kg" to "千克" 
# and blank "0"\
# and -amount sale for goods
# not in sale
units = df.loc[:, "单位"].replace("kg", "千克").replace("kG", "千克").replace("KG", "千克").replace("Kg", "千克").replace("", "0")
kind = df.loc[:, "商品类型"].replace("12g*8", "一般商品")
amount = abs(df.loc[:, "销售数量"])
insale = df.loc[:, "是否促销"].replace("9.9", "否")


# In[95]:


df.loc[:, "单位"] = units
df.loc[:, "商品类型"] = kind
df.loc[:, "销售数量"] = amount


# In[96]:


# profit = amount * price per item
df.loc[:, ["销售数量", "销售金额", "商品单价"]].fillna(0)
df.eval('销售金额 = 商品单价 * 销售数量', inplace=True)


# In[97]:


df = df.dropna()   #drop NAN


# In[98]:


df = df.drop_duplicates() # drop duplica


# In[100]:


# get the df to analyse the belows
df.to_csv("task1_1.csv", index=False, encoding='gb2312')


# In[101]:


# 1-2 calculate profits of each categorie


# In[102]:


df_sumprofit_by_cate = df.loc[:, ["大类名称", "销售金额"]].groupby(by="大类名称").sum()
df_sumprofit_by_cate.to_csv("task1_2.csv", index=True, encoding='gb2312')


# In[103]:


# 1-3 calculate 促销/非促销 profits of each medium categorie
df_profit_by_saleornot =df.groupby(["中类名称", "是否促销"]).sum().loc[:, ["销售金额"]]
df_profit_by_saleornot.to_csv("task1_3.csv", index=True, encoding='gb2312')


# In[104]:


# 1-5
df_consumer_by_daysinmon = df.loc[:, ["顾客编号", "销售日期", "销售月份", "销售金额"]]
# consume per mon
cpm = df_consumer_by_daysinmon.loc[:, ["顾客编号", "销售月份", "销售金额"]].groupby(["顾客编号", "销售月份"]).sum()
# consume days
cds = df_consumer_by_daysinmon.loc[:, ["顾客编号", "销售月份", "销售日期"]].drop_duplicates().groupby(["顾客编号", "销售月份"]).count()


# In[105]:


df_consumer_by_daysinmon = pd.merge(cpm, cds, how='inner', on=["顾客编号", "销售月份"])


# In[106]:


df_consumer_by_daysinmon.to_csv("task1_5.csv", index=True, encoding='gb2312')


# In[ ]:




