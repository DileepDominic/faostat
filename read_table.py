import sqlite3
from pandas import DataFrame

database = r"database/cropdb.db"
conn = sqlite3.connect(database)
c = conn.cursor()

c.execute('''  
select distinct Area from CROP
          ''')

df = DataFrame(c.fetchall(), columns=['Area'])    
print(df)