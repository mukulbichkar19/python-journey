import array


a = array.array('i',[1,3,4,5,3])

del a[2] #deletes array element
a.remove(3) #deletes first element with value = 3

print("Array of type int: ")
for i in a:
	print(i)