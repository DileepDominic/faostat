import pandas as pd
import sqlite3
from pandas.io import sql

cnx = sqlite3.connect('database/cropdb.db')
df = pd.read_csv('dataset/Production_Crops_E_All_Data.csv', header=1)
sql.to_sql(df, 
                name='CROP', 
                con=cnx, 
                if_exists='append') 
cnx.close()   