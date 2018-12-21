from collections import deque

class Queue(object):
    def __init__(self):
        this.self = self


# Use deque for implementing queue as it is more efficient than lists append and
# pop operations
queue = deque([])

# Similar to insert in queue is append
queue.append("I")
queue.append("came")
queue.append("in")
queue.append("first")

print(queue)

# Similar to remove in queue
queue.popleft()

print(queue)

print("The size of queue is: ")
print(len(queue))
