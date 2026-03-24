class bird:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(self.name, self.age)
class penguin(bird):
    def __init__(self, name, age,swim):
        self.swim = swim

        super().__init__(name,age)

ob = penguin("Tom","001","Yes")            
ob.display()      
