class Employee:

	def __init__(self, name, age):
		self.name = name
		self.age = age
		self.__salary = 90000

	def printEmpInfo(self):
		print(self.name, self.age, self.__salary)

	def setSalary(self, salary):
		self.__salary = salary

e = Employee('Aby', 22)
e.setSalary(78000)
e.__salary = 8000
e.printEmpInfo()

del e

#print(e)


