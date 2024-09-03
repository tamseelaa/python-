smallest=0
largest=0
user_input=input("Enter a number: ")
if user_input!=" ":
        num=float(user_input)
        smallest=largest=num
while user_input!=" ":
    num=float(user_input)

    if num<smallest:
           smallest=num
    if num>largest:
           largest=num
    user_input=input("Enter a number: ")
print(f"smallest:{smallest}")
print(f"largest:{largest}")



