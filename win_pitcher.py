import data_structure as data
import pandas as pd
#
#
# データの操作部分
#
#
#data = '勝利'
data_col = ['選手名2017']
for col in data.df_m.columns:
    #print(col)
    if '勝利' in col:
        data_col.append(col)
        #print(data_col)
data.df_m = pd.concat(data.df_all,axis=1)
#print(df_m)
data.df_m = data.df_m.sort_values('勝利2017',ascending=False) # 2017年の勝利数に応じてソートする
#print(df_m)
data.df_m = data.df_m[data_col] #データ表示をdata_col分だけにする
#print(df_m)
data.df_m.to_csv('勝利数.csv') #CSVファイルへ書き込み
#df_m.head(20)

#print(df_m)
