try:
    f = open("newfile.txt", "r")
    # Perform operations on the file
    f.close()
except FileNotFoundError:
    print("The file 'newfile.txt' does not exist or could not be found.")