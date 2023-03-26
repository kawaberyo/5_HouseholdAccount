import sqlite3
import os.path
import datetime

class SQLInput: # このクラス名はイマイチ
  def __init__(self, date:datetime, category:str, price:int, item:str):
    self.date = date
    self.category = category
    self.price = price
    self.item = item
    # この辺に書く入力値が正当なものかを判定する処理追加


class SQLRegister:
    def __init__(self, dbname:str):
        self.dbname = dbname
    
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

    def insert(self, data: SQLInput):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()

        query = """
            INSERT INTO account
                (date, category, price, name)
            values
                (?, ?, ?, ?)
            """
        cur.execute(query,(data.date, data.category, data.price, data.item))
        conn.commit()
        conn.close()


if __name__ == '__main__':
    sample_data = SQLInput(
        datetime.date(2022, 3, 18),
        "食費",
        10000,
        "サンプル"
    )
    input_data = sample_data

    sql = SQLRegister("Account.db")
    sql.create_db()
    sql.insert(input_data)

