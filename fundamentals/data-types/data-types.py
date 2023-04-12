# Data types

# string
name = 'Matthew'

# `isInstance(a, b)` compares whether the variable 'a' is the type of data declared as parameter 'b'
print(f'Is {name} a string? {isinstance(name, str)}')

# integer
age = 2
print(f'is {age} an integer? {isinstance(age, int)}')

# float
decimal = 2.2
print(f'is {decimal} a float? {isinstance(decimal, float)}')

# can place `int` in front of a string to transform into an integer
number = '24'
age2 = int(number)
print(type(age2))
