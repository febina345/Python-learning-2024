#Python calculator

operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


if operator == "+":
    result = num1+num2
    print(round(result,2))
elif operator == "-":
    result = num1-num2
    print(round(result,2))
elif operator == "*":
    result = num1*num2
    print(round(result,2))
elif operator == "/":
    result = num1/num2
    print(round(result,3))
else:
    print(f"{operator} is not valid operator")


