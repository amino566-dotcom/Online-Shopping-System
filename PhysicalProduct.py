from product import Product

class PhysicalProduct(Product):

    def __init__(self, name, price , stock, weight):
        super().__init__(name, price)
        self.stock = stock
        self.weight = weight

    @property
    def stock(self):
        return self.__stock
    
    @stock.setter
    def stock(self, value):
        if isinstance(value, int) and value >= 0:
            self.__stock = value

        else:
            raise ValueError("Stock must be a non-negative integer.")

    def reduce_stock(self, quantity):
        if isinstance(quantity , int) and 0 < quantity <= self.__stock:
            self.__stock -= quantity
        else:
            raise ValueError("stock must be positive.")

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if isinstance(value, (int, float)) and not isinstance(value, bool) and value > 0:
            self.__weight = value
        else:
            raise ValueError("Weight must be positive.")
        
    def get_final_price(self):
        return self.price

