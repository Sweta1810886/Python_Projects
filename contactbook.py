import tkinter as tk
root = tk.Tk()
root.geometry("350x400")
root.title("Contact Book")
root.configure(background="dark gray")

contacts = []

def clear_entries():
    nameEntry.delete(0, tk.END)
    numberEntry.delete(0, tk.END)
    emailEntry.delete(0, tk.END)
    addressEntry.delete(0, tk.END)

def add_contact():
    name = nameEntry.get()
    phone = numberEntry.get()
    email = emailEntry.get()
    address = addressEntry.get()

    if name == "" or phone == "":
        return

    contact = f"{name} | {phone} | {email} | {address}"
    contacts.append(contact)
    contact_list.insert(tk.END, contact)
    clear_entries()

def view_contact():
    selection = contact_list.curselection()
    if not selection:
        return

    index = selection[0]
    data = contacts[index].split(" | ")

    clear_entries()
    nameEntry.insert(0, data[0])
    numberEntry.insert(0, data[1])
    emailEntry.insert(0, data[2])
    addressEntry.insert(0, data[3])


def search_contact():
    name = nameEntry.get().lower()
    contact_list.delete(0, tk.END)

    for contact in contacts:
        if name in contact.lower():
            contact_list.insert(tk.END, contact)


def update_contact():
    selection = contact_list.curselection()
    if not selection:
        return

    index = selection[0]

    name = nameEntry.get()
    phone = numberEntry.get()
    email = emailEntry.get()
    address = addressEntry.get()

    updated_contact = f"{name} | {phone} | {email} | {address}"
    contacts[index] = updated_contact

    contact_list.delete(index)
    contact_list.insert(index, updated_contact)
    clear_entries()

def delete_contact():
    selection = contact_list.curselection()
    if not selection:
        return

    index = selection[0]
    contacts.pop(index)
    contact_list.delete(index)
    clear_entries()


#-----------------------------GUI-----------------------------------

name = tk.Label(root, text="Name:", bg = "dark gray")
name.place(x=10, y=20)
nameEntry = tk.Entry(root, font=("Ariel", 10, "bold"), width=35, bg="gray")
nameEntry.place(x=65, y=20)

number = tk.Label(root, text="Phone:", bg = "dark gray")
number.place(x=10, y=40)
numberEntry = tk.Entry(root, font=("Ariel", 10, "bold"), width=35, bg="gray")
numberEntry.place(x=65, y=40)

email = tk.Label(root, text="Email:", bg = "dark gray")
email.place(x=10, y=60)
emailEntry = tk.Entry(root, font=("Ariel", 10, "bold"), width=35, bg="gray")
emailEntry.place(x=65, y=60)

address = tk.Label(root, text="Address:", bg = "dark gray")
address.place(x=10, y=80)
addressEntry = tk.Entry(root, font=("Ariel", 10, "bold"), width=35, bg="gray")
addressEntry.place(x=65, y=80)
addressEntry.place(x=65, y=80)

add_button = tk.Button(root, text = "ADD", command=add_contact, bg="green")
add_button.place(x=25, y=120)

view_button = tk.Button(root, text = "VIEW", command=view_contact, bg="orange")
view_button.place(x=76, y=120)

search_button = tk.Button(root, text = "SEARCH", command=search_contact, bg="yellow")
search_button.place(x=130, y=120)

update_button = tk.Button(root, text = "UPDATE", command=update_contact, bg = "grey")
update_button.place(x=203, y=120)

delete_button = tk.Button(root, text = "DELETE", command=delete_contact, bg="red")
delete_button.place(x=275, y=120)

contact_list = tk.Listbox(root, font=("Ariel", 10, "bold"), height=12, width=40, bg= "gray")
contact_list.place(x=30, y=165)

root.mainloop()