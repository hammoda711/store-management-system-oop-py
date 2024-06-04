from user import User
from item import Item
from order import Order
from customer import Customer


class Admin(User):
    '''
    class for the whole store system where the admin has the most privilges
    '''
    def __init__(self):
        self.orders = []
        self.customers = []
    
    #item issues
    
    def add_item(self,item):
        Item.all_items.append(item)
        Item.all_ids[item.name]=item.id
        
        
    def find_item(self,item):
        if item in Item.all_items and item.stock>0:
            #return item
            print(item)
        elif item in Item.all_items and item.stock<=0:
            #return "this item is out of stock"
            print ("this item is out of stock")
        else:
            #return "this item is not found"
            print("this item is not found")
            
        
    def delete_item(self,item):
        Item.all_items.remove(item)
        del Item.all_ids[item.name]
    
    
    #customer issues
    def add_customer(self, customer):
        Customer.all_customers.append(customer)
        customer_added = Customer(customer)
        return customer_added
    
    def find_customer(self,customer):
        if customer in Customer.all_customers  : #and customer.id !=0
            print(customer)
            #return customer
        else:
            #return "this customer is not defined"
            print( "this customer is not defined")
    
    def delete_customer(self, customer):
        Customer.all_customers.remove(customer)

        
    
    #reports
    def sales_report(self):
        total_sales=0
        for order in Order.all_orders:
            total_sales += order.order_cost()
        return total_sales
    
    def stock_report(self):
        stock_alarm = []
        for item in Item.all_items:
            if item.stock < 2:
                stock_alarm.append(item)
        return f"{stock_alarm} \n watch out!!! this item is about to be sold out"