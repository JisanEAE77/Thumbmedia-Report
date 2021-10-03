import pandas as pd
import glob
import os
import pathlib
import sys
path=pathlib.Path().absolute()
dirname, filename = os.path.split(os.path.abspath(__file__))
dnp=sys.argv[1]
path=dirname.replace('/panda', '/'+dnp)

all_files = glob.glob(path + "/*.csv.gz")

li = []
hd=1 if dnp=='premium' else 0

for filename in all_files:

    df = pd.read_csv(filename, index_col=None, header=hd, low_memory=False)
    if 'Username' not in df:
        if filename.find('ThumbMedia') != -1:
            username = 'ThumbMedia'
        elif filename.find('Thumb_Media_Music') != -1:
            username = 'Thumb_Media_Music'
        else:
            username = 'Thumb_Media'
    df['Username'] = username
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)
frame.to_csv(path+'/output/merge.csv.gz', index = False, header=True)

print('success')





