list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'g', 'd', 'e', 'a', 'b', 'a'];

dict = {}

for l in list:
	if l in dict.keys():
		val = dict[l] + 1
		dict[l] = val
	else:
		dict[l] = 1

for k,v in dict.items():
	print(k + " :: " + str(v))
