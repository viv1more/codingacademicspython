#Q1:
#WAR to create class person to store name ,age ,sex of person . derive class employee
#from class person to strore designation and salary(Single Inheritance)


class person:
    def __init__(self ,nm,ag,se):
        self.nm=nm
        self.ag=ag
        self.se=se

    def display(self):
        print("Name of employee:",self.nm)
        print("Age of employee:",self.ag)
        print("Gender of employee:",self.se)


class employee(person):
    def __init__(self,nm,ag,se,d,s):
        person.__init__(self,nm,ag,se)
        self.d=d
        self.s=s
        

    def display1(self):
        self.display()
        print("Salary of employee:",self.d)
        print("Designation of employee:",self.s)
        
e=employee("Shubham",22,"male","Software devloper",95000)
e.display1()


'''
Name of employee: Shubham
Age of employee: 22
Gender of employee: male
Salary of employee: Software devloper
Designation of employee: 95000

'''
