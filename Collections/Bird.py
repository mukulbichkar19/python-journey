#Parent Class
class Bird:
	def __init__(self):
		print('Bird is ready')

	def whoisThis(self):
		print('Bird')

	def swim(self):
		print('Swim faster')


#Child class
class Penguin(Bird):
	def __init__(self):
		super().__init__() #Calls parent class constructor
		print("Penguin is ready")

	def whoisThis(self):
		print('Penguin')

	def run(self):
		print("run faster")


peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()
