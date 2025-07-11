#if = Used to do ome code only IF some conditions is True
#  Else do something else

age= int(input("Enter your age: "))
if age >= 100:
    print("You are too old to sign up")
elif age >=18:
    print("You are now signed up")
elif age <0:
    print("You haven't been born yet")

else:
    print("You must be 18 plus to sign up!")


#example 2

response = input("Would you like food ? (Y/N) : ")

if response == "Y":
    print("Have some food!")
else:
    print("No food for you!")

#Example 3

name = input("Enter Your Name : ")

if name == "":
    print("You did not write your name!")
else:
    print(f"Hello{name}!")


#Example 4  -Boolean

for_sale =True

if for_sale:
    print("This item is for sale!")
else:
    print("This item is not for sale")

online = False

if online:
    print("The user is Online ")
else:
    print("The user is offline")
