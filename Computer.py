class computer:
    _max_price = 30000
    def price(self,c_price):
        self._max_price = c_price
        print(self._max_price)
object =computer()
object.price(40000)        
