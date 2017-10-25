import socket
import threading

bind_ip = "127.0.0.1"
bind_port = 9999

# create socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((bind_ip,bind_port))

print "[*] Listening on %s:%d" % (bind_ip,bind_port)

while True:
	# receive message from server
	message,addr = server.recvfrom(2048)

	print "[*] Accepting connection from: %s:%d." % (addr[0],addr[1])
	print "[*] Server received: %s with length %d." % (message,len(message))

	# send the count to client
	server.sendto(str(len(message)), addr)
	print "[*] Length sent."