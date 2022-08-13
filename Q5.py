#WAP to read any text file and convert all small letters to capital letters

import os
fn=input("Enter FileName:")
fp=open(fn,"r")
str=fp.read()
fp.close()
os.remove(fn)
fp=open(fn,"w")
for i in range(len(str)):
    if ((ord(str[i])>=ord('A')) and (ord(str[i])<=ord('Z'))):
        fp.write(chr(ord(str[i])-(ord['a']-ord('A'))))
    else:
        fp.write(str[i])
fp.close()
