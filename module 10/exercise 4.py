import random

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        new_speed = self.current_speed + speed_change
        if new_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif new_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = new_speed

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)  # Drive for one hour

    def print_status(self):
        print(f"{'Registration':<19} {'Max Speed':<12} {'Current Speed':<15} {'Distance':<20}")
        for car in self.cars:
            print(f"{car.registration_number:<19} {car.max_speed:<12} {car.current_speed:<15} {car.travelled_distance:<20}")

    def race_finished(self):
        return any(car.travelled_distance >= self.distance for car in self.cars)


cars = []
for i in range(1, 11):
    max_speed = random.randint(100, 200)
    registration_number = f"F1-82{i}"
    cars.append(Car(registration_number, max_speed))

# Create a race
race = Race("Grand Demolition Derby", 8000, cars)

# Simulate the race
hours = 0
while not race.race_finished():
    race.hour_passes()
    hours += 1
    if hours % 10 == 0:  # Print status every 10 hours
        print(f"\nStatus after {hours} hours:")
        race.print_status()

# Final status at the end of the race
print(f"\nFinal status after {hours} hours:")
race.print_status()