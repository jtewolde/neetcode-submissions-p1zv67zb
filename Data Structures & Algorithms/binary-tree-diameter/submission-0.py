# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Initial Approach using recursive DFS function:

        # Create a dfs function where the current node is the argument
        # Initialize a res variable to keep track of diameter

        # Inside DFS function:
        # Initialize base case of null node, return 0 for diameter
        # Use recursion dfs function on both left and right children of curr node
        # Calculate the diameter by adding the left and right heights
        # Use nonlocal res variable to update the diameter
        # Return the max with res and left + right and add one

        # Outside of DFS:
        # Use the dfs function on root, then return res

        res = 0

        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            diameter = left + right

            nonlocal res
            res = max(res, diameter)

            return 1 + max(left, right)

        dfs(root)
        return res























