#
#
# 奪三振順にソート
# 投球回に誤差あり！！余裕があったら解決する.
#
#

import data_structure as data
import pandas as pd
import math

#
# データの操作部分
#

data_col = ['登録名', 'チーム2018']
df = data.df_m

#
# 2009~2018年の奪三振数を計算
# 問題点：投球回の端数をどうするか.
#
for i in range(len(df)):
    df.loc[i,'総奪三振数'] = 0
    df.loc[i,'総投球回'] = 0
    df.loc[i,'総奪三振率'] = 0
    pitch_num = 0 # 投球回数
    so_num = 0 # 奪三振数
    for col in df.columns:
        if '投球回' in col:
            if not math.isnan(df.loc[i,col]):
                pitch_num += df.loc[i,col]
        if '奪三振' in col:
            if not math.isnan(df.loc[i,col]):
                so_num += df.loc[i,col]

    df.loc[i,'総投球回'] = pitch_num
    df.loc[i,'総奪三振数'] = so_num
    #df.loc[i,'総WHIP数'] = (hit_num + base_on_balls_num + hit_by_pitch_num) / pitch_num
    df.loc[i,'総奪三振率'] = so_num / pitch_num

for col in df.columns:
    if '奪三振' in col:
        data_col.append(col)

data_col = data_col + ['総投球回']

df = df.sort_values('総奪三振率',ascending=False) # 奪三振率に応じてソートする

#print(data_col)
df = df[data_col] #データ表示をdata_col分だけにする

df.to_csv('probability_so.csv') #CSVファイルへ書き込み
#df.head(20)
