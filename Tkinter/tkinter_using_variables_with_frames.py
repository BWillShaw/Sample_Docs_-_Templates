from tkinter import *
from tkinter import ttk
# import ThemedTk library
from ttkthemes import ThemedTk

# Creating root using ThemedTk
root = ThemedTk(theme="arc")

# Setting window width and height
root.geometry("1000x600")

# Overlay bitmap to remove Python logo
root.iconbitmap(r"C:\Users\brand\Python_Projects" +
                r"\Templates\Tkinter\transparent.ico")

# Setting root title
root.title("Pillar II Configuration")

# Create frames

# F1 - Legal entity name
f1 = Frame(root)
f1.pack()
label1 = Label(f1,text="Legal Name")
label1.pack()


# F2 - Business type
f2 = Frame(root)
f2.pack()
label2 = Label(f2, text="Primary business activity")
label2.pack()

# F3 - Industry type
f3 = Frame(root)
f3.pack()
label3 = Label(f3, text="Industry type")
label3.pack()


# F4 - Pillar 2 Classification
f4 = Frame(root)
f4.pack()
label4 = Label(f4, text="Pillar 2 classification")
label4.pack()


# F5 - Immediate Parent Entity
f5 = Frame(root)
f5.pack()
label5 = Label(f5, text="Immediate Parent Entity (IPE)")
label5.pack()


# F6 - Ultimate Parent Entity
f6 = Frame(root)
f6.pack()
label6 = Label(f6, text="Ultimate Parent Entity (UPE)")
label6.pack()


# F7 - Jurisdiction
f7 = Frame(root)
f7.pack()
label7 = Label(f7, text="Jurisdiction")
label7.pack()

root.mainloop()