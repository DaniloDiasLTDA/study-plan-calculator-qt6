# core-concepts/oop/06_design_patterns.py
import datetime


# --- Padrão 1: Singleton (Uma única instância) ---
class DatabaseConnection:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print("Criando a instância única pela primeira vez")
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "dados_carregados"):
            self.modo = "Safe"
            self.dados_carregados = 50


# --- Padrão 2: Mixin (Funcionalidade plugável) ---
class LogavelMixin:
    def log_mensagem(self, mensagem):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] - {self.__class__.__name__}: {mensagem}")


class ContaBancaria(LogavelMixin):
    def __init__(self, saldo):
        self.saldo = saldo
        self.log_mensagem(f"Conta criada com saldo inicial de R$ {saldo:.2f}")

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.log_mensagem(f"Saque de R$ {valor:.2f} efetuado.")
        else:
            self.log_mensagem("Tentativa de saque falhou: saldo insuficiente.")


# --- Padrão 3: Metaclasses (Interceptação de criação) ---
class MetaVerificadora(type):
    def __new__(mcs, name, bases, attrs):
        print(f"--> Analisando a classe {name} antes de ela nascer...")
        if "__doc__" not in attrs or not attrs["__doc__"]:
            raise TypeError(f"A classe {name} PRECISA ter uma docstring explicativa!")
        return super().__new__(mcs, name, bases, attrs)


if __name__ == "__main__":
    # Teste Singleton
    conf1 = DatabaseConnection()
    conf2 = DatabaseConnection()
    print(f"São o mesmo objeto? {conf1 is conf2}")  # Deve ser True

    # Teste Mixin
    conta = ContaBancaria(500)
    conta.sacar(100)
