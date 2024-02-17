# Read a text file in Python
file_path = "C:\\Users\\91904\\OneDrive\\Desktop\\LPythonSelf\\PythonSeries\\Day7_FileIO\\file_IO\\newfile.txt" # Replace with the path to your text file
with open(file_path, "r") as file:
    content = file.read()

print(content)
