#
#
# 勝ち数順にソート
#
#

import data_structure as data
import pandas as pd
#
#
# データの操作部分
#
#
#data = '勝利'
data_col = ['登録名', 'チーム2018']
#data_col = ['選手名']
df = data.df_m
print('lksndflksjdnf')
print(df)
for col in df.columns:
    #print(col)
    if '勝利' in col:
        data_col.append(col)
        #print(data_col)
#df = pd.concat(data.df_all,axis=1)
#print(df)
df = df.sort_values('勝利2018',ascending=False) # 2017年の勝利数に応じてソートする
#print(df)
print(data_col)
df = df[data_col] #データ表示をdata_col分だけにする
#print(df)
df.to_csv('勝利数.csv') #CSVファイルへ書き込み
#df.head(20)

#print(df)
