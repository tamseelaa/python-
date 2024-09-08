"""born_year = int(input("enter your born year"))
age= 2024-born_year
if age >= 18:
    print("Yahoo you are welcome!")
if age < 18:
    print("oops ur not eligible")
if age==0:
    print("are u a human being")
print("thankyou")

born_year = int(input("enter your born year"))
age= 2024-born_year
if age >= 18:
    print("Yahoo you are welcome!")
elif 0< age <18:
    print("you are not eligible")
else:
    print("your input is not allowed")

vowel or constant
v=(input("enter your character in lower alphabet"))
if v == 'a':
    print("its a vowel")
elif v == 'e':
    print("its a vowel")
elif v=='i':
    print("its a vowel")
elif v=='o':
    print("its a vowel")
elif v=='u':
    print("its a vowel")
else :
    print("its not a vowel")
happy or sad

feeling=input("how ur feeling: :-) or :-(")
happy_count=feeling.count(":-)")
sad_count=feeling.count(":-(")

if happy_count==0 and sad_count==0:
    print("none")
elif happy_count==sad_count:
    print("unsure")
elif happy_count > sad_count:
    print("happy")
else:
    print("sad")

i=1
while i<11:
    print(i)
    i=i+1 #i+=1

greet=int(input("how many time you want me to enter your greeting"))
first_greeting=0
while first_greeting<greet:
    print("good morning")
    first_greeting+=1

command=input("enter your command:")
while command!="exit":
    print("program is running")
    command=input("enter your command:")
print("this program has stop")

import random
dice1=dice2= roll_times=0
while (dice1 !=3 or dice2 !=3):
    dice1=random.randint(1,3)
    dice2=random.randint(1,3)
    roll_times +=1
print(f"the two dices were rolled {roll_times}times.")
command=input("enter your command:")
while command!="stop":
    if command=="break":
        break
    print("this program is running"+command)
    command=input("enter your command:")
    print("this program has stop")


num=10
while num<100:
    num=num+10
    if num==50:
        continue
        print("current number:",num)
HERE SEE WHATS THE PROBLEM


command=input("enter command:")
while command!="stop":
    if command=="break":
       break
    print("this program is running" + command)
    command=input("enter your command:")
else:
    print("goodbye")


first_num=1
while first_num<=5:
      second_num=1
      while second_num<=5:
        print(f"{first_num} times{second_num}is {first_num*second_num}")
        second_num+=1
      first_num+=1



import random

num1=random.randint(100,999)
num2=random.randint(1000,9999)
print(f"three digit number: ",num1 )
print(f"four digit number: ",num2)

import random
while True
num=random.randint(1,100)
while a!=num:
    a=int(input("enter your number:"))

    if a>num:
        print("number is higher")
    elif a<num:
           print("number is lower")
    elif a==num:
        print("number is equal")
        DIDNT GET IT


while True:
    n=int(input("enter your number to find factor of it:"))
    if n<=0:
      break
    f=1
    new_number=1
    while new_number<=n:
        f=f*new_number
        new_number+=1
    print(f"the factorial of the number is {f}")
  """
from operator import truediv

"""
names=["juha", "viivi", "ahmed","pekka"]
print(names)
print(len(names))
print(names[0])
print(names[-1])
print(names[1])
print(names[1:])
print(names[1:3])
print(names[len(names)-1])
print(names.index("ahmed"))

if "Ahmad" in names:
    print("Ahmad")
    print(names.index("Ahmad"))

    if "ahmed" in names:
        print("ahmed found")
        print(names.index("ahmed"))

for name in names:
    print(names.index("ahmed"))

#iteration 1
name= names[0]
#iteration 2
name= name[1]

for name in names:
    print(f"name in for loop: {name}")
new_name= name +"_new_name"
"""
"""
for number in range (1,20,2):
   print(number)
number2=list(range(1,11))
print(number2)

name=[]
name=input("enter a name: ")
index=0
while name != "" and index <len (name):
    print(name[index])
    index+=1
#exactly same thing but easier

name=input("enter a name: ")
for i in name:
    print(i)
"""
"""
sentence=input("enter a sentence: ")
sentence= " "+ sentence
for index in range (1,len(sentence)):
    if sentence [index-1] == " " and sentence [index] !=" " :
         print(sentence[index])
    index=index+1 
    """
"""
#function
def greeting(name):#name in a parameter 1 usage
    print("hi its monday",name)
    return
greeting("nam nam")
print("this is an example")
def greeting(times):#times is a parameter 2 usage
    for i in range(times):
        print("hi its monday")
greeting(3)
greeting(10)
def grocery(item):
    print("here is your shopping list:")
    for i in item:
        print("-"+i)
    return
shopping_list=["fish","mushroom","white carrot","icecream"]
grocery(shopping_list)
ask teacher
def calculation (a,b):
    add=a+b
    return add
num1=int(input("enter number:"))
num2=int(input("enter number:"))

calculation(num1,num2)
subs=calculation(num1,num2)
print(subs)

def draw_sprues(a):
   print("a spurce is coming")
   for i in range(0,a):
       print(" "*(a-1),"*"*((i*2)-1))
   i=+1
   print(" "*(a-1),"*")
draw_sprues(6)"""