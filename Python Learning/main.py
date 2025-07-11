#variable = A container for a value (String. Integer, float, boolean)
# A variable behaves as if it was the value it contains

first_name = "Febina"
food = "Apple"
email= "febs@gmail.com"

print(first_name)
print(f"Hello {first_name}")  #fString
print(f"My favourite fruit is {food}")
print(f"my email is {email}")


#Integer
age = 30
quantity = 30
num_of_students = 20

print(age)
print(f"You are {age} years old")
print(f"you are buying {quantity} items")
print(f"your class has {num_of_students} students")


#floats
price = 10.99
GPA = 3.2
distance = 10

print(f"The price is ${price}")
print(f"Your GPA is {GPA}")
print(f"You ran {distance} km")

#Boolean

is_student = True
for_sale =True
is_online = False

print(f"Are you a Student : {is_student} ")

if is_student:
    print("You are a student")
else:
    print("You are not a student ")

if for_sale:
    print("That item for sale")
else:
    print("That item not available")

if is_online:
    print("You are online")
else:
    print("You are offline")