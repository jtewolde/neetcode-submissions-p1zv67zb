# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Initial approach for this problem using DFS
        # Create a modified version of DFS where it checks if the left node < root node < right node
        # Initialize helper function where it takes three parameters, node, left boundary, and right boundary
        # Create base cases for helper DFS Function:
        # If root node is null, return True as empty tree is still BST
        # If the comparison left < node.val < right doesn't hold, return False
        # Use recursion by running function on both left and right children of node
        # Return the result of two recurisons using AND Operation
        # Call helper function where it takes root node and boundaries are -inf and inf

        # Takes node and boundaries
        def validHelper(node, left, right):
            # if root is null, return True as empty tree is BST
            if not node:
                return True

            # See if comparison is valid, else, return False
            if not (left < node.val < right):
                return False

            return (validHelper(node.left, left, node.val)
                    and validHelper(node.right, node.val, right))

        return validHelper(root, float("-inf"), float("inf"))




        


