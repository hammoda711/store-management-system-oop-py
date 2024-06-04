from item import Item
from product import Phone 
from admin import Admin
from order import Order
from customer import Customer

if __name__ == "__main__":
    #items
    nokia1 = Phone("asia200", 750.0,1)
    nokia2 = Phone("6600",500.0,0)
    iphone = Phone("15 pro max",500.0,11)
    samsong = Phone("galaxyS4",1000.0,10)

    admin =Admin()

    #add cutomer only belongs to the admin (it is an admin privilge!!)
    customer1 = admin.add_customer("mohamed taher")
    customer2 = admin.add_customer("sara mohamed")
    customer2 = admin.add_customer("hesham desoky")

    #delete customer (it is an admin privilge!!)
    admin.delete_customer("hesham desoky")
    print(admin.find_customer("hesham desoky"))        #output

    #admin privileges 
    admin.add_item(nokia1)
    admin.add_item(nokia2)
    admin.add_item(iphone)

    #admin.find_item(nokia1)                            #output

    admin.delete_item(nokia2)
    #admin.find_item(nokia2)                            #output

    #admin.delete_customer("mohamed taher")
    #print(Customer.all_customers)                      #output
    #admin.find_customer("mohamed taher")               #output

    print(Customer.all_customers)                       #output

    #customer privileges
    customer1.add_order(iphone,1)
    customer1.add_order(nokia1,1)
    customer1.add_order(samsong,2)
    customer2.add_order(samsong,2)
    #customer1.delete_order(nokia1)
    #print(customer1.view_orders())                     
    print(customer1.customer_total_pay())                #output


    #reports
    print(admin.sales_report())                          #output
    print(admin.stock_report())                          #output


    #orders
    #print(Order.all_orders)
    #Order.display_all_instances()

    #order=Order(customer1,nokia1,2)
    #print(order.order_cost())
