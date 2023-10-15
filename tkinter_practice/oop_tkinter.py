import tkinter as tk
from tkinter import ttk


class UseInputFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.input_users = tk.StringVar()

        label = tk.Label(self, text="Enter your name: ")
        entry = tk.Entry(self, textvariable=self.input_users)
        button = tk.Button(self, text="Greet", command=self.greet)

        label.pack(side="left")
        entry.pack(side="left")
        entry.focus()
        button.pack(side="left")

    def greet(self):
        print(f"Hello {self.input_users.get()}!")


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Hello, World!")

        UseInputFrame(self).pack(padx=15, pady=15)


app = App()
app.mainloop()
