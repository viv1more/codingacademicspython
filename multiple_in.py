#Q4:
#WRP to create class rectangle(l,b) and circle(r) and derived class cylinder(r,h)
#to calculate area(Multiple inheritance)


class rectangle:
    def __init__(self ,l,b):
        self.l=l
        self.b=b
    def display(self):
        self.area=self.l*self.b
        print("Lenght:",self.l)
        print("breadth:",self.b)
        print("Area of rectangle is :",self.area)


class circle:
    def __init__(self ,r):
        self.pi=3.14
        self.r=r
    def display1(self):
        self.area1=self.pi*self.r*self.r
        print("radius:",self.r)
        print("Area of circle is :",self.area1)

class cylinder(rectangle,circle):
    def __init__(self ,r,l,b,r1,h):
        rectangle.__init__(self ,l,b)
        circle.__init__(self ,r)
        self.pi=3.14
        self.r1=r1
        self.h=h
        self.a=2*(3.14)*r1*h+2*(3.14)*r1*r1

    def display2(self):
        self.display()
        self.display1()
        print("Area of cylinder is:",self.a)
        


cy=cylinder(20,30,50,7,66)
cy.display2()


'''op:
Area of cylinder is: 3209.08
Lenght: 30
breadth: 50
Area of rectangle is : 1500
radius: 20
Area of circle is : 1256.0
'''
