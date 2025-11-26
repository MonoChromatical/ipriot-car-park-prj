Car Park System using Python OOP. Tracks cars, sensors, and displays.


Screenshot evidence

First commit
![img.png](img.png)

src folder after second commit
![img_1.png](img_1.png)

ANSWERS 2.3 Identify classes, methods, and attributes

| Class Name | Attributes                           | Methods                                                             |
| ---------- |--------------------------------------|---------------------------------------------------------------------|
| `CarPark`    | Location, capacity, plates, displays | register(), add_car(), remove_car(), update_displays(), available_bays() |
| `Sensor`     | id, is_active, car_park              | detect_vehicle(), _scan_plate(), update_car_park()                  |
| `Display`    | id, message, is_on                   | update()                                                            |