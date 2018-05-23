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

# In-order Traversal
# Left -> Root -> Right
    def InorderTraversal(self, root):
        res = []
        if root:
            res = self.InorderTraversal(root.left)
            res.append(root.data)
            res = res + self.InorderTraversal(root.right)
        return res

# Preorder traversal
# Root -> Left ->Right
    def PreorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res

# Postorder traversal
# Left ->Right -> Root
    def PostorderTraversal(self, root):
        res = []
        if root:
            res = self.PostorderTraversal(root.left)
            res = res + self.PostorderTraversal(root.right)
            res.append(root.data)
        return res

# Level-Order (BFS)
    def LevelOrderTraversal(self, root):
        thisLevel = [root]
        vals = [root.data]
        while thisLevel:
            nextLevel = []
            for n in thisLevel:
                if n.left:
                    nextLevel.append(n.left)
                    vals.append(n.left.data)
                if n.right:
                    nextLevel.append(n.right)
                    vals.append(n.right.data)
            thisLevel = nextLevel
        return vals

# initializes tree root
root = Node(12)

# inserts nodes
root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)

root.PrintTree()

print("post: ", root.PostorderTraversal(root))
print("pre: ", root.PreorderTraversal(root))
print("in: ", root.InorderTraversal(root))
print("level: ", root.LevelOrderTraversal(root))
