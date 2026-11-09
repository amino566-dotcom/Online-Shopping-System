from product import Product

class DigitalProduct(Product):
    def __init__(self, name, price, download_url):
        super().__init__(name, price)

        self.download_url = download_url

    @property
    def download_url(self):
        return self.__download_url

    @download_url.setter
    def download_url(self, value):
        if (isinstance(value , (str)) 
        and not isinstance(value , bool) == bool 
        and value.strip().startswith("https://")):
            self.__download_url = value
        else:
            raise ValueError("Download url is invalid.")
        
    def get_final_price(self):
        return self.price
    
    def get_download_link(self):
        return self.__download_url
    
    
