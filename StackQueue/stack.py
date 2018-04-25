# LIFO

# Space: O(n)

# Insertion/Deletion: O(1)
#

class Stack:

    def __init__(self):
        self.stack = []

# Use list append method to push element
    def push(self, dataval):
        if dataval not in self.stack:
            self.stack.append(dataval) # append adds item to END of list
            return True
        else:
            return False

# Use list pop method to remove element
    def remove(self):
        if len(self.stack) <= 0:
            return ("No element in the Stack")
        else:
            return self.stack.pop() # pop removes LAST item in list

# Use peek to look at the top of the stack
    def peek(self):
	    return self.stack[0]

    def isEmpty(self):
        if not self.stack:
            print("Stack is empty")
        else:
            print("Stack is not empty")

AStack = Stack()

AStack.isEmpty()

AStack.push("Mon")
AStack.push("Tue")

AStack.peek()

AStack.isEmpty()

print(AStack.peek())

AStack.push("Wed")
AStack.push("Thu")

print(AStack.peek())
print(AStack.remove())
