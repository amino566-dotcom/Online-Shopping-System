from payment import Payment

class Paypal(Payment):
    def process_payment(self , amount):
        self.validate_amount(amount)
        return f"Payment of ${amount:.2f} processed successfully through PayPal."