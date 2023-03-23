import unittest
import sqlite3
import os.path
import datetime
from register import SQLopperation

class TestSQLopperation(unittest.TestCase):

    def setUp(self):
        self.sql = SQLopperation()
        self.sample = {
            'date': datetime.date(2022, 3, 18),
            'category': '食費',
            'price': 10000,
            'item': 'サンプル'
        }
        self.sql.create_db()

    def tearDown(self):
        os.remove(self.sql.dbname)

    def test_insert(self):
        self.sql.insert(self.sample)
        conn = sqlite3.connect(self.sql.dbname)
        cur = conn.cursor()
        cur.execute("SELECT * FROM account")
        result = cur.fetchone()
        self.assertEqual(result[1], str(self.sample['date']))
        self.assertEqual(result[2], self.sample['category'])
        self.assertEqual(result[3], self.sample['price'])
        self.assertEqual(result[4], self.sample['item'])

if __name__ == '__main__':
    unittest.main()