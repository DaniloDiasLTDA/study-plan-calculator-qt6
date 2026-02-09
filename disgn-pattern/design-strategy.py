from abc import ABC, abstractmethod


class StrategyBackup(ABC):
    @abstractmethod
    def save_file(self, file_name):
        pass


class BackupGoogleDrive(StrategyBackup):
    def save_file(self, file_name):
        return f"Arquivo '{file_name}' foi salvo no Google Drive "


class BackupFTP(StrategyBackup):
    def save_file(self, file_name):
        return f"Arquivo '{file_name}'salvo no FTP."


class OldService:
    def save_raw_data(self, data):
        return f"LOG ANTIGO: Dados bruto: {data}"


class OldAdapterSaver(StrategyBackup):
    def __init__(self, old_service_instance):
        self.old_service = old_service_instance

    def save_file(self, file_name):
        return self.old_service.save_raw_data(file_name)


class ManagementBackup:
    def __init__(self, strategy: StrategyBackup):
        self._strategy = strategy

    def define_strategy(self, new_strategy: StrategyBackup):
        print("---Alterando a estratégia de backup---")
        self._strategy = new_strategy

    def execute_backup(self, file_name):
        result = self._strategy.save_file(file_name)
        print(result)


drive = BackupGoogleDrive()
ftp = BackupFTP()

management = ManagementBackup(drive)
management.execute_backup("curriculo_danilo.pdf")

management.define_strategy(ftp)
management.execute_backup("fotos_viagem.zip")
