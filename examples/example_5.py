# Input: Student's test score
score = int(input("Enter the test score: "))

# Initialize an empty string for the output message
output = ""

# Conditional statements to determine the grade
if score >= 90:
    output = "Your grade is A."
elif score >= 80:
    output = "Your grade is B."
elif score >= 70:
    output = "Your grade is C."
elif score >= 60:
    output = "Your grade is D."
else:
    output = "Your grade is F."

# Print the output message
print(output)
