# def cheese_and_crackers(cheese_count, boxes_of_crackers):
# 	print(f"You have {cheese_count} cheeses!")
# 	print(f"You have {boxes_of_crackers} boxes of crackers!")
# 	print("Man that is enough for a party!")
# 	print("Get a blanket.\n")


# print("We can just give the function numbers directly:")
# cheese_and_crackers(20, 30)


# print("OR, we can use variables from our script:")
# amount_of_cheese = 10
# amount_of_crackers = 50

# cheese_and_crackers(amount_of_cheese, amount_of_crackers)


# print("We can ever do math inside too:")
# cheese_and_crackers(10 + 20, 5 + 6)


# print("And we can combine the two, variables and math:")
# cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# def test_func(text1, number1):
# 	print("Enter some text...")
	
# 	print("Enter a number...")
	
# 	print(f"You entered {text1} and {number1}")

# prompt = " >"
# text1 = input(prompt)
# number1 = int(input(prompt))
# test_func()


def test_func():
	prompt = " >"
	print("Enter some text...")
	text1 = input(prompt)
	print("Enter a number...")
	number1 = int(input(prompt))
	print(f"You entered {text1} and {number1}")


# test_func()


# This doesn't work

def what_to_call(func_to_call):
	{func_to_call}()

print("Enter a func to call")
prompt = " >"
user_function = input(prompt)
what_to_call("{user_function}")






