class Node:

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:

    # initialize empty head
    def __init__(self, head=None):
        self.head = head

    # Inserts to front of list
    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    # loop through nodes that exist and return a total count
    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    # finds first occurence of data in list
    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            print("Data not in list")
        return current.get_data()

    # deletes
    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            print("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            #points previous node to current.next node (deletes current)
            previous.set_next(current.get_next())

    # prints list starting from head
    def printList(self):
        current = self.head
        if current == None:
            print("List is empty")
        else:
            while current:
                print(current.get_data())
                current = current.get_next()

# Testing area

list = LinkedList()
list.insert("a")
print("list size: ", list.size())
list.printList()
list.insert("b")
print("list size: ", list.size())
list.printList()
list.insert("c")
print("list size: ", list.size())
list.printList()
list.insert("d")
print("list size: ", list.size())
list.printList()
list.delete("b")
print("list size: ", list.size())
list.printList()
print("find c in list: ", list.search("c"))
