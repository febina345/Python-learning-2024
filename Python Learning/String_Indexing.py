#indexing = accessing elements of a sequence using [] (indexing operator)
#    [start : end : step]


credit_number = "1234-5678-9012-3456"

print(credit_number[0])
print(credit_number[0:4])
print(credit_number[:4])
print(credit_number[5:9])
print(credit_number[5:])
print(credit_number[-1])
print(credit_number[::2])

# create a program to get last 4 digits of a credit card number
last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")