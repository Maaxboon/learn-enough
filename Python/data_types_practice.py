# Data types and operators practice

# Get user input
name = input("Enter your name: ")
age_str = input("Enter your age: ")
height_str = input("Enter your height in meters: ")

# Convert input to appropriate types
age = int(age_str)
height = float(height_str)

# Perform calculations
birth_year = 2024 - age
is_adult = age >= 18

# Create output string
output = f"""
Name: {name}
Age: {age}
Height: {height:.2f} meters
Birth Year: {birth_year}
Is Adult: {is_adult}
"""

# Print the result
print(output)

# Bonus: String manipulation
uppercase_name = name.upper()
name_length = len(name)

print(f"Your name in uppercase: {uppercase_name}")
print(f"Your name has {name_length} characters")
