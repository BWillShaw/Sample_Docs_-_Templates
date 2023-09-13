import tkinter as tk

def on_select(value):
    print(f"Selected value is {value}")

root = tk.Tk()

# Create a Tkinter variable to hold the selected value
selected_value = tk.StringVar(root)
selected_value.set("Option 1")  # set the default option

# Create the OptionMenu widget
drop_down = tk.OptionMenu(root, selected_value, "Option 1", "Option 2", "Option 3", command=on_select)
drop_down.pack()

root.mainloop()
