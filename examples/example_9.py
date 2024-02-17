# Input: Number of purchased software sets from the user
units = int(input("Enter the number of software sets purchased: "))

# Initialize variables for the discount percentage and cost per unit
cost_per_unit = 2700
discount_percentage = 0

# Determine the discount percentage based on the number of units
if 10 <= units <= 19:
    discount_percentage = 10
elif 20 <= units <= 49:
    discount_percentage = 20
elif 50 <= units <= 99:
    discount_percentage = 30
elif units >= 100:
    discount_percentage = 40

# Calculate total cost after discount
total_cost = units * cost_per_unit * (1 - discount_percentage / 100)

# Prepare the output message
output = f"The amount of discount is {discount_percentage}%, total amount of the purchase after the discount is £{total_cost:.2f}"

# Print the output message
print(output)
