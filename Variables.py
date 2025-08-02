"""
Different type of variables in python are as follows
Basic Types
int - No limit and does not cause underflow/overflow
float - 64-bit double precision values and maximum of 1.8*10^308. Greater than this is represented as inf
complex - It contains real and imaginary parts
bool - True/False
str - Used to represent string.
bytes - Represents binary data

"""
value = 3
temperature = 36.3
first_name = 'Ram'

print(type(value))
print(type(temperature))
print(type(first_name))

#Multiple assignments
a = 5;b=10;c=150
d = e = f = 0
print(a,b,c)
print(d,e,f)

"""
Container Types: list, tuple, set, dictionary
A list is an indexed collection of similar/dissimilar entities
A tuple is an immutable collection
A set is a collection of unique values
A dictionary is a collection of key-value pairs, with unique keys enclosed in ' '

String: Ordered collection, immutable and iterable.
List: Ordered collection, mutable and iterable.
Tuple: Ordered collection, immutable and iterable.
Set: Unordered collection, mutable and iterable.
Dictionary: Unordered collection, mutable and iterable.
"""
lst = [10, 20, 30, 20, 30, 40, 50, 10]
tpl = ('Let Us Python', 350, 195.00)
s = {10, 20, 30, 40}
dct = {'ME101' : 'SOM', 'EE101' : 'Electronics'}
print(lst[0], tpl[2]) # prints 10 195.0
print(dct['ME101']) # prints SOM





