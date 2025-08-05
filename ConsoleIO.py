
#Single input from console
fullname = input('Enter your full name: ')
print('Entered name is: ', fullname)

#Multipl inputs from console
fname, mname, lname = input('Enter first name, middle and last name: ').split()
print('Constructed full name is: ', fname, mname, lname)

#The input received from input() function is always string so for numeric input we
#need to convert it to a number using int() or relevant type conversion
sides_of_triangle = [int(x) for x in input('Enter three sides of a triange: ').split()]
print(sides_of_triangle)

length, breadth = input('Enter the length and breadth of rectangle: ').split()
area_of_rectangle = int(length) * int(breadth)
print('The area of a rectangle is: ', area_of_rectangle)


###################################################################################

"""
print(objects, sep = ' ', end = '\n', file = sys.stdout, flush = False)
This means that, by default, objects will be printed on screen (sys.stdout), separated by a space (sep = ' '), and the last printed object will be followed by a newline (end = '\n'). In the code snippet above, flush = False indicates that the output stream will not be flushed.
"""
r, l, b = 1.5678, 10.5, 12.66
print(f'radius = {r}') #format using string literals (preferred style)
print(f'length = {l} breadth = {b} radius = {r}')