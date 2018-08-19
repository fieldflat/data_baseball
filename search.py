#
# 文字列を入力し, その選手の成績を表示する.
#

import pandas as pd
import data_structure as data

while 1 == 1:
    str = input('Input player\'s name >>> ')
    if str == '':
        break
    k=1
    for i in data.df_m.index:
        if data.df_m.loc[i,'登録名'] == str:
            print(data.df_m.iloc[i,0:])
            k=0

    if k == 1:
        print('No data')
