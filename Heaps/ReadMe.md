# Heaps

The heap is one maximally efficient implementation of an abstract data type called a priority queue, and in fact priority queues are often referred to as "heaps"

A common implementation of a heap is the binary heap, in which the tree is a binary tree

In a heap, the highest (or lowest) priority element is always stored at the root.

A heap is not a sorted structure and can be regarded as partially ordered

The root element will be at Arr[0]

'''Arr[i/2]''' 	Returns the parent node

'''Arr[(2*i)+1]''' 	Returns the left child node

'''Arr[(2*i)+2]''' Returns the right child node

### HeapSort
Heap Sort uses Binary Heap to sort an array in O(nLogn) time.
