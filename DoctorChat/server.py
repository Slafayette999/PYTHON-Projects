from socket import *
from clienthandler import ClientHandler

HOST = "localhost"
PORT = 6000
ADDRESS = (HOST, PORT)
server = socket(AF_INET, SOCK_STREAM)
server.bind(ADDRESS)
server.listen(5)

def main():
    print("Doctor server is running")
    
    while True:
        print("Waiting for connection...")
        (client, address) = server.accept()
        print("...connected from: ", address)
        handler = ClientHandler(client)
        handler.start()

if __name__ == "__main__":
        main()
                          
