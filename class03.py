#!/usr/bin/python3

# Script Name:  Ops 401 Class 03 Challenge Solution
# Author:   MaryGrace Ledesma
# Date of Last Revision: October 05, 2022
# Description of Purpose:   Create an uptime sensor tool 

# Import libraries
import os, time, datetime, smtplib
from getpass import getpass

# Declaration of variable
iphost = input("Enter host to ping: ")                  
from_email = input("Enter destination email: ")
from_password = getpass()

up = "Network Active"
down = "Network Inactive"
last = 0
ping_result = 0

now = datetime.datetime.now()
timestamp = now.strftime('%m-%d-%Y %T %p')
# context = ssl.create_default_context()    

# Declaration of Function
def up_ealert():
    global now 
    global timestamp

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()

    # Ask the user for an email address and password to use for sending notifications.
    server.login(from_email, from_password)

    # Clearly indicate in the message which host status changed, the status before and after, and a timestamp of the event.
    ui_msg = "Hello, \nYour network is Active.\n %s" % timestamp
    server.sendmail('ping.alert@myserver.com', from_email, ui_msg)
    server.quit()

def down_ealert():
    global now
    global timestamp

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(from_email, from_password)
    ui_msg = "Attention!, \nYour network is Inactive.\n %s" % timestamp
    server.sendmail('ping.alert@myserver.com', from_email, ui_msg)
    server.quit()


def pingme():
    global now
    global timestamp
    global ping_result
    global last

    response = os.system("ping -c 1 " + iphost)         
    if response == 0:                                   
        ping_result = up
    else:
        ping_result = down
    print()                                             
    print(timestamp + f" {iphost}: " + ping_result)     
    print()

    # Send an email to the administrator if a host status changes (from “up” to “down” or “down” to “up”).
    if ((ping_result != last) and (ping_result == up)):
        last = up
        up_ealert()
    elif ((ping_result != last) and (ping_result == down)):
        last = down
        down_ealert()
        

# Main

while True:
    pingme()                                            
    time.sleep(2)                                       
     
# End




