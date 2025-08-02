"""
Strings in python can be enclosed in single, double or triple quotes
If there are characters like ', ", or \ within a string, they can be retained in two ways:
Escape them by preceding them with a \.
Prepend the string with r, therefore, indicating that it is a raw string.



"""


message = r"If string in python contains \ or single quote ' or double quote \" "
print(message)


word = "Bamboozled"
print(word[0:]) #Prints the entire word
print(word[1:3]) #Prints the substring from char at index 1 to index 3-1 i.e. 2, Output: am
print(word[:-5])


#Slicing Operations
print(word[::-1]) #Should reverse the word, Output: delzoobmaB

#Built-In Functions
"""
len() - Returns the length of string. Used as len("This is a sample string")
min() - Used to get the character with min value. Ex: min('Surreal') -> S
max() - Used to get the character with max value. Ex: max('Surreal') -> u
upper() - Converts string to uppercase
lower() - Converts string to lowercase
capitalize() - Converts the first character of a string to uppercase
title() - Converts the first character of each word to uppercase
swapcase() - Swaps cases in string

str() - Converts an int, float, complex to a string
chr(<int>) - Returns the unicode value of string, ord(<char>) - Does the reverse, given a character returns the int

str.isalpha() - Used to determine if string is all aplhabets
str.isdigit() - Used to determine if string is all digits
str.isalnum() - Used to determine if srtring is alphanumeric
str.islower() - Checks if all characters within the string are lowercase
str.isupper() - Checks if all characters within the string are uppercase

str.startsWith('And') - Checks if string starts with provided string
str.endsWith('And') - Checks if string ends with provided string

str.find('It') - Find the occurence of character
str.replace('It', 'Him') - replace the occurence of 'It' with 'Him'

str.lstrip() - Used to trim the left hand white spaces
str.rstrip() -Used to trim the white spaces on right hand side
str.strip() - Strips the white spaces on both the sides

str.split('DELIMITER') - Splits the string based on the delimiter
str.partition('DELIMITER') - Partition the string into part before the DELIMITER, the DELIMITER itself and the part after the DELIMITER

str.replace('l','L',<Count of Occurences>) - Replaces all occurences of l with L

"""
print("Length of word: ",word," is: ",len(word))

poem_line = 'And Quiet Flows The Don'

print(poem_line.isalpha(), type(poem_line))


print(chr(65), ord('A'))


s1 = "He said, \"Let Us Python\""
s2 = r'He said "Let Us Python"'
print(s1, s2)

s3 = 'C\\Users\\Kanetkar\\Documents'
print(s3.split('\\'))
print(s3.partition('\\'))

s4 = '   Flanked on both sides    '
print(s4.strip())





