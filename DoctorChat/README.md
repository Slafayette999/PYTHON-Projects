# DoctorChat (Python Socket Chat Server)

DoctorChat is a multi-client chat simulation built using Python sockets, threading, and simple natural language processing.
Each client connects to the server, starts a session with a Doctor object, exchanges messages, and has their conversation 
history saved between sessions. 

## Features
- Multi-client support using threads
- Server-client communication over TCP sockets
- Text transformation that reflects statements back to the user
- Persistent conversation history saved using pickle
- Clean, modular project design

## File Overview
- **server.py** - Starts the server, listens for incoming client connections.
- **client.py** - Runs a client session; allows a user input and displays doctor replies
- **clienthandler.py** - Handles individual client sessions with threading and persistence.
- **doctor.py** - Contains the Doctor class that generates responses using hedges, qualifiers, and history.

  ## Requirements
  - Python 3.x
 
  ## How to Run
Start the server: server.py
Start a client in a new terminal: client.py

## Purpose
This project demonstrates Python fundamentals commonly required in developer roles:
- Networking (sockets)
- Concurrency (threading)
- Object-oriented programming
- File persistence
- Moduler program design
