# ex33_func.py

# turned the previous hard coded exercise into a function with user input request

def iterate(num_var):
	
	i = 0
	numbers = []
	while i < num_var:
		print(f"At the top i is {i}")
		numbers.append(i)
		i = i + 1
	print("Numbers now: ", numbers)
	print(f"At the bottom i is {i}")
	print("The numbers: ")
	for num in numbers:
		print(num)
	

print("Please input a number to iterate. ")
num_var = int(input())

iterate(num_var)