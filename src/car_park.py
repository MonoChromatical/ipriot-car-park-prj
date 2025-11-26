from display import Display
from sensor import Sensor
from pathlib import Path
from datetime import datetime
import json


class CarPark:
    def __init__(self, location, capacity, plates=None, sensors=None, displays=None, log_file=Path("log.txt")):
        self.location = location
        self.capacity = capacity
        self.plates = plates if plates is not None else []
        self.sensors = sensors if sensors is not None else []
        self.displays = displays if displays is not None else []
        self.log_file = log_file if isinstance(log_file, Path) else Path(log_file)
        self.log_file.touch(exist_ok=True)

    def __str__(self):
        return f"Car park at {self.location} with {self.capacity} bays"

    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Component must be a Sensor or Display")

        if isinstance(component, Sensor):
            self.sensors.append(component)

    def add_car(self, plate):
        self.plates.append(plate)
        self.update_displays()
        self._log_car_activity(plate, "entered")

    def remove_car(self, plate):
        self.plates.remove(plate)
        self.update_displays()
        self._log_car_activity(plate, "exited")

    @property
    def available_bays(self):
        return max(0, self.capacity - len(self.plates))

    def update_displays(self):
        data = {
            "available_bays": self.available_bays,
            "temperature": 25  # placeholder
        }
        for display in self.displays:
            display.update(data)

    def _log_car_activity(self, plate, action):
        with self.log_file.open("a") as f:
            f.write(f"{plate} {action} at {datetime.now():%Y-%m-%d %H:%M:%S}\n")

    def write_config(self, config_file="config.json"):
        with open(config_file, "w") as f:
            json.dump(
                {
                    "location": self.location,
                    "capacity": self.capacity,
                    "log_file": str(self.log_file),
                },
                f,
            )

    @classmethod
    def from_config(cls, config_file="config.json"):
        config_path = Path(config_file) if not isinstance(config_file, Path) else config_file
        with config_path.open() as f:
            config = json.load(f)
        return cls(
            config["location"],
            config["capacity"],
            log_file=config["log_file"],
        )