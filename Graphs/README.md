# Graphs

A graph can be easily presented using the python dictionary data types. We represent the vertices as the keys of the dictionary and the connection between the vertices also called edges as the values in the dictionary.

## DFS

- for entire graph: O(|V|+|E|)
- space: O(|V|)
- uses a stacks

## BFS

- returns shortest path
- uses a queue

Replacing the stack with a queue will instead explore the breadth of a vertex depth before moving on. This behavior guarantees that the first path located is one of the shortest-paths present, based on number of edges being the cost factor.
