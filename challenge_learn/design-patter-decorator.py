from abc import ABC, abstractmethod


class Pizza(ABC):
    def __init__(self):
        self.description = "Pizza desconhecida"

    def get_description(self):
        return self.description

    @abstractmethod
    def cost(self):
        pass


class ThinCrustPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Pizza de Massa Fina"

    def cost(self):
        return 15.00


class ThickCrustPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Pizza de Massa Grossa"

    def cost(self):
        return 18.00


class ToppingDecorator(Pizza):
    @abstractmethod
    def get_description(self):
        pass


class Cheese(ToppingDecorator):
    def __init__(self, pizza):
        super().__init__()
        self.pizza = pizza

    def get_description(self):
        return self.pizza.get_description() + ", Cheese"

    def cost(self):
        return self.pizza.cost() + 2.50


class Olives(ToppingDecorator):
    def __init__(self, pizza):
        super().__init__()
        self.pizza = pizza

    def get_description(self):
        return self.pizza.get_description() + ", Olives"

    def cost(self):
        return self.pizza.cost() + 1.50


class Peppers(ToppingDecorator):
    def __init__(self, pizza):
        super().__init__()
        self.pizza = pizza

    def get_description(self):
        return self.pizza.get_description() + ", Peppers"

    def cost(self):
        return self.pizza.cost() + 2.00


order = ThinCrustPizza()

order = Cheese(order)

order = Olives(order)

order = Peppers(order)


print(f"Pedido: {order.get_description()}")
print(f"Total: R$ {order.cost():.2f}")
