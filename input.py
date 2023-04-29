import tkinter as tk

class InputWindow:
    def create(self):
        # ウィンドウを作成する
        window = tk.Tk()
        window.title("入力フォーム")
        window.geometry("500x300")


        # 日付入力欄の作成
        date_label = tk.Label(window, text="日付")
        date_label.grid(row=0, column=0)
        date_entry = tk.Entry(window)
        date_entry.grid(row=0, column=1)

        # 分類入力欄の作成
        category_label = tk.Label(window, text="分類")
        category_label.grid(row=1, column=0)
        category_entry = tk.Entry(window)
        category_entry.grid(row=1, column=1)

        # 値段入力欄の作成
        price_label = tk.Label(window, text="値段")
        price_label.grid(row=2, column=0)
        price_entry = tk.Entry(window)
        price_entry.grid(row=2, column=1)

        # 名称入力欄の作成
        name_label = tk.Label(window, text="名称")
        name_label.grid(row=3, column=0)
        name_entry = tk.Entry(window)
        name_entry.grid(row=3, column=1)

        # ボタンの作成
        submit_button = tk.Button(window, text="送信")
        submit_button.grid(row=4, column=1)


        # 入力欄の幅をウィンドウの幅に合わせる
        for child in window.winfo_children():
            if isinstance(child, tk.Entry):
                child.config(width=window.winfo_width() // 2)
                
        # ウィンドウのサイズが変更された場合に入力欄の幅も変更する
        def resize_entries(event):
            for child in window.winfo_children():
                if isinstance(child, tk.Entry):
                    child.config(width=event.width // 2)
                    
        window.bind("<Configure>", resize_entries)


        # ウィンドウを表示する
        window.mainloop()

input_data = InputWindow().create()
