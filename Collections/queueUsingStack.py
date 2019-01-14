class QueueUsingStack():

	stack1 = [];
	stack2 = [];

	def __init__(self):
		print("Inside QueueUsingStack constructor")
	

	def enqueue(self, value):
		self.stack1.append(value)

	def isEmpty(self, stack):
		if(len(stack) == 0):
			return True
		return False

	def deque(self):
		if(not self.isEmpty(self.stack1)):
			while(not self.isEmpty(self.stack1)):
				self.stack2.append(self.stack1.pop())

			dequed_element = self.stack2.pop()
			print(str(dequed_element) + " element was dequed")

			while(not self.isEmpty(self.stack2)):
				self.stack1.append(self.stack2.pop())
		else:
			print("Queue does not have sufficient elements to deque")

	def size(self):
		return len(self.stack)

	

	def printQueue(self):
		if(len(self.stack1) > 0):
			print(self.stack1)
		else:
			print("Queue is empty")



qs = QueueUsingStack()
qs.enqueue(1)
qs.enqueue(23)
qs.enqueue(90)
qs.enqueue(8)
qs.deque()
qs.printQueue()

"""
	enqueue(1)
	enqueue(23)
	enqueue(90)
	enqueue(8)

	queue => [1,23,90,8]

	deque() => [23,90,8]

	enqueue(100)

	queue => [23,90,8,100]


 Stack = []


"""
