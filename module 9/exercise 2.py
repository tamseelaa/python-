class Car:

    def __init__(self,reg_number,max_speed):
        travelled_distance, current_speed = 0, 0
        self.max_speed=max_speed
        self.current_speed = current_speed
        print(f"Car properties:\n 1:registration number = {reg_number}\n"
                 f" 2:maximum speed = {max_speed}km/h \n 3:current speed = {current_speed} \n"
                 f" 4: travelled distance = {travelled_distance}")


    def accelerate(self,  speed):
        #self.current_speed= self.current_speed + speed
       # if self.current_speed>self.max_speed:
       #     self.current_speed=self.max_speed
       # elif self.current_speed<0:
            #self.current_speed=0
       #new method
        self.current_speed= min(max(self.current_speed+speed,0),self.max_speed)
        return self.current_speed
#properties call
reg_no,max_sd="ABC-123 ",142
car=Car(reg_no,max_sd)
#acceleration call
speed1=car.accelerate(30)
speed2=car.accelerate(70)
speed3=car.accelerate(50)
print(f"\nCurrent speed after +30 km/h: {speed1} km/h")
print(f"Current speed after +70 km/h: {speed2} km/h")
print(f"Current speed after +50 km/h: {speed3} km/h")
#emergency break call
final_speed = car.accelerate(-200)
print(f"Final speed after emergency brake: {final_speed} km/h")