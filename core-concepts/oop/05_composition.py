
# Resp: Composição (has-a) - classes especializadas montam uma classe maior.
class Engine:
    def __init__(self, type):
        self.type = type

    def __str__(self):
        return f"Engine: {self.type}"

class Vehicle:
    def __init__(self, model, engine_obj):
        self.model = model
        self.engine = engine_obj # O veículo TEM UM motor

if __name__ == "__main__":
    eng1 = Engine('V12')
    my_car = Vehicle("Ferrari", eng1)
    print(f"Modelo: {my_car.model}, Motor: {my_car.engine.type}")
