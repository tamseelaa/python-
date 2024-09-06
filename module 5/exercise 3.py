number = int(input("Enter an integer: "))
if number <= 1:
    print(f"{number} is not a prime number.")
else:
    divisor_count = 0
    for i in range(2, number):
        if number % i == 0:
            divisor_count += 1
            break
    if divisor_count == 0:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
