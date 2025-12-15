

# 1. Representação (__str__ vs __repr__)
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title}, {self.author}"

    def __repr__(self):
        return f"Book(title:'{self.title}', author:'{self.author}')"


# 2. Context Manager (__enter__ e __exit__)
class ConnectionDB:
    def __init__(self, name_data):
        self.name_data = name_data
        self.connected = False

    def __enter__(self):
        print(f"--Abrindo conexão com o {self.name_data} --")
        self.connected = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"--Limpando o banco de dados do {self.name_data} --")
        self.connected = False


# 3. Operadores de Comparação (__eq__, __lt__, etc)
class StockManual:
    def __init__(self, ticker, price, company):
        self.ticker = ticker
        self.price = price
        self.company = company

    def __str__(self):
        return f"{self.ticker} by {self.price}, costs {self.company}"

    def __eq__(self, value):
        return self.price == value.price

    def __lt__(self, value):
        return self.price < value.price

    def __gt__(self, value):
        return self.price > value.price

    def __le__(self, value):
        return self.price <= value.price

    def __ge__(self, value):
        return self.price >= value.price


if __name__ == "__main__":
    # Teste Context Manager
    with ConnectionDB("PostgreSQL") as db:
        if db.connected:
            print("Status dentro do with: Conectado")

    # Teste Comparação
    s1 = StockManual("A", 100, "CompA")
    s2 = StockManual("B", 105, "CompB")
    print(f"s1 < s2? {s1 < s2}")
