zander=int(input("enter the length of zander in cm "))
size_limit=42
if zander>=size_limit:
    print("its good")
elif zander<size_limit:
    print(f"release it back not suitable. its smaller by",size_limit-zander ,"cm")