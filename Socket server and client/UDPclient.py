def UDPcli(addr, tm):
    # UDPclient: takes an addres (IP, port) and a timeout value as arguments  
	import socket
	# create a socket object
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
	# Send data
	sent = s.sendto(b'Hello World', addr)
	print('sent bytes:', sent)
	# Receive response
	s.settimeout(tm)
	data, server = s.recvfrom(1024)
	print('received:', data)
	s.close() 

