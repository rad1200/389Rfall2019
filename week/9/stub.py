#!/usr/bin/env python2

import sys
import struct
import base64
from datetime import datetime

# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# Some constants. You shouldn't need to change these.
MAGIC = 0x8BADF00D
VERSION = 1

if len(sys.argv) < 2:
    bork("Usage: python stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
magic, version = struct.unpack("<LL", data[0:8])
timestamp, author= struct.unpack("<L8s", data[8:20])
(section,)=struct.unpack("L", data[20:24])
if section<0:
    bork("invalid section count")
else:
    print("valid time")

try:
    realts= datetime.fromtimestamp(timestamp)
except ValueError:
    bork("invalid timestamp")

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))
print("TIMESTAMP: %s" % timestamp)
print("AUTHOR: %s" % author)
print("SECTION: %d" % section)

# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual FPFF body. Good luck!

print("-------  BODY  -------")
offset = 24
i = 0



while i < int(section):

    stype, slen = struct.unpack("<LL", data[offset:offset+8])
    slen = int(slen)
    offset=offset+8
    if stype == 1:
        output = struct.unpack("<%ds" % slen, data[offset: (offset + slen)])
        print("ASCII: %s" % (output))
        
    elif stype == 2:
        output = struct.unpack("<%ds" % slen, data[offset : (offset + slen)])
        output = output.decode('utf-8')
        print("UTF-8: %s" % (output))
        
    elif stype == 3:
        (output,) = struct.unpack("<" + ("%s" % 'L' * int(slen/4)), data[offset : (offset  + slen)])
        print("WORDS: %s" % (output))
        
    elif stype == 4:
        (output,) = struct.unpack("<" + ("%s" % 'L' * int(slen/8)), data[offset : (offset + slen)])
        print("DWORDS: %s" % (output))

    elif stype == 5:
        (output,) = struct.unpack("<" + ("%s" % 'L' * int(slen/8)), data[offset : (offset + slen)])
        print("DOUBLES: %s" % (output))

    elif stype == 6:

            output = struct.unpack("<dd", data[offset : (offset + slen)])

            if (output[0] > 180) or (output[0] < -180) or (output[1] > 180) or (output[1] < -180):
                bork("coords invalid")
            else:
                print("COORDS: %s" % str(output))
      

    elif stype == 7:
        if slen == 4:
            output = struct.unpack("<L", data[offset : (offset + slen)])
            print("REFERENCE: %d" % output[0])
        else:
            bork("reference invalid")            
    elif stype == 8:
        png_magic = [137, 80, 78, 71, 13, 10, 26, 10]
        output = struct.unpack("<" + ("%s" % 'B' * (slen)), data[offset : (offset + slen)])

        png = png_magic + list(output)

    	image = open("pngimage.png", "wb")
    	image.write(bytearray(png))
   	print ("CREATED %s" % "pngimage.png")

    elif stype == 9:
        gif87_magic = [47, 49, 46, 38, 37, 61]
        output = struct.unpack("<" + ("%s" % 'B' * (slen)), data[offset : (offset + slen)])

        gif87 = gif87_magic + list(output)

    	image = open(gif87img.gif, "wb")
    	image.write(bytearray(gif87))
    	print ("CREATED %s" % "gif87img.gif")
 
    elif stype == 10:
        gif89_magic = [47, 49, 46, 38, 39, 61]
        output = struct.unpack("<" + ("%s" % 'B' * (slen)), data[offset : (offset + slen)])

        gif89 = gif89_magic + list(output)

        image = open(gif89img.gif, "wb")
        image.write(bytearray(gif89))
        print ("CREATED %s" % "gif89img.gif")

        
    offset = offset + slen
    i = i + 1


