import sqlite3
import os.path
import datetime

class SQLopperation:
    def __init__(self):
        self.dbname = 'Account.db'
    
    def create_db(self):
        if not os.path.isfile(self.dbname):
            conn = sqlite3.connect(self.dbname)
            # sqliteを操作するカーソルオブジェクトを作成
            cur = conn.cursor()

            # accountというtableを作成してみる
            # 大文字部はSQL文。小文字でも問題ない。
            cur.execute(
                '''CREATE TABLE account(
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

    def insert(self, data):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()

        conn.commit()
        conn.close()


if __name__ == '__main__':
    sample = {
        'date' : datetime.date(2022, 3, 18),
        'category' : '食費',
        'price' : 10000,
        'item' : 'サンプル'
    }
    
    sql = SQLopperation()
    sql.create_db(sample)

