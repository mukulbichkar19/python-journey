#To check if the list is empty
lst = []
if not lst:
    print('Input list is empty base case')
else:
    print('Operate on the list')

"""
In-Built Functions in List
len(lst) # return number of items in the list
max(lst) # return maximum element in the list
min(lst) # return minimum element in the list
sum(lst) # return sum of all elements in the list
any(lst) # return True if any element of lst is True
all(lst) # return True if all elements of lst are True
del( )   # deletes element or slice or entire list
sorted(lst) # return sorted list, lst remains unchanged
sorted(lst, reverse=True) # return sorted list in reverse order
reversed(lst)# used for reversing lst

The sorted() function returns a new sorted list and keeps the original list unchanged. Also, the reversed() function returns a list_reverseiterator object, which has to be converted into a list using the list() function to get a reversed list.
"""
sample = [20,30,11,12,40,50]
print('Reversed Sample: ', sample[::-1])
print(sorted(sample, reverse=True))

lst1 = [1,2,3]
lst2 = [4,5]
lst2 = []
print('Combined List: ',lst1+lst2)


"""
lst.append(x) # append element x to the list
lst.remove(x) # removes element x from the list
lst.index(x) # returns the index of x from the list
lst.pop() # removes last item in list
lst.pop(x) # removes the x item in list
lst.insert(index, value) # insert value in index position
lst.count(x) # counts the occurence of x in the list
lst.reverse() # reverse the list
lst.sort() # sorts the list in natural order i.e. ascending order
lst.sort(reverse=True) # sorts the list in opposite of natural order i.e. descending order
"""

#Implementing Stack data structure

stack = []
stack.append(12)
stack.append(22)
stack.append(45)

print('After appending elements to stack: ',stack)

stack.pop()
stack.pop()
print('After popping elements from stack: ', stack)

#Implementing queue data structure (Cannot use list so use Deque from collections)
from collections import deque

q = deque()
q.append(12)
q.append(14)
q.append(15)

print('Queue after enqueue operation', q)

q.popleft()
q.popleft()
print('Queue after dequeue operation: ', q)
q.popleft()
print('Size of queue after removing all elements: ',len(q))

"""
Tuples are immutable, ordered collection of objects.
They can be used wherever we have pairs of immutable objects 
like grid pairs, (x,y) co-ordinates, custom object that needs immutability
we should use tuples.
tuple.sort(key=lambda x: (x[0])) #Sort the tupe based on 0th element
Tuples cannot be modified so we don't have append, remove, pop functions on it
Iteration and other operations are similar to list.
"""
users_score = [("Alice", 30), ("Bob", 75), ("Rock", 11)]
users_score.sort(key=lambda x: (x[0]))
print(users_score)



s = {}
t = {1, 4, 5, 2, 3}
print(type(s), type(t))


