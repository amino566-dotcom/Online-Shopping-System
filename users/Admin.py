from user import User

class Admin(User):
    def __init__(self, name, email, password, role):
        super().__init__(name, email, password)

        self.role = role

    @property
    def role(self):
        return self.__role
    
    @role.setter
    def role(self, value):
        if isinstance(value, str) and value.strip():
            self.__role = value.strip()
        else:
            raise ValueError("Role must be a non-empty string!")
    
    def get_info(self):
        info = super().get_info()
        info["role"] = self.role
        return info
    
    def add_product(self, product, catalog):

        if product in catalog:
            raise ValueError("Product already exists!")

        catalog.append(product)
        return "Product added successfully!"
    
    def remove_product(self, product, catalog):
        if product not in catalog:
            raise ValueError("product does not exist")
        
        catalog.remove(product)
        return "Product removed successfully!"
