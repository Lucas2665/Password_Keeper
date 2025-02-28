import tkinter as tk
from tkinter import messagebox
import csv
from utils import csv_file_path

def show_add_password(window, cipher_suite, show_main_menu, show_passwords):
    # Clear the window
    for widget in window.winfo_children():
        widget.destroy()

    # Create a frame to center the labels, entries and buttons
    frame = tk.Frame(window)
    frame.pack(expand=True, anchor=tk.CENTER, pady=(0, 40))

    # Create Labels and Entries
    labelSite = tk.Label(frame, text="Site: ")
    labelSite.pack()
    entrySite = tk.Entry(frame, justify="center")
    entrySite.pack()

    labelUser = tk.Label(frame, text="User: ")
    labelUser.pack()
    entryUser = tk.Entry(frame)
    entryUser.pack()

    labelPassword = tk.Label(frame, text="Password: ")
    labelPassword.pack()
    entryPassword = tk.Entry(frame, show="*")
    entryPassword.pack()

    def save():
        site = entrySite.get()
        user = entryUser.get()
        password = entryPassword.get()
        
        if site == "" or user == "" or password == "":
            messagebox.showerror("Error", "Fill in all")
        else:
            encrypted_user = cipher_suite.encrypt(user.encode()).decode()
            encrypted_password = cipher_suite.encrypt(password.encode()).decode()
            # Create or save csv file in append mode
            with open(csv_file_path, "a", newline="") as file:
                # Write the data in the csv file
                writer = csv.writer(file)
                writer.writerow([site, encrypted_user, encrypted_password])
                # Show message box
                messagebox.showinfo("Save", "Saved successfully")
                # Clean the entries
                entrySite.delete(0, tk.END)
                entryUser.delete(0, tk.END)
                entryPassword.delete(0, tk.END)

    # Save button
    buttonSave = tk.Button(frame, text="Save", width=15, height=1, command=save)
    buttonSave.pack(pady=(20,10))

    # Back to main menu button
    buttonBack = tk.Button(frame, text="Back to Main Menu", width=15, height=1, command=lambda: show_main_menu(window, cipher_suite, show_add_password, show_passwords))
    buttonBack.pack(pady=1)