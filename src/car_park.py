from display import Display
from sensor import Sensor



class CarPark:
    def __init__(self, location, capacity, plates=None, sensors=None, displays=None):
        self.location = location
        self.capacity = capacity
        self.plates = plates if plates is not None else []
        self.sensors = sensors if sensors is not None else []
        self.displays = displays if displays is not None else []

    def __str__(self):
        return f"Car park at {self.location} with {self.capacity} bays"

    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Component must be a Sensor or Display")

        if isinstance(component, Sensor):
            self.sensors.append(component)