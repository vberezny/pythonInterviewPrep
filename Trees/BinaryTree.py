#height of complete binary tree with N nodes is at most O(log N)

#full binary tree is when each node has exactly 0 or 2 children

class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data


    def insert(self, data):
# Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

# initializes tree root
root = Node(12)

# inserts nodes
root.insert(6)
root.insert(14)
root.insert(3)
root.insert(18)
root.insert(21)

root.PrintTree()
