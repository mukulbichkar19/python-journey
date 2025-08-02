"""
Data Type conversion is possible in python and is achieved using the following functions:
int(float/numeric string)     # from float/numeric string to int
int(numeric string, base)     # from numeric string to int in base
float(int/numeric string)     # from int/numeric string to float
float(int)                    # from int to float
complex(int/float)            # convert to complex with imaginary part 0
complex(int/float, int/float) # convert to complex
bool(int/float)               # from int/float to True/False (1/0)
str(int/float/bool)           # converts to a string
chr(int)                      # yields character corresponding to int
"""



"""
There are a few built-in functions in python
abs(x)         # returns absolute value of x
pow(x, y)      # returns value of x raised to y 
min(x1, x2,...)# returns smallest argument
max(x1, x2,...)# returns largest argument 
divmod(x, y)   # returns a pair(x // y,x % y)
round(x [,n])  # returns x rounded to n digits after . 
bin(x)         # returns binary equivalent of x
oct(x)         # returns octal equivalent of x
hex(x)         # returns hexadecimal equivalent of x
"""

a = abs(-3)                # assigns 3 to a
print(a)
print(min(10, 20, 30, 40)) # prints 10
print(max(10, 20, 40, 50)) # prints 50
print(hex(26))             # prints 1a
print(pow(2, 4))           # prints 16
print(divmod(17, 3))       # Quotient 5, Remainder 2
print(bin(64), oct(64), hex(64))
print(round(2.567), round(2.5678, 2))