#!/usr/bin/env python
# coding: utf-8

# In[155]:


import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud


# In[157]:


# 3-1
# generate who consumed most
df = pd.read_csv('task1_1.csv', encoding='gb2312')
df_mostconsumer = df.loc[:, ["顾客编号", "销售金额"]].groupby(["顾客编号"]).sum().sort_values(by=["销售金额"], ascending=False).head(10)
df_mostconsumer_info = df[df["顾客编号"].isin(df_mostconsumer.index.tolist())]


# In[158]:


list_consumers_info = []
for num in df_mostconsumer.index.tolist():
    df_oneconsumer = df_mostconsumer_info[df_mostconsumer_info.顾客编号.isin([num])]
    list_consumer_info = []
    list_consumer_info.append(" ".join(df_oneconsumer.大类名称.tolist()))
    list_consumer_info.append(" ".join(df_oneconsumer.中类名称.tolist()))
    list_consumer_info.append(" ".join(df_oneconsumer.小类名称.tolist()))
    list_consumers_info.append(" ".join(list_consumer_info))


# In[159]:


# drwa 
cloud = WordCloud(
    #设置字体，不指定就会出现乱码
    font_path=r'C:/Windows/fonts/simhei.ttf' ,
    # font_path=path.join(d,'simsun.ttc'),
    width=200,
    height=200,
    #设置背景色
    background_color='white',
    #词云形状
#     mask="14109.jpg",
    #允许最大词汇
    max_words=2000,
    #最大号字体
    max_font_size=40
)
for x in range(0, len(list_consumers_info)):
    word_cloud = cloud.generate(list_consumers_info[x])
    word_cloud.to_file("task3_1_wordcloud_{}.png".format(x))


# In[165]:


# 3-2
df_mostincome = df.loc[:, ["大类名称", "销售月份", "销售数量"]].groupby(["大类名称", "销售月份"]).sum().sort_values(by="销售数量", ascending=False)
df_mostincome.to_csv("task3_2.csv", index=True, encoding='gb2312')


# In[163]:


# 3-3
df.loc[:, ["大类名称", "销售数量", "是否促销"]].groupby(["大类名称", "是否促销"]).sum()


# In[ ]:




