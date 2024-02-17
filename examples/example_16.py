# Input: Coordinates of a point (x, y)
x = float(input("Enter the x coordinate of the point: "))
y = float(input("Enter the y coordinate of the point: "))

# Determine the coordinate quarter
if x > 0 and y > 0:
    output = "I"
elif x < 0 and y > 0:
    output = "II"
elif x < 0 and y < 0:
    output = "III"
elif x > 0 and y < 0:
    output = "IV"
elif x == 0 and y == 0:
    output = "The point is at the origin"
else:
    output = "The point lies on an axis, not strictly in a quarter"

# Print the output message
print(output)
