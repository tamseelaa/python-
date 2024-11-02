class Car:

    def __init__(self,reg_number,max_sp):
        travelled_distance, current_speed = 0, 0
        print(f"Car properties:\n 1:registration number = {reg_number}\n"
                 f" 2:maximum speed = {max_sp}\n 3:current speed = {current_speed} \n"
                 f" 4: travelled distance = {travelled_distance}")

Car("ABC-123 ","142 km/h ")