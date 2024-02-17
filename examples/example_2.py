# Input: Number of points received by the team
points = int(input("Enter the number of points: "))

# Initialize an empty string for the output message
output = ""

# Conditional statements to determine the match result and assign it to the output variable
if points == 3:
    output = "win"
elif points == 1:
    output = "draw"
elif points == 0:
    output = "lose"

# Print the output message
print(output)