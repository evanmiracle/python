print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

print("Let's play a number guessing game . . .")
print("Guess a number . . . (type the number character only like 7)", end=' ')
x = int(input())
print(f"You guessed {x}")
