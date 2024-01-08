class Node:
    # An object for storing a single node of a linked list.
    # Models 2 attributes the data and the link to the next node in the list 
    
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data
    
class Linkedlist:

    # Singly Linked list

    def __init__(self):
        self.head = None
    
    def is_empty(self):
        self.head == None

    def size(self):

        #Returns the number of nodes and takes O(n) time
         
        current = self.head
        count = 0

        while current: 
            count += 1
            current = current.next_node

        return count
        