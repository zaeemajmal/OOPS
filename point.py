class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
object = point(int(input("Enter X point:- ")),int(input("Enter Y point:- ")))
print(object)
