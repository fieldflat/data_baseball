#
# 総勝ち数順にソート
#

import data_structure as data
import pandas as pd
import math

#
# データの操作部分
#

data_col = ['登録名', 'チーム2018', '総負け数']
df = data.df_m
for col in df.columns:
    if '敗北' in col:
        data_col.append(col)

#
# 「総負け数」カラムの追加
#
for i in range(len(df)):
    df.loc[i,'総負け数'] = 0
    for col in data_col:
        if '敗北' in col:
            if not math.isnan(df.loc[i,col]):
                df.loc[i,'総負け数'] += df.loc[i,col]


df = df.sort_values('総負け数',ascending=False) # 2018年の勝利数に応じてソートする

#print(data_col)
df = df[data_col] #データ表示をdata_col分だけにする

df.to_csv('総負け数.csv') #CSVファイルへ書き込み
#df.head(20)
