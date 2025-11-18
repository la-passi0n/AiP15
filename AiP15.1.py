import tkinter as tk
import requests


class CatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Факты о кошках")
        self.root.geometry("350x250")

        tk.Label(root, text="🐱 Факты о кошках", font=("Arial", 14)).pack(pady=10)

        tk.Button(root, text="Получить факт",
                  command=self.get_fact, width=15).pack(pady=10)

        self.text = tk.Text(root, height=8, width=40)
        self.text.pack(pady=10, padx=10)

        self.status = tk.Label(root, text="Нажмите кнопку")
        self.status.pack()

    def get_fact(self):
        try:
            self.status.config(text="Загружаем...")
            response = requests.get("https://catfact.ninja/fact")
            data = response.json()

            self.text.delete(1.0, tk.END)
            self.text.insert(tk.END, data['fact'])
            self.status.config(text="Факт загружен!")

        except:
            self.text.delete(1.0, tk.END)
            self.text.insert(tk.END, "Ошибка загрузки")
            self.status.config(text="Ошибка")


root = tk.Tk()
app = CatApp(root)
root.mainloop()
