import random
class Car:

    def __init__(self,reg_number,max_speed):
        self.travelled_distance,current_speed = 0, 0
        self.max_speed=max_speed
        self.reg_number=reg_number
        self.current_speed = current_speed


    def accelerate(self,  speeds):
        self.current_speed= self.current_speed + speeds
        if self.current_speed>self.max_speed:
            self.current_speed=self.max_speed
        elif self.current_speed<0:
            self.current_speed=0
        return self.current_speed


    def drive(self,hours):

        distances = self.current_speed * hours
        self.travelled_distance += distances
        return self.travelled_distance



#creating a list of car name and also telling class constructors
cars=[]
for i in range(1,11):
    car = Car(f"F1-82{i}", random.randint(100,200))
    cars.append(car)


distance=0
while distance <10000:
    for car in cars:
        car.accelerate(random.randint(-15,10))
        distance = car.drive(1)
        if distance>10000:
            print(f"we got a winner here Finally : {car.reg_number}")
            break


print(f"{'Registration':<19} {'Max Speed':<12} {'Distance Traveled':<20} {'Current Speed':<15}")
print("=" * 65)
for car in cars:
    print(f"{car.reg_number :<19} {car.max_speed:<12} {car.travelled_distance:<20} {car.current_speed:<15}")







