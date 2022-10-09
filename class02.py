#!/usr/bin/python3

# Script Name:  Ops 401 Class 02 Challenge Solution
# Author:   MaryGrace Ledesma
# Date of Last Revision: October 04, 2022
# Description of Purpose: Create an uptime sensor tool that sends ICMP packets and evaluate the result.

# Import libraries
import os, time, datetime

# Declaration of variable
iphost = input("Enter host to ping: ")  #accept user input for target IP address.
UP = "Network Active"
DOWN = "Network Inactive"

# Declaration of Function
def pingme():
    print("-" * 50)                                     #print continuous dash for output readability
    now = datetime.datetime.now()
    timestamp = now.strftime('%m-%d-%Y %T')         

    response = os.system("ping -c 1 " + iphost)         #transmit a single ICMP (ping) packet to a specific IP 
    if response == 0:                                   #assign success or failure to a status variable.
        ping_result = UP
    else:
        ping_result = DOWN

    print()                                             #print empty line
    print(timestamp + f" {iphost}: " + ping_result)     #print the status variable along with a comprehensive timestamp and destination IP tested.
    print()

# Main

while True:
    pingme()                                            
    print("Start: %s" %time.ctime())
    time.sleep(2)                                       #send packet every 2 seconds
    print("End: %s" %time.ctime())
    
# End




