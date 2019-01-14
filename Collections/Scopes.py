import sys, math
isuniversal = 90 #Anything defined in global scope is global

#Any variable defined within the function scope/local scope is a local variable

def foo():
	x = "local here"
	global isuniversal
	print("Inside function foo() isuniversal: ")
	print(isuniversal)
	print("Locally the value of isuniversal is: ")
	print(x)

def bar():
	y = 76

	def barr():
		global y #global keyword can be used to make a variable global inside a function
		y = 80

	print("Before calling barr: ", y)
	barr()
	print("After calling barr: ", y)


bar()
print("y in main: ", y)
foo()
print("Outside the function foo() isuniversal: ")
print(isuniversal)
print("The value of math pi: ")
print(math.pi)
print("max value: ")
print(sys.maxsize)
print("min value: ")
print(-sys.maxsize-1)
print(math.pow(2,63))
#print(dir(math))