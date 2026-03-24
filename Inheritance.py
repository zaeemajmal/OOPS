class person:
    def __init__(self,name,ID):
        self.name = name
        self.ID = ID
    def display(self):
        print(self.name, self.ID)
class employee(person):
    def __init__(self, name, ID,salary,post):
        self.post = post
        self.salary = salary
        person.__init__(self,name,ID)
ob = employee("Tom","001",50000,"Admin")            
ob.display()        
                        
        