import tkinter as tk


class ExpenseForm(tk.Tk):
    def __init__(self):

        super().__init__()        # TKから__init__メソッドを呼び出す。
        self.title("入力フォーム")
        self.geometry("500x300")

        self.create_widgets()
        self.bind_widgets()
        self.resize_widgets()

    def create_widgets(self):
        # 日付入力欄の作成
        date_label = tk.Label(self, text="日付")
        date_label.grid(row=0, column=0)
        self.date_entry = tk.Entry(self)
        self.date_entry.grid(row=0, column=1)

        # 分類入力欄の作成
        category_label = tk.Label(self, text="分類")
        category_label.grid(row=1, column=0)
        self.category_entry = tk.Entry(self)
        self.category_entry.grid(row=1, column=1)

        # 値段入力欄の作成
        price_label = tk.Label(self, text="値段")
        price_label.grid(row=2, column=0)
        self.price_entry = tk.Entry(self)
        self.price_entry.grid(row=2, column=1)

        # 名称入力欄の作成
        name_label = tk.Label(self, text="名称")
        name_label.grid(row=3, column=0)
        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=3, column=1)

        # ボタンの作成
        submit_button = tk.Button(self, text="送信")
        submit_button.grid(row=4, column=1)
        
    def bind_widgets(self):
        # ボタンにコマンドを設定する
        submit_button = self.nametowidget("submit_button")
        submit_button.config(command=self.submit)
        
        # ウィンドウのサイズが変更された場合に入力欄の幅も変更する
        self.bind("<Configure>", self.resize_widgets)
        
    def resize_widgets(self, event=None):
        # 入力欄の幅をウィンドウの幅に合わせる
        for child in self.winfo_children():
            if isinstance(child, tk.Entry):
                child.config(width=self.winfo_width() // 2)
                
    def submit(self):
        # 送信ボタンがクリックされたときの処理を記述する
        pass
        

if __name__ == "__main__":
    form = ExpenseForm()
    form.mainloop()
