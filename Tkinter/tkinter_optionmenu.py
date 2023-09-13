import tkinter as tk

def on_select(value):
    print(f"Selected value is {value}")

root = tk.Tk()

frame = tk.Frame(root)
frame.pack(pady=10, padx=10)

# Create an Entry widget
entry = tk.Entry(frame)
entry.pack(side=tk.LEFT)

# Create a Tkinter variable to hold the selected value from the drop-down
selected_value = tk.StringVar(frame)
selected_value.set("Option 1")  # default value

# Create the OptionMenu widget
drop_down = tk.OptionMenu(frame, selected_value, "Option 1", "Option 2", "Option 3", command=on_select)
drop_down.pack(side=tk.LEFT)

root.mainloop()
