# ChatGPTにて作成

import unittest
import tkinter as tk
from tkcalendar import DateEntry
from tkinter import ttk
from unittest.mock import MagicMock

from input import ExpenseForm

class TestExpenseForm(unittest.TestCase):
    def setUp(self):
        self.form = ExpenseForm()

    def tearDown(self):
        self.form.destroy()

    def test_create_widgets(self):
        self.assertIsInstance(self.form.date_entry, DateEntry)
        self.assertIsInstance(self.form.category_entry, ttk.Combobox)
        self.assertIsInstance(self.form.price_entry, tk.Entry)
        self.assertIsInstance(self.form.name_entry, tk.Entry)

    def test_submit_form(self):
        # submit_formメソッドが呼ばれたときに、入力フォームの内容を取得できるかどうかを確認する
        self.form.date_entry.set_date("2023-05-04")
        self.form.category_entry.set("Option 1")
        self.form.price_entry.insert(0, "1000")
        self.form.name_entry.insert(0, "Test")
        self.form.destroy = MagicMock()
        self.form.submit_form()
        self.assertEqual(self.form.information, ["2023-05-04", "Option 1", "1000", "Test"])
        self.form.destroy.assert_called_once()

if __name__ == "__main__":
    unittest.main()


"""
このテストコードでは、ExpenseFormクラスの以下の2つのメソッドをテストしています。

・test_create_widgets: ExpenseFormクラスのインスタンス生成後、
日付入力欄、分類入力欄、値段入力欄、名称入力欄が正しく作成されているかどうかを確認する。

・test_submit_form: 入力フォームに値を入力し、
送信ボタンを押下したときに、入力フォームの内容が正しく取得でき、
self.informationが正しい値を持っているかどうかを確認する。
また、フォームをクリアするためのdestroyメソッドが呼び出されているかどうかも確認する。
"""