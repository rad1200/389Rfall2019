# Writeup 8 - Binaries II

Name: Radhika Khare
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Radhika Khare

## Assignment Writeup

### Part 1 (100 pts)
Answer the following questions regarding the server executable (for which source is provided).

1. How is the per-session administrator password generated? Are there any inherent weaknesses in this implementation?
One time randomly generated password using a time based seed. It doesn't limit number of attempts for the password which makes it vulnerable to possible brute forcing. Also the password is of a fixed size every time which reduces variability of the password and thus also makes it easier to brute force.

2. Describe two vulnerabilities in this program. Provide specific line numbers and classifications of the vulnerability. Explain potential ramifications as well as ways to avoid these vulnerabilities when writing code.
Line 68 utilizes gets() which can cause buffer overflow issues. This would cause it to read data without 
3. What is the flag?

4. Describe the process you followed to obtain the flag: vulnerabilities exploited, your inputs to the server in a human-readable format, etc. If you create any helper code please include it.
