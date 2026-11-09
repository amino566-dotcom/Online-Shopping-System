from user import User

class Customer(User):

    def __init__(self, name, email, password, address):
        super().__init__(name, email, password)

        self.address = address
        self.__order_history = []

    @property
    def address(self):
        return self.__address
    
    @address.setter
    def address(self, value):
        if (isinstance(value , str) 
            and not isinstance(value, bool)
            and value.strip()):
            self.__address = value.strip()
        else:
            raise ValueError("address is invalid!")
    
    def place_order(self, order):
        
        self.__order_history.append(order)
        return "Order placed successfully!"
    
    def ger_order_history(self):
        return self.__order_history.copy()
    
    def get_info(self):
        return super().get_info()