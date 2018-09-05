#
#
# wips順にソート
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
# 2009~2018年の総WHIP数を計算
# 問題点：投球回の端数をどうするか.
#
for i in range(len(df)):
    df.loc[i,'総WHIP数'] = 0
    df.loc[i,'総投球回'] = 0
    df.loc[i,'総与四球'] = 0
    df.loc[i,'総与死球'] = 0
    df.loc[i,'総被安打'] = 0
    pitch_num = 0 # 投球回数
    base_on_balls_num = 0 # 四球数
    hit_by_pitch_num = 0 # 死球数
    hit_num = 0 # 被安打数
    for col in df.columns:
        if '投球回' in col:
            if not math.isnan(df.loc[i,col]):
                pitch_num += df.loc[i,col]
        if '与四球' in col:
            if not math.isnan(df.loc[i,col]):
                base_on_balls_num += df.loc[i,col]
        if '与死球' in col:
            if not math.isnan(df.loc[i,col]):
                hit_by_pitch_num += df.loc[i,col]
        if '被安打' in col:
            if not math.isnan(df.loc[i,col]):
                hit_num += df.loc[i,col]
    df.loc[i,'総投球回'] = pitch_num
    df.loc[i,'総与四球'] = base_on_balls_num
    df.loc[i,'総与死球'] = hit_by_pitch_num
    df.loc[i,'総被安打'] = hit_num
    #df.loc[i,'総WHIP数'] = (hit_num + base_on_balls_num + hit_by_pitch_num) / pitch_num
    df.loc[i,'総WHIP数'] = (hit_num + base_on_balls_num) / pitch_num

#print(df)
for col in df.columns:
    if 'WHIP' in col:
        data_col.append(col)

data_col = data_col + ['総投球回', '総与四球', '総与死球', '総被安打']

df = df.sort_values('総WHIP数',ascending=True) # 2018年の勝利数に応じてソートする

#print(data_col)
df = df[data_col] #データ表示をdata_col分だけにする

df.to_csv('whip.csv') #CSVファイルへ書き込み
#df.head(20)
