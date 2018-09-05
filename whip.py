#
#
# wips順にソート
#
#


import data_structure as data
import pandas as pd

#
# データの操作部分
#

data_col = ['登録名', 'チーム2018']
df = data.df_m

#print(df)
for col in df.columns:
    if 'WHIP' in col:
        data_col.append(col)
df = df.sort_values('WHIP2018',ascending=True) # 2018年の勝利数に応じてソートする

#print(data_col)
df = df[data_col] #データ表示をdata_col分だけにする

df.to_csv('whip.csv') #CSVファイルへ書き込み
#df.head(20)
