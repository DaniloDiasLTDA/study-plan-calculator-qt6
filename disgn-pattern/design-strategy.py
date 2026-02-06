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

old_service = OldService()

adapter = OldAdapterSaver(old_service)

print(adapter.save_file("projeto_final.zip"))
