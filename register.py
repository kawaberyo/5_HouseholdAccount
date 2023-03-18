import sqlite3
import os.path

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
                    name STRING NOT NULL,
                    )'
                '''
            )
            # データベースへコミット。これで変更が反映される。
            conn.commit()
            conn.close()


if __name__ == "__main__":
    sql = SQLopperation()
    sql.create_db()

