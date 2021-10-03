import pandas as pd
import numpy as np
import os
import pathlib
path=pathlib.Path().absolute()
dirname, filename = os.path.split(os.path.abspath(__file__))
dirname=dirname.replace('/panda', '')
f1 = os.path.join(dirname, 'csv/output/partners.csv.gz') # use your path
f2 = os.path.join(dirname, 'premium/output/partners.csv.gz')# use your path
f3 = os.path.join(dirname, 'super/output/partners.csv.gz') # use your path
op = os.path.join(dirname, 'total.csv.gz') # use your path

files=[f1,f2,f3]
print(dirname)

df1 = pd.read_csv(f1, index_col=None, header=0, low_memory=False)
df2 = pd.read_csv(f2, index_col=None, header=0, low_memory=False)
df3 = pd.read_csv(f3, index_col=None, header=0, low_memory=False)

df=df1.merge(df2,on='Channel ID',how='outer').merge(df3,on='Channel ID',how='outer')\
    .drop('Country_y', axis=1)\
    .drop('Country', axis=1).rename(columns={"Country_x":"Country"})

df['YT Premium']=df['YT Premium'].replace(np.nan, 0)
df['AdSense']=df['AdSense'].replace(np.nan, 0)
df['Content ID']=df['AdSense'].replace(np.nan, 0)
df['Super Chat']=df['Super Chat'].replace(np.nan, 0)
df['Total Earnings NO SuperChat'] = df['YT Premium']+df['AdSense']
df['Content ID']=0
df['Country US Totals']=np.where(df['Country'].astype(str).str[:2]=='US', df['YT Premium']+df['Content ID']+df['AdSense']+df['Super Chat'],0)
df = df[["Username", "Channel ID",  "Channel Display Name","AdSense","Content ID","YT Premium","Total Earnings NO SuperChat"
    ,"Super Chat","Country US Totals"]]
# df.pop('Country_y')
# df.rename(columns={"Country_x":"Country"})
print(df)
df.to_csv(op, index = False, header=True)
