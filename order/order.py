from users.Customer import Customer
class Order():
    def __init__(self, order_id, customer, cart):
        self.order_id = order_id
        self.customer = customer
        self.__items = cart.get_items().copy()
        self.__total = cart.get_total()
        self.__status = "pending"

    @property
    def order_id(self):
        return self.__order_id
    
    @order_id.setter
    def order_id(self, value):
        if (isinstance(value, int)
            and not isinstance(value, bool)
            and value >= 1):
            self.__order_id = value
        else:
            raise ValueError("order_id is invalid!")
    
    @property
    def customer(self):
        return self.__customer
    
    @customer.setter
    def customer(self, value):
        if isinstance(value, Customer):
            self.__customer = value
        else:
            raise ValueError("customer is invalid!")
        
    @property
    def total(self):
        return self.__total
    
    @total.setter
    def total(self, value):
        if (isinstance(value, (int, float))
            and not isinstance(value, bool)
            and value >=0):
            self.__total = value
        else:
            raise ValueError("total is invalid!")
        

    @property
    def items(self):
        return self.__items.copy()
                 
    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, value):
        if (isinstance(value, str)
            and not isinstance(value, bool)
            and value.strip()):
            self.__status = value
        else:
            raise ValueError("customer is invalid!")
        
    def update_status(self , status):
        if (isinstance(status, str)
        and status.strip() in ("pending", "paid", "shipped", "cancelled")):

            self.__status = status.strip()
            return self.status
            
        else:
            raise ValueError("invalid status")
        
    def get_order_info(self):
        return {
            "order_id": self.order_id,
            "customer": self.customer.get_info(),
            "items": self.items,
            "total": self.total,
            "status": self.status
        }

