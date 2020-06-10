#!/bin/python

# simple port scanner
# usage: python3 scanner.py <ip-address>   

import sys
import socket
from datetime import datetime

# define target

if ( len(sys.argv) == 2 ) :
	target = socket.gethostbyname(sys.argv[1]) #translate hostname to ip
else:
	print("invalid arguments")
	print("usage: python3 scanner.py <ip>")

# add a banner
print("-" * 50)
print("Scanning target "+ target)
print("Time started: " + str(datetime.now()))
print("-" * 50)

# scan for open ports
try:
	for port in range(20,85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port))
		if result == 0:
			print("Port {} is open".format(port))
		s.close()
except KeyboardInterrupt:
	print("\nExiting script.")
	sys.exit()
except socket.gaierror:
	print("\nHostname could not be resolved.")
	sys.exit()
except socket.error:
	print("\nCouldn't connect to server.")
	sys.exit()