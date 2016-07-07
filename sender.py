#!/usr/bin/python
# SUMMARY:
# This script, sends a prayer to random IPv4 address, 
# and on random port within 1-1024
# prayer is scrape from another website.
# Coded by rcd

import socket
import sys
import random
import struct 
import requests
from bs4 import BeautifulSoup
from BeautifulSoup import BeautifulSoup
from sgmllib import SGMLParser   
                                 
class TextExtractor(SGMLParser): 
    def __init__(self):          
        self.text = []           
        SGMLParser.__init__(self)
    def handle_data(self, data): 
        self.text.append(data)   
    def getvalue(self):          
        return ''.join(ex.text)  
                                 
          
def strip_tags(content):
	global ex
	ex = TextExtractor()
	send_me = ""
	for p in content:
		ex.feed(str(p))
		send_me = ex.getvalue()
	return send_me

def send_datagram(host, port, data):
	try:
	   s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	except:
	   print "socket() failed"
	   sys.exit(1)

	print "[+] Sending the datagram"
	return s.sendto(data, (host, port))

# scrape prayer from a daily prayer website
print "[+] Getting a new prayer"
daily_prayer = "http://www.plough.com/en/subscriptions/daily-prayer"

result = requests.get(daily_prayer)
content = BeautifulSoup(result.content).findAll('div',{'class':'post-content'})
data = strip_tags(content)

print "[+] Generating Random IP Address Recipient"
# random IP address generator
host = socket.inet_ntoa(struct.pack('>I', random.randint(1,0xffffffff)))

print "[+] Generating Random Port"
# random Port
port = random.randint(1,1024)

# send

bytes_sent = send_datagram(host, port, data)

if bytes_sent>0:
	print data
	print "Prayer sent! "+str(bytes_sent)+" bytes"
else:
	print "Prayer not sent :("

