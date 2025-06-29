class PizzaOrderTracker:
    _instance = None
    
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.orders = []
        return cls._instance
    
    def add_order(self, pizza_type):
        self.orders.append(pizza_type)
        print(f"Added {pizza_type} pizza to orders")
    
    def show_orders(self):
        print("Current orders:", ", ".join(self.orders) or "None")

# Usage
tracker1 = PizzaOrderTracker()
tracker1.add_order("Pepperoni")

tracker2 = PizzaOrderTracker()
tracker2.add_order("Meat Lover")

print("\nBoth trackers are the same instance:", tracker1 is tracker2)

tracker1.show_orders()
