import random
num=random.randint(1,10)
while True:
    a=int(input("Enter a number: "))
    if a>num:
     print("This Number is higher")
    elif a<num:
     print("This Number is lower")
    else:
     print("correct")
     break
