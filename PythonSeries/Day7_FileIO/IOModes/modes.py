
#With Syanax
# Opening a file in exclusive creation mode for writing
with open(r'C:\Users\91904\OneDrive\Desktop\LPythonSelf\PythonSeries\Day7_FileIO\IOModes\file.txt', 'x') as f:
    f.write('This file was created exclusively.')

# Writing to a file in text mode
with open('file.txt', 'w') as f:
    f.write('Hello, world!')


# Reading a file in text mode
with open('file.txt', 'r') as f:
    content = f.read()

# Appending to a file in text mode
with open('file.txt', 'a') as f:
    f.write('\nThis is a new line.')

# Opening a file in binary mode for reading
with open('file.bin', 'rb') as f:
    content = f.read()

# Opening a file in binary mode for writing
with open('file.bin', 'wb') as f:
    f.write(b'This is a binary file.')

# Opening a file in binary mode for appending
with open('file.bin', 'ab') as f:
    f.write(b'\nThis is a new binary line.')



# Reading and writing to a file in text mode
with open('file.txt', 'r+') as f:
    content = f.read()
    f.write('\nThis is a new line.')

# Writing to a file in text mode and reading from it
with open('file.txt', 'w+') as f:
    f.write('Hello, world!')
    f.seek(0)
    content = f.read()

# Appending to a file in text mode and reading from it
with open('file.txt', 'a+') as f:
    f.write('\nThis is a new line.')
    f.seek(0)
    content = f.read()

# Opening a file in text mode for exclusive creation
with open('file.txt', 'xt') as f:
    f.write('This file was created exclusively.')

# Opening a file in universal newline mode
with open('file.txt', 'rU') as f:
    content = f.read()

# Opening a file in update mode
with open('file.txt', 'r+b') as f:
    content = f.read()
    f.seek(0)
    f.write(b'This is a new line.')

# Opening a file in binary mode for reading and writing
with open('file.bin', 'rb+') as f:
    content = f.read()
    f.seek(0)
    f.write(b'This is a new binary line.')    