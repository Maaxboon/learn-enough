""" Tasks
Create a Python script named name_tag_processor.py in the /home/labex/project directory. (Recommend to use WebIDE)
Use the input() function to prompt the user to enter an astronaut's full name.
Process the entered name to create a standardized name tag by performing the following operations:
Convert the full name to uppercase.
Replace any spaces with underscores.
Add the prefix "ASTRONAUT_" to the beginning of the processed name.
Print the original name and the processed name tag.
Requirements
The script must be named name_tag_processor.py and located in the /home/labex/project directory.
Use appropriate string methods as learned in the lab, such as upper() and replace(). You can get more information about string methods in the Python documentation.
The script should run without any errors and prompt the user for input.
The output should display both the original name and the processed name tag. """


# Step 1: Prompt the user for input
name = str(input("Hello astronaut! Enter your name: "))

# Step 2: Convert input name to upper case
case_name = name.upper()

# Step 3: Replace spaces with underscores
tag_name = case_name.replace(" ","_")

# Step 4: Create the final standardized name tag
standardized_tag = f"ASTRONAUT_{tag_name}"

print(f"Original name: {name}")
print(f"Processed name tag: {standardized_tag}")