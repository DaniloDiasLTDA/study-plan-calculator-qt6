from dataclasses import dataclass

# Obs: Usando eq=Flase para evitar que o dataclass gere automaticamente métodos de comparação!


@dataclass(eq=False)
class AssetData:
    price: float

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


@dataclass(eq=False)
class StockData(AssetData):
    ticker: str
    company: str


@dataclass(eq=False)
class BondData(AssetData):
    description: str
    duration: int
    interest: float


if __name__ == "__main__":
    stock = StockData(100, "ABCD", "ABCD Company")
    bond = StockData(230, "XYZ", "XYZ Company")

    print(f"Stock Data: {stock}")
    print(f"Stock < Bond? {stock < bond}")
