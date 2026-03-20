class car:
    def __init__(self,speed,mileage,name):
        self.speed = speed
        self.mileage = mileage
        self.name = name
ob = car(300,25,"BMW")
print(ob.speed,ob.mileage,ob.name)