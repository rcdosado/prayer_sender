#!/usr/bin/python
# SUMMARY:
# This script, sends a prayer to random IP addresses
# prayer is scrape from another website.
# Coded by rcd

import socket
import sys
import random
import struct 
import requests
from bs4 import BeautifulSoup
from BeautifulSoup import BeautifulSoup, NavigableString


from sgmllib import SGMLParser   
                                 
class TextExtracter(SGMLParser): 
    def __init__(self):          
        self.text = []           
        SGMLParser.__init__(self)
    def handle_data(self, data): 
        self.text.append(data)   
    def getvalue(self):          
        return ''.join(ex.text)  
                                 
          
def strip_tags(content):
	ex = TextExtracter()
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

	print "[+] sending "+data+" at IP "+host+", port "+str(port)
	return s.sendto(data, (host, port))


result = requests.get("http://www.plough.com/en/subscriptions/daily-prayer")
html = BeautifulSoup(result.content)
content = html.findAll('div',{'class':'post-content'})

host = socket.inet_ntoa(struct.pack('>I', random.randint(1,0xffffffff)))
port = random.randint(1,1024)
data = "every good boy does fine"

bytes_sent = send_datagram(host, port, data)
print "sent "+str(bytes_sent)+" bytes"

