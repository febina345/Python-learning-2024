

unit = input("Is this temperature is in Celsius or Farenheit ? (C/F) : ")
temp = float(input("Enter the temperature to be converted: "))


if unit == "C":
    temp = round((9*temp) / 5 +32,1)
    print(f"The temperature in Farenheit is : {temp}0F")
elif unit == "F":
    temp = round((temp - 32) *5 /9,1)
    print(f"The temperature in Celsius is {temp} 0C")
else:
    print(f"{unit} is an invalid unit of measurement")

