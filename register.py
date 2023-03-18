import sqlite3
import os.path
import datetime

class SQLopperation:
    def create_db(self):
        dbname = 'Account.db'
        if not os.path.isfile(dbname):
            conn = sqlite3.connect(dbname)
            # sqliteを操作するカーソルオブジェクトを作成
            cur = conn.cursor()

            # personsというtableを作成してみる
            # 大文字部はSQL文。小文字でも問題ない。
            cur.execute(
                '''CREATE TABLE persons(
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    date DATE NOT NULL,
                    category STRING NOT NULL,
                    price INTEGER NOT NULL,
                    name STRING NOT NULL
                    )
                '''
            )
            # データベースへコミット。これで変更が反映される。
            conn.commit()
            conn.close()

    def insert(self, datalist):
        data=1


if __name__ == '__main__':
    sample = {
        'date' : datetime.date(2022, 3, 18),
        'category' : '食費',
        'price' : 10000,
        
    }
    
    sql = SQLopperation()
    sql.create_db()

