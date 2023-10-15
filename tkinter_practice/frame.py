import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x300")

main_frame = ttk.Frame(root)
main_frame.pack(side="left", expand=True, fill="both")

tk.Label(main_frame, text="Label Top 1", background="yellow").pack(
    side="top", fill="both", expand=True)
tk.Label(main_frame, text="Label Top 2", background="blue").pack(
    side="top", fill="both", expand=True)
tk.Label(root, text="Label Left 3", background="green").pack(
    side="left", fill="both", expand=True)

root.mainloop()
