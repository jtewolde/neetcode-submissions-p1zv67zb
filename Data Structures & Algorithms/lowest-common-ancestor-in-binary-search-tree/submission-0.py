# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Approach for solving this problem
        # Start at the root of the tree:
        # Create a while loop that iterates through binary search tree until LCA is found
        # Declare if statements for different situations of where p and q are in the tree
        # If p.val and q.val are greater than curr.val(right children), set curr to curr.right
        # If p.val and q.val are less that curr(left children), set curr to curr.left
        # Else, if p and q are on different subtrees, return curr

        curr = root

        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                return curr

                