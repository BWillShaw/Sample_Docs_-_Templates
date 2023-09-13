import tkinter as tk
from tkinter import ttk

class InputFrame(tk.Frame):
    def __init__(self, master, label, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.label_frame = tk.Frame(self)
        self.label_frame.pack(side="left")
        
        self.input_frame = tk.Frame(self)
        self.input_frame.pack(side="left")
        
        self.label = ttk.Label(self.label_frame, text=label)
        self.label.pack()

class TimeAndDateFrame(InputFrame):
    def __init__(self, master, label, *args, **kwargs):
        super().__init__(master, label, *args, **kwargs)
        self.entry = ttk.Entry(self.input_frame)
        self.entry.pack()

class StringInputFrame(InputFrame):
    def __init__(self, master, label, *args, **kwargs):
        super().__init__(master, label, *args, **kwargs)
        self.entry = ttk.Entry(self.input_frame)
        self.entry.pack()

class DropdownFrame(InputFrame):
    def __init__(self, master, label, options, *args, **kwargs):
        super().__init__(master, label, *args, **kwargs)
        self.var = tk.StringVar()
        self.dropdown = ttk.Combobox(self.input_frame, textvariable=self.var, values=options)
        self.dropdown.pack()

class TickBoxFrame(InputFrame):
    def __init__(self, master, label, *args, **kwargs):
        super().__init__(master, label, *args, **kwargs)
        self.var = tk.BooleanVar()
        self.checkbox = ttk.Checkbutton(self.input_frame, variable=self.var)
        self.checkbox.pack()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Customer Information Form")
    root.geometry("1000x600")

    StringInputFrame(root, "First Name").pack(fill="x", padx=5, pady=5)
    StringInputFrame(root, "Last Name").pack(fill="x", padx=5, pady=5)
    StringInputFrame(root, "Email").pack(fill="x", padx=5, pady=5)
    DropdownFrame(root, "Gender", ["Male", "Female", "Other"]).pack(fill="x", padx=5, pady=5)
    TickBoxFrame(root, "Subscribe to newsletter").pack(fill="x", padx=5, pady=5)

    tk.Button(root, text="Submit", command=lambda: print("Form Submitted")).pack(padx=5, pady=5)

    root.mainloop()

