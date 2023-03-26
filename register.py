import sqlite3
import os.path
import datetime


class ExpenseInput: 
  def __init__(self, date: datetime.date, category: str, price: int, item: str):
    self.date = date
    self.category = category
    self.price = price
    self.item = item
    # 入力値が正当なものかを判定する処理を追加することが望ましい


class ExpenseRegister:
    def __init__(self, dbname: str):
        self.dbname = dbname
    
    def create_db(self):
        if not os.path.isfile(self.dbname):
            conn = sqlite3.connect(self.dbname)
            # sqliteを操作するカーソルオブジェクトを作成
            cur = conn.cursor()

            # expenseというtableを作成
            cur.execute(
                '''CREATE TABLE expense(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date DATE NOT NULL,
                    category STRING NOT NULL,
                    price INTEGER NOT NULL,
                    item STRING NOT NULL
                    )
                '''
            )
            # データベースへコミット。これで変更が反映される。
            conn.commit()
            conn.close()

    def insert(self, data: ExpenseInput):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()

        query = """
            INSERT INTO expense
                (date, category, price, item)
            values
                (?, ?, ?, ?)
            """
        cur.execute(query,(data.date, data.category, data.price, data.item))
        conn.commit()
        conn.close()


if __name__ == '__main__':
    sample_data = ExpenseInput(
        datetime.date(2022, 3, 18),
        "食費",
        10000,
        "サンプル"
    )
    input_data = sample_data

    exp_reg = ExpenseRegister("Expense.db")
    exp_reg.create_db()
    exp_reg.insert(input_data)
