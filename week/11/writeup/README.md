# Writeup 1 - Web I

Name: Radhika Khare
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Radhika khare


## Assignment details
This assignment has two parts. It is due by 11/27/19 at 11:59PM.

**There will be late penalty of 5% per day late!**

### Part 1 (40 Pts)

Such a Quick Little, website!

[http://142.93.136.81:5000/](http://142.93.136.81:5000/)

### Part 2 (60 Pts)
Complete all 6 levels of:

[https://xss-game.appspot.com](https://xss-game.appspot.com)

Produce a writeup. We will not take off points for viewing the source code and/or viewing hints, but we strongly discourage reading online write-ups as that defeats the purpose of the homework.

Level 1: in the query box i entered <script>alert("im sad")</script> to display an alert that says "im sad"

Level 2: i did <img src="image.gif" onerror="alert("hi sad, im dad")"> to produce an alert that says "hi sad, im dad". Since the <script> tags won't work I looked into other tags that could execute javascript. I learned that onerror executes a javascript command in the case of an error loading an image
  
Level 3: i changed the url to https://xss-game.appspot.com/level3/frame#3' onerror='alert("lol")'; to produce an alert that says "lol". Again since we couldn't use the script tags i utilized onerror. Based on the code I found the chooseTab function which makes the URL. I realized that by manipulating the amount of single quotes in my addition for the URL i can execute my desired alert() when it's trying to get the value for the num parameter

level 4: i inserted 4')+ alert('goodbye into the textbox to get an alert of goodbye. As recommended by a hint I started looking at how the timer was called taking note of the <img src ... "startTimer('{{ timer }}');" /> line from timer.html in particular. By doing 4') im giving the integer seconds value it wants but manipulating the quotations such that with the + I can execute the alert. The ending ') you'd expect the alert to have is included in the statement already so it's not needed

level 5: i changed the url to be https://xss-game.appspot.com/level5/frame/signup?next=alert("let this alert you") on the sign up page were the alert is "let this alert you". The following line in signup.html <link ... href="/static/game-frame-styles.css" /> 


### Format

Part 1 and 2 can be answered in bullet form or full, grammatical sentences.

### Scoring

* Part 1 is worth 40 points
* Part 2 is worth 60 points

### Tips

Remember to document your thought process for maximum credit!

Review the slides for help with using any of the tools or libraries discussed in
class.
