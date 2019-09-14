# Writeup 2 - OSINT

Name: Radhika Khare
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Radhika Khare

## Assignment Writeup

### Part 1 (45 pts)

1. His name is Eric Norman
2. His workplace is Wattsamp Energy power plant. The website is wattsamp.net
3. Utilizing instantusername.com from the OSINT handbook I was able to find ejnorman84 on instagram and reddit. He followed the University of Maryland and Texas Football instagram accounts revealing some of his associations. Additionally using the username in his instagram bio i was able to use instantusername.com again to find his twitter account under @EricNorman84. His instagram is followed by user jenniferscash whose bio is about getting cash which ties to a tweet by @EricNorman84's tweet about reading about cash because of credit fraud. He has two emails he indicated he had on twitter ejnorman84@gmail.com and ejnorman@protonmail.com. After searching wattsamp in the linked in search bar i was able to discover that he did indeed have a LinkedIn profile (same picture and location was El Paso area, Texas which is also some new information). From the Wattsamp website and LinkedIn it was made clear that his specific role at Wattsamp was Power Plant Control Specialist. Wattsamp.net is registered under Eric Norman as found running whois. It's registered to the address 1300 Abdel Drive, El Paso TX 79835 and the phone number is 2026562837, with the registration email being ejnorman84@gmail.com
4. 157.230.179.99 is an IP discovered using dnstrails whose hosting provider is Digital Ocean and according to Shodan it's located in New York. Other IPs found through dns trails were 216.239.38.109, 216.239.36.109,216.239.34.109 which according to Shodan are google servers located in Omaha.
5. I found a comment in the admin page referring to a backend into the login page but as I have yet to find it i don't know if it's a red herring. Additionally I wasn't able to do much yet with robots.txt if you don't include finding the one flag but i guess i found it. Also I found the wattsamp.net/assets page that i discovered by using a URL fuzzer from pentest-tools.org. 
6. ports 22 and 80 open and 1337 amongst others; 22 is ssh port while 80 is the http port and 1337 has the waste service. This info was found utilizing nmap -p-. 
7. Found using the nmap -O -sV flags were the following guesses for OS 
8. CMSC389R-{Do_you-N0T_See_this},CMSC389R-{html_h@x0r_lulz},CMSC389R-{n0_indexing_pls},

### Part 2 (75 pts)
How I wrote the python script was using the base code given.Then after using netcat to see the format of how the captcha was formatted and what came after I began writing code. Overall I'm looping through each line in the wordlist until I would not get a response that was fail. Within the loop a socket connection is made to the site I parse the first input i get from the connection which is the captcha using string methods then send back the response to the equation. After that I recieved from the connection again and got the prompt for the username to which i sent ejnorman84 back. Then I went ahead and recieved the password and sent back the word I was trying from the word list if the word was right I put it in a file and all my socket connection closes then forever so I could see what worked. My socket closes each iteration because that's something needed in socket programming. Putting in sleep statements before recieving data and having while loops ensuring I recieved all the data I'm expecting allowed me to properly go through the entire word list.So this is the flag I found in flag.txt in the home directory CMSC389R-{!enough_nrg_4_a_str0ng_Pa$$wrd}. Basically how I found this is was I did the ls command and then I was like hmm I wonder if going to the home directory would be useful but I thought probably not. But I went to the directory anyways. Then I saw the file called flag.txt and thought it was probably a red herring but it wasn't. But in all (some) seriousness, the home directory is always a good first place to look for things because people often save their stuff in the home directory by default.I'm just so happy I'm finishing this homework on time and 6 hours of office hours paid off. Thanks for holding so many office hours this week!
*Please use this space to detail your approach and solutions for part 2. Don't forget to upload your completed source code to this /writeup directory as well!*
