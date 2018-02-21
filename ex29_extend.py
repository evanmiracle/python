# ex29 extended  to include user input
print("How many people? Input a number and press enter.")
people = int(input())
print("How many cats? Input a number and press enter.")
cats = int(input())
print("How many dogs? Input a number and press enter.")
dogs = int(input())

if people < cats:
	print("Too many cats!")

if people > cats:
	print("Not many cats!")

if people < dogs:
	print("The world is drooled on")

if people > dogs:
	print("The world is dry")


print(f"How many more dogs? There are currently {dogs} dogs.  Input a number and press enter")
more_dogs = int(input())
dogs += more_dogs


if people >= dogs:
	print("People are greater than or equal to dogs")


if people <= dogs:
	print("People are less than or equal to dogs")

if people == dogs:
	print("People are dogs")


