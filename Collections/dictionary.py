"""This is a docstring"""
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


appetizers = ['burgers', 'fries', 'soups'];
sides = ['macncheese', 'mashed potatoes', 'fried mushrooms']
drinks = ['wine', 'beer', 'whiskey', 'rum', 'vodka']

food_menu = {}

food_menu['appetizers'] = appetizers
food_menu['sides'] = sides
food_menu['drinks'] = drinks


print(food_menu.get('drinks'))

"""
for k,v in food_menu.items():
	print("We have following options for ", k)
	for i in v:
		print(i)
"""