gas=int(input("enter how many gallon of gasoline you have ,also to end program enter negative value"))
def gallon(n):
    liter=3.78541*n
    print(f" {n}gallon = {liter}")

while True:
    if gas<0:
        print("Program is ending bye")
        break
    elif gas>=1:
        gallon(gas)
        gas = int(input("enter how many gallon of gasoline you have ,Also to end program enter negative value"))

