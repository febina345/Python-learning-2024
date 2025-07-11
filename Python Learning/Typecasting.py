#Typecasting = The process of converting a value of one data type to another (string, integer, float, boolean
#Explicit vs Implicit


#Explicit
name = "Feb"
age = 30
gpa = 3.2
student = True

type(name)

print(type(name))
print(type(age))
print(type(gpa))
print(type(student))

age = float(age)
print(age)

gpa = int(gpa)
print(gpa)

student = str(student)
print(student)
print(type(student))

age = bool(age)
print(age)
print(type(age))

#Implicit typecasting -automatically converting data types

x = 2
y=2.0
x= x/y
print(x)

