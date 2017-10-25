import socket
import threading

'''
This program comes with tcpclient.py
Run tcpserver.py first -- python tcpserver.py
Then run tcpclient.py -- python tcpclient.py
Printable statements shall determine how TCP server and client interact. 
'''

bind_ip = "127.0.0.1"
bind_port = 9999

# create socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip,bind_port))

server.listen(5)

print "[*] Listening on %s:%d" % (bind_ip,bind_port)

# client_handling thread
def handle_client(client_socket):

	#print out what client sends
	request = client_socket.recv(1024)

	# send the count to client
	print "[*] Server received: %s with length %d" % (request,len(request))
	client_socket.send(str(len(request)))
	print "[*] Length sent."

	client_socket.close()

# run the server
while True:
	clientSocket,addr = server.accept()

	print "[*] Accepted connection from: %s:%d" % (addr[0],addr[1])

	# start our client thread to handle data 
	client_handler = threading.Thread(target=handle_client, args=(clientSocket,))
	client_handler.start()