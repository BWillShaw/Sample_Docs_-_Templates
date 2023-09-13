import tkinter as tk 
from tkinter import ttk

def fetch_input():
    user_input = q1_entry.get()
    print(f"\nYou entered: {user_input}")

root = tk.Tk()
root.title("Brandon's First Form")
root.geometry("1000x600")
root.iconbitmap(r"C:\Users\brand\Python_Projects\Templates" +
                r"\Tkinter\transparent.ico")
root.configure(bg="lightblue")
root.grid_columnconfigure(1, minsize=0)

# Title label 
Welcome_label = ttk.Label(
    root, 
    text="Welcome to the Quiz Form!",
    background="lightblue", 
    font=("Arial",20)
    )
# Position for title label
Welcome_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

# Label for First Name input
q1_label = ttk.Label(
    root, 
    text="First Name:",
    background="lightblue", 
    font=("Arial",10)
    )

# Position for First Name label
q1_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

# Create First Name entry variable object
first_name = tk.StringVar()

# First Name entry field, variable set to entry object
q1_entry = ttk.Entry(
    root,
    textvariable=first_name,
    font = ("Arial", 10)
)

# Position for entry field
q1_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

# First Name submission button
q1_button = ttk.Button(
    root,
    text="Submit",
    command=fetch_input
)

q1_button.grid(row=3, column=0, padx=10, pady=10, sticky="w")



#style = ttk.Style(root)
#style.theme_use('vista')


root.mainloop()