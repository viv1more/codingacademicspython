#WAP to read any text file and print report of total characters

fn=input("Enter FileName:")
fp=open(fn,"r")
str=fp.read()
A=0
a=0
sc=0
d=0
for i in range(len(str)):
    if ((ord(str[i])>=ord('A')) and (ord(str[i])<=ord('Z'))):
        A=A+1
    elif(ord(str[i])>=ord('a')) and (ord(str[i])<=ord('z')):
        a=a+1
    elif(ord(str[i])>=ord('0')) and (ord(str[i])<=ord('9')):
        d=d+1
    else:
        sc=sc+1
        
print("      Report of file    ")
print("*******************************")
print("Character Type       Total Count")
print("*******************************")
print("Capital Letter              ",A)
print("Small Letter                ",a)
print("special Characters          ",sc)
print("Digits:                     ",d)
print("*******************************")
fp.close()

'''
op:
Enter FileName:a.txt
      Report of file    
*******************************
Character Type       Total Count
*******************************
Capital Letter               5
Small Letter                 39
special Characters           12
Digits:                      3
*******************************

'''
