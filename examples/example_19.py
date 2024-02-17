# Input: Three sides of a triangle
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

# Initialize the output variable
output = ""

# Check for triangle impossibility first
if a + b <= c or a + c <= b or b + c <= a:
    output = "impossible"
else:
    # Use the squares of the sides to determine the triangle type without sorting
    a2, b2, c2 = a**2, b**2, c**2
    if a2 + b2 == c2 or a2 + c2 == b2 or b2 + c2 == a2:
        output = "rectangular"
    elif a2 + b2 > c2 and a2 + c2 > b2 and b2 + c2 > a2:
        output = "acute"
    else:
        output = "obtuse"

# Print the output message
print(output)
