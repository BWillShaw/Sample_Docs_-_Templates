from tkinter import *
from tkinter import ttk

root = Tk()

root.geometry("1000x600")
root.title("Pillar II Configuration")

frames = ["Legal Name", "Primary business activity", "Industry type", 
          "Pillar 2 classification", "Immediate Parent Entity (IPE)",
          "Ultimate Parent Entity (UPE)", "Jurisdiction"]

for text in frames:
    frame = Frame(root)
    frame.pack(pady=5, fill=X)  # fill=X will make sure the frame takes the full width of the parent

    label = Label(frame, text=text, anchor="w")
    label.pack(side=LEFT, padx=5)

    entry = Entry(frame)
    entry.pack(side=LEFT, padx=5, expand=True, fill=X)  # expand=True and fill=X will make the Entry widget take up the remaining space in the frame

root.mainloop()
