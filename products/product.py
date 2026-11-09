from abc import ABC, abstractmethod

class Product(ABC):

    
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if isinstance(value , (float, int)) and value > 0:
            self.__price = value
        else:
            print("the price is invalid.")

    @abstractmethod
    def get_final_price(self):
        return self.__price
    
