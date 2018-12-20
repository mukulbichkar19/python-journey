from Node import Node;
from LinkedList import LinkedList;

class TestLL(object):
    def __init__(self):
        this.self = self;


n1 = Node(5)
n2 = Node(10)
n3 = Node(20)
n4 = Node(30)

ll = LinkedList(n1)
ll.append(n3)
ll.append(n2)
ll.append(n4)

ll.print();

print("The length of linked list is: " + str(ll.length()));

ll.insert(90, 7)

ll.insert(120, 3)

ll.delete_value(890)

ll.delete_value(20)

print("Before deleting: ")

ll.print()

print("After deleting: ")

ll.delete_pos(4)

ll.print()
