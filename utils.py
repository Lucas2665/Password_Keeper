import os
from cryptography.fernet import Fernet

def get_resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = os.path.join(os.environ['_MEIPASS'], relative_path)
    except KeyError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Define the path to the CSV file
csv_file_path = get_resource_path("passwords.csv")

# Define the path to the icon
icon_path = "C:/Users/Lucas/Pictures/ICON/Password_Keeper.ico"

def initialize_cipher_suite():
    # Load the key from the file or generate a new one if it doesn't exist
    key_path = get_resource_path("key.key")
    if not os.path.exists(key_path):
        key = Fernet.generate_key()
        with open(key_path, "wb") as key_file:
            key_file.write(key)
    else:
        with open(key_path, "rb") as key_file:
            key = key_file.read()

    return Fernet(key)

"""import os
from cryptography.fernet import Fernet

# Define the path to the CSV file
csv_file_path = os.path.join(os.path.dirname(__file__), "passwords.csv")

# Define the path to the icon
icon_path = "C:/Users/Lucas/Pictures/ICON/Password_Keeper.ico"

def initialize_cipher_suite():
    # Load the key from the file or generate a new one if it doesn't exist
    key_path = os.path.join(os.path.dirname(__file__), "key.key")
    if not os.path.exists(key_path):
        key = Fernet.generate_key()
        with open(key_path, "wb") as key_file:
            key_file.write(key)
    else:
        with open(key_path, "rb") as key_file:
            key = key_file.read()

    return Fernet(key) 
    """