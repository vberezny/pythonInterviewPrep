# Heap is a special tree structure in which each parent node is less than or equal to its child node
# (Min Heap)

# Max Heap is opposite

# library: heapq, has following functions: heapify, heappush, heappop, heapreplace

import heapq

H = [21,1,45,78,3,5]

# Use heapify to create heap from H
heapq.heapify(H)
print(H)

# Inserting a data element to a heap always adds the element at the last index.
# But you can apply heapify function again to bring the newly added element to the
# first index only if it smallest in value.

# Add element
heapq.heappush(H,8)
print(H)

# You can remove the element at first index by using this function.

# Remove element from the heap
heapq.heappop(H)

print(H)

# heapreplace function removes the smallest element of the heap and inserts the
# new incoming element at some place not fixed by any order.

# Replace an element
heapq.heapreplace(H,6)
print(H)
