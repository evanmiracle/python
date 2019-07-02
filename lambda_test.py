# lambda function for filtering lists

x = [-5, 7, 9, -4, 2]
greater_than_zero = filter(lambda n: (n > 0), x)
print(list(greater_than_zero))