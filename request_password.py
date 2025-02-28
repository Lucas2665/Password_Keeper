import tkinter as tk
from tkinter import messagebox
from utils import icon_path
import os

def request_password(window, show_main_menu):
    # Hide the main window
    window.withdraw()

    # Create a new window for password entry
    password_window = tk.Toplevel(window)
    password_window.title("Enter Password")
    password_window.geometry("300x150")

    # Create a frame to center the labels, entries and buttons
    frame = tk.Frame(password_window)
    frame.pack(expand=True, anchor=tk.CENTER, pady=(0, 10))

    # Set the icon for the password window
    password_window.iconbitmap(icon_path)

    # Protocol to handle window close event
    password_window.protocol("WM_DELETE_WINDOW", window.quit)

    # Label and entry for the password
    label = tk.Label(frame, text="Enter Password:")
    label.pack(pady=1)
    entry = tk.Entry(frame, show="*")
    entry.pack(pady=5)

    def check_password(event=None): # Event=None to call ENTER key
        correct_password = os.getenv("PASSWORD_KEEPER_PASSWORD")
        if entry.get() == correct_password:
            password_window.destroy()
            window.deiconify()
            show_main_menu()
        else:
            messagebox.showerror("Error", "Incorrect Password")
            entry.delete(0, tk.END)

    # Bind the Enter key to the check_password function
    entry.bind('<Return>', check_password)

    # Button to submit the password
    button = tk.Button(frame, text="Submit", width=16, height=1, command=check_password)
    button.pack(pady=10)