class opr:
    def __init__(self,a):
        self.a = a
    def __eq__(self,other):
        if (self.a == other.a):
            print("Both are equal")
        elif (self.a < other.a):
            print("A2 is greater than A1")
        elif (self.a > other.a):
            print("A2 is less than A1")        
a1= opr(45)
a2= opr(45)    
a1 == a2