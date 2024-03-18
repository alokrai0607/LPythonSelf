import json

def json_to_txt(json_data, output_file):
    # Load JSON data
    data = json.loads(json_data)

    # Open the output text file in write mode
    with open(output_file, 'w') as f:
        # Iterate over each key-value pair in the JSON data
        for key, value in data.items():
            # Write the key-value pair to the text file
            f.write(f"{key}: {value}\n")

# Example usage
json_data = '{"name": "John Doe", "age": 30, "city": "New York", "email": "johndoe@example.com"}'
output_file = "output.txt"
json_to_txt(json_data, output_file)
