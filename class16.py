#!/usr/bin/python3

# Script Name:  Ops 401 Class 16 Challenge Solution
# Author:   MaryGrace Ledesma
# Date of Last Revision:    October 24, 2022
# Description of Purpose:   Python script that automate brute force wordlist attack tool part 1 of 3

import time, getpass

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
    ask_user = int(input("Enter your selected mode: "))

    if ask_user == 1:
        iterator()

    if ask_user == 2:
        pw_check()

# Main

mode_menu()

# End