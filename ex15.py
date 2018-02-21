from sys import argv

script, filename = argv

txt = open(filename)

# open command takes a parameter and returns a variable value (opens the file you specify)

print(f"Here's your file {filename}:")
print(txt.read())

# call the read function on txt.  Give a file a command with . name of command and any parameters

print("Type the file name again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

txt.close()
txt_again.close()


