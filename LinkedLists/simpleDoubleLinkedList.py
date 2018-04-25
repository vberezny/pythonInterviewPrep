class DoubleNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

    def traverseForward(self):
        node = self
        while node != None:
            print (node.val) # access the node value
            node = node.next # move on to the next node

    def traverseBackward(self):
        node = self
        while node != None:
            print (node.val)
            node = node.prev


node1 = DoubleNode(67)
node2 = DoubleNode(68)
node3 = DoubleNode(69)

node1.next = node2 # 12->99
node2.next = node3 # 99->37
node2.prev = node1
node3.prev = node2

node1.traverseForward()
node3.traverseBackward()
