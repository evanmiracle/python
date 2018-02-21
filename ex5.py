my_name = 'Evan Miracle'
my_age = 40 #comment
my_height = 72 #inches
my_weight = 160 # lbs
my_eyes = 'brown'
my_teeth = 'white'
my_hair = 'brown'

# this works in python 3.51
print("Test %s" % my_name)

# the code below only works in 3.6 or later 
print(f'Lets talk about {my_name}.')
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")

print(f"His teeth are usually {my_teeth} depending on coffee.")

total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")

# code for earlier versions of python
print('Lets talk about %s' % my_name)
print("He's %s inches tall." % my_height)
print("He's %s pounds heavy." % my_weight)
print("Actually that's not too heavy.")

# multples seem only to work when explicit
print("He's got" , my_eyes, "eyes and",my_hair, "hair.")

# This should work too 
print("He's got %s eyes and %s hair." %(my_eyes, my_hair) )

print("His teeth are usually %s depending on coffee." % my_teeth)

total = my_age + my_height + my_weight
print("If I add", my_age, my_height, my_weight, "I get", total)
