# Input: Tax brackets and size of the amount from the user
a = int(input("Enter the lower limit of the tax bracket: "))
b = int(input("Enter the middle limit of the tax bracket: "))
c = int(input("Enter the upper limit of the tax bracket: "))
s = int(input("Enter the size of the amount: "))

# Initialize a variable for the tax amount
tax = 0

# Determine the tax based on the amount
if s <= a:
    tax = 0
elif a < s <= b:
    tax = s * 0.1
elif b < s <= c:
    tax = s * 0.25
else:
    tax = s * 0.5

# Prepare the output message
output = f"The tax calculated from the amount is {tax:.2f}"

# Print the output message
print(output)
