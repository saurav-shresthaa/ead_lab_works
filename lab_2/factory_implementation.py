from enum import Enum

class PizzaSize(Enum):
    LARGE = "large"
    MEDIUM = "medium"
    SMALL = "small"

class Pizza:
    def __init__(self, name, size):
        self.name = name
        self.size = size
    
    def get_description(self):
        return f"{self.size.value} {self.name} pizza"
    
    def __str__(self):
        return self.get_description()

class MeatLoverPizza(Pizza):
    def __init__(self, size):
        super().__init__("Meat Lover", size)
    
    def get_description(self):
        return f"{super().get_description()}"

class PepperoniPizza(Pizza):
    def __init__(self, size):
        super().__init__("Pepperoni", size)
    
    def get_description(self):
        return f"{super().get_description()}"

class VeggiePizza(Pizza):
    def __init__(self, size):
        super().__init__("Veggie", size)
    
    def get_description(self):
        return f"{super().get_description()}"

class PizzaFactory:
    def create_pizza(self, pizza_type, size):
        try:
            pizza_size = PizzaSize(size)
        except ValueError:
            pizza_size = PizzaSize.MEDIUM #default
            
        if pizza_type.lower() == "meat_lover":
            return MeatLoverPizza(pizza_size)
        elif pizza_type.lower() == "pepperoni":
            return PepperoniPizza(pizza_size)
        elif pizza_type.lower() == "veggie":
            return VeggiePizza(pizza_size)
        else:
            return Pizza("Custom", pizza_size)

if __name__ == "__main__":
    factory = PizzaFactory()
    
    pizza1 = factory.create_pizza("meat_lover", "large")
    pizza2 = factory.create_pizza("pepperoni", "medium")
    pizza3 = factory.create_pizza("veggie", "small")
    
    print(pizza1)
    print(pizza2)
    print(pizza3)
