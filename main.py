import tkinter as tk
from request_password import request_password
from utils import initialize_cipher_suite, icon_path
from main_menu import show_main_menu
from add_password import show_add_password
from show_passwords import show_passwords

# Initialize the cipher suite
cipher_suite = initialize_cipher_suite()

# Create Window
window = tk.Tk()
window.title("Password Manager")
window.geometry("450x350")
window.iconbitmap(icon_path)

# Call the function to request the password
request_password(window, lambda: show_main_menu(window, cipher_suite, show_add_password, show_passwords))

# Start the window
tk.mainloop()