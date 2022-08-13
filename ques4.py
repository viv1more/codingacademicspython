#question 4
#WAP to read any text file and convert all capital letters to small letters

import os
fn=input("Enter FileName:")
fp=open(fn,"r")
str=fp.read()
fp.close()
os.remove(fn)
fp=open(fn,"w")
for i in range(len(str)):
    if ((ord(str[i])>=ord('A')) and (ord(str[i])<=ord('Z'))):
        fp.write(chr(ord(str[i])-(ord['A']-ord('a'))))
    else:
        fp.write(str[i])
fp.close()
