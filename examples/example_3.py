# Input: A number from the user
number = float(input("Enter a number: "))

# Initialize an empty string for the output message
output = ""

# Conditional statements to determine the nature of the number and assign an appropriate message
if number > 0:
    output = "It is a positive number"
elif number < 0:
    output = "It is a negative number"
else:
    output = "It is Zero"

# Print the output message
print(output)
