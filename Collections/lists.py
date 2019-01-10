colors = ["orange", "white", "blue", "green"];

##print(colors[3]);

for color in colors:
    print(color);

if "orange" in colors:
    print("Yay");
else:
    print("Nay");

for i in range(1,10):
    print(i);

# List functions
nums = [1, 2, 3, 5, 8];

nums.append(9); # O(1)

nums.insert(4, 40); #O(n)

nums.pop(); # O(1)

print("Min in list is: " + str(min(nums)));
print("Max in list is: " + str(max(nums)));
print(nums);
print(len(nums));

squares = []

for x in range(1,11):
	squares.append(x**2)

print(squares)

# lists are mutable and can be altered. 


