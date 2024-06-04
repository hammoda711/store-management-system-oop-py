# Store Management System

A **Store Management System** designed to efficiently manage inventory, sales, and orders for a store. It leverages object-oriented programming (OOP) concepts and is implemented in native Python without any external libraries.

## Features

1. **Item Management**:
  
  - The `Item` class handles inventory items.
  - Features include adding, finding, and deleting items.
2. **Order Management**:
  
  - The `Order` class manages customer orders.
  - Track order status and fulfillment.
3. **User Roles**:
  
  - The system supports different user roles:
    - `Admin`: Responsible for overall system management.
    - `Customer`: Places orders and interacts with the system.
    - `Product`: Represents the items available for sale.
4. **Sales Reports**:
  
  - Generate sales reports to analyze performance.
  - View total sales over specific periods.
5. **Restock Alerts**:
  
  - Receive warnings when stock levels are low.
  - Ensure timely restocking to prevent shortages.

## Project Structure

- **`main.py`**: The main entry point for the application.
- **`item.py`**: Contains the `Item` class.
- **`order.py`**: Implements order-related functionality.
- **`user.py`**: Defines user roles (admin, customer, product).
- **`admin.py`**: Contains the `Admin` class which is responsible moste of the job in the system
- **`customer.py`**: Contains `Customer` class which is responsible for handling orders.

## Usage

1. Clone the repository:
  
  ```bash
  git clone https://github.com/hammoda711/store-management-system
  ```
  
2. Run the application:
  
  ```bash
  python main.py
  ```
  
3. Follow the prompts to add items, manage orders, and generate reports.
  

## Future Enhancements

Check out the `future_ideas.py` file for ideas on how to further enhance the system.

## UML Diagram

[store-management-system/UML.svg at main · hammoda711/store-management-system (github.com)](https://github.com/hammoda711/store-management-system/blob/main/UML.svg)

## License
