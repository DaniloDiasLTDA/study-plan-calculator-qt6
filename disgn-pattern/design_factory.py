from abc import ABC, abstractmethod


class Parts(ABC):
    @abstractmethod
    def get_name(self):
        pass


class KeyboardBrazil(Parts):
    def get_name(self):
        return "Teclado ABNT2"


class KeyboardEUA(Parts):
    def get_name(self):
        return "Teclado ANSI"


class StoreMaintenance(ABC):
    def make_repair(self):
        part = self.create_part()
        print(f"Iniciando reparo com: {part.get_name()}")
        print("Finalizando manutenção padrão.")

    @abstractmethod
    def create_part(self):
        pass


class ItStoreSalvador(StoreMaintenance):
    def create_part(self):
        return KeyboardBrazil()


class ItStoreMiami(StoreMaintenance):
    def create_part(self):
        return KeyboardEUA()


salvador_store = ItStoreSalvador()
miami_store = ItStoreMiami()

print("--- Atendimento em Salvador ---")
salvador_store.make_repair()

print("--- Atendimento em Miami ---")
miami_store.make_repair()
