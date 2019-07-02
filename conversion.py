list12 = ["1", "2"]
list34 = ["3", "4"]
# unit_type = 2
# if str(unit_type) in list12:
#     print("temp")

def conversion():
    """function to convert values conditionally
    if temp then C to F or F to C
    if length then feet to meters or meters to feet"""
    global unit_type
    def temp_convert():
        """function to convert temp"""
        global temp_out
        #if unit_type == "Celsius" 
        if unit_type == 1:
            temp_in = int(input("please enter a temp in Celsius "))
            temp_out = (5/9 * temp_in - 32)
        #if unit_type == "Fahrenheit"
        if unit_type == 2: 
            temp_in = int(input("please enter a temp in Fahreneit "))
            temp_out = (9/5 * temp_in + 32)
        print(temp_out)
    def length_convert():
        """function to convert temp"""
        global length_out
        if unit_type == 3:
        #if unit_type == "Meters"
            length_in = int(input("please enter a length in meters "))
            length_out = (3.281 * length_in)
        #if unit_type == "Feet"
        if unit_type == 4:
            length_in = int(input("please enter a length in feet"))
            length_out = (length_in/3.281)
        print(length_out)
    #ask for the type of conversion
    # unit_type = input("Please select a conversion type enter")
    unit_type = input("""Please select a conversion type enter 
    1 - Celsius 
    2 - Fahrenheit
    3 - Meters
    4 - Feet
    """)
    return unit_type
    #error check
    # list12 = [1, 2]
    # list34 = [3, 4]
    # print(list12)
    if str(unit_type) in list12:
        temp_convert()
        print("temp")
    elif str(unit_type) in list34:
        length_convert()
        print("length")
    else: 
        print("You've entered an incorrect value ") 

# list12 = [1, 2]
# list34 = [3, 4]

print(list12, list34)  
# print(unit_type) 
conversion()







