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
