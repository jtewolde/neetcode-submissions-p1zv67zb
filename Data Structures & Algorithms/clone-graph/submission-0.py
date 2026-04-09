"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Approach of solving this graph problem is by using DFS
        # Run down on problem is to use a hashmap to map the original graph nodes to the new nodes
        # Create copies of the node that we are on and then recursively create copies of its neighbors

        # Initialize hashmap for mapping original node to new nodes
        originalToNew = {}

        # Edge case: If node is null, return None
        if not node:
            return None

        # Create dfs function that takes node as argument
        def dfs(node):
            # The node already has a copy, just return the copy
            if node in originalToNew:
                return originalToNew[node]

            # Create copy of node with the original node's value
            # Map copy node to the original node in hashmap
            copy = Node(node.val)
            originalToNew[node] = copy

            # Iterate through all of the node neighbors
            # Recursively make copies of all of the neighbors
            # Add the copy's neighbors to the list of neighbors
            for neigh in node.neighbors:
                copy.neighbors.append(dfs(neigh))

            # Return the copy node
            return copy

        # Run DFS on given node 
        return dfs(node)




