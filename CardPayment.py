from payment import Payment

class CardPayment(Payment):
    def __init__(self, cart_number):
        self.cart_number = cart_number

    @property
    def cart_number(self):
        return self.__cart_number
    
    @cart_number.setter
    def cart_number(self, cart_number):
        if (isinstance(cart_number , str)
            and not isinstance(cart_number, bool)
            and cart_number.strip()
            and len(cart_number) == 16
            and cart_number.isdigit()):
            self.cart_number = cart_number
        else:
            raise ValueError("cart number is invalid")

    def process_payment(self , amount):
        self.validate_amount(amount)
        return f"Payment of ${amount:.2f} processed successfully through Cart."