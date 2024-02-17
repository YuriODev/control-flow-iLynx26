# Input: A three-digit integer
number = int(input("Enter a three-digit number: "))

# Extract digits
first_digit = number // 100
second_digit = (number % 100) // 10
third_digit = number % 10

# Initialize count
count = 0

# Count identical digits using direct comparison
if first_digit == second_digit == third_digit:
    count = 3
elif first_digit == second_digit or first_digit == third_digit or second_digit == third_digit:
    count = 2

# Prepare the output message
output = f"{count}"

# Print the output message
print(output)
