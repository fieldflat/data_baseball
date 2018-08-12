import numpy
import pandas as pd

#urlをリスト形式で取得
df_all = [] #各要素に各年のデータが入る
years = range(17,8,-1) # years = [17,16,15,...,8]
urls = []
ii = 2017

#URLを入力：2017年だけ命名規則が違う
for year in years:
    if(year==17):
        urls.append('http://baseball-data.com/stats/pitcher-all/era-1.html')
    else:
        urls.append('http://baseball-data.com/'+ "{0:02d}".format(year)+'/stats/pitcher-all/era-1.html')

#データをURLから取得
for url in urls:
    print('取得URL：'+url)
    df = pd.io.html.read_html(url) #URLから情報を読み取る
    df = df[0] # 様々なtableデータがdf[0], df[1], ... というリストに格納されていく. 最初のtableのみを使用するため, df[0]を指定する.
    #df.to_csv('{0}.csv'.format(ii)) #CSVファイルへ書き込み
    ii = ii - 1
    df_all.append(df) # [[],[],[],...,[]]の形の2重リストになっている.

#選手IDの作成
name_list = []
dic = {}
for i in range(len(df_all)):
    name_list.extend(df_all[i]['選手名']) # extend ... リスト同士の連接
    #print(df_all[i]['選手名'])
name_list = list(set(name_list)) # setは集合を表す. リストのように順番は持たず, 重複するデータは一つにまとめられる. (上のコード実行で名前が重複しているため, これを実行)
#print(name_list)
for i,name in enumerate(name_list): # iには0,1,2..., nameにはname_listの内容が順々に格納されていく.
    #print('i:{0}\t name:{1}'.format(i, name))
    dic[name] = i

#ディクショナリdicには, 名前と選手IDの対が格納されている.
#選手IDの付与
for i in range(len(df_all)): #iは年数のindex
    df_all[i]['ID'] = -1
    for j in range(len(df_all[i])):
        df_all[i].loc[j,'ID'] = dic[df_all[i].loc[j,'選手名']] #df_all[i]の各データの'ID'に,先ほど作成したdicの選手IDを付与. jは各行を示す.
        #print(df_all[i])
    df_all[i].index = df_all[i]['ID']
    #print(df_all[i].index)
    df_all[i] = df_all[i].drop('ID',axis=1) #ID列を削除

#index被りを除去
#過去に複数の球団に所属していた場合は, 複数の名前が存在しているので, それを取り除く
for i in range(len(df_all)):
    doubled_index = []
    count = df_all[i].index.value_counts()
    for j in count.index:
        if(count.loc[j]>1):
            doubled_index.append(j)
    df_all[i] = df_all[i].drop(doubled_index)

#カラム名に年を付ける
ii=2017
for i in range(len(df_all)):
    for col_name in df_all[i].columns:
        df_all[i] = df_all[i].rename(columns = {col_name:col_name+"20"+"{0:02d}".format(years[i])}) #選手名2017のように...
    df_all[i].to_csv('{0}.csv'.format(ii)) #CSVファイルへ書き込み
    ii = ii-1

df_m = pd.concat(df_all,axis=1)
df_m.to_csv('all_pitcher_data.csv') #CSVファイルへ書き込み
#print(df_m)
