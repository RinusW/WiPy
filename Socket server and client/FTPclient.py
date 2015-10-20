def FTPcli():
	# FTPclient, expect time of day as response frome server
	import socket
	# create a socket object
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	addr = ('192.168.1.25', 9999)
	s.connect(addr)
	tm = s.recv(1024)
	s.close()
	print("The time got from the server is %s" % tm.decode('ascii'))

