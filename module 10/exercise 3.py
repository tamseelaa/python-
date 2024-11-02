import time,os,sys

def typingPrint(text):
   for character in text:
      sys.stdout.write(character)
      sys.stdout.flush()
      time.sleep(0.1)

class Elevator:
    def __init__(self, bottom_floor, top_floor,elevator_number):
        self.current_floor = bottom_floor
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevator_number=elevator_number

    def go_to_floor(self, target):
        if target < self.bottom_floor or target > self.top_floor:
            print("Target floor out of range.\n")
            return

        while self.current_floor != target:
            if self.current_floor < target:
                self.floor_up()
            else:
                self.floor_down()


        #target reached statement
        print(f"Reached floor {self.current_floor}\n")


    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator {self.elevator_number}  is Moving up: now at floor {self.current_floor}:\n")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator: {self.elevator_number}  is Moving down: now at floor {self.current_floor}\n")

class Building:
    def __init__(self,bottom_floor,top_floor,num_elevator):
        self.bottom_floor=bottom_floor
        self.top_floor=top_floor
        self.num_elevator=num_elevator
        self.elevators=[Elevator(bottom_floor,top_floor,i) for i in range(num_elevator)]

    def run_elevator(self,elevator_number,destination_floor):
        elevator = self.elevators[elevator_number - 1]  # Convert to zero-index
        elevator.go_to_floor(destination_floor)

    def fire_alarm(self):
        for i in range(self.num_elevator):
            elevator = self.elevators[i]
            typingPrint(f"Fire!!!!!!! Go quickly to the ground floor\n")
            elevator.go_to_floor(1)





building = Building(1, 10, 5)  # Create a building with 5 elevators
building.run_elevator(1, 6) # Run elevator 1 to floor 6
building.run_elevator(2, 4)
building.run_elevator(3, 10)
building.run_elevator(4, 5)
building.run_elevator(5, 8)
building.fire_alarm()