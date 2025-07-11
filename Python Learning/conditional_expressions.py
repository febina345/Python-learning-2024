#conditional expressions = A one-line shortcut for the if-else statement (ternary operator)
#                          print or assign one of two values based on a condition
#                          x if condition else y

num = -5

print("Positive" if num>0 else "negetive")
num=5
result = "Even" if num%2 == 0 else "ODD"
print(result)
num=5
a = 6
b = 7
max_num = a if a>b else b
print(max_num)
min_num =a if a<b else b
print(min_num)
Age = 12
status  = "Adult" if Age >=18 else "Child"
print(status)

temperatue = 30
weather= "Hot" if temperatue>20 else"cold"
print(weather)
user_role = "guest"
access_level = "Full Acces" if user_role == "admin" else "Limited access"
print(access_level)