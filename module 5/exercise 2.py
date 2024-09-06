num=[ ]
while True:
    user = input("Enter a number (or only press Enter to quit): ")
    if user == "":
        break

    number = float(user)
    num.append(number)

num.sort(reverse=True)
decs_five = num[:5]
if decs_five:
    print("The five greatest numbers are:", decs_five)
else:
    print("No numbers were entered.")





