# Writeup 8 - Binaries II

Name: Radhika Khare
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Radhika Khare

## Assignment Writeup

### Part 1 (100 pts)
Answer the following questions regarding the server executable (for which source is provided).

1. How is the per-session administrator password generated? Are there any inherent weaknesses in this implementation?
One time randomly generated password using a time based seed. It doesn't limit number of attempts for the password which makes it vulnerable to possible brute forcing. Also the password is of a fixed size every time which reduces variability of the password and thus also makes it easier to brute force. Finally the biggest issue is that in memory its human readable as its in plaintext.

2. Describe two vulnerabilities in this program. Provide specific line numbers and classifications of the vulnerability. Explain potential ramifications as well as ways to avoid these vulnerabilities when writing code.
Line 68 utilizes gets() which can cause buffer overflow issues. This would cause it to read data without checking the length of bytes entered which means that the data can overflow into memory used for something else. Line 46 poses a vulnerability because the printf() could be used for string injection based on what they enter for input. There should be something like %s to control that a string is printed out.

3. What is the flag?
CMSC389R-{expl017-2-w1n}
4. Describe the process you followed to obtain the flag: vulnerabilities exploited, your inputs to the server in a human-readable format, etc. If you create any helper code please include it.
If you generate the password the same way as in server.c and print it, it is possible to generate the password the same way which is a major vulnerability of the program. Taking the password generating code from server.c directly I would generate the password (i added loop of 5 time of doing this password generation bc time delays and finally was able to figure out how to make it work for about the 2nd of so password generated. I was originally thinking of generating a python script but for the sake of simplicity decided to just do ./a.out && nc ec2-18-222-89-163.us-east-2.compute.amazonaws.com 1337 where a.out was my executable. After finally escalating privilege I realized that using the 4th option i can exploit the buffer overflow error. I noted that the buff variable is 33 bytes/characters. The command cat flag which shows the flag is only 8 chars long. I want to add the command into that part of memory to allow the command to be used. To deal with this I had to add 25 spaces after to deal with the rest of the buffer. Then after adding it to the list of available commands I wanted to execute it making what I executed be "cat flag                         cat flag". After multiple tries I remembered that I needed 25 spaces again to fill the buffer size properly making my input "cat flag                         cat flag                         ".

my c script findpass.c




