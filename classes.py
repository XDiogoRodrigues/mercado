import locale

locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')


class Product:

    def __init__(self, name: str, price: float, quantity: int, is_in_stock: bool):
        self.__name: str = name.title()
        self.__price: float = float(price)
        self.__quantity: int = quantity
        self.__is_in_stock: bool = is_in_stock
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name: str):
        self.__name = new_name

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, new_price: float):
        self.__price = new_price
    
    @property
    def quantity(self):
        return self.__quantity
    
    @quantity.setter
    def quantity(self, new_quantity: int):
        self.__quantity = new_quantity
    
    @property
    def is_in_stock(self):
        return self.__is_in_stock

    @is_in_stock.setter
    def is_in_stock(self, stock: bool):
        self.__is_in_stock = stock


class ShoppingCart:

    def __init__(self):
        self.__items: list = []

    @property
    def items(self):
        return self.__items
    
    @items.setter
    def items(self, new_item: dict):
        self.__items.append(new_item)
                                          
    def add_item(self, item_verification: Product):
        in_list: bool = False
        for item in self.items:
            for chave, valor in item.items():
                if chave == item_verification.name:
                    item[chave][1] += 1
                    in_list = True
        if in_list == False:
            product: dict = {f'{item_verification.name}': [item_verification.price, 1]}
            self.items = product
               
       
