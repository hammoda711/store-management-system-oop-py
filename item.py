from abc import ABC, abstractmethod
class Item(ABC):
    """
    Abstract base class for an item in the store.
    """
    all_items=[]
    all_ids={}
    counter = 0
    def __init__(self, name:str , price:float, stock=0):
        
        #inputs validation
        assert isinstance(price, float) and price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert isinstance(stock, int) and stock >= 0, f"stock {stock} is not greater or equal to zero!"
        
        self.name = name
        self.price = price
        self.stock = stock
        Item.counter += 1
        self.id = Item.counter
        
        
        #Item.all_items.append(self)
        #Item.all_ids[self.name]=self.id
        
    def update_stock(self, quantity):
    #quantity ordered from one item (Order class)
        self.stock-=quantity
        #return self.stock
    
    def restock(self, quantity):
        self.stock += quantity

    
    @abstractmethod
    def discount(self):
        pass    
    
    
    def __repr__(self):
            return f"{self.__class__.__name__}('{self.name}', price:{self.price}, stock:{self.stock}, id:{self.id})"
            