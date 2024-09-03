year=int(input("Enter a year number to find if its a leap year or not : "))
if year%4==0 or (year%400==0 and year%100==0):
    print(f"{year} a leap year")
else:
    print(f"{year} is not a leap year")