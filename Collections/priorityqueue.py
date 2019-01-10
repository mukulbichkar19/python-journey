import heapq


pq = []

# Adding tuple's
heapq.heappush(pq, (1, 'leet'))
heapq.heappush(pq, (-1, 'code'))
heapq.heappush(pq, (4, 'lsd'))
heapq.heappush(pq, (2, 'cia'))

while pq:
	next_item = heapq.heappop(pq)
	print(next_item)

