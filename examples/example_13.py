# Input: A two-digit number from the user
number = int(input("Enter a two-digit number: "))

# Check if the number is within the valid range
if number < 10 or number > 99:
    output = "0"
else:
    # Extract digits
    first_digit = number // 10
    second_digit = number % 10
    
    # Compare digits
    if first_digit > second_digit:
        output = "1"
    elif second_digit > first_digit:
        output = "2"
    else:
        output = "="

# Print the output message
print(output)
