import tkinter as tk
import requests


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("API данные")
        self.root.geometry("400x300")

        tk.Button(root, text="Случайная шутка", command=self.joke).pack(pady=5)

        self.text = tk.Text(root, height=10, width=50)
        self.text.pack(pady=10)

        tk.Button(root, text="Очистить", command=self.clear).pack()

    def joke(self):
        try:
            data = requests.get("https://official-joke-api.appspot.com/random_joke").json()
            self.text.insert(tk.END, f"😄 {data['setup']}\n{data['punchline']}\n\n")
        except:
            self.text.insert(tk.END, "Ошибка получения данных\n\n")

    def clear(self):
        self.text.delete(1.0, tk.END)


root = tk.Tk()
app = App(root)
root.mainloop()
