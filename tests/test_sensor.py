import unittest

from car_park import CarPark
from sensor import EntrySensor, ExistSensor


class TestSensor(unittest.TestCase):

    def setUp(self):
        self.car_park = CarPark("123 Example Street", 2)

    def test_entry_sensor_detect_vehicle_adds_car(self):
        entry_sensor = EntrySensor(id=1, is_active=True, car_park=self.car_park)

        entry_sensor._scan_plate = lambda: "TEST-001"

        entry_sensor.detect_vehicle()

        self.assertIn("TEST-001", self.car_park.plates)

    def test_exit_sensor_detect_vehicle_removes_car(self):
        self.car_park.plates.append("TEST-002")

        exit_sensor = ExistSensor(id=2, is_active=True, car_park=self.car_park)

        exit_sensor._scan_plate = lambda: "TEST-002"

        exit_sensor.detect_vehicle()

        self.assertNotIn("TEST-002", self.car_park.plates)