import tkinter as tk
# ttk are new set of widgets
from tkinter import ttk
# tkinter._test()

# # Enabling High-DPI in Window 10
# try:
#     from ctypes import windll
#     windll.shcore.SetProcessDpiAwereness(1)
# except:
#     pass


def greet():
    # user_name.get() => get value
    print(f"Hello, {user_name.get() or 'World'} ")


# Create a window
root = tk.Tk()
# root.geometry("300x100")
root.title("Greeter")

# column with index 0 and weight = 1
root.columnconfigure(0, weight=1)

# # pack puts elements to window
# ttk.Label(root, text="Hello, World!", padding=(30, 10)).pack()

# Create frame for user field
user_frame = ttk.Frame(root, padding=(20, 10, 20, 0))
# user_frame.pack(side="top")
user_frame.grid(row=0, column=0, sticky="EW")

user_name = tk.StringVar()
# create textbox input user name with entry field
name_label = ttk.Label(user_frame, text="Name: ")
# name_label.pack(side="left", padx=(0, 10))
name_label.grid(row=0, column=0)
name_entry = ttk.Entry(user_frame, width=15, textvariable=user_name)
# name_entry.pack(side="left")
name_entry.grid(row=0, column=1)
name_entry.focus()

# Create frame for buttons
buttons_frame = ttk.Frame(root, padding=(20, 0, 20, 10))
# buttons_frame.pack(side="top")
buttons_frame.grid(row=1, column=0, sticky="EW")
buttons_frame.columnconfigure(0, weight=1)
buttons_frame.columnconfigure(1, weight=1)

# create BUTTON
greet_button = ttk.Button(buttons_frame, text="Greet", command=greet)
# greet_button.pack(side="left", fill="both", expand=True)
# greet_button.pack(side="left")
greet_button.grid(row=0, column=0, sticky="EW")

quit_button = ttk.Button(buttons_frame, text="Quit", command=root.destroy)
# quit_button.pack(side="left")
quit_button.grid(row=0, column=1, sticky="EW")

# excute to display window (start application)
root.mainloop()
