from tkinter import *
from tkinter import simpledialog, messagebox
from tkinter.filedialog import askopenfilename, askdirectory
import os
import pyAesCrypt


def get_file():
    Tk().withdraw()
    path = askopenfilename(title='SELECT A FILE TO OPEN')
    return path

def encrypt(path):
    # user selects folder to put a new encrypted file in
    Tk().withdraw()
    messagebox.showinfo("byteMe: INFO",
                        "SELECT DIRECTORY FOR NEW ENCRYPTED FILE")
    folder = askdirectory(title='byteMe')

    # window input
    name_str = simpledialog.askstring("FILENAME", "NAME OF NEW ENCRYPTED FILE:")
    filename = os.path.join(folder, name_str + ".txt.acs")

    exists = os.path.isfile(filename)
    if not exists:
        encrypted_file = open(filename, "w")
    else:
        encrypted_file = open(filename)
    encrypted_file_path = filename
    with open(path) as input_file:
        input_file_path = path
        # encryption/decryption buffer size - 64K
        bufferSize = 64 * 1024
        password = "superpass"
        pyAesCrypt.encryptFile(input_file_path, encrypted_file_path,
                               password,
                               bufferSize)
        input_file.close()
    encrypted_file.close()
    return encrypted_file_path

def decrypt(path):
    encrypted_file = open(path)
    encrypted_file_path = path

    # user selects folder to put a new decrypted file in
    Tk().withdraw()
    messagebox.showinfo("byteMe: INFO",
                        "SELECT DIRECTORY FOR NEW DECRYPTED FILE")
    folder = askdirectory(title='byteMe')

    name_str = simpledialog.askstring("FILENAME", "NAME OF NEW DECRYPTED FILE:")
    filename = os.path.join(folder, name_str + ".txt")

    exists = os.path.isfile(filename)
    if not exists:
        output_file = open(filename, "w")
    else:
        output_file = open(filename)
    output_file_path = filename
    with open(path) as input_file:
        input_file_path = path
        # encryption/decryption buffer size - 64K
        bufferSize = 64 * 1024
        password = "superpass"
        pyAesCrypt.decryptFile(encrypted_file_path, output_file_path, password,
                               bufferSize)
        output_file.close()
    encrypted_file.close()
    return output_file_path
