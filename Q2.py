#WAP to read ,write and appen any text file using menu driven program

def create():
    fn=input("Enter FileName:")
    fp=open(fn,"w")
    ch=1
    while ch==1:
        str=input("Enter Sentence:")
        fp.write(str)
        fp.write("\n")
        ch=int(input("Enter 1 to continue:"))
    fp.close()
    print(fn,"File Created Succesfully..!!")

def read():
    fn=input("Enter FileName:")
    fp=open(fn,"r")
    str=fp.read()
    print(str)
    fp.close()

def append():
    fn=input("Enter FileName:")
    fp=open(fn,"a")
    ch=1
    while ch==1:
        str=input("Enter Sentence:")
        fp.write(str)
        fp.write("\n")
        ch=int(input("Enter 1 to continue:"))
    fp.close()
    print(fn,"File Created Succesfully..!!")

ch=1
while ch<4:
    print("1:create")
    print("2:Read")
    print("3:Append")
    print("4:Exit")
    ch=int(input("Enter Your Choice:"))
    if ch==1:
        create()
    elif ch==2:
        read()
    elif ch==3:
        append()
    else:
        print("Wrong Choice")
        
'''
#op

1:create
2:Read
3:Append
4:Exit
Enter Your Choice:2
Enter FileName:a.txt
hello
how are you?
my name is priyanka
welcome to SIBAR

1:create
2:Read
3:Append
4:Exit
Enter Your Choice:4
Wrong Choice
'''


    
    
