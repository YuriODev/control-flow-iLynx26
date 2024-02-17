# Input: Height (in meters) and mass (in kilograms)
height = float(input("Enter your height in meters: "))
mass = float(input("Enter your mass in kilograms: "))

# Calculate the Body Mass Index (BMI)
bmi = mass / (height ** 2)

# Categorize the BMI
if bmi < 18.5:
    output = f"Your body mass index is: {bmi:.2f}, that is underweight."
elif 18.5 <= bmi <= 24.9:
    output = f"Your body mass index is: {bmi:.2f}, that is normal weight."
elif bmi > 24.9:
    output = f"Your body mass index is: {bmi:.2f}, that is overweight."

# Print the output message
print(output)
