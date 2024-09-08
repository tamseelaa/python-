import random
def dice():
    add=0
    while add != 6:
        add = random.randint(0, 6)
        print(add)
dice()
