# from sys import argv

# script, first, second, third = argv

# print("The script is called:", script)
# print("Your first varible is:", first)
# print("Your second variable is:", second)
# print("Your third variable is called:", third)

# to run the script type python ./ex13.py and three arguments for 1st-3rd

from sys import argv

script, second, third = argv
first = input("What is your first variable? ")

# can't seem to nest these two the input variable if on its own line works as you'd want it to
print("The script is called:", script)
print("Your first varible is:", first)
print("Your second variable is:", second)
print("Your third variable is called:", third)

# to run the script type python ./ex13.py and two arguments for 2nd and 3rd you will be prompted for the 1st


