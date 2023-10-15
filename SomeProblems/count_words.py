def count_words(input_file, output_file):
    try:
        with open(input_file, 'r') as f:
            content = f.read()

        word_count = len(content.split())

        with open(output_file, 'w') as f:
            f.write(f"Number of words: {word_count}")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"Error: {e}")

# Input
input_file_name = "input.txt"
output_file_name = "output.txt"

# Output
count_words(input_file_name, output_file_name)
