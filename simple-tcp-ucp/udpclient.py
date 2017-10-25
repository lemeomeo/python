import socket

'''
This program comes with udpserver.py
Run udpserver.py first -- python udpserver.py
Then run udpclient.py -- python udpclient.py
Printable statements shall determine how UDP server and client interact. 
'''

target_host = "127.0.0.1"
target_port = 9999

# create socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# create message to send and length
message = "HI SERVER THIS IS CLIENT"
length = len(message)

# send the message
print "[*] Client sent message: %s" % message
client.sendto(message, (target_host, target_port))

# receive the count
data,addr = client.recvfrom(4096)

# check the count
if int(data) == len(message):
	print ("[*] Server got the correct string.")
else:
	print ("[*] Server did not get the correct string.")

client.close()