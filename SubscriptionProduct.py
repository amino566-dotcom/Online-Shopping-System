from product import Product

class SubscriptionProduct(Product):
    def __init__(self, name, price, duration):
        super().__init__(name, price)

        self.duration = duration

    @property
    def duration(self):
        return self.__duration
    
    @duration.setter
    def duration(self, value):
        if (isinstance(value , int) 
            and value > 0
            and not isinstance(value, bool) ):
            self.__duration = value
        else:
            raise ValueError("duration is invalid.")
        
    