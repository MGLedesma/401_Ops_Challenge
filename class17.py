#!/usr/bin/python3

# Script Name:  Ops 401 Class 17 Challenge Solution
# Author:   MaryGrace Ledesma
# Date of Last Revision:    October 25, 2022
# Description of Purpose:   Python script that automate brute force wordlist attack tool part 2 of 3

import time, getpass
from pexpect import pxssh

# declaration of variable
session = pxssh.pxssh()
host = input("Enter IP address: ")
username = input("Enter username: ")
password = getpass.getpass(prompt="Enter a password: ")

try:
    session.login(host, username, password)
    session.sendline('uptime')

def iterator():
    dict_path = input("Enter your dictionary filepath:\n")
    file = open(dict_path)
    line = file.readline()
    print(line)

    while line:
        line = line.rstrip()
        word = line
        print(word)
        time.sleep(1)
        line = file.readline()
    file.close()    

def pw_check():
    password = getpass.getpass()
    dict_path = input("Enter your dictionary filepath:\n")
    file = open(dict_path)
    line = file.readline()
    
    if password in line:
        print("Entered password is in the list")
    else:
        print("Entered password is not in the list")


def mode_menu():
    print(" --- Mode Menu --- ") 
    print("[1] Offensive; Dictionary Iterator")
    print("[2] Defensive; Password Recognized")
    print("[0] to EXIT")
    ask_user = int(input("Enter your selected mode: "))

    if ask_user == 1:
        iterator()

    if ask_user == 2:
        pw_check()
    
    if ask_user == 0:
        print("Exiting!")
        quit

# Main

mode_menu()

# End