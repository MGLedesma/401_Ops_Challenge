#!/usr/bin/python3

# Script Name:  Ops 401 Class 03 Challenge Solution
# Author:   MaryGrace Ledesma
# Date of Last Revision: October 05, 2022
# Description of Purpose:   Create an uptime sensor tool 

# Import libraries
#from ctypes.wintypes import MSG
import os, time, datetime, smtplib
from getpass import getpass

# Declaration of variable
iphost = input("Enter host to ping: ")                  
ui_email = input("Enter destination email: ")
ui_password = getpass()

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
    server.login(ui_email, ui_password)
    ui_msg = "Hello, \nYour network is Active.\n %s" % timestamp
    server.sendmail('ping.alert@myserver.com', ui_email, ui_msg)
    server.quit()

def down_ealert():
    global now
    global timestamp

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(ui_email, ui_password)
    ui_msg = "Attention!, \nYour network is Inactive.\n %s" % timestamp
    server.sendmail('ping.alert@myserver.com', ui_email, ui_msg)
    server.quit()


def pingme():
    global now
    global timestamp
    global ping_result
    global last

    if ((ping_result != last) and (ping_result == up)):
        last = up
        up_ealert()
    elif ((ping_result != last) and (ping_result == down)):
        last = down
        down_ealert()
        
    response = os.system("ping -c 1 " + iphost)         
    if response == 0:                                   
        ping_result = up
    else:
        ping_result = down
    print()                                             
    print(timestamp + f" {iphost}: " + ping_result)     
    print()

# Main

while True:
    pingme()                                            
    time.sleep(2)                                       
     
# End



# Declaration of variables


# Requirements
# In Python, add the below features to your uptime sensor tool.

# The script must:

# Ask the user for an email address and password to use for sending notifications.
# Send an email to the administrator if a host status changes (from “up” to “down” or “down” to “up”).
# Clearly indicate in the message which host status changed, the status before and after, and a timestamp of the event.
# Important Notes

# DO NOT commit your email password in plain text within your script to GitHub as this easily becomes public.
# Create a new “burner” account for this exercise. Do not use an existing email account.
# Stretch Goals (Optional Objectives)
# In Python, add the below features to your uptime sensor tool.

# Append all status changes to an event log. Each event must include a timestamp, event code, any host IP addresses involved, and a human readable description.
# Check for BURNER_EMAIL_ADDRESS and BURNER_EMAIL_PASSWORD environment variables (eg: loaded from .profile). If found, the script skips requesting credentials via user input.
# Alternatively, send the notification email from a cloud mailer service (like Mailgun, or AWS SES), instead of SMTP through your burner address.



