numbers=[5,8,5,2,9,5,10]

unique=[]
for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)

