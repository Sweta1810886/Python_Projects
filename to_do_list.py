import tkinter as tk

root = tk.Tk()
root.title("TO DO List")
root.geometry("600x400")


def add_command():
    task = ent.get()
    lbox.insert(tk.END, task)
    ent.delete(0, tk.END)

def mark_command():
    pos = lbox.curselection()[0]
    text = lbox.get(pos)
    lbox.delete(pos)
    lbox.insert(tk.END, f"{text} \u2713")

def delete_command():
    pos = lbox.curselection()[0]
    lbox.delete(pos)

lbl = tk.Label(root, text = "Enter your task:", font =("Ariel", 10, "bold"))
lbl.place(x=10, y=20)

ent = tk.Entry(root, width = 50, background = "lightblue")
ent.place(x=120, y=20)

lbox = tk.Listbox(root, width=50, height = 10, background= "lightyellow")
lbox.place(x = 120, y=70)

bt1 = tk.Button(root, text = "ADD", width=10, background="grey", command=add_command)
bt1.place(x=120, y=250)

bt1 = tk.Button(root, text = "MARK", width=10, background="green", command=mark_command)
bt1.place(x=230, y=250)

bt1 = tk.Button(root, text = "DELETE", width=10, background="red", command = delete_command)
bt1.place(x=340, y=250)



root.mainloop()