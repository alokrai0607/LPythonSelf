
# f = open("demo.txt", "r")
# data = f.read()
# print(data)

try:
    f = open("PythonSeries\Day7_FileIO\demo.txt" , "r")
    # Perform operations on the file
    f.close()
except FileNotFoundError:
    print("The file 'demo.txt' does not exist or could not be found.")

