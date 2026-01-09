from socket import *
from codecs import decode

HOST = "localhost"
PORT = 6000
BUFSIZE = 1024
ADDRESS = (HOST, PORT)
CODE = "ascii"

server = socket(AF_INET, SOCK_STREAM)
server.connect(ADDRESS)

patientName = input("Enter your name: ")
server.send(patientName.encode())

greeting = decode(server.recv(BUFSIZE), CODE)
print(greeting)

while True:
    sentence = input("\n>>")
    if sentence.upper() == "QUIT":
        server.send(bytes(sentence, CODE))
        print("Have a nice day!")
        break
    server.send(bytes(sentence, CODE))
    reply = decode(server.recv(BUFSIZE), CODE)

    print(reply)
    
server.close()

