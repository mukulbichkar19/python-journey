from collections import deque


queue = deque([])

queue.append(5)
queue.append(10)
queue.append(12)
queue.append(9)

print(queue)

queue.popleft()

print(queue)


# [1 2 3 4 5]
# [3 2 1 4 5]
# pop first k elements and add them in stack
# [3 2 1] 
# use intermediate queue and add stack elements to it and 
# also dequeu elements from queue to intermediate queue

