#(01) resposta: Classe é um molde com a parte lógica, enquanto o objeto é algo criado a partir da definição da classe.
class Car:
    def __init__(self, color: str, model: str):
        self.color = color
        self.model = model

    def driving(self):
        return f"Cor do carro: {self.color}, modelo: {self.model}"

car1 = Car("Red", "Ferrari")
print(car1.driving())


#(03) Resposta: É um indicador para a instância especifica do objeto que está chamando o método.
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"Nome: {self.name} ainda não se matriculou"

class Student(Person):
    def __init__(self, name: str, student_id: int):
        super().__init__(name)
        self.student_id = student_id

    def introduce(self):
        return f"Nome: {self.name}, Matricula: {self.student_id}"

student = Student("João", 2555)
print(student.introduce())
