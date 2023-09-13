import tkinter as tk

# Create root
root = tk.Tk()
root.title("Brandon's First Form")
root.geometry("1000x600")
root.iconbitmap(r"C:\Users\brand\Python_Projects\Templates" +
                r"\Tkinter\transparent.ico")
root.configure(bg="lightblue")
root.grid_columnconfigure(1, minsize=0)

# Create frames
frame1 = tk.Frame(root)
frame2 = tk.Frame(root)

# Create widgets (objects)
label1 = tk.Label(frame1, text="Label 1")
entry1 = tk.Entry(frame1)

label2 = tk.Label(frame2, text="Label 2")
entry2 = tk.Entry(frame2)

# Pack widgets into their respective frames
label1.pack(side=tk.LEFT)
entry1.pack(side=tk.LEFT)

label2.pack(side=tk.LEFT)
entry2.pack(side=tk.LEFT)

# Pack frames into the root window
frame1.pack(pady=10)
frame2.pack(pady=10)

root.mainloop()
