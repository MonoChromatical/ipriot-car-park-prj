from abc import ABC, abstractmethod
import random


def _generate_plate():
    number = format(random.randint(0, 999), '03d')
    return f"MOON-{number}"


class Sensor(ABC):
    def __init__(self, id, is_active, car_park):
        self.id = id
        self.is_active = is_active
        self.car_park = car_park

    def __str__(self):
        status = "active" if self.is_active else "inactive"
        return f"Sensor {self.id} is {status}"

    @abstractmethod
    def update_car_park(self, plate):
        pass

    def _scan_plate(self):
        return _generate_plate()

    def detect_vehicle(self):
        plate = self._scan_plate()
        self.update_car_park(plate)

class EntrySensor(Sensor):


    def update_car_park(self, plate):
        self.car_park.add_car(plate)
        print(f"Incoming vehicle detected. Plate {plate}")

class ExitSensor(Sensor):

    def _scan_plate(self):
        return random.choice(self.car_park.plates)

    def update_car_park(self, plate):
        self.car_park.remove_car(plate)
        print(f"Outgoing vehicle detected. Plate {plate}")