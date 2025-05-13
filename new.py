# Open the original file for reading
with open("demofile.txt", "r") as file:
    content = file.read()

# Make the replacements
content = content.replace("testing purposes", "tested")
content = content.replace("Good Luck!", "Bad Luck!")
content = content.replace("demofile.txt", "newdemo.txt")

# Write the modified content to a new file
with open("newdemo.txt", "w") as new_file:
    new_file.write(content)

# Print the result
print("Modified content:\n")
print(content)

