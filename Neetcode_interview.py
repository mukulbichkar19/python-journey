# Looping from i = 5 to i = 2
for i in range(5, 1, -1):
    print(i)


# Modding is similar to most languages
print(10 % 3)

# Except for negative values
print(-10 % 3)

# To be consistent with other languages modulo
import math
print(math.fmod(-10, 3))

#More math helpers
print(math.floor(3/2))
print(math.ceil(3/2))
print(math.sqrt(2))
print(math.pow(2,4))

# Declaring max/min Int
float("inf")
float("-inf")
print(float("inf"), float("-inf"))

# But still less than infinity
print(math.pow(2, 200) < float("inf"))

#Containers

#Lists
arr = [1] * 5
print(arr)

# Loop through multiple arrays simultaneously with unpacking
nums1 = [1, 3, 5]
nums2 = [2, 4, 6]
for n1, n2 in zip(nums1, nums2):
    print(n1, n2)

nums = [11,2,30,49,51]
nums.reverse()
print(nums)

nums.sort()
print(nums)

nums.sort(reverse=True)
print(nums)

names = ["bob", "alice", "jabe", "doe"]
names.sort()
print('Names sorted in ascending order: ' ,names)
names.sort(reverse=True)
print('Names sorted in descending order: ' ,names)

names.sort(key=lambda x:len(x))
print('Names sorted based on length of names: ' ,names)

# List Comprehensions
arr = [i for i in range(5)]
print(arr)

arr = [[0] * 5 for i in range(3)] #Initialize 2-D array
print(arr)

# For Queue we use the dequeue 
from collections import deque
q = deque()
q.append(45)
q.append(20)

print(q)

q.popleft()
print(q)

# HashMap (Dict)
myMap = {}
myMap["alice"] = 99
myMap["bob"] = 102

for k,v in myMap.items():
    print(k, v)

#Heaps (Use arrays under the hood)
import heapq
minheap = []
print('Pushing to heap')
heapq.heappush(minheap, 3)
heapq.heappush(minheap, 10)
heapq.heappush(minheap, 12)

print('Popping from heap')
while len(minheap):
    print(heapq.heappop(minheap))

# Max Heap does not exists 
# To make it work before pushing the value we multiply it with -1
# and on popping we multiply with -1 again.
maxHeap = []
heapq.heappush(maxHeap, -20)
heapq.heappush(maxHeap, -10)
heapq.heappush(maxHeap, -35)
print('After Popping from heap')
while len(maxHeap):
    print(heapq.heappop(maxHeap) * -1)

# We can build a heap from array using heapify method
arr = [2,1,6,7,80]
heapq.heapify(arr)
print('Poppping elements from max heap after heapifying:')
while len(arr):
    print(heapq.heappop(arr))

arr = [2,1,6,7,80]
arr = [arr[i] * -1 for i in range(len(arr))]
heapq.heapify(arr)
print('Popping from max heap after heapifying: ')
while len(arr):
    print(heapq.heappop(arr) * -1)

# List Comprehension Trial (Used for filtering, mapping and transforming)
nums = [1,2,3,4,5,6,7,8]
squared = [num**2 for num in nums]
print('Squared Numbers: ', squared)

word = "interview"
unqiue_chars = {w for w in word}
print('Unique characters: ', unqiue_chars)

input_word = "banana"
char_count_map = {w:input_word.count(w) for w in set(input_word)}
print('Char Frequency map: ', char_count_map)


charMap = {}
for w in input_word:
    charMap[w] = charMap.get(w, 0) + 1
print('CharMap similar to Java: ', charMap)

# Most efficient way to get a character counter dictionary
from collections import Counter
charMap2 = Counter(input_word)
print('Using in-built Counter', charMap2)
for k,v in charMap2.items():
    print(k,' :: ', v)

# Creating Adjacency List from Edges
edges = [(0,1),(0,2),(1,2),(2,3)]
adj = {i:[] for i in range(0,len(edges))}
for u,v in edges:
    adj[u].append(v)
    adj[v].append(u)
print('After populating: ', adj)