# Input: Current date (day, month, year)
day = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))

# Check for leap year
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Initialize output message
output = ""

# Manually handle each month's end-of-month logic
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10:
    if day < 31:
        day += 1
    else:  # Last day of the month
        day = 1
        month += 1
elif month == 4 or month == 6 or month == 9 or month == 11:
    if day < 30:
        day += 1
    else:  # Last day of the month
        day = 1
        month += 1
elif month == 2:
    # Check for leap year
    if is_leap:
        if day < 29:
            day += 1
        else:  # Last day of February in a leap year
            day = 1
            month += 1
    else:  # Not a leap year
        if day < 28:
            day += 1
        else:
            day = 1
            month += 1
elif month == 12:
    if day < 31:
        day += 1
    else:  # Transition to the next year
        day = 1
        month = 1
        year += 1
else:
    output = "Invalid date provided."

# Prepare the output message if it's not set to "Invalid date provided."
if output == "":
    output = f"Next day's date: {day:02d}.{month:02d}.{year}"

# Print the output message
print(output)
