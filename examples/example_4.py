# Input: Initial speed of the spacecraft in km/s
v = float(input("Enter the spacecraft's initial speed in km/s: "))

# Initialize an empty string for the output message
output = ""

# Conditional statements to determine the spacecraft's trajectory
if v < 7.8:
    output = "The device will fall to the Earth's surface."
elif 7.8 <= v < 11.2:
    output = "The device will become a satellite of the Earth."
elif 11.2 <= v < 16.4:
    output = "The device will become a satellite of the Sun."
else:
    output = "The device will leave the Solar System."

# Print the output message
print(output)