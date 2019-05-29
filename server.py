import socket
host = '127.0.0.1'
port = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.listen(2)
c, addr = s.accept()
print("Connection from: ",str(addr))
while True:
    data = c.recv(1024)
    if not data:
        continue
    print("from user: "+str(data))
##    data = str(data)
    # c.send(data)
