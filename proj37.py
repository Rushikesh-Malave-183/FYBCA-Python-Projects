# Writing to a file
file = open('output.txt', 'w')
file.write("Hello, this is sample text written to a file.")

# Reading from a file
file = open('output.txt', 'r')
print("Content of the file:\n", file.read())
