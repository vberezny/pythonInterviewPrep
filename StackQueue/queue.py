# FIFO

# Insertion/Deletion: O(1)

# Space: O(n)

class Queue:

  def __init__(self):
      self.queue = []

# Insert method to add element
  def addtoq(self,val):
      if val not in self.queue:
          self.queue.insert(0, val) # insert(0, val) inserts val BEFORE position 0 (start of list)
          return True
      return False

# Pop method to remove element
  def removefromq(self):
      if len(self.queue)>0:
          return self.queue.pop() # pop removes LAST item in list
      return ("No elements in Queue!")

  def size(self):
      return len(self.queue)

TheQueue = Queue()
TheQueue.addtoq("Mon")
TheQueue.addtoq("Tue")
TheQueue.addtoq("Wed")
print(TheQueue.size())
print(TheQueue.removefromq())
print(TheQueue.removefromq())
print(TheQueue.removefromq())
print(TheQueue.removefromq())
