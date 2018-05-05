# Sorts

## Merge Sort

Merge Sort is a Divide and Conquer algorithm. It divides input array in two halves, calls itself for the two halves and then merges the two sorted halves. The merge() function is used for merging two halves.

- O(n log n) (worst/avg/best)

- Space: O(n)

- Divide and Conquer

## Quick Sort

Like Merge Sort, QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot. There are many different versions of quickSort that pick pivot in different ways:

    - Always pick first element as pivot.
    - Always pick last element as pivot (implemented below)
    - Pick a random element as pivot.
    - Pick median as pivot.

The key process in quickSort is partition(). Target of partitions is, given an array and an element x of array as pivot, put x at its correct position in sorted array and put all smaller elements (smaller than x) before x, and put all greater elements (greater than x) after x. All this should be done in linear time.

- Worst Case: The worst case occurs when the partition process always picks greatest or smallest element as pivot. O(n^2)

- Best Case: The best case occurs when the partition process always picks the middle element as pivot. O(n log n)

- Average Case: O(n log n)

Although the worst case time complexity of QuickSort is O(n2) which is more than many other sorting algorithms like Merge Sort and Heap Sort, QuickSort is faster in practice, because its inner loop can be efficiently implemented on most architectures, and in most real-world data. QuickSort can be implemented in different ways by changing the choice of pivot, so that the worst case rarely occurs for a given type of data. However, merge sort is generally considered better when data is huge and stored in external storage. 
