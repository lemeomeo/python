import socket

target_host = "127.0.0.1"
target_port = 9999

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host,target_port))

# send some data 
message = "HI SERVER THIS IS CLIENT"
print "[*] Client sent message: %s" % message
client.send(message)

# get some data
response = client.recv(4096)
if int(response) == len(message):
	print ("[*] Server got the correct string.")
else:
	print ("[*] Server did not get the correct string.")