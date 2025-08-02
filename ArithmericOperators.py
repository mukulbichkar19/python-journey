""" Different types of arithmetic operators in python are:
+ - Addition
- -Subtraction
* - Multiplication
/ - Division
% - Remainder, Evaluated using a - (b *  (a//b))
// - Floor Division (Returns the quotient which is less than or equal to the actual quotient)
** - Exponential
"""

print(10 // 3)     # yields 3
print(-10 // 3)    # yields -4
print(10 // -3)    # yields -4
print(-10 // -3)   # yields 3
print(3 // 10)     # yields 0
print(3 // -10)    # yields -1
print(-3 // 10)    # yields -1
print(-3 // -10)   # yields 0

print("Evaluating % Operator")
print(10 % 3)    # yields 1
print(-10 % 3)   # yields 2
print(10 % -3)   # yields -2
print(-10 % -3)  # yields -1
print(3 % 10)    # yields 3
print(3 % -10)   # yields -7
print(-3 % 10)   # yields 7
print(-3 % -10)  # yields -3


"""
Precendence of Operators follow the PEMDAS rule
()          # Parentheses
**          # Exponentiation
*, /, //, % # Multiplication, Division (Associativity from left to right)
+, -        # Addition, Subtraction
"""

print("2 + 4 * 5 =", 2 + 4 * 5)     # prints 22
print("(2 + 4) * 5 =", (2 + 4) * 5) # prints 30
print("20 / 2 ** 3 =",20 / 2 ** 3)  # prints 2.5
