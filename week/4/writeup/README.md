# Writeup 2 - Pentesting

Name: Radhika Khare
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Radhika Khare

## Assignment Writeup

### Part 1 (45 pts)

The flag is CMSC389R- {p1ng_as_a_$erv1c3}. After doing the nc wattsamp.net 1337 command when the prompt says enter the ip address I first did 157.230.179.99; ls. This command I injected allowed me to ping the server then get a listing of the files in that system. From there I saw there was a home folder I wanted to check out so I did the nc command again at the prompt I did 157.230.179.99; ls ./home. The command 
showed me that there was a file called flag.txt (also part of the reason I looked at the home folder first was homework 2). I repeated doing the nc command once again and the at the prompt entered 157.230.179.99;cat ./home/flag.txt. Basically at the prompt I would enter the expected value of an ip then a semicolon and then the command I wanted to run, thus executing the command I wanted. The semicolon is a command separator that works with unix based system like the wattsamp server
### Part 2 (55 pts)

*Please use this space to detail your approach and solutions for part 2. Don't forget to upload your completed source code to this /writeup directory as well!*
