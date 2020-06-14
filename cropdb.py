import sqlite3
from sqlite3 import Error


def create_connection(database):
    conn = None
    try:
        conn = sqlite3.connect(database)
        print("cropdb.db opened database successfully")
    except Error as e:
        print(e)
    return conn


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    database = r"database/cropdb.db"
    table_creation = r"ddl/tbl_crop.ddl"
    connection = create_connection(database)
    create_table(connection, table_creation)

if __name__ == '__main__':
    main()


cursorObj = conn.cursor()
cursorObj.execute('ddl/tbl_crop.ddl')




