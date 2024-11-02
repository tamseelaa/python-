class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.current_floor = bottom_floor
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor

    def go_to_floor(self, target):
        if target < self.bottom_floor or target > self.top_floor:
            print("Target floor out of range.")
            return

        while self.current_floor != target:
            if self.current_floor < target:
                self.floor_up()
            else:
                self.floor_down()

        #target reached statement
        print(f"Reached floor {self.current_floor}")

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Moving up: now at floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Moving down: now at floor {self.current_floor}")

elevator = Elevator(0, 10)


print("Going to floor 5:")
elevator.go_to_floor(5)

print("Going back to the bottom floor:")
elevator.go_to_floor(0)
