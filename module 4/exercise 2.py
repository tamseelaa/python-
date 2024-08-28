while True:
     n=int(input("Enter a number in inches to find its cm: "))
     if n<=0:
         print("ended")
         break
     if n>=1:
         print(n*2.54)
