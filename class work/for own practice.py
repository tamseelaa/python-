"""numbers = []

# Collect numbers from the user
while True:
    user_input = input("Enter a number (or press Enter to quit):")

    if user_input == "":
        break

    # Convert input to float and add to the list
    number = float(user_input)
    numbers.append(number)

# Sort the numbers in descending order
numbers.sort(reverse=True)

# Get the top 5 numbers
top_five = numbers[:5]

# Print the result
if top_five:
    print("The five greatest numbers are:", top_five)
else:
    print("No numbers were entered.")
# Get input from the user
number = int(input("Enter an integer: "))

# Handle the case for numbers less than or equal to 1
if number <= 1:
    print(f"{number} is not a prime number.")
else:
    # Assume the number is prime
    is_prime = 1  # 1 means prime, 0 means not prime

    # Use a for loop to check divisibility
    for i in range(2, number):
        if number % i == 0:
            is_prime = 0
            break

    # Output result based on is_prime value
    print(f"{number} is a prime number." if is_prime == 1 else f"{number} is not a prime number.")
def is_prime(n):
    if n <= 1:
        return False
    # Check divisibility from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Ask the user for input
number = int(input("Enter an integer: "))

# Check if the number is prime
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
number = int(input("Enter an integer: "))

# Prime numbers are greater than 1
if number <= 1:
    print(f"{number} is not a prime number.")
else:
    is_prime = True  # Assume the number is prime initially

    # Check divisibility from 2 to number-1
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    # Output the result
    if is_prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
import random
number=int(input("enter a number"))
add=0
for i in range(0,number):
    number=random.randint(1,6)
    add=add+number
print(f"sum of all dices rolled are: {add}")

divisor = 0
integ=int(input("enter an integer"))
if integ<=0:
    print("Its not prime")
for i in range(2,integ):

    if integ%i==0:
      divisor=+1
      break
    if divisor==0:
     print("not prime")
    else:
     print("prime")"""
city=[]
for i in range(5):
    user = input("enter a city")
    city.append(user)
for i in city:
    print(i)
