from collections import deque

def reverseKElements(queue, k):
	size = len(queue)
	if(k > size):
		print("Cannot perform action.")
	else:
		stack = []
		cnt = 0
		while(cnt != k):
			stack.append(queue.popleft())
			cnt += 1

		while(stack):
			queue.append(stack.pop())

		cnt = 0
		
		while(cnt != (size-k)):
			element = queue.popleft()
			queue.append(element)
			cnt += 1


	print(queue)



queue = deque([1,2,3,4,5])
reverseKElements(queue, 4)