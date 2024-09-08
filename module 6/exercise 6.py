def unit_price(cm, euros):
    radius = (cm / 2) / 100
    area = 3.14 * (radius ** 2)
    price = euros / area
    return price
diameter1 = float(input("Enter the diameter of the 1st pizza in centimeters: "))
price1 = float(input("Enter the price of the 1st pizza in euros: "))
diameter2 = float(input("Enter the diameter of the 2nd pizza in centimeters: "))
price2 = float(input("Enter the price of the 2nd pizza in euros: "))
price_1= unit_price(diameter1, price1)
price_2 = unit_price(diameter2, price2)
if price_1 < price_2:
    print("The 1st pizza gives better value for money.")
elif price1 > price_2:
    print("The 2nd pizza gives better value for money.")
else:
    print("Both of the pizzas give the same value for money.")