from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display

def main():
    car_park = CarPark("Moondalup", 100, log_file="moondalup.txt")

    car_park.write_config("moondalup_config.json")

    car_park = CarPark.from_config("moondalup_config.json")

    entry_sensor = EntrySensor(id=1, is_active=True, car_park=car_park)
    exit_sensor = ExitSensor(id=2, is_active=True, car_park=car_park)

    display = Display(
        id=1,
        car_park=car_park,
        message="Welcome to Moondalup",
        is_on=True,
    )

    car_park.register(display)
    car_park.register(entry_sensor)
    car_park.register(exit_sensor)

    for _ in range(10):
        entry_sensor.detect_vehicle()

    for _ in range(2):
        exit_sensor.detect_vehicle()

    print(f"Final plates in car park: {car_park.plates}")
    print(f"Available bays: {car_park.available_bays}")

if __name__ == "__main__":
    main()