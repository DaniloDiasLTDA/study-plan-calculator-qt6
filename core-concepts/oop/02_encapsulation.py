# Encapsulamento


class BankAccount:
    def __init__(self, amount):
        self._balance = amount

    def deposit(self, value):
        if value > 0:
            self._balance += value
        else:
            raise ValueError("Valor inválido")

    def withdraw(self, value):
        if value > 0:
            self._balance -= value
        else:
            raise ValueError("Saldo insuficiente.")


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise ValueError("Largura não é positiva")

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            raise ValueError("A altura deve ser um valor positivo.")

    @property
    def area(self):
        return self._width * self._height


# Teste Rectangle
print("--- Testes Retangulo ---")
rectangle1 = Rectangle(width=10, height=5)
print(f"Largura: {rectangle1.width}, Altura: {rectangle1.height}")
print(f"Área: {rectangle1.area}")


class Employee:
    def __init__(self, name: str, base_salary: float):
        self._name = name
        self.base_salary = base_salary

    @property
    def name(self):
        return self._name

    @property
    def base_salary(self):
        return self._base_salary

    @base_salary.setter
    def base_salary(self, value: float):
        if value > 1000:
            self._base_salary = value
        else:
            raise ValueError("O salário base deve ser maior que R$ 1000,00.")

    def calculate_salary(self):
        return 0


class Developer(Employee):
    def __init__(self, name: str, base_salary: float, dev_bonus: float):
        super().__init__(name, base_salary)
        self._dev_bonus = dev_bonus

    def calculate_salary(self):
        return self._base_salary * (1 + self._dev_bonus)


class Manager(Employee):
    def __init__(self, name, base_salary, risk_bonus: float):
        super().__init__(name, base_salary)
        self._risk_bonus = risk_bonus

    def calculate_salary(self):
        return self._base_salary + self._risk_bonus


# Teste Employee
try:
    employee = Employee("Danilo", 220)  # Vai dar erro proposital
except ValueError as e:
    print(f"Erro ao inicializar Funcionario: {e}")

dev = Developer("Danilo", 1020, 0.15)
print(f"Salário Developer: R${dev.calculate_salary():.2f}")
