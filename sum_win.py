#
# 総勝ち数順にソート
#

import data_structure as data
import pandas as pd

#
# データの操作部分
#

data_col = ['登録名', 'チーム2018', '総勝ち数']
df = data.df_m
for col in df.columns:
    if '勝利' in col:
        data_col.append(col)

df = df.sort_values('総勝ち数',ascending=False) # 2018年の勝利数に応じてソートする

print(data_col)
df = df[data_col] #データ表示をdata_col分だけにする

df.to_csv('総勝ち数.csv') #CSVファイルへ書き込み
#df.head(20)
