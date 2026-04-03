class reverse:
    def __init__(self,string):
        self.string = string
    def flip(self):
        rev = ""
        for i in self.string:
            rev = i + rev
        print(rev)      
ob =  reverse(input("Enter the string:- "))
ob.flip()