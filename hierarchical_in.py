#Q2:
#Wrire a program to create class person(name,age,sex) of person derive class employee
#(des, salary) and students(roll_no,marks) from class person(Hierarchical inheritance)

class person:
    def __init__(self ,nm,ag,se):
        self.nm=nm
        self.ag=ag
        self.se=se

    def display(self):
        print("Name of person:",self.nm)
        print("Age of person:",self.ag)
        print("Gender of person:",self.se)

class employee(person):
    def __init__(self,des,s,nm,ag,se):
        person.__init__(self,nm,ag,se)
        self.des=des
        self.s=s

    def display1(self):
        print("Designation of employee is:",self.des)
        print("Salary of employee is: ",self.s)
        self.display()

class student(person):
    def __init__(self,roll_no,marks,nm,ag,se):
        person.__init__(self,nm,ag,se)
        self.roll_no=roll_no
        self.marks=marks

    def display2(self):
        print("------------------------------------")
        print("Roll number of student is:",self.roll_no)
        print("Marks of student is: ",self.marks)
        self.display()

e=employee("HR",35000,"Shubham",24,"male")
e.display1()
s=student(101,88,"adesh",20,"male")
s.display2()



'''
Designation of employee is: HR
Salary of employee is:  35000
Name of person: Shubham
Age of person: 24
Gender of person: male
------------------------------------
Roll number of student is: 101
Marks of student is:  88
Name of person: adesh
Age of person: 20
Gender of person: male
'''
