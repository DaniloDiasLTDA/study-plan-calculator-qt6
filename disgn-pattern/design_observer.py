from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass

class BackupSystem:
    def __init__(self):
        self._observers = [] # Lista de inscritos

    def subscribe(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def unsubscribe(self, observer):
        self._observers.remove(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

    def run_backup(self, file_name):
        print(f"Executando backup de {file_name}...")
        self.notify(f"Backup do arquivo '{file_name}' concluído com sucesso!")

class UserNotification(Observer):
    def update(self, message):
        print(f"Notificação de atualização: {message}")

class ITSupport(Observer):
    def update(self, message):
        print(f"Empresa dev: Enviando log para o servidor: {message}")


system = BackupSystem()
user = UserNotification()
ti = ITSupport()

system.subscribe(user)
system.subscribe(ti)

system.run_backup("relatorio_financeiro.pdf")