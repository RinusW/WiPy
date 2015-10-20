def FTPserv():
	# FTPserver, waiting for a connection and then sends a simple message
	import socket
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(('', 9999))
	s.listen(1)	# just queue up a single request
	while True:
		conn, addr = s.accept()
		print("Got a connection from %s" % str(addr))
		conn.send(b'Hello, WiPy calling .... ')
		conn.close()
	print('The End')

