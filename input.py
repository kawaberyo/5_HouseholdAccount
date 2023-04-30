import tkinter as tk
from tkcalendar import DateEntry
from tkinter import ttk

class ExpenseForm(tk.Tk):
    def __init__(self):
        self.winsize = {"width":250, "height":170}
        self.font = ("メイリオ", 12)  # フォントの設定

        super().__init__()        # TKから__init__メソッドを呼び出す。
        self.title("入力フォーム")
        self.geometry("250x170")
        self.wm_minsize(width=self.winsize["width"], height=self.winsize["height"])
        self.window_center()
        self.create_widgets()
        self.bind_widgets()
        self.arrange_widgets()
        self.resize_entry()


    def create_widgets(self):
        # 日付入力欄の作成
        date_label = tk.Label(self, text="日付")
        date_label.grid(row=0, column=0)
        self.date_entry = DateEntry(self, width=30, background='darkblue', foreground='white', borderwidth=2, showweeknumbers=False)
        self.date_entry.grid(row=0, column=1)

        # 分類入力欄の作成
        # TODO: 分類情報をデータベースから持ってくる処理を書く
        options = ["Option 1", "Option 2", "Option 3"]
        category_label = tk.Label(self, text="分類")
        category_label.grid(row=1, column=0)
        self.category_entry = ttk.Combobox(self, values=options, width=30)
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
        submit_button = tk.Button(self, text="送信", command=self.submit_form, width=5)
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
        # フォームの内容をクリアして入力フォームを閉じる。
        self.date_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.destroy()


    def arrange_widgets(self, event=None):
        # ウィンドウが画面上に表示された後にウィンドウの幅を取得し、入力欄の幅を変更する
        for child in self.winfo_children():
            if isinstance(child, tk.Entry):
                margin = 50
                px_size = self.winfo_width()
                child.config(width=int(px_size))
                # サイズがピクセル表記で指定させるため、指定したサイズの実際のピクセルサイズを調べる
                borderwidth = child.winfo_reqwidth()
                # プルダウン式の入力枠は19ピクセルだけ大きいので、補正する
                if isinstance(child, (DateEntry,ttk.Combobox)):
                    margin += 19
                child.config(width=int((px_size-margin) * (px_size / borderwidth)))
            # フォントを変更する
            child.config(font=self.font)

    def resize_entry(self):
        # ウィンドウのサイズが変更された場合に入力欄の幅も変更する
        self.bind("<Configure>", self.arrange_widgets)

    def window_center(self):
        # ウィンドウを中央に移動する
        x_pos = (self.winfo_screenwidth() - self.winsize["width"]) / 2
        y_pos = (self.winfo_screenheight() - self.winsize["height"]) / 2
        self.geometry("+%d+%d" % (x_pos, y_pos))

if __name__ == "__main__":
    form = ExpenseForm()
    form.mainloop()
