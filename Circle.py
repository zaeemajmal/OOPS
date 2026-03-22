class circle:
    def __init__(self,radius):
        self.radius = radius
    def circumfrence(self):
            C = 2 * (22/7) * self.radius
            return C
    def area(self):
            A = (22/7) * self.radius * self.radius
            return A


radius = float(input("Enter the radius- "))
ob = circle(radius)
C = ob.circumfrence()
A = ob.area()
print("The circumfrence of the circle is ", round(C,2))
print("The area of the circle is ", round(A,2))





  
