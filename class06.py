#!/usr/bin/python3

# Script Name:  Ops 401 Class 06 Challenge Solution
# Author:   MaryGrace Ledesma
# Date of Last Revision:    October 10, 2022
# Description of Purpose:   Python script that utilizes the cryptography library 1 of 3

# import library
from operator import truediv
from statistics import mode
from click import option
from cryptography.fernet import Fernet
import os.path
from os.path import exists

# declaration of variables
key = Fernet.generate_key()
f = Fernet(key)    
key_exist = os.path.exists("key.key")

# declaration of functions
# if key does not exist, generate key
def write_key(): 
    key
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# if key exist, load key
def load_key():  
    return open("key.key", "rb").read()

def key_check():
    if key_check == key_exist:
        load_key
    else:
        write_key

# to encrypt 
def encrypt_file():
    filepath = input("Enter the file path to encrypt: ")
    with open(filepath, "rb") as file:
        # read all file data
        file_data = file.read()
        # encrypt data
    encrypt_file = f.encrypt(file_data)
        # write the encrypted file
    with open(filepath, "wb") as file:
        file.write(encrypt_file)
    print("Cipherfile is " + str(encrypt_file.decode('utf-8')))

def encrypt_message():
    encrypt_message = input("Type the message you want to encrypt: ")
    encrypted = f.encrypt(encrypt_message.encode())
    print("Ciphertext is " + str(encrypted.decode('utf-8')))

# to decrypt
def decrypt_file():
    filepath = input("Enter the cipherfile to decrypt: ")
    with open(filepath, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
        # decrypt data
    decrypt_file = f.decrypt(encrypted_data)
        # write the original file
    with open(filepath, "wb") as file:
        file.write(decrypt_file)
    print("Decrypted file is " + str(decrypt_file.decode('utf-8')))

def decrypt_message():
    message_decrypt = input("Enter ciphertext to decrypt: ")
    decrypted = f.decrypt(message_decrypt.encode())
    print("Decrypted message is " + str(decrypted.decode('utf-8')))

# cryptograpy menu for user input
def mode_menu():
    print()
    print("-- Cyptograpy Menu --")
    print("[1] encrypt a file")
    print("[2] decrypt a file")
    print("[3] encrypt a message")
    print("[4] decrypt a message")
    print("[0] to EXIT")
    ask_user = int(input("Select mode to perform: "))

    if ask_user == 1:
        encrypt_file()
        mode_menu()
        
    elif ask_user == 2:
        decrypt_file()
        mode_menu()
    
    elif ask_user == 3:
        encrypt_message()
        mode_menu()

    elif ask_user == 4:
        decrypt_message()
        mode_menu()
    
    elif ask_user == 0:
        print("Exiting Program!")
        quit

    else: 
        print("Invalid input, Select mode to perform: ")
        mode_menu()
    
# Main

key_check()
print("-" * 60)
print("key is " + str(key.decode('utf-8')))

mode_menu()

# Exit
        