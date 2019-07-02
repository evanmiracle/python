#oscillating random generated correction around zero

import numpy as np

offset = np.random.randint(-7, 7)
print(f"Starting position is {offset}")
while offset != 0 :
	if offset > 0 :
		correction = np.random.randint(1, 7)
		print(f"random subtraction correction . . . {correction}")
		offset = offset - correction
	else :
		correction = np.random.randint(1, 7)
		print(f"random addition correction . . . {correction}")
		offset = offset + correction
	print(offset)
