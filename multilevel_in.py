#q3WAP to creat quadrilateral class (side1, side2,side3,side4)to find perimeter. derive
#rectangle class(side1 ,side2) from it to find area and perimeter. derive square class(side1)
##from rectangle to find area and perimeter(Multilevel Inheritance)


class quadrilateral:
    def __init__(self,side1,side2,side3,side4):
        self.side1=side1;
        self.side2=side2;
        self.side3=side3;
        self.side4=side4;

    def display(self):
        self.q=self.side1+self.side2+self.side3+self.side4
        print("side1:",self.side1)
        print("side2:",self.side2)
        print("side3:",self.side3)
        print("side4:",self.side4)
        print("Perimeter of quadrilateral is:",self.q)
        
    
class rectangle(quadrilateral): 
    def __init__(self,l,w,side1,side2,side3,side4):
        quadrilateral.__init__(self,side1,side2,side3,side4)
        self.l=l
        self.w=w

    def display1(self):
        self.a=self.l*self.w
        self.peri=2*(self.l*self.w)
        print("Lenght:",self.l)
        print("Width:",self.w)
        print("Area of rectangle is: ",self.a)
        print("Perimeter of rectangle is: ",self.peri)
        self.display()

class square(rectangle):
    def __init__(self,s1,s2,l,w,side1,side2,side3,side4):
        rectangle.__init__(self,l,w,side1,side2,side3,side4)
        #quadrilateral.__init__(self,side1,side2,side3,side4)
        self.s1=s1
        self.s2=s2

    def display2(self):
        self.area=self.s1*self.s2
        self.perimeter=4*(self.s1*self.s2)
        
        print("side1:",self.s1)
        print("side2:",self.s2)
        print("Area of square is: ",self.area)
        print("Perimeter of =square is: ",self.perimeter)
        self.display1()
       

s=square(20,2,7,8,6,4,29,7)
s.display2()


'''
op:
side1: 20
side2: 2
Area of square is:  40
Perimeter of =square is:  160
Lenght: 7
Width: 8
Area of rectangle is:  56
Perimeter of rectangle is:  112
side1: 6
side2: 4
side3: 29
side4: 7
Perimeter of quadrilateral is: 46

>>>'''
