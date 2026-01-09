from threading import Thread
from codecs import decode
from doctor import Doctor
import pickle
import os

BUFSIZE = 1024
CODE = "ascii"

class ClientHandler(Thread):

    def __init__(self, client):
        Thread.__init__(self)
        self.client = client

    def save(self, fileName = None):
        if fileName:
            self.fileName = fileName
        else:
            return
        fileObj = open(self.fileName, "wb")
        pickle.dump(self.dr, fileObj)
        fileObj.close()

    def load(self, filename):
        fileObj = open(filename, "rb")
        info = pickle.load(fileObj)
        fileObj.close()
        return info
        
    def run(self):

        patientName = decode(self.client.recv(BUFSIZE), CODE)
        filename = patientName + ".dat"

        if os.path.exists(filename):
            self.dr = self.load(filename)
            self.client.send(bytes("Welcome back, " + patientName + "!\n", CODE))
            
        else:
            self.dr = Doctor(patientName)
            self.client.send(bytes("Hello " + patientName, CODE))
        
        while True:
            sentence = decode(self.client.recv(BUFSIZE), CODE)

            if sentence.upper() == "QUIT":
                break

            reply = self.dr.reply(sentence)
            self.client.send(bytes(reply, CODE))
            
        self.save(filename)
        print("Disconnected")

        self.client.close()  
