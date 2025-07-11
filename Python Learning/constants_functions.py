import math
x=9.4
print(math.pi)
print(math.e)
result = math.sqrt(x)
print(result)
result2 = math.ceil(x)
print(result2)
result3 = math.floor(x)
print(result3)

#calculate circumference of circle

radius = float(input("Enter the radius of the circle: "))

circumference = 2 * math.pi * radius

print(f"The circumference is:  {round(circumference,2)} cm")

#Area of circle

radius = float(input("Enter the radius of a circle: "))
area = math.pi* pow(radius,2)

print(f"Area of the circle is : {round(area,2)} cm^2")

#Hypotanuse calculator
a = float(input("Enter side A : "))
b = float(input("Enter side B: "))

c= math.sqrt(pow(a,2) + pow(b,2))

print(f"The hypotanuse of  a triangle is {round(c,2)}")

