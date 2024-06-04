from item import Item
class Phone(Item):
    def discount(self):
        return self.price*0.8

