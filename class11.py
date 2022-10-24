#!/usr/bin/python3 

# Script Name:  Ops 401 Class 11 Challenge Solution
# Author:   MaryGrace Ledesma
# Date of Last Revision:    October 17, 2022
# Description of Purpose:   Python script that create a TCP port range scanner that test if port is open or close.

# import library
import sys, random
from scapy.all import ICMP, IP, sr1, sr, TCP
from sys import flags

# declaration of variable
host = input("Enter IP address: ")
port_range = [22, 23, 80, 443, 3389]

# declaration of function
def resp_none():
    print=(f"IP: {port_range} is silently dropped")


# Main
for dst_port in port_range:
    src_port = random.randint(1025, 65534)
    resp = sr1(IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=1,verbose=0)
print(resp)

#if resp != port_range:



# Utilize the scapy library
# Define host IP
# Define port range or specific set of ports to scan
# Test each port in the specified range using a for loop
# If flag 0x12 received, send a RST packet to graciously close the open connection. Notify the user the port is open.
# If flag 0x14 received, notify user the port is closed.
# If no flag is received, notify the user the port is filtered and silently dropped.