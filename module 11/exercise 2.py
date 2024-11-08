from car import Car
class ElectricCar(Car):
    def __init__(self,register_number,max_speed,capacity):
        super().__init__(register_number,max_speed)
        self.capacity=capacity

class GasolineCar(Car):
    def __init__(self, register_number,max_speed,liters):
        super().__init__(register_number,max_speed)
        self.liters=liters

ecar=ElectricCar("ABC-15",180,52.5)

gcar=GasolineCar("ACD-123",165,32.3)

y=ecar.accelerate(50)
print(f"Average speed of electronic car in all drive : {y}")
z=ecar.drive(3)
print(f"the car travelled {z}km in 3 hour drive\n\n")

g=gcar.accelerate(30)
print(f"Average speed of gasoline car in all drive : {g}")
f=gcar.drive(3)
print(f"the car travelled {f}km in 3 hour drive\n\n")


