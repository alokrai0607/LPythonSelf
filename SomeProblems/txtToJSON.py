import json

def text_to_json(text_data):
    # Split text data into lines
    lines = text_data.strip().split('\n')
    
    # Extract key-value pairs from each line
    json_data = {}
    for line in lines:
        key, value = line.split(':', 1)
        json_data[key.strip()] = value.strip()
    
    return json.dumps(json_data, indent=4)

# Example usage
text_data = """
name: John Doe
age: 30
city: New York
email: johndoe@example.com
"""

json_output = text_to_json(text_data)
print(json_output)
