#Q5
#Creat class student(roll_no ,name)derive marks and sport classes from student.
#Derived result from marks and sports


class student:
    def __init__(self,roll_no,nm):
        self.roll_no=roll_no
        self.nm=nm

    def display(self):
        print("Roll number of student is:",self.roll_no)
        print("Name of student is: ",self.nm)
        #print("Student base class")
       # print("------------------------------------")

class marks(student):
    def __init__(self,m,roll_no,nm):
        student.__init__(self,roll_no,nm)
        self.m=m

    def display1(self):
        print("Marks of students are:",self.m)
        self.display()

class sports(student):
    def __init__(self,snm,roll_no,nm):
        student.__init__(self,roll_no,nm)
        self.snm=snm
    def display2(self):
        print("Student palys sport:",self.snm)
       # self.display()

class result(sports,marks):
    def __init__(self,r,m,snm,roll_no,nm):
        marks.__init__(self,m,roll_no,nm)
        sports.__init__(self,snm,roll_no,nm)
        self.r=r
    def display3(self):
        print("Total marks=",self.r)
        self.display1()
        self.display2()
        
    


#main method:

'''m1=marks(200,1,"priya")
m1.display1()

s=sports("Hollyboll",2,"nilesh")
s.display2()
'''
r=result(500,300,"hollyboll",1,"xyz")
r.display3()



'''
op:
Total marks= 500
Marks of students are: 300
Roll number of student is: 1
Name of student is:  xyz
Student palys sport: hollyboll
------------------------------------
'''
