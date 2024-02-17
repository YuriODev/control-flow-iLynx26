# Input: Coordinates of point A (x, y) and the circle's radius r
x = float(input("Enter the x coordinate of point A: "))
y = float(input("Enter the y coordinate of point A: "))
r = float(input("Enter the radius of the circle: "))

# Determine whether the point belongs to the circle centered at the origin
if x**2 + y**2 <= r**2:
    output = "The point belongs to the circle"
else:
    output = "The point is outside the circle"

# Print the output message
print(output)
