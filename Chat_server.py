import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind (("127.0.0.1" ,4444))

server.listen()

client,addr = server.accept()

done = False

while not done:
    msg = client.recv(1024).decode('utf-8')
    if msg == 'sunniya sattu':
        done = True

    else:
        print(msg)

    client.send(input("Message>>>:").encode('utf-8'))
