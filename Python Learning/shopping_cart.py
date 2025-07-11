

item = input("What Item Would You Like To Buy : ")
price = float(input("What Is The Price?: "))
quantity =int(input("How many would you like ? : "))

total = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Your Total is : ${round(total,2)}")