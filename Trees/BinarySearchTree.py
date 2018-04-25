# BST: left_subtree (keys)  ≤  node (key)  ≤  right_subtree (keys), duplicate keys not allowed

# Searching: worst case O(h) where h is height of tree, therefore at least O(log n) comparisons
# a BST can degenrate to a linked list, in this case search time reduces to O(n)

# Deletion: replace the node being deleted with the
# largest node in the left subtree and then delete that largest node

class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

# Insert method to create nodes
    def insert(self, data):

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

# findval method to compare the value with nodes
    def findval(self, val):
        if val < self.data:
            if self.left is None:
                return str(val)+" Not Found"
            return self.left.findval(val)
        elif val > self.data:
            if self.right is None:
                return str(val)+" Not Found"
            return self.right.findval(val)
        else:
            print(str(self.data) + ' is found')


# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()


root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
print(root.findval(7))
print(root.findval(14))
