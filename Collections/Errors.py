class Error(Exception):
	""" Base class for other exceptions """
	pass

class ValueTooSmall(Error):
	""" Raised when the input value is too small """
	pass

class ValueTooLarge(Error):
	""" Raised when the value is too large """
	pass

number = 10

while True:
	try:
		user_input = int(input('Enter a value: '))
		if user_input < number:
			raise ValueTooSmall
		el		if(user_input > number):
			raise ValueTooLarge
		break
	except ValueTooSmall:
		print("The entered value is too small, try again\n")
	except ValueTooLarge:
		print("The entered value is too high, try again\n")

print("Congrats you have guessed it correctly")