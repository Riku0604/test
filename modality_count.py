import pandas as pd
import numpy as np
import os
#CSVファイルの読み込み
data=pd.read_csv('deptDF.csv')
#部門人数格納用データフレームの生成
df=pd.DataFrame()
#行列の転置
data2=data.T


#各モダリティ人数の取得
df["RT"]=(data2=='RT').sum()
df["MR"]=(data2=='MR').sum()
df["TV"]=(data2=='TV').sum()
df["KS"]=(data2=='KS').sum()
df["NM"]=(data2=='NM').sum()
df["TV"]=(data2=='TV').sum()
df["XO"]=(data2=='XO').sum()
df["CT"]=(data2=='CT').sum()
df["XP"]=(data2=='XP').sum()
df["AG"]=(data2=='AG').sum()
df["ET"]=(data2=='ET').sum()
df["AS"]=(data2=='AS').sum()
#日付をindexに指定
df.index = np.arange(1, len(df)+1)

print(df)

#出力用フォルダを作成
os.makedirs("modality", exist_ok=True)

# CSVファイルを出力します
df.to_csv("modality\\addData.csv", index=True )