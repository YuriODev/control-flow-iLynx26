# Input: Number of working hours and hourly rate from the user
hours_worked = int(input("Enter the number of hours worked: "))
hourly_rate = float(input("Enter the hourly rate: "))

# Initialize the pay variable
pay = 0

# Calculate pay with overtime
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    pay = (40 * hourly_rate) + (overtime_hours * hourly_rate * 1.5)
else:
    pay = hours_worked * hourly_rate

# Prepare the output message
output = f"The total pay is {pay:.2f}"

# Print the output message
print(output)
