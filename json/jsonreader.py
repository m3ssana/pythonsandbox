import json

# Open the JSON file and load its contents
with open('people.json', 'r') as f:
    data = json.load(f)

# Print the contents in a readable format
print(json.dumps(data, indent=4))
