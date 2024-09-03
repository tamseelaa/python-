while True:
     n=int(input("Enter a number in inches to find its cm:  and you can enter negative value to end the program"))
     if n<=0:
         print("ended")
         break
     if n>=1:
         print(n*2.54)
