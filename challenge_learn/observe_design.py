from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, temperature, wind_speed, pressure):
        pass


class Subject(ABC):
    @abstractmethod
    def register_observer(self, observer):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass


class WeatherStation(Subject):
  def __init__(self):
    self._observers = []
    self._temperature = 0
    self._wind_speed = 0
    self._pressure = 0

  def register_observer(self, observer):
    self._observers.append(observer)

  def remove_observer(self, observer):
    self._observers.remove(observer)

  def notify_observers(self):
    for observer in self._observers:
      observer.update(self._temperature, self._wind_speed, self._pressure)

  def set_measurements(self, temperature, wind_speed, pressure):
    self._temperature = temperature
    self._wind_speed = wind_speed
    self._pressure = pressure

    self.notify_observers()


class UserInterface(Observer):
    def update(self, temperature, wind_speed, pressure):
      print(f"UI: Exibindo no Painel: {temperature}°C e {wind_speed}km/h.")


class Logger(Observer):
  def update(self, temperature, wind_speed, pressure):
    print(f"LOGGER: Registrando no banco de dados: Pressão em {pressure}hPa.")


class AlertSystem(Observer):
  def update(self, temperature, wind_speed, pressure):
    if temperature > 35:
      print("ALERTA! Calor extremo detectado!")
    if wind_speed > 50:
      print("ALERTA! Ventos fortes! Risco de queda de árvores.")


station = WeatherStation()

interface = UserInterface()
sys_logg = Logger()
alert_system = AlertSystem()

station.register_observer(interface)
station.register_observer(sys_logg)
station.register_observer(alert_system)

station.set_measurements(25, 10, 1013)

station.set_measurements(22, 65, 1005)