month=int(input("Enter a number of any month= "))
numbers=(12,1,2),(6,7,8),(9,10,11),(3,4,5)
season="Winter","Summer","Autumn","Spring"
if 0<month<=12:
    for i in range(len(numbers)):
        if month in numbers[i]:
            print(season[i])
            break
else:
            print("invalid entry")


