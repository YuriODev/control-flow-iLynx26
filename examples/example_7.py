# Input: Day, month, and year (last two digits) from the user
day = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year = int(input("Enter the last two digits of the year: "))

# Initialize an empty string for the output message
output = ""

# Check if the product of day and month equals the year
if day * month == year:
    output = "The date is magic!"
else:
    output = "The date is not magic."

# Print the output message
print(output)
