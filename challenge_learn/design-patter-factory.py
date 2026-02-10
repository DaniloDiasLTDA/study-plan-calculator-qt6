from abc import ABC, abstractmethod


class Zone(ABC):
    @abstractmethod
    def get_display_name(self):
        pass

    @abstractmethod
    def get_offset(self):
        pass


class ZoneEastern(Zone):
    def get_display_name(self):
        return "US/Eastern"

    def get_offset(self):
        return -5


class ZoneCentral(Zone):
    def get_display_name(self):
        return "US/Central"

    def get_offset(self):
        return -6


class ZoneMountain(Zone):
    def get_display_name(self):
        return "US/Mountain"

    def get_offset(self):
        return -7


class ZonePacific(Zone):
    def get_display_name(self):
        return "US/Pacific"

    def get_offset(self):
        return -8


class ZoneFactory:
    @staticmethod
    def create_zone(zone_id):
        if zone_id == "US/Eastern":
            return ZoneEastern()
        elif zone_id == "US/Central":
            return ZoneCentral()
        elif zone_id == "US/Mountain":
            return ZoneMountain()
        elif zone_id == "US/Pacific":
            return ZonePacific()
        else:
            raise ValueError(f"ID de zona desconhecido: {zone_id}")


class Calendar:
    def __init__(self, zone_factory):
        self.factory = zone_factory
        self.zone = None

    def create_calendar(self, zone_id):
        self.zone = self.factory.create_zone(zone_id)
        print(f"Calendário configurado para {self.zone.get_display_name()}")


# --- TESTANDO O CÓDIGO ----

factory = ZoneFactory()
pacific_zone = factory.create_zone("US/Pacific")


calendar = Calendar(factory)
calendar.create_calendar("US/Mountain")

print(f"Zona: {pacific_zone.get_display_name()}")
print(f"Offset: {pacific_zone.get_offset()}")


print("--- Configurando Calendário ---")
print(f"Deslocamento atual: {calendar.zone.get_offset()} horas")
