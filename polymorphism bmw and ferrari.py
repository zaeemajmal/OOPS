class BMW:
    def fuel_type(self):
        print("BMW's fuel type is petrol")
    def max_speed(self):
        print("BMW's top speed is 300 km/h")  
class Ferrari:
    def fuel_type(self):
        print("Ferrari's fuel type is diesel")
    def max_speed(self):
        print("Ferrari's top speed is 290 km/h")
ob = BMW()
object = Ferrari() 
for i in (ob,object):
    i.fuel_type()
    i.max_speed()
    
