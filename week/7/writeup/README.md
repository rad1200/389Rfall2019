# Writeup 7 - Forensics I

Name: Radhika Khare
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Radhika Khare

## Assignment Writeup

### Part 1 (100 pts)

1. Using the file command I determined it was JPEG file
2. Using exiftool I found gps coordinates 41 deg 53' 54.87" N, 87 deg 37' 22.53" W which translates to Chicago Illinois. Best Buy in John Hancock center
3. original time: 2018:08:22 11:33:24.801 
gps time: 2018:08:22 16:33:24Z (this is in zulu time)
4. iPhone 8 by Apple (iPhone 8 back camera 3.99mm f/1.8)
5. 539.5 m Above Sea Leve
6. CMSC389R-{look_I_f0und_a_str1ng}. this was found doing strings image| grep CMSC*. CMSC389R-{abr@cadabra} was found by first doing binwalk then upon discovery of a hidden png file did dd and extracted it and then opened the file and there it was

