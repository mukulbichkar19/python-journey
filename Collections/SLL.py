from ListNode import ListNode

class SLL:
	def isEmpty(head):
		if(head == None):
			return True
		return False

	def printSLL(head):
		temp = head
		while(temp):
			print(temp.val)
			temp = temp.next 
		print("None")

	def insertAtHead(head, val):
		newNode = ListNode(val)
		newNode.next = head
		head = newNode
		return head

	def insertAtPos(head, val, pos):
		newNode = ListNode(val)
		count = 1
		temp = head
		while(temp and count != pos-1):
			count += 1
			temp = temp.next
	
		if(temp):
			newNode.next = temp.next
			temp.next = newNode
		return head

	def append(head, val):
		temp = head
		while(temp.next):
			temp = temp.next
		temp.next = ListNode(val)
		return head

	def search(head, val):
		if(head == None):
			return -1
		pos = 1
		temp = head
		while(temp):
			if(temp.val == val):
				return pos
			pos += 1
			temp = temp.next
		return 0

	def deleteAtHead(head):
		if(head != None):
			return head.next

	def deleteByValue(head, val):
		if(head == None):
			return head
		if(head.val == val):
			head = head.next

		temp = head

		while(temp.next):
			if(temp.next != None and temp.next.val == val):
				temp.next = temp.next.next
			else:
				temp = temp.next
		return head

	def length(head):
		temp = head
		size = 0
		while(temp):
			temp = temp.next
			size += 1
		return size

	def removeDuplicates(head):
		visited = set([])
		temp = head
		while(temp):
			visited.add(temp.val)
			while(temp and temp.next and (temp.next.val in visited)):
				temp.next = temp.next.next
			temp = temp.next
		return head

	def getNNodeFromEnd(head, n):
		"""
		# Approach 1: Using 2 iterations
		size = 0
		t = head
		while(t):
			t = t.next
			size += 1
		temp = head
		cnt = 0
		while(cnt != (size-n)):
			temp = temp.next
			cnt += 1
		return temp"""
		ptr1 = ptr2 = head
		# Set the diff between ptr1 and ptr2 equal to n
		diff = 0
		while(ptr2 and diff != n):
			ptr2 = ptr2.next
			diff += 1
		
		while(ptr2):
			ptr2 = ptr2.next
			ptr1 = ptr1.next

		return ptr1

	head = ListNode(45)
	node1 = ListNode(5)
	node2 = ListNode(2)
	node3 = ListNode(13)
	node4 = ListNode(11)
	node5 = ListNode(9)

	head.next = node1
	node1.next = node2
	node2.next = node3
	node3.next = node4
	node4.next = node5

	#head = insertAtHead(head, 110)
	#head = insertAtPos(head, 190, 3)
	#head = append(head, 78)
	#print(search(head, 78))
	#printSLL(head)
	#head = deleteAtHead(head)
	#head = deleteByValue(head, 90)
	#printSLL(head)
	#print(length(head))
	#print("Before Removing Duplicates: ")
	#printSLL(head)
	#removeDuplicates(head)
	#print("After Removing Duplicates: ")
	#printSLL(head)
	#print(length(head))
	print(getNNodeFromEnd(head, 2).val)















