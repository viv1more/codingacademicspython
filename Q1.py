#WAP to read any text file
fn= input("Enter file name:")
fp=open(fn,"r")
for each in fp:
    print(each)
fp.close()

'''
#op:
Enter file name:Q1.py
#WAP o read any text file

fn= input("Enter file name:")

fp=open(fn,"r")

for each in fp:

    print(each)

fp.close()
'''
