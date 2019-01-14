import sys

def writeToFile():
	try:
		f = open('testfile.txt', 'w')
		f.write("Hello World this is my first line\n")
		f.write("I am learning python\n")
		f.write("And I am loving it")
	finally:
		f.close()


def readFile():
	try:
		f = open('testfil.txt', 'r')
		for line in f:
			print(line)
	except:
		print("Exception can be caught")
		print(sys.exc_info()[0])
	

writeToFile()
readFile()





