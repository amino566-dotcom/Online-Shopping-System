from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

    def validate_amount(self, amount):
        
        if (isinstance(amount, (int, float))
            and not isinstance(amount, bool)
            and amount > 0):
            return True

        raise ValueError("Invalid payment amount!")
