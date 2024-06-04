from item import Item
class Order:
    all_orders=[]
    #instances = []
    def __init__(self,customer,item,quantity):
        
        self.customer = customer
        self.item = item
        self.quantity = quantity
        #Order.instances.append(self)
        
        
    def order_cost(self):
        return self.quantity * self.item.price
    
    def __str__(self):
        return f"Order[Customer: {self.customer}, Item: {self.item.name}, Quantity: {self.quantity}]"
    
    def __repr__(self):
        return self.__str__()