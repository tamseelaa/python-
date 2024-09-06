import random
add=0
dice=int(input("enter how many dices to roll at the same time"))
for i in range(0,dice):
    dice=random.randint(1,6)
    add=add+dice
print(add)