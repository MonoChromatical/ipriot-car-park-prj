import unittest
from pathlib import Path

from car_park import CarPark


class TestCarPark(unittest.TestCase):

    LOG_FILENAME = "new_log.txt"

    def setUp(self):

        self.car_park = CarPark("123 Example Street", 100)

    def test_car_park_initialized_with_all_attributes(self):
        self.assertIsInstance(self.car_park, CarPark)
        self.assertEqual(self.car_park.location, "123 Example Street")
        self.assertEqual(self.car_park.capacity, 100)
        self.assertEqual(self.car_park.plates, [])
        self.assertEqual(self.car_park.displays, [])
        self.assertEqual(self.car_park.available_bays, 100)
        self.assertEqual(self.car_park.log_file, Path("log.txt"))

    def test_add_car(self):
        self.car_park.add_car("FAKE-001")
        self.assertEqual(self.car_park.plates, ["FAKE-001"])
        self.assertEqual(self.car_park.available_bays, 99)

    def test_remove_car(self):
        self.car_park.add_car("FAKE-001")
        self.car_park.remove_car("FAKE-001")
        self.assertEqual(self.car_park.plates, [])
        self.assertEqual(self.car_park.available_bays, 100)

    def test_overfill_the_car_park(self):
        for i in range(100):
            self.car_park.add_car(f"FAKE-{i}")
        self.assertEqual(self.car_park.available_bays, 0)

        self.car_park.add_car("FAKE-100")
        self.assertEqual(self.car_park.available_bays, 0)

        self.car_park.remove_car("FAKE-100")
        self.assertEqual(self.car_park.available_bays, 0)

    def test_removing_a_car_that_does_not_exist(self):
        with self.assertRaises(ValueError):
            self.car_park.remove_car("NO-1")

    def test_register_raises_type_error(self):
        with self.assertRaises(TypeError):
            self.car_park.register("Not a Sensor or Display")

    def test_log_file_created(self):
        new_carpark = CarPark("123 Example Street", 100, log_file=self.LOG_FILENAME)
        self.assertTrue(Path(self.LOG_FILENAME).exists())

    def tearDown(self):
        # Delete the log file if it exists
        Path(self.LOG_FILENAME).unlink(missing_ok=True)

    def test_car_logged_when_entering(self):
        new_carpark = CarPark("123 Example Street", 100, log_file=self.LOG_FILENAME)
        new_carpark.add_car("NEW-001")
        with new_carpark.log_file.open() as f:
            last_line = f.readlines()[-1]
        self.assertIn("NEW-001", last_line)
        self.assertIn("entered", last_line)
        self.assertIn("\n", last_line)

    def test_car_logged_when_exiting(self):
        new_carpark = CarPark("123 Example Street", 100, log_file=self.LOG_FILENAME)
        new_carpark.add_car("NEW-001")
        new_carpark.remove_car("NEW-001")
        with new_carpark.log_file.open() as f:
            last_line = f.readlines()[-1]
        self.assertIn("NEW-001", last_line)
        self.assertIn("exited", last_line)
        self.assertIn("\n", last_line)

