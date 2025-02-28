import tkinter as tk
import main

def show_main_menu(window, cipher_suite, show_add_password, show_passwords):
    # Clear the window
    for widget in window.winfo_children():
        widget.destroy()

    # Create a frame to center the buttons
    frame = tk.Frame(window)
    frame.pack(expand=True, anchor=tk.CENTER, pady=(0, 40))

    # Create a welcome label
    welcome_label = tk.Label(frame, text="Welcome!", font=("Arial", 20, "bold"))
    welcome_label.pack(pady=3)

    # Create main menu buttons
    buttonAdd = tk.Button(frame, height=3, width=20, text="Add New Password", command=lambda: show_add_password(window, cipher_suite, show_main_menu, show_passwords))
    buttonAdd.pack(pady=10)

    buttonShow = tk.Button(frame, height=3, width=20, text="Show Passwords", command=lambda: show_passwords(window, cipher_suite, show_main_menu, show_add_password))
    buttonShow.pack(pady=10)

    