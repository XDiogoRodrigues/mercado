import locale

locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')


class Product:

    def __init__(self, name: str, price: float, quantity: int, is_in_stock: bool):
        self.__name: str = name.title()
        self.__price: float = price
        self.__quantity: int = quantity
        self.__is_in_stock: bool = is_in_stock
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, new_price):
        self.__price = new_price
    
    @property
    def quantity(self):
        return self.__quantity
    
    @quantity.setter
    def quantity(self, new_quantity):
        self.__quantity = new_quantity
    
    @property
    def is_in_stock(self):
        return self.__is_in_stock

    @is_in_stock.setter
    def is_in_stock(self, stock):
        self.__is_in_stock = stock
    
    def __str__(self):
        return f'Nome: {self.name}\nPreço: {locale.currency(self.price)}'