#!/usr/bin/python3

# Script Name:  Ops 401 Class 02 Challenge Solution
# Author:   MaryGrace Ledesma
# Date of Last Revision: October 04, 2022
# Description of Purpose: Create an uptime sensor tool that sends ICMP packets and evaluate the result.

# Import libraries
import os, time, datetime

# Declaration of variable
iphost = input("Enter host to ping: ")
UP = "Network Active"
DOWN = "Network Inactive"

# Declaration of Function
def pingme():
    print("-" * 50)
    now = datetime.datetime.now()
    timestamp = now.strftime('%m-%d-%Y %T')

    response = os.system("ping -c 1 " + iphost)
    if response == 0:
        ping_result = UP
    else:
        ping_result = DOWN

    print()
    print(timestamp + f" {iphost}: " + ping_result)
    print()

# Main

while True:
    pingme()
    print("Start: %s" %time.ctime())
    time.sleep(2)
    print("End: %s" %time.ctime())
    
# End

# Transmit a single ICMP (ping) packet to a specific IP every two seconds.
# Assign success or failure to a status variable.
# For every ICMP transmission attempted, print the status variable along with a comprehensive timestamp and destination IP tested.
# Example output: 2020-10-05 17:57:57.510261 Network Active to 8.8.8.8

# Stretch Goals (Optional Objectives)
# Save the output to a text file as a log of events.
# Accept user input for target IP address.




