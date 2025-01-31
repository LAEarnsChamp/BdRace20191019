{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 109,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "df = pd.read_csv('附件.csv', encoding='gb2312')\n",
    "units = df.loc[:, \"单位\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0         个\n",
       "1         袋\n",
       "2         袋\n",
       "3         袋\n",
       "4         袋\n",
       "         ..\n",
       "42811    千克\n",
       "42812    千克\n",
       "42813     提\n",
       "42814    千克\n",
       "42815     罐\n",
       "Name: 单位, Length: 42816, dtype: object"
      ]
     },
     "execution_count": 110,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# replace unit \"kg\" to \"千克\"\n",
    "units.replace(\"kg\", \"千克\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "metadata": {},
   "outputs": [],
   "source": [
    "df.loc[:, \"单位\"] = units"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "metadata": {},
   "outputs": [],
   "source": [
    "# profit = amount * price per item\n",
    "df.loc[:, [\"销售数量\", \"销售金额\", \"商品单价\"]].fillna(0)\n",
    "df.eval('销售金额 = 商品单价 * 销售数量', inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 113,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>顾客编号</th>\n",
       "      <th>大类编码</th>\n",
       "      <th>大类名称</th>\n",
       "      <th>中类编码</th>\n",
       "      <th>中类名称</th>\n",
       "      <th>小类编码</th>\n",
       "      <th>小类名称</th>\n",
       "      <th>销售日期</th>\n",
       "      <th>销售月份</th>\n",
       "      <th>商品编码</th>\n",
       "      <th>规格型号</th>\n",
       "      <th>商品类型</th>\n",
       "      <th>单位</th>\n",
       "      <th>销售数量</th>\n",
       "      <th>销售金额</th>\n",
       "      <th>商品单价</th>\n",
       "      <th>是否促销</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>12</td>\n",
       "      <td>蔬果</td>\n",
       "      <td>1201</td>\n",
       "      <td>蔬菜</td>\n",
       "      <td>120109</td>\n",
       "      <td>其它蔬菜</td>\n",
       "      <td>20150101</td>\n",
       "      <td>201501</td>\n",
       "      <td>DW-1201090311</td>\n",
       "      <td></td>\n",
       "      <td>生鲜</td>\n",
       "      <td>个</td>\n",
       "      <td>8.000</td>\n",
       "      <td>16.00000</td>\n",
       "      <td>2.00</td>\n",
       "      <td>否</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>20</td>\n",
       "      <td>粮油</td>\n",
       "      <td>2014</td>\n",
       "      <td>酱菜类</td>\n",
       "      <td>201401</td>\n",
       "      <td>榨菜</td>\n",
       "      <td>20150101</td>\n",
       "      <td>201501</td>\n",
       "      <td>DW-2014010019</td>\n",
       "      <td>60g</td>\n",
       "      <td>一般商品</td>\n",
       "      <td>袋</td>\n",
       "      <td>6.000</td>\n",
       "      <td>3.00000</td>\n",
       "      <td>0.50</td>\n",
       "      <td>否</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>15</td>\n",
       "      <td>日配</td>\n",
       "      <td>1505</td>\n",
       "      <td>冷藏乳品</td>\n",
       "      <td>150502</td>\n",
       "      <td>冷藏加味酸乳</td>\n",
       "      <td>20150101</td>\n",
       "      <td>201501</td>\n",
       "      <td>DW-1505020011</td>\n",
       "      <td>150g</td>\n",
       "      <td>一般商品</td>\n",
       "      <td>袋</td>\n",
       "      <td>1.000</td>\n",
       "      <td>2.40000</td>\n",
       "      <td>2.40</td>\n",
       "      <td>否</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>3</td>\n",
       "      <td>3</td>\n",
       "      <td>15</td>\n",
       "      <td>日配</td>\n",
       "      <td>1503</td>\n",
       "      <td>冷藏料理</td>\n",
       "      <td>150305</td>\n",
       "      <td>冷藏面食类</td>\n",
       "      <td>20150101</td>\n",
       "      <td>201501</td>\n",
       "      <td>DW-1503050035</td>\n",
       "      <td>500g</td>\n",
       "      <td>一般商品</td>\n",
       "      <td>袋</td>\n",
       "      <td>1.000</td>\n",
       "      <td>8.30000</td>\n",
       "      <td>8.30</td>\n",
       "      <td>否</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "      <td>15</td>\n",
       "      <td>日配</td>\n",
       "      <td>1505</td>\n",
       "      <td>冷藏乳品</td>\n",
       "      <td>150502</td>\n",
       "      <td>冷藏加味酸乳</td>\n",
       "      <td>20150101</td>\n",
       "      <td>201501</td>\n",
       "      <td>DW-1505020020</td>\n",
       "      <td>100g*8</td>\n",
       "      <td>一般商品</td>\n",
       "      <td>袋</td>\n",
       "      <td>1.000</td>\n",
       "      <td>11.90000</td>\n",
       "      <td>11.90</td>\n",
       "      <td>否</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>42811</td>\n",
       "      <td>1605</td>\n",
       "      <td>12</td>\n",
       "      <td>蔬果</td>\n",
       "      <td>1201</td>\n",
       "      <td>蔬菜</td>\n",
       "      <td>120106</td>\n",
       "      <td>菌菇类</td>\n",
       "      <td>20150430</td>\n",
       "      <td>201504</td>\n",
       "      <td>DW-1201060002</td>\n",
       "      <td>散称</td>\n",
       "      <td>生鲜</td>\n",
       "      <td>千克</td>\n",
       "      <td>0.217</td>\n",
       "      <td>3.90600</td>\n",
       "      <td>18.00</td>\n",
       "      <td>否</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>42812</td>\n",
       "      <td>1572</td>\n",
       "      <td>12</td>\n",
       "      <td>蔬果</td>\n",
       "      <td>1201</td>\n",
       "      <td>蔬菜</td>\n",
       "      <td>120102</td>\n",
       "      <td>根茎</td>\n",
       "      <td>20150430</td>\n",
       "      <td>201504</td>\n",
       "      <td>DW-1201020040</td>\n",
       "      <td>散称</td>\n",
       "      <td>生鲜</td>\n",
       "      <td>千克</td>\n",
       "      <td>0.440</td>\n",
       "      <td>0.86240</td>\n",
       "      <td>1.96</td>\n",
       "      <td>否</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>42813</td>\n",
       "      <td>1170</td>\n",
       "      <td>30</td>\n",
       "      <td>洗化</td>\n",
       "      <td>3016</td>\n",
       "      <td>纸制品</td>\n",
       "      <td>301603</td>\n",
       "      <td>无芯纸</td>\n",
       "      <td>20150430</td>\n",
       "      <td>201504</td>\n",
       "      <td>DW-3016030007</td>\n",
       "      <td>10卷</td>\n",
       "      <td>一般商品</td>\n",
       "      <td>提</td>\n",
       "      <td>1.000</td>\n",
       "      <td>14.50000</td>\n",
       "      <td>14.50</td>\n",
       "      <td>是</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>42814</td>\n",
       "      <td>2605</td>\n",
       "      <td>12</td>\n",
       "      <td>蔬果</td>\n",
       "      <td>1201</td>\n",
       "      <td>蔬菜</td>\n",
       "      <td>120101</td>\n",
       "      <td>叶菜</td>\n",
       "      <td>20150430</td>\n",
       "      <td>201504</td>\n",
       "      <td>DW-1201010023</td>\n",
       "      <td>散称</td>\n",
       "      <td>生鲜</td>\n",
       "      <td>千克</td>\n",
       "      <td>0.718</td>\n",
       "      <td>1.83808</td>\n",
       "      <td>2.56</td>\n",
       "      <td>否</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>42815</td>\n",
       "      <td>2610</td>\n",
       "      <td>23</td>\n",
       "      <td>酒饮</td>\n",
       "      <td>2317</td>\n",
       "      <td>进口饮料</td>\n",
       "      <td>231702</td>\n",
       "      <td>进口果汁</td>\n",
       "      <td>20150430</td>\n",
       "      <td>201504</td>\n",
       "      <td>DW-2317020131</td>\n",
       "      <td>490ml</td>\n",
       "      <td>联营商品</td>\n",
       "      <td>罐</td>\n",
       "      <td>1.000</td>\n",
       "      <td>8.00000</td>\n",
       "      <td>8.00</td>\n",
       "      <td>否</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>42814 rows × 17 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "       顾客编号  大类编码 大类名称  中类编码  中类名称    小类编码    小类名称      销售日期    销售月份  \\\n",
       "0         0    12   蔬果  1201    蔬菜  120109    其它蔬菜  20150101  201501   \n",
       "1         1    20   粮油  2014   酱菜类  201401      榨菜  20150101  201501   \n",
       "2         2    15   日配  1505  冷藏乳品  150502  冷藏加味酸乳  20150101  201501   \n",
       "3         3    15   日配  1503  冷藏料理  150305   冷藏面食类  20150101  201501   \n",
       "4         4    15   日配  1505  冷藏乳品  150502  冷藏加味酸乳  20150101  201501   \n",
       "...     ...   ...  ...   ...   ...     ...     ...       ...     ...   \n",
       "42811  1605    12   蔬果  1201    蔬菜  120106     菌菇类  20150430  201504   \n",
       "42812  1572    12   蔬果  1201    蔬菜  120102      根茎  20150430  201504   \n",
       "42813  1170    30   洗化  3016   纸制品  301603     无芯纸  20150430  201504   \n",
       "42814  2605    12   蔬果  1201    蔬菜  120101      叶菜  20150430  201504   \n",
       "42815  2610    23   酒饮  2317  进口饮料  231702    进口果汁  20150430  201504   \n",
       "\n",
       "                商品编码    规格型号  商品类型  单位   销售数量      销售金额   商品单价 是否促销  \n",
       "0      DW-1201090311            生鲜   个  8.000  16.00000   2.00    否  \n",
       "1      DW-2014010019     60g  一般商品   袋  6.000   3.00000   0.50    否  \n",
       "2      DW-1505020011    150g  一般商品   袋  1.000   2.40000   2.40    否  \n",
       "3      DW-1503050035    500g  一般商品   袋  1.000   8.30000   8.30    否  \n",
       "4      DW-1505020020  100g*8  一般商品   袋  1.000  11.90000  11.90    否  \n",
       "...              ...     ...   ...  ..    ...       ...    ...  ...  \n",
       "42811  DW-1201060002      散称    生鲜  千克  0.217   3.90600  18.00    否  \n",
       "42812  DW-1201020040      散称    生鲜  千克  0.440   0.86240   1.96    否  \n",
       "42813  DW-3016030007     10卷  一般商品   提  1.000  14.50000  14.50    是  \n",
       "42814  DW-1201010023      散称    生鲜  千克  0.718   1.83808   2.56    否  \n",
       "42815  DW-2317020131   490ml  联营商品   罐  1.000   8.00000   8.00    否  \n",
       "\n",
       "[42814 rows x 17 columns]"
      ]
     },
     "execution_count": 113,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.dropna()   #drop NAN"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>顾客编号</th>\n",
       "      <th>大类编码</th>\n",
       "      <th>大类名称</th>\n",
       "      <th>中类编码</th>\n",
       "      <th>中类名称</th>\n",
       "      <th>小类编码</th>\n",
       "      <th>小类名称</th>\n",
       "      <th>销售日期</th>\n",
       "      <th>销售月份</th>\n",
       "      <th>商品编码</th>\n",
       "      <th>规格型号</th>\n",
       "      <th>商品类型</th>\n",
       "      <th>单位</th>\n",
       "      <th>销售数量</th>\n",
       "      <th>销售金额</th>\n",
       "      <th>商品单价</th>\n",
       "      <th>是否促销</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>12</td>\n",
       "      <td>蔬果</td>\n",
       "      <td>1201</td>\n",
       "      <td>蔬菜</td>\n",
       "      <td>120109</td>\n",
       "      <td>其它蔬菜</td>\n",
       "      <td>20150101</td>\n",
       "      <td>201501</td>\n",
       "      <td>DW-1201090311</td>\n",
       "      <td></td>\n",
       "      <td>生鲜</td>\n",
       "      <td>个</td>\n",
       "      <td>8.000</td>\n",
       "      <td>16.00000</td>\n",
       "      <td>2.00</td>\n",
       "      <td>否</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>20</td>\n",
       "      <td>粮油</td>\n",
       "      <td>2014</td>\n",
       "      <td>酱菜类</td>\n",
       "      <td>201401</td>\n",
       "      <td>榨菜</td>\n",
       "      <td>20150101</td>\n",
       "      <td>201501</td>\n",
       "      <td>DW-2014010019</td>\n",
       "      <td>60g</td>\n",
       "      <td>一般商品</td>\n",
       "      <td>袋</td>\n",
       "      <td>6.000</td>\n",
       "      <td>3.00000</td>\n",
       "      <td>0.50</td>\n",
       "      <td>否</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>15</td>\n",
       "      <td>日配</td>\n",
       "      <td>1505</td>\n",
       "      <td>冷藏乳品</td>\n",
       "      <td>150502</td>\n",
       "      <td>冷藏加味酸乳</td>\n",
       "      <td>20150101</td>\n",
       "      <td>201501</td>\n",
       "      <td>DW-1505020011</td>\n",
       "      <td>150g</td>\n",
       "      <td>一般商品</td>\n",
       "      <td>袋</td>\n",
       "      <td>1.000</td>\n",
       "      <td>2.40000</td>\n",
       "      <td>2.40</td>\n",
       "      <td>否</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>3</td>\n",
       "      <td>3</td>\n",
       "      <td>15</td>\n",
       "      <td>日配</td>\n",
       "      <td>1503</td>\n",
       "      <td>冷藏料理</td>\n",
       "      <td>150305</td>\n",
       "      <td>冷藏面食类</td>\n",
       "      <td>20150101</td>\n",
       "      <td>201501</td>\n",
       "      <td>DW-1503050035</td>\n",
       "      <td>500g</td>\n",
       "      <td>一般商品</td>\n",
       "      <td>袋</td>\n",
       "      <td>1.000</td>\n",
       "      <td>8.30000</td>\n",
       "      <td>8.30</td>\n",
       "      <td>否</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "      <td>15</td>\n",
       "      <td>日配</td>\n",
       "      <td>1505</td>\n",
       "      <td>冷藏乳品</td>\n",
       "      <td>150502</td>\n",
       "      <td>冷藏加味酸乳</td>\n",
       "      <td>20150101</td>\n",
       "      <td>201501</td>\n",
       "      <td>DW-1505020020</td>\n",
       "      <td>100g*8</td>\n",
       "      <td>一般商品</td>\n",
       "      <td>袋</td>\n",
       "      <td>1.000</td>\n",
       "      <td>11.90000</td>\n",
       "      <td>11.90</td>\n",
       "      <td>否</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>42811</td>\n",
       "      <td>1605</td>\n",
       "      <td>12</td>\n",
       "      <td>蔬果</td>\n",
       "      <td>1201</td>\n",
       "      <td>蔬菜</td>\n",
       "      <td>120106</td>\n",
       "      <td>菌菇类</td>\n",
       "      <td>20150430</td>\n",
       "      <td>201504</td>\n",
       "      <td>DW-1201060002</td>\n",
       "      <td>散称</td>\n",
       "      <td>生鲜</td>\n",
       "      <td>千克</td>\n",
       "      <td>0.217</td>\n",
       "      <td>3.90600</td>\n",
       "      <td>18.00</td>\n",
       "      <td>否</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>42812</td>\n",
       "      <td>1572</td>\n",
       "      <td>12</td>\n",
       "      <td>蔬果</td>\n",
       "      <td>1201</td>\n",
       "      <td>蔬菜</td>\n",
       "      <td>120102</td>\n",
       "      <td>根茎</td>\n",
       "      <td>20150430</td>\n",
       "      <td>201504</td>\n",
       "      <td>DW-1201020040</td>\n",
       "      <td>散称</td>\n",
       "      <td>生鲜</td>\n",
       "      <td>千克</td>\n",
       "      <td>0.440</td>\n",
       "      <td>0.86240</td>\n",
       "      <td>1.96</td>\n",
       "      <td>否</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>42813</td>\n",
       "      <td>1170</td>\n",
       "      <td>30</td>\n",
       "      <td>洗化</td>\n",
       "      <td>3016</td>\n",
       "      <td>纸制品</td>\n",
       "      <td>301603</td>\n",
       "      <td>无芯纸</td>\n",
       "      <td>20150430</td>\n",
       "      <td>201504</td>\n",
       "      <td>DW-3016030007</td>\n",
       "      <td>10卷</td>\n",
       "      <td>一般商品</td>\n",
       "      <td>提</td>\n",
       "      <td>1.000</td>\n",
       "      <td>14.50000</td>\n",
       "      <td>14.50</td>\n",
       "      <td>是</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>42814</td>\n",
       "      <td>2605</td>\n",
       "      <td>12</td>\n",
       "      <td>蔬果</td>\n",
       "      <td>1201</td>\n",
       "      <td>蔬菜</td>\n",
       "      <td>120101</td>\n",
       "      <td>叶菜</td>\n",
       "      <td>20150430</td>\n",
       "      <td>201504</td>\n",
       "      <td>DW-1201010023</td>\n",
       "      <td>散称</td>\n",
       "      <td>生鲜</td>\n",
       "      <td>千克</td>\n",
       "      <td>0.718</td>\n",
       "      <td>1.83808</td>\n",
       "      <td>2.56</td>\n",
       "      <td>否</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>42815</td>\n",
       "      <td>2610</td>\n",
       "      <td>23</td>\n",
       "      <td>酒饮</td>\n",
       "      <td>2317</td>\n",
       "      <td>进口饮料</td>\n",
       "      <td>231702</td>\n",
       "      <td>进口果汁</td>\n",
       "      <td>20150430</td>\n",
       "      <td>201504</td>\n",
       "      <td>DW-2317020131</td>\n",
       "      <td>490ml</td>\n",
       "      <td>联营商品</td>\n",
       "      <td>罐</td>\n",
       "      <td>1.000</td>\n",
       "      <td>8.00000</td>\n",
       "      <td>8.00</td>\n",
       "      <td>否</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>42813 rows × 17 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "       顾客编号  大类编码 大类名称  中类编码  中类名称    小类编码    小类名称      销售日期    销售月份  \\\n",
       "0         0    12   蔬果  1201    蔬菜  120109    其它蔬菜  20150101  201501   \n",
       "1         1    20   粮油  2014   酱菜类  201401      榨菜  20150101  201501   \n",
       "2         2    15   日配  1505  冷藏乳品  150502  冷藏加味酸乳  20150101  201501   \n",
       "3         3    15   日配  1503  冷藏料理  150305   冷藏面食类  20150101  201501   \n",
       "4         4    15   日配  1505  冷藏乳品  150502  冷藏加味酸乳  20150101  201501   \n",
       "...     ...   ...  ...   ...   ...     ...     ...       ...     ...   \n",
       "42811  1605    12   蔬果  1201    蔬菜  120106     菌菇类  20150430  201504   \n",
       "42812  1572    12   蔬果  1201    蔬菜  120102      根茎  20150430  201504   \n",
       "42813  1170    30   洗化  3016   纸制品  301603     无芯纸  20150430  201504   \n",
       "42814  2605    12   蔬果  1201    蔬菜  120101      叶菜  20150430  201504   \n",
       "42815  2610    23   酒饮  2317  进口饮料  231702    进口果汁  20150430  201504   \n",
       "\n",
       "                商品编码    规格型号  商品类型  单位   销售数量      销售金额   商品单价 是否促销  \n",
       "0      DW-1201090311            生鲜   个  8.000  16.00000   2.00    否  \n",
       "1      DW-2014010019     60g  一般商品   袋  6.000   3.00000   0.50    否  \n",
       "2      DW-1505020011    150g  一般商品   袋  1.000   2.40000   2.40    否  \n",
       "3      DW-1503050035    500g  一般商品   袋  1.000   8.30000   8.30    否  \n",
       "4      DW-1505020020  100g*8  一般商品   袋  1.000  11.90000  11.90    否  \n",
       "...              ...     ...   ...  ..    ...       ...    ...  ...  \n",
       "42811  DW-1201060002      散称    生鲜  千克  0.217   3.90600  18.00    否  \n",
       "42812  DW-1201020040      散称    生鲜  千克  0.440   0.86240   1.96    否  \n",
       "42813  DW-3016030007     10卷  一般商品   提  1.000  14.50000  14.50    是  \n",
       "42814  DW-1201010023      散称    生鲜  千克  0.718   1.83808   2.56    否  \n",
       "42815  DW-2317020131   490ml  联营商品   罐  1.000   8.00000   8.00    否  \n",
       "\n",
       "[42813 rows x 17 columns]"
      ]
     },
     "execution_count": 114,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.drop_duplicates() # drop duplica"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "metadata": {},
   "outputs": [],
   "source": [
    "# get the df to analyse the belows\n",
    "df.to_csv(\"task1_1.csv\", index=False, encoding='gb2312')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 1-2 calculate profits of each categorie"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_sumprofit_by_cate = df.groupby(by=\"大类名称\").sum().loc[:, [\"销售金额\"]]\n",
    "df_sumprofit_by_cate.to_csv(\"task1_2.csv\", index=True, encoding='gb2312')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 118,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 1-3 calculate 促销/非促销 profits of each medium categorie\n",
    "df_profit_by_saleornot =df.groupby([\"中类名称\", \"是否促销\"]).sum().loc[:, [\"销售金额\"]]\n",
    "df_profit_by_saleornot.to_csv(\"task1_3.csv\", index=True, encoding='gb2312')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
