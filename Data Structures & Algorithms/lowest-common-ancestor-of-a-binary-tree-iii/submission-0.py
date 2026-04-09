"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # Approach: Use a hashmap to store visited nodes when traversing upward from both p and q nodes
        # LCA means the lowest/deepest node in BST that both nodes, p and q, are descendants/children of
        # First, create a visited set that keeps track of visited nodes when traversing upward through p node using parent attribute
        # Then, start from q node and traverse upward again
        # If any nodes in q's path exists in set, return that node

        # Initialize visited hashset that stores visited nodes in p/q's traversal path
        visited = set()

        # Traverse tree starting from p to root node, storing each visited node into set
        while p:
            visited.add(p)
            p = p.parent

        # Now, traverse through tree starting from q to root,
        # Check if current parent node exists in visited, if so > return that node
        while q:
            if q in visited:
                return q
            q = q.parent

        

        