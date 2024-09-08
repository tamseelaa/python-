import random
user=int(input("enter the number of which sided a dice should be "))
def dice_side(n):
    return random.randint(1,n)

ans = 0
while ans != user:
   ans = dice_side(user)
   print(f"Rolled: {ans}")
