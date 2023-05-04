import sqlite3
import os.path
import datetime
import re


class ExpenseInput:
    def __init__(self, date: datetime.date, category: str, price: int, item: str):
        if not isinstance(date, datetime.date):
            raise ValueError("Invalid date format")
        self.date = date

        if not isinstance(category, str) or not re.match(r'^[a-zA-Z\sぁ-んァ-ン一-龥]+$', category):
            raise ValueError("Invalid category")
        self.category = category

        if not isinstance(price, int) or price <= 0:
            raise ValueError("Invalid price")
        self.price = price

        if not isinstance(item, str) or not re.match(r'^[a-zA-Z\sぁ-んァ-ン一-龥]+$', item):
            raise ValueError("Invalid item")
        self.item = item


class ExpenseRegister:
    def __init__(self, dbname: str):
        self.dbname = dbname

    def create_db(self):
        if not os.path.isfile(self.dbname):
            try:
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
                        );
                    '''
                )
                # データベースへコミット。これで変更が反映される。
                conn.commit()

                # categoryというtableを作成
                cur.execute(
                    '''CREATE TABLE category (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT UNIQUE NOT NULL
                        );
                    '''
                )
                # データベースへコミット。これで変更が反映される。
                conn.commit()

            except Exception as e:
                print("Error:", e)

            finally:
                conn.close()

    def insert(self, data: ExpenseInput):
        try:
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

        except Exception as e:
            print("Error:", e)

        finally:
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
