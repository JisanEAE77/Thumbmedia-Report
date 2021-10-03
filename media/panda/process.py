import pandas as pd
import numpy as np
import os
import pathlib
path=pathlib.Path().absolute()
dirname, filename = os.path.split(os.path.abspath(__file__))

file=dirname.replace('/panda', '/csv/output/')


df = pd.read_csv(file+'merge.csv.gz', index_col=None, header=0, low_memory=False)
df['Channel ID'] = np.where(df['Channel ID'].astype(str).str[:2]!='UC', 'UC' + df['Channel ID'],df['Channel ID'])
nd=df.groupby('Channel ID', as_index=False).aggregate({
    "Partner Revenue": "sum",
    "Country": "first",
    # "Channel Display Name": "first",
    # "Username": "first"
    "Content Type": "first"
})
nd['AdSense'] = np.where(nd['Content Type'].str.contains('Partner-provided'), nd['Partner Revenue'],0)
nd['Content ID'] = np.where(nd['Content Type'].str.contains('Partner-provided'), 0,nd['Partner Revenue'])
nd=nd.drop('Partner Revenue', axis=1).drop('Content Type', axis=1)


nd.to_csv(file+'partners.csv.gz', index=False, header=True)
print('success')
