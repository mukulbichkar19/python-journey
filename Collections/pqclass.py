import heapq

class Skill(object):
	def __init__(self, name, priority):
		self.name = name
		self.priority = priority

	def __lt__(self, other):
		return self.priority < other.priority


skills = []

heapq.heappush(skills, Skill("Java", 9))
heapq.heappush(skills, Skill("C", 8))
heapq.heappush(skills, Skill("JavaScript", 6))

for s in skills:
	print(s.name + " :: " + str(s.priority))
