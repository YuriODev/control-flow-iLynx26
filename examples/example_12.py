# Input: A number from the user
number = int(input("Enter a number: "))

# Determine if the number ends with 5
if number % 10 == 5:
    output = "True"
else:
    output = "False"

# Print the output message
print(output)
