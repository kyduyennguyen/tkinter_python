import tkinter as tk
from tkinter import ttk
import tkinter.font as font


class DistanceCoverter(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Distance Converter")
        # self.columnconfigure(0, weight=1)
        self.frames = dict()

        # main_frame = CalculateFrame(self, padding=(30, 15))
        # main_frame.grid()
        container = ttk.Frame(self)
        container.grid(padx=60, pady=30, sticky="EW")

        meets_to_feet = MetresToFeet(container, self)
        meets_to_feet.grid(column=0, row=0, sticky="NSEW")

        feet_to_metres = FeetToMetres(container, self)
        feet_to_metres.grid(column=0, row=0, sticky="NSEW")

        self.frames[MetresToFeet] = meets_to_feet
        self.frames[FeetToMetres] = feet_to_metres

        self.show_frames(MetresToFeet)

        for FrameClass in (FeetToMetres, MetresToFeet):
            frame = FrameClass(container, self)
            self.frames[FrameClass] = frame
            frame.grid(column=0, row=0, sticky="NSEW")

        # --- action when press Enter for button ---
        # self.bind("<Return>", main_frame.calculateFeet)
        # self.bind("<KP_Enter>", main_frame.calculateFeet)
        # self.bind("<Return>", frame.calculate)
        # self.bind("<KP_Enter>", frame.calculate)

    def show_frames(self, container):
        frame = self.frames[container]
        frame.tkraise()


class MetresToFeet(ttk.Frame):
    def __init__(self, container, controller, **kwargs):
        super().__init__(container, **kwargs)

        self.metres_value = tk.StringVar()
        self.feet_value = tk.StringVar(value="Feet shown here")

        # --- Widgets ---
        self.metres_label = ttk.Label(self, text="Metres: ")
        self.metres_input = ttk.Entry(
            self, textvariable=self.metres_value, font=("Segoe UI", 15))
        self.feet_label = ttk.Label(self, text="Feet: ")
        self.feet_display = ttk.Label(self, textvariable=self.feet_value)
        self.feet_button = ttk.Button(
            self, text="Calculate Feet", command=self.calculate_feet)
        self.switch_page_button = ttk.Button(
            self, text="Switch to feet conversion", command=lambda: controller.show_frames(FeetToMetres))

        # --- Layout ---
        self.metres_label.grid(column=0, row=0, sticky="W")
        self.metres_input.grid(column=1, row=0, sticky="EW")
        self.metres_input.focus()

        self.feet_label.grid(column=0, row=1, sticky="W")
        self.feet_display.grid(column=1, row=1, sticky="EW")
        self.feet_button.grid(column=0, row=2, columnspan=2, sticky="EW")
        self.switch_page_button.grid(
            column=0, row=3, columnspan=2, sticky="EW")

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def calculate_feet(self, *args):
        try:
            metres = float(self.metres_value.get())
            feet = metres * 3.28084
            self.feet_value.set(f"{feet:.3f}")
        except ValueError:
            pass


class FeetToMetres(ttk.Frame):
    def __init__(self, container, controller, **kwargs):
        super().__init__(container, **kwargs)

        self.metres_value = tk.StringVar(value="Metres shown here")
        self.feet_value = tk.StringVar()

        # --- Widgets ---
        self.feet_label = ttk.Label(self, text="Feet: ")
        self.feet_input = ttk.Entry(
            self, textvariable=self.feet_value, font=("Segoe UI", 15))
        self.metres_label = ttk.Label(self, text="Metres: ")
        self.metres_display = ttk.Label(self, textvariable=self.metres_value)
        self.metres_button = ttk.Button(
            self, text="Calculate Metres", command=self.calculate)
        self.switch_page_button = ttk.Button(
            self, text="Switch to metres conversion", command=lambda: controller.show_frames(MetresToFeet))

        # --- Layout ---
        self.feet_label.grid(column=0, row=0, sticky="W")
        self.feet_input.grid(column=1, row=0, sticky="EW")
        self.feet_input.focus()

        self.metres_label.grid(column=0, row=1, sticky="W")
        self.metres_display.grid(column=1, row=1, sticky="EW")
        self.metres_button.grid(column=0, row=2, columnspan=2, sticky="EW")
        self.switch_page_button.grid(
            column=0, row=3, columnspan=2, sticky="EW")

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def calculate(self, *args):
        try:
            feet = float(self.feet_value.get())
            metres = feet / 3.28084
            self.metres_value.set(f"{metres:.3f}")
        except ValueError:
            pass


root = DistanceCoverter()

font.nametofont("TkDefaultFont").configure(size=15)

root.mainloop()
