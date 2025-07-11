# Function to print star pattern using a while loop
def print_star_pattern(rows):
    i = 1  # Initialize row counter
    while i <= rows:
        print('*' * i)  # Print i stars in the i-th row
        i += 1  # Increment the row counter


# Input for number of rows
num_rows = int(input("Enter the number of rows for the star pattern: "))
print_star_pattern(num_rows)
