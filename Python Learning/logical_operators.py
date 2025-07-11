#logical operators = used on conditional statements

#   and = checks two or more conditions if True
#   or = checks if at least one condition is True
#  not = True if condition is False, and vice versa

#and
temp = -20
sunny=False

if temp >0 and temp < 30:
    print("The temperature is good")
else:
    print("The temperature is bad")

    #or
if temp >= 0  or temp <=30:
    print("The temperature is good")
else:
    print("The temperature is bad")

if not sunny:
    print("Its cloudy outside")
else:
    print("Its sunny outside")