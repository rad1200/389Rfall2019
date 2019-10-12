# Writeup 6 - Binaries I

Name: Radhika Khare
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Radhika Khare

## Assignment Writeup

### Part 1 (50 pts)
CMSC389R-{di5a55_0r_d13}

### Part 2 (50 pts)
It took me a bit to understand what was going on until I started looking at the graphical view of binary ninja. From the structure of the assembly I noted that the strings and function calls might be of some use. First I just ran ./crackme and got the "did you even try disassembling" error (I'm somewhat rephrasing what it said but it was along those lines). Taking a deeper look at the x86 main function I realized it went into that branch where that was printed if there was only one argument (./crackme). So i tried printing random arguments and kept getting the "Multi-word arguments can be quoted ;)" error. Taking a look at why this is I noted the stream of 3 checks it looks and determined I was failing check1. Looking into check1 I noted a call to strcmp and that it was comparing the argument to "Oh God". When I did ./crackme "Oh God" I got a new response/error (note that I use the term error loosely here to mean anything that isn't the correct flag) which was "I wish you cared more about the environment". Looking onwards onto check2 I saw the getenv method. After a bit of research I discovered that check2 was basically asking me to set an environment variable FOOBAR to "seye ym " EXCEPT it was supposed to be reversed so FOOBAR was equals " my eyes". I tried doing the FOOBAR =" my eyes" and ./crackme "Oh God" on separate prompt lines before realizing that if I did that then FOOBAR wouldn't be an environment variable for the crackme script so I did it on the same line as FOOBAR= " my eyes" ./crackme "Oh God" which worked smoothly and followed the ideas of environment variables. Now it brings me to check 3"Oh God" on separate prompt lines before realizing that if I did that then FOOBAR wouldn't be an environment variable for the crackme script so I did it on the same line as FOOBAR= " my eyes" ./crackme "Oh God" which worked smoothly and followed the ideas of environment variables. Now it brings me to check 3"Oh God" on separate prompt lines before realizing that if I did that then FOOBAR wouldn't be an environment variable for the crackme script so I did it on the same line as FOOBAR= " my eyes" ./crackme "Oh God" which worked smoothly and followed the ideas of environment variables. I was met with the response "open sesame'. Now it brings me to check 3 where I first noted that we were to open a file called sesame. Once the file gets read I noted them there were multiple cases checking the hex values. After doing all the hex decoding I found that it said " they burn". I echoed " they burn" and then redirected it to sesame. I followed that with my FOOBAR environment setting and the running of crack me and got CMSC389R-{di5a55_0r_d13}

