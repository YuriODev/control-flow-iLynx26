# Input: Number representing a day of the week
day_number = int(input("Enter the day number: "))

# Initialize an empty string for the output message
output = ""

# Conditional statements to assign the name of the day
if day_number == 1:
    output = "Monday"
elif day_number == 2:
    output = "Tuesday"
elif day_number == 3:
    output = "Wednesday"
elif day_number == 4:
    output = "Thursday"
elif day_number == 5:
    output = "Friday"
elif day_number == 6:
    output = "Saturday"
elif day_number == 7:
    output = "Sunday"
else:
    output = "Invalid day number"

# Print the output message
print(output)
