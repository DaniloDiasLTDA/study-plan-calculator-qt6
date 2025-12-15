from abc import ABC, abstractmethod


# 1. Polimorfismo Ad-Hoc
class Cat:
    @staticmethod
    def make_sound():
        print("Sound cat")

class Dog:
    @staticmethod
    def make_sound():
        print("Sound Dog")

def play_sound(animal):
    animal.make_sound()


# 2. Polimorfismo por Herança
class Animal:
    def make_sound(self):
        print("Este animal faz um som.")

class Cat2(Animal):
    def make_sound(self):
        print("O gato está miando.")


# 3.0 Classes Abstratas (ABC) - Notifier
class Notifier(ABC):
    @abstractmethod
    def send(self, message: str):
        pass

class EmailNotifier(Notifier):
    def send(self, message: str):
        print(f"Enviando um Email: {message}")

class SMSNotifier(Notifier):
    def send(self, message: str):
        print(f"Enviando um SMS: {message}")


# 3.1 Classes Abstratas (ABC) - Assets
class Asset(ABC):
    def __init__(self, price: float):
        self.price = price

    @abstractmethod
    def get_description(self) -> str:
        pass

class Stock(Asset):
    def __init__(self, ticker: str, price: float, description: str):
        super().__init__(price)
        self.ticker = ticker
        self.description = description

    def get_description(self) -> str:
        return f"{self.ticker}: {self.price:.2f} -- {self.description}"

class Bond(Asset):
    def __init__(self, price: float, name: str, duration: int, interest_rate: float):
        super().__init__(price)
        self.name = name
        self.duration = duration
        self.interest_rate = interest_rate

    def get_description(self) -> str:
        return f"{self.name}: {self.duration} anos : {self.interest_rate:.2f}%"


# --- AREA DE TESTES ---

# --- 1. Teste Polimorfismo Ad-Hoc ---")
cat = Cat()
dog = Dog()
play_sound(cat)
play_sound(dog)


# --- 2. Teste Polimorfismo por Herança ---
generic_animal = Animal()
inherited_cat = Cat2()

generic_animal.make_sound()
inherited_cat.make_sound()


# --- 3.0 Teste Notificadores (ABC) ---
email_sender = EmailNotifier()
sms_sender = SMSNotifier()

email_sender.send("Olá Cliente via Email")
sms_sender.send("Olá Cliente via SMS")


# Testando Ação (Stock)
my_stock = Stock("AAPL", 150.00, "Apple Inc.")
print(f"Ativo 1: {my_stock.get_description()}")


# Testando Título (Bond)
my_bond = Bond(1000.00, "Tesouro Direto", 5, 12.5)
print(f"Ativo 2: {my_bond.get_description()}")