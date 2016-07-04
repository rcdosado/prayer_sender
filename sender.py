#!/usr/bin/python
# SUMMARY:
# This script, sends a prayer to random IP addresses
# prayer is scrape from another website.
# Coded by rcd

import socket
import sys
import random

#generate random IP addresses
host = socket.inet_ntoa(struct.pack('>I', random.randint(1,0xffffffff)))
port = random.randint(1,65535)
data = "every good boy does fine"


try:
   s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except:
   print "socket() failed"
   sys.exit(1)

s.sendto(data, (host, port))
