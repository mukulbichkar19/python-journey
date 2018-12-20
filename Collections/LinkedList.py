from Node import Node

class LinkedList(object):
    def __init__(self, head = None):
        self.head = head

    """ Insert add a new node at the given position """
    def insert(self, value, pos):
        if(self.head == None and pos > 0):
            print("LL is empty adding as head")
            self.head = Node(value)
        elif(self.head and pos > self.length()):
            print("Position exceeds the linked list size appending at end")
            self.append(Node(value))
        else:
            curr_cnt = 0
            temp = self.head
            while temp != None and curr_cnt != pos:
                temp = temp.next
                curr_cnt += 1
            new_node = Node(value)
            new_node.next = temp.next
            temp.next = new_node

    """ Add a new node at the end of the linked list """
    def append(self, new_node):
        temp = self.head;
        if self.head:
            while temp.next:
                temp = temp.next
            temp.next = new_node;
        else:
            self.head = new_node;

    """ Calculates the total length of the linked list """
    def length(self):
        len = 0;
        if(self.head == None):
            return len
        else:
            temp = self.head
            while temp:
                len += 1
                temp = temp.next
            return len

    """ Print the linked list """
    def print(self):
        temp = self.head
        output = '';
        if self.head:
            while temp:
                output += str(temp.value)
                output += " --> "
                temp = temp.next;
            output += "EOL"
            print(output)
        else:
            print("Linked List is empty")


    """ Delete by value searches the element and deletes the first occurence"""
    def delete_value(self, val):
        found = None
        if(self.head == None):
            print("The linked list is empty, cannot delete")
        else:
            temp = self.head
            while temp.next:
                if(temp.next.value == val):
                    temp.next = temp.next.next
                    found = True
                    print("Deleted the first occurence of : " + str(val));
                    break
                temp = temp.next
        if(found == None):
            print("The val " + str(val) + " does not exist in the linked list")


    """ Delete by position delete's the element at given position if such a
    position exists """
    def delete_pos(self, position):
        if(self.head == None):
            print("Cannot delete as ll is empty")
        elif(self.head != None and self.length() < position):
            print("Cannot delete as ll is smaller than the entered position value")
        else:
            cnt = 1
            len = self.length()
            temp = self.head
            while temp and cnt != position-1:
                temp = temp.next
                cnt += 1
            if(position == len):
                temp.next = None
            elif(position == 0):
                self.head = temp.next
            else:
                print("Deleting node at position: " + str(position)
                + " with value: " +str(temp.next.value))
                temp.next = temp.next.next
