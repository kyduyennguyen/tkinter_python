import tkinter as tk
from tkinter import ttk
import tkinter.font as font

root = tk.Tk()
root.title("Distance Converter")

font.nametofont("TkDefaultFont").configure(size=15)

metres_value = tk.StringVar()
feet_value = tk.StringVar(value="Feet shown here")


def calculateFeet(*args):
    try:
        metres = float(metres_value.get())
        feet = metres * 3.28084
        feet_value.set(f"{feet:.3f}")
    except ValueError:
        pass


root.columnconfigure(0, weight=1)

main_frame = ttk.Frame(root, padding=(30, 15))
main_frame.grid()


# --- Widgets ---
metres_label = tk.Label(main_frame, text="Metres: ")
metres_input = tk.Entry(
    main_frame, textvariable=metres_value, font=("Segoe UI", 15))
feet_label = tk.Label(main_frame, text="Feet: ")
feet_display = tk.Label(main_frame, textvariable=feet_value)
feet_button = tk.Button(
    main_frame, text="Calculate Feet", command=calculateFeet)

# --- Layout ---
metres_label.grid(column=0, row=0, sticky="W")
metres_input.grid(column=1, row=0, sticky="EW")
metres_input.focus()

feet_label.grid(column=0, row=1, sticky="W")
feet_display.grid(column=1, row=1, sticky="EW")
feet_button.grid(column=0, row=2, columnspan=2, sticky="EW")

for child in main_frame.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.bind("<Return>", calculateFeet)
root.bind("<KP_Enter>", calculateFeet)

root.mainloop()
