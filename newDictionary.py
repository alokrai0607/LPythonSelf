sample = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New York"
}

keys_to_extract = ["name", "salary"]

new = {key: sample[key] for key in keys_to_extract}

print(new)
