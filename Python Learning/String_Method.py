
#name = input("Enter your full name : ")
#phone_num = input("Enter your phone number: ")

#result = len(name)
#result = name.find("m")
#result = name.rfind("o")
#name = name.capitalize()
#name  = name.upper()
#name = name.lower()
#result = name.isdigit()
#result = name.isalpha()

#result = phone_num.count("-")
#result = phone_num.replace("-","")

print(help(str))

#Excercise --validate user input excercise
#1. username is no more tahn 12 characters
#2. username must not contain spaces
#3. username must not contain digits


user_name = input("Enter your user name: ")
user_name.find(" ")
user_name.isalpha()
#result = "Valid user" if len(user_name) <12  else "non valid"
#print(result)
if len(user_name) >12:
    print("Your user name can't be more than 12 characters")
elif not user_name.find(" ") == -1:
    print("Your user name can't contain spaces")
elif not user_name.isalpha():
    print("Your user name can't contain numbers")
else:
    print(f"Welcome {user_name}")


