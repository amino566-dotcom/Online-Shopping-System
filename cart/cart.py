class Cart():
    def __init__(self):
        self.__items = {}
        self.__discount = 0

    def add_product(self, product, quantity):
        
        if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity <= 0:
            raise ValueError("Quantity must be a positive integer!")

        if product not in self.__items:
            self.__items[product] = quantity
        else:
            self.__items[product] += quantity
        return self.__items
    
    def remove_product(self, product):
        if product not in self.__items:
            raise ValueError("product does not exist")
        
        self.__items.pop(product)
        return "deleted successfully!"
    
    def update_quantity(self, product, quantity):
        if product not in self.__items:
            raise ValueError("Product does not exist!")
        if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity <= 0:
            raise ValueError("Quantity must be a positive integer!")

        self.__items[product] = quantity

        return self.__items
    
    def get_subtotal(self):
        total = 0
        if not self.__items:
            raise ValueError ("No product is added!")
        
        for product ,quantity in self.__items.items():
            total += product.get_final_price() * quantity
        return total
    
    def apply_discount(self, discount):
        
        total = self.get_subtotal() *(1 - discount/100) 
    
    def get_total(self):
        return self.apply_discount()
    
    def clear(self):
        self.__items.clear()
        return "Cart got cleared!"
