import unittest
import os.path
import sqlite3
from datetime import date
from register import ExpenseInput, ExpenseRegister


class TestExpenseRegister(unittest.TestCase):
    def setUp(self):
        self.dbname = "test_expense.db"
        self.exp_reg = ExpenseRegister(self.dbname)
        self.exp_reg.create_db()
        self.sample_data = ExpenseInput(
            date(2022, 3, 18),
            "食費",
            10000,
            "サンプル"
        )

    def tearDown(self):
        os.remove(self.dbname)

    def test_insert(self):
        self.exp_reg.insert(self.sample_data)

        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        cur.execute("SELECT * FROM expense")
        result = cur.fetchone()

        self.assertEqual(result[1], str(self.sample_data.date))
        self.assertEqual(result[2], self.sample_data.category)
        self.assertEqual(result[3], self.sample_data.price)
        self.assertEqual(result[4], self.sample_data.item)

        conn.commit()
        conn.close()

if __name__ == '__main__':
    unittest.main()


"""

テストプログラムの説明:
・unittestモジュールをインポートし、
    unittest.TestCaseクラスを継承したTestExpenseRegisterクラスを定義します。
・setUpメソッドは、各テストメソッドが実行される前に実行されます。
    ここでは、テスト用のデータベースファイルを作成し、
    ExpenseRegisterクラスのインスタンスとExpenseInputクラスのインスタンスを作成します。
・tearDownメソッドは、各テストメソッドが実行された後に実行されます。
    ここでは、テスト用のデータベースファイルを削除します。
・test_insertメソッドは、
    ExpenseRegister.insertメソッドが正しく動作するかをテストします。
    ExpenseRegister.insertメソッドを呼び出してサンプルデータを挿入し、
    データベースから取得した結果とサンプルデータを比較して、
    正しく挿入されたかどうかを検証します。


このテストでは、
setUp()メソッドでExpenseRegisterオブジェクトとテストデータをセットアップし、
tearDown()メソッドでテスト後にデータベースファイルを削除します。
test_insert()メソッドでは、insert()メソッドを呼び出し、
その後、データベースに挿入されたデータが正しいかどうかを検証します。
"""