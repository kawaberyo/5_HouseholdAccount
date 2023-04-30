import tkinter as tk
import tkinter.font as tkFont

class ExpenseForm(tk.Tk):
    def __init__(self):

        super().__init__()        # TKから__init__メソッドを呼び出す。
        self.title("入力フォーム")
        self.geometry("500x300")
        self.wm_minsize(width=500, height=300)
        
        self.create_widgets()
        self.bind_widgets()
        self.arrange_widgets()
        self.resize_entry()

    def create_widgets(self):
        # 日付入力欄の作成
        date_label = tk.Label(self, text="日付")
        date_label.grid(row=0, column=0)
        self.date_entry = tk.Entry(self, width=30)
        self.date_entry.grid(row=0, column=1)

        # 分類入力欄の作成
        category_label = tk.Label(self, text="分類")
        category_label.grid(row=1, column=0)
        self.category_entry = tk.Entry(self, width=30)
        self.category_entry.grid(row=1, column=1)

        # 値段入力欄の作成
        price_label = tk.Label(self, text="値段")
        price_label.grid(row=2, column=0)
        self.price_entry = tk.Entry(self, width=30)
        self.price_entry.grid(row=2, column=1)

        # 名称入力欄の作成
        name_label = tk.Label(self, text="名称")
        name_label.grid(row=3, column=0)
        self.name_entry = tk.Entry(self, width=30)
        self.name_entry.grid(row=3, column=1)


    def bind_widgets(self):
        # ボタンの作成
        submit_button = tk.Button(self, text="送信", command=self.submit_form)
        submit_button.grid(row=4, column=0, columnspan=2)

    def submit_form(self):
        # フォームの内容を取得する
        date = self.date_entry.get()
        category = self.category_entry.get()
        price = self.price_entry.get()
        name = self.name_entry.get()

        # TODO: フォームの内容をどこかに保存する処理を書く
        print(f"データ入手・・・日付: {date}、分類: {category}、値段: {price}、名前: {name}")

        # フォームをクリアする
        self.clear_form()

    def clear_form(self):
        # フォームの内容をクリアする
        self.date_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)


    def arrange_widgets(self, event=None):
        # ウィンドウが画面上に表示された後にウィンドウの幅を取得し、入力欄の幅を変更する
        self.update()

        # テキストの測定

        for child in self.winfo_children():
            if isinstance(child, tk.Entry):
                px_size = self.winfo_width()
                child.config(width=int(px_size))
                print(px_size)
                font = tkFont.Font(family=child.cget("font"), size=child.cget("width"))
                font_width = font.measure("テキスト")
                print(font_width)
                child.config(width=int(px_size * px_size / font_width / 2))

    def resize_entry(self):
        # ウィンドウのサイズが変更された場合に入力欄の幅も変更する
        self.bind("<Configure>", self.arrange_widgets)

if __name__ == "__main__":
    form = ExpenseForm()
    form.mainloop()
