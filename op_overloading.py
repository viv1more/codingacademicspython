#Q6
#Create class coordinate(x,y,z)and overload+,-,*operator for addition,substraction
#multipliaction of 2 co-ordinates


class coordinate:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def __str__(self):
        print(coordinate("%d%d%d",(self.x,self.y,self.z)))
    def __add__(self,other):
        return(self.x+other.x,self.y+other.y,self.z+other.z)
    def __sub__(self,other):
        return(self.x-other.x,self.y-other.y,self.z-other.z)
    def __sub__(self,other):
        return(self.x*other.x,self.y*other.y,self.z*other.z)
    def __sub__(self,other):
        return(self.x/other.x,self.y/other.y,self.z/other.z)
   
c1=coordinate(5,-9,6)
c2=coordinate(10,-2,-5)
print("Addition of 2 numbers: ",c1+c2)
print("Substraction of 2 numbers: ",c1-c2)
print("Multiplication of 2 numbers: ",c1-c2)
print("Division of 2 numbers: ",c1-c2)
 

'''
op:
Addition of 2 numbers:  (15, -11, 1)
Substraction of 2 numbers:  (0.5, 4.5, -1.2)
Multiplication of 2 numbers:  (0.5, 4.5, -1.2)
Division of 2 numbers:  (0.5, 4.5, -1.2)'''
