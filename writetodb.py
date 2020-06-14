
import csv, sqlite3
import pandas as pd

df = pd.read_csv(r'../input/dataset/Production_Crops_E_All_Data.csv',encoding='unicode_escape')

#print(df)

database = r"database/cropdb.db"
conn = sqlite3.connect(database)
df.to_sql('CROP', conn, if_exists='replace', index = False)