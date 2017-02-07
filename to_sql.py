from sqlalchemy import create_engine
import pandas as pd
import glob

cnx = create_engine(
    'postgresql://aliphelan:khaL3#si@34.198.205.31:5432/aliphelan')

path ='fars_data/'
all_files = glob.glob(path + "/*.csv")

list_ = []
for file_ in all_files:
    df = pd.read_csv(file_,index_col=None, header=0)
    list_.append(df)