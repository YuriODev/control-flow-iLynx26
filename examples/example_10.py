# Input: Name of the month from the user
month = input("Enter the name of the month: ")

# Initialize an empty string for the output message
output = ""

# Determine the number of days in the month using if-else
if month == "January" or month == "March" or month == "May" or month == "July" or month == "August" or month == "October" or month == "December":
    output = f"{month} has 31 days in it."
elif month == "April" or month == "June" or month == "September" or month == "November":
    output = f"{month} has 30 days in it."
elif month == "February":
    output = "February has 28 or 29 days in it."
else:
    output = "Invalid month name"

# Print the output message
print(output)
