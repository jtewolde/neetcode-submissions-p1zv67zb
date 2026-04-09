# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Initial approach for this tree problem
        # 1. Use recursive DFS to determine max height of treee
        # If the node is null, return depth of 0
        # Else, Use recursion on left and right children of root.
        # Return the max depth between left and right children + 1 for final answer

        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left, right)