"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # Approach: Use DFS/Recursion and a helper function to traverse through n-ary tree in postorder
        # Postorder traversal in a n-ary tree means recursively processing each child subtree from left to right
        # Then, adding the current node's value to the final result array

        # Initialize ans array that will store final order of postorder traversal
        ans = []

        # Define the recurisve helper function that takes current node as a parameter
        # If the current node is null, return empty array
        def helper(node):
            if node == None:
                return
            
            # Iterate through all children in current node, recursively call helper function on child
            for child in node.children:
                helper(child)
            # Append node val to ans list after processing all children
            ans.append(node.val)

        helper(root)
        return ans

            