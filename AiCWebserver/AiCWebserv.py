def AiCWebserv():
	# minimal Ajax in Control Webserver
	import socket	
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(('', 80))
	s.listen(0)	# just queue up some requests
	while True:
		conn, addr = s.accept()
		print("Got a connection from %s" % str(addr))
		request = conn.recv(1024)
		conn.sendall('HTTP/1.1 200 OK\nConnection: close\nServer: nanoWiPy\nContent-Type: text/html\n\n')
##		print("Content = %s" % str(request))
		request = str(request)
		ib = request.find('Val=')
		if ib > 0 :
			ie = request.find(' ', ib)
			Val = request[ib+4:ie]
			print("Val =", Val)
			conn.send(Val)
		else:
			with open('AiCWebpage.htm', 'r') as html:
				conn.send(html.read())
		conn.sendall('\n')
		conn.close()
		print("Connection wth %s closed" % str(addr))
