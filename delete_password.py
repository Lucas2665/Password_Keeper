import csv
from tkinter import messagebox
from utils import csv_file_path

def delete_password(listbox, cipher_suite):
    selected = listbox.curselection()
    if not selected:
        messagebox.showerror("Error", "No password selected")
        return

    # Get the selected password
    selected_password = listbox.get(selected[0])

    confirm = messagebox.askyesno("Delete Password", "Are you sure you want to delete this password?")
    if not confirm:
        return

    # Remove the selected password from the listbox
    listbox.delete(selected[0])

    # Read all passwords from the csv file
    with open(csv_file_path, "r") as file:
        reader = csv.reader(file)
        passwords = list(reader)

    # Write the passwords back to the csv file, excluding the deleted one
    with open(csv_file_path, "w", newline="") as file:
        writer = csv.writer(file)
        for password in passwords:
            decrypted_user = cipher_suite.decrypt(password[1].encode()).decode()
            decrypted_password = cipher_suite.decrypt(password[2].encode()).decode()
            if f" Site: {password[0]} | User: {decrypted_user} | Password: {decrypted_password} " != selected_password:
                writer.writerow(password)