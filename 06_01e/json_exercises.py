# Basic JSON Operations

# Import the json module
import json

# Load JSON data from a file
with open("data.json", "r") as file:
    data = json.load(file)

# Print the loaded JSON data
print(data)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York', 'skills': ['Python', 'SQL', 'Machine Learning']}

# Access and print specific values
print(data["name"])  # Output: Alice
print(data["skills"])  # Output: ['Python', 'SQL', 'Machine Learning']

# Modify the JSON data (update age, add a new skill)
data["age"] = 26
data["skills"].append("Data Analysis")

# Print updated data
print(
    data)  # Output: {'name': 'Alice', 'age': 26, 'city': 'New York', 'skills': ['Python', 'SQL', 'Machine Learning', 'Data Analysis']}

# Save the modified data back to the JSON file
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

# Verify changes by reloading the JSON file
with open("data.json", "r") as file:
    updated_data = json.load(file)

print(updated_data)  # Output should reflect the updated JSON content
