class Animal:
	def __init__(self, name, age, species):
		self.name = name
		self.age = age
		self.species = species

	def action(self):
		if(self.species == 'Canine'):
			print(self.name, " barks")
		elif(self.species == 'Birds'):
			print(self.name, " sings")
		else:
			print(self.name, "is a dumbo")


	def whoIsThis(self):
		self.action()

	def printObj(self):
		print(self.name, self.age, self.species)




dog = Animal("Sheru", 12, "Canine")

dog.whoIsThis()
#dog.printObj()
#dog.action()