#!/usr/bin/python3

# Script Name:  Ops 401 Class 06 Challenge Solution
# Author:   MaryGrace Ledesma
# Date of Last Revision:    October 10, 2022
# Description of Purpose:   Python script that encrypts a single file.

# import library
from cryptography.fernet import Fernet
import os.path
from os.path import exists

# declaration of variables
user_choice = "y"
key_exists = exists(key_file_path)

# declaration of function
def key():
    key = load_key()
    print("key is" + str(key.decode('wtf-8')))

def load_key():
    return open("key.key", "rb").read()

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key-files:
        key-file.write(key)

def ask_user():

def encrypt_file():

def decrypt_file():

def encrypt_message():

def decrypt_message():

# while True
#     ask_user()

