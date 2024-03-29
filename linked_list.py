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
    def add(self, data):
        #Adds new node containing data at the head of the list
        #Takes O(1) time
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node


    def search(self, key):
        # Searches for the first node that matches the key 
        # Returns the node or "None"
        #Takes o(n) time

        current = self.head

        while current: 
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None
     
    def insert(self, data, index):
        if index == 0:
            self.add(data)
        if index > 0:
            new = Node(data)

            position = index
            current = self.head 
        


    def __repr__(self):
        #Return a string representation of a list
        #Takes O(n) time
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else: 
                nodes.append("[%s]" % current.data)
            current = current.next_node
        return '->' .join(nodes)
        
