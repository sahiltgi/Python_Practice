# Singly Linked List Insertion (at the End, at the Beginning)

## -----------------------------------------------------------
#      (head)A -> (head.next)B -> C -> None
# 1) Create an Empty node class.
# 2) Initialize the Node class with the data and the next pointer to None.
# 3) After Node creation, create a LinkedList class and initialize it with head pointer.
# 4) Create a linked list (llist) object and initialize it with LinkedList() class object.
# 5) Now define an append function and initialize it with data variable.
# 6) Initialize new_node with Node(data).
# 7) Check if Linked List is empty and if it is True, then initialize self.head with new_node and return else initialize it to last_node and run while loop.
# 8) Move forward using last_node.next and if it is found to be None, then initialize last_node.next to new_node.
# 9) Define a print_node function and initialize self.head to current node and print it and move forward using current_node.next.
## -----------------------------------------------------------

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_node(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node




llist = LinkedList()
llist.append("A")
llist.append("B")
llist.print_node()