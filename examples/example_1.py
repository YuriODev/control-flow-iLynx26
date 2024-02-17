# Input: Temperature value from the user
temperature = float(input("Enter temperature in degrees Celsius: "))

# Initialize an empty string for the output message
output = ""

# Conditional statements to check the temperature and assign appropriate messages
if temperature <= 0:
    output = "A cold, isn't it?"
elif temperature > 0 and temperature < 10:
    output = "Cool."
else:
    output = "Nice weather we're having."

# Print the output message
print(output)