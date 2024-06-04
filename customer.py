from user import User
from order import Order
class Customer(User):
    counter = 0
    all_customers=[]
    def __init__(self,customer):
        super().__init__(customer,'')
        self.customer=customer
        self.personal_orders=[]
        Customer.counter += 1
        self.id = Customer.counter
        
        
    def add_order(self,item,quantity):
        if item.stock >= quantity:
            order = Order(self,item,quantity)
            item.update_stock(quantity)
            Order.all_orders.append(order)
            self.personal_orders.append(order)
            
        else:
            print("there is no enough stock for this item")
            
    def view_orders(self):
        return self.personal_orders
            
        
    def delete_order(self, order_id):
        order_to_delete = None
        for order in self.personal_orders:
            if id(order) == order_id:  # Using id() to identify the specific order
                order_to_delete = order
                break

        if order_to_delete:
            order_to_delete.item.restock(order_to_delete.quantity)
            self.personal_orders.remove(order_to_delete)
            Order.all_orders.remove(order_to_delete)
            print(f"Order {order_id} has been deleted.")
        else:
            print("Order not found.")
    
    
    
    def customer_total_pay(self):
        customer_total_pay=0
        for order in self.personal_orders:
            customer_total_pay += order.order_cost()  
        return customer_total_pay
    def __str__(self):
        return f"{self.customer}, id:{self.id}"
        
        