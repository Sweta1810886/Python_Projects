import tkinter as tk
import string
import random

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x400")
root.configure(background="dark grey")

def gen():
    password_entry.delete(0, tk.END)
    num = int(entry1.get())
    charVal = string.ascii_letters + string.digits + string.punctuation
    pwd = ""
    for i in range(num+1):
        pwd += random.choice(charVal)
    password_entry.insert(tk.END, pwd)
    entry1.delete(0, tk.END)


label1 = tk.Label(root, text="Password Generator", font=("Arial", 15), bg="yellow")
label1.place(x=100, y=5)

label2 = tk.Label(root, text="Enter the length of your password:", bg="dark gray")
label2.place(x=35, y=50)

entry1 = tk.Entry(root)
entry1.place(x=235, y=50)

button = tk.Button(root, text="Generate Password", font=("Ariel", 10, "bold"), background="green",
                   foreground="black", command=gen)
button.place(x=130, y=90)

label3 = tk.Label(root, text="Password:", bg = "dark gray")
label3.place(x=75, y= 135)

password_entry = tk.Entry(root, width=25)
password_entry.place(x=150, y=135)

root.mainloop()