import tkinter as tk 
from tkinter import ttk
from PIL import Image, ImageTk

# intialise main window
root = tk.Tk()
root.title('Custom Window Demo')

# Use external 'transparent.ico' file to remove Tk
# icon. 16 x 16, 32 bpp, 8-bit alpha .ico using GIMP
root.iconbitmap(r"C:\Users\brand\Python_Projects\Templates\Tkinter\transparent.ico")

# root.geometry = window size
root.geometry("600x400")

# root.configure(bg=[color]) sets the background color
# Can also use hex (#FF0000) or rgb tuple (255,0,0)
root.configure(bg='lightblue')

# root.configure(cursor=[type]) sets the type of cursor
root.configure(cursor='arrow')

# create a label object and configure with tkk.Label()
label = ttk.Label(root, text="User Input 1", background='lightblue', font=('Arial', 14))

# label.grid(row=, column=, padx=, pady=) used for position
label.grid(row=0, column=0, padx=10, pady=10)

# create a user entry object using ttk.Entry
entry = ttk.Entry(root, font=('Arial', 14))

# entry.grid to position user input field
entry.grid(row=0, column=1, padx=10, pady=10)

# create a button object for user to submit
button = ttk.Button(root, text="Submit")

# button.grid to position submit button
button.grid(row=0, column=3, padx=10, pady=10)

# create style object to implement Windows theme
style = ttk.Style(root)
style.theme_use('vista')

root.mainloop()