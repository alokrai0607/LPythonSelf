# Edit file (r+)
f = open(r"C:\Users\91904\OneDrive\Desktop\LPythonSelf\PythonSeries\Day7_FileIO\Override\newt.txt", "r+")
f.write("shiv")
print(f.read())
f.close()


# Truncate (w+)
f = open(r"C:\Users\91904\OneDrive\Desktop\LPythonSelf\PythonSeries\Day7_FileIO\Override\newt.txt", "w+")
f.write("shiv")
print(f.read())
f.close()

