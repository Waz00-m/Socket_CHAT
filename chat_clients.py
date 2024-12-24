import socket

user = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

user.connect(("127.0.0.1",4444))

finished = False

while not finished:
    user.send(input("Message>>:").encode('utf-8'))
    msg = user.recv(1024).decode('utf-8')
    if msg == 'sunniya sattu':
        finished = True
    else:
        print (msg)

