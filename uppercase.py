class IOstring:
    def __init__(self):
        self.str = ""
    def uppercase(self):
        str = input("Enter string:- ")
        print(str.upper())
    def __del__(self):
        print("Destructor called")
ob = IOstring()
ob.uppercase()
del ob
#print(ob)