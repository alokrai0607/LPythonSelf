
# f = open("demo.txt", "r")
# data = f.read()
# print(data)



try:
    f = open("demo.txt" , "r+t")
    # Perform operations on the file
    f.close()
except FileNotFoundError:
    print("The file 'demo.txt' does not exist or could not be found.")

