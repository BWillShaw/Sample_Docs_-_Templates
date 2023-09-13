import tkinter as tk

def update_label():
    label.config(text="New text")
    
def get_text():
    user_entry = entry.get()
    print(f"You entered: {user_entry}") 

root = tk.Tk()

label = tk.Label(root, text="Old text")
button1 = tk.Button(root, text="Update", command=update_label)
label.pack()
button1.pack()

entry = tk.Entry(root)
button2 = tk.Button(root, text="Submit", command=get_text)
entry.pack()
button2.pack()


root.mainloop()