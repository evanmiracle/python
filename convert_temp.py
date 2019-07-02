def convert_temp():
	""" work in progress Function to convert temperature 
	asks for Temperature to convert and Units
	"""
	# temp = int(input("What temp? "))
	temp = float(input("What temp? "))
	temp_type = type(temp)
	# int_type = type(100)
	float_type = type(100.0)
	if temp_type == int_type:
		print(temp)
	else:
		print("not a number")
	units = str(input("What units? (Celsius, Fahrenheit, or Kelvin)"))

convert_temp()