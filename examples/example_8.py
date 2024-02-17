# Input: Decimal number from the user
decimal = int(input("Enter a decimal number (1-10): "))

# Initialize an empty string for the output message
output = ""

# Conditional statements to convert decimal number to Roman numeral
if decimal == 1:
    output = "I"
elif decimal == 2:
    output = "II"
elif decimal == 3:
    output = "III"
elif decimal == 4:
    output = "IV"
elif decimal == 5:
    output = "V"
elif decimal == 6:
    output = "VI"
elif decimal == 7:
    output = "VII"
elif decimal == 8:
    output = "VIII"
elif decimal == 9:
    output = "IX"
elif decimal == 10:
    output = "X"
else:
    output = "Invalid number"

# Print the output message
print(output)
