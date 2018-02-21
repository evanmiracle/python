# ex31

print("""You enter a dark room with two doors.
	Do you go through door #1 or door#2?""")


door = input("> ")

if door == "1":
	print("There's a giant bear here eating a cheese cake.")
	print("What do you do?")
	print("1.  Take the cake.")
	print("2.  Scream at the bear.")

	bear = input("> ")

	if bear == "1":
		print("The bear eats your face off.  Sorry :( ")
	elif bear == "2":
		pint("The bear eats your legs off.  sorry :( ")
	else:
		print(f"We doing {bear} is probably best.")
		print("The bear runs away.")

elif door =="2":
	print("You stare into the endless abyss at Cthulhu's retina.")
	print("1. blueberries.")
	print("2. yellow jacket clothespins")
	print("3. understanding revolvers yelling melodies")

	insanity = input("> ")

	if insanity == "1"	or insanity == "2":
		print("Jello is the beginning and ending")
		print("Good Job!")

	else:
		print("Insanity reigns supreme")
		print("Good Job!")

else:
	print("You enter the hypercube of doom, sorry :( ")




