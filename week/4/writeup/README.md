# Writeup 2 - Pentesting

Name: Radhika Khare
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Radhika Khare

## Assignment Writeup

### Part 1 (45 pts)

The flag is CMSC389R- {p1ng_as_a_$erv1c3} found in the flag.txt directory of the home folder. After doing the nc wattsamp.net 1337 command when the prompt says enter the ip address I first did 157.230.179.99; ls. This command I injected allowed me to ping the server then get a listing of the files in that system. From there I saw there was a home folder I wanted to check out so I did the nc command again at the prompt I did 157.230.179.99; ls ./home. The command showed me that there was a file called flag.txt (also part of the reason I looked at the home folder first was homework 2). I repeated doing the nc command once again and the at the prompt entered 157.230.179.99;cat ./home/flag.txt. Basically at the prompt I would enter the expected value of an ip then a semicolon and then the command I wanted to run, thus executing the command I wanted. The semicolon is a command separator that works with unix based system like the wattsamp server. One thing I realized while working on part 2 is that technically I could not give an ip and just enter the command I want to inject using ;cmd. In fact doing so is more efficient as it avoids the time latency of having to execute the ping command first before doing the desired command. By doing ;cmd (where cmd is the command I want to enter) instead I am able to fail out of the execution of ping and then immediately run the command desired. It's important that I precede the command desired with the ; because otherwise it believes I'm trying to enter cmd as input for the ping function rather than run the command itself. The whole reason why I was able to do this exploit of command injection was because the server passes unchecked and unsafe user input into the unix shell so while they were expecting a ping related input (IP/hostname) it allowed for arbitrary unix commands to be injected. Additionally it's important to note that I can enter multiple commands at a time (when finding the flag I hadn't but I utilized this idea for part 2) so when the prompt is given to me to enter ip I can enter something like ;cmd1;cmd2;cmd3 etc. One way Eric Norman can avoid the exploit is by avoiding command line calls like ping all together. Utilizing shell commands without proper limitations on what users can enter opens the command injection vulnerability like it did for Norman. In the case that he really does want the ping to execute but nothing else he could have a check in his program for characters commonly used in command injections like ";","|" and "&" and have the input either be rejected or removed of such characters (parsing through the string input). Especially in the case of ping it's unlikely the input would include one of those malicious characters as it takes in a hostname or IP. To be even tighter on restrictions he can add checks for certain commands that he wants to restrict and make sure the user doesn't enter it (by parsing through string input).
### Part 2 (55 pts)

For part 2 I created a "shell within a shell" sort of situation
*Please use this space to detail your approach and solutions for part 2. Don't forget to upload your completed source code to this /writeup directory as well!*
