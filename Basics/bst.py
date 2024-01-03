class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class BST:
    def __init__(self):
        self.root = None
        
    def insert(self, data):
        new_node = Node(data)
        
        if not self.root:
            self.root = new_node
            
