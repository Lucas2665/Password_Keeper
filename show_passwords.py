import tkinter as tk
from tkinter import messagebox
import csv
import os
from delete_password import delete_password
from utils import csv_file_path

def show_passwords(window, cipher_suite, show_main_menu, show_add_password):
    # Clear the window
    for widget in window.winfo_children():
        widget.destroy()

    # Create a frame to center the labels, entries and buttons
    frame = tk.Frame(window)
    frame.pack(expand=True, anchor=tk.CENTER, pady=(0, 20))


    # Search entry and button
    search_frame = tk.Frame(frame)
    search_frame.pack(pady=(0, 10))
    search_label = tk.Label(search_frame, text="Search Site:")
    search_label.pack(side=tk.LEFT)
    search_entry = tk.Entry(search_frame)
    search_entry.pack(side=tk.LEFT, padx=(5, 10))
    #search_button = tk.Button(search_frame, text="Search", command=lambda: search_password(search_entry.get(), listbox, cipher_suite))
    #search_button.pack(side=tk.LEFT)


    # Create the Listbox to display the passwords
    listbox = tk.Listbox(frame, height=10, width=55)
    listbox.pack()


    # Back to main menu button
    buttonBack = tk.Button(frame, text="Back to Main Menu", width=15, height=1, command=lambda: show_main_menu(window, cipher_suite, show_add_password, show_passwords))
    buttonBack.pack(pady=(20,10))

    # Delete password button
    buttonDelete = tk.Button(frame, text="Delete Password", width=15, height=1, command=lambda: delete_password(listbox, cipher_suite), state=tk.DISABLED)
    buttonDelete.pack(pady=5)

    # Enable the delete button when a password is selected
    def on_select(event):
        if listbox.curselection():
            buttonDelete.config(state=tk.NORMAL)
        else:
            buttonDelete.config(state=tk.DISABLED)

    # Call function on_select when a password is selected
    listbox.bind('<<ListboxSelect>>', on_select)

    # Check if the file exists
    if not os.path.exists(csv_file_path):
        messagebox.showinfo("Info", "No passwords found.")
        return

    # Open the csv file in read mode
    with open(csv_file_path, "r") as file:
        # Read the data in the csv file
        reader = csv.reader(file)
        for row in reader:
            decrypted_user = cipher_suite.decrypt(row[1].encode()).decode()
            decrypted_password = cipher_suite.decrypt(row[2].encode()).decode()
            listbox.insert(tk.END, f" Site: {row[0]} | User: {decrypted_user} | Password: {decrypted_password} ")

"""   
def search_password(site, listbox, cipher_suite):
    Searches for a password entry by site name and displays the results in a listbox.

    Args:
        site (str): The name of the site to search for.
        listbox (tk.Listbox): The Tkinter Listbox widget to display the search results.
        cipher_suite (Fernet): The Fernet cipher suite used for decrypting the stored credentials.

    Returns:
        None

    Side Effects:
        - Clears the current contents of the listbox.
        - Displays a message box if no passwords are found.
        - Inserts the decrypted user and password information into the listbox for matching site entries.

    listbox.delete(0, tk.END)
    if not os.path.exists(csv_file_path):
        messagebox.showinfo("Info", "No passwords found.")
        return
    with open(csv_file_path, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if site.lower() in row[0].lower():
                decrypted_user = cipher_suite.decrypt(row[1].encode()).decode()
                decrypted_password = cipher_suite.decrypt(row[2].encode()).decode()
                listbox.insert(tk.END, f" Site: {row[0]} | User: {decrypted_user} | Password: {decrypted_password} ")

                """