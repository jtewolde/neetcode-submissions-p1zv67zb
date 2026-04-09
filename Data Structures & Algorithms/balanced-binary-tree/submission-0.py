# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Initial approach for this problem:
        # Initialize balanced array where first index is set to True as default
        # Create DFS function to traverse thorugh the tree
        # Establish base case if the root is null, return 0 as it is the height 
        # Perform dfs on left and right children of current node
        # If the absoulte value of left - right is greater than 1, return 0 as it is not balanced tree
        # Else, return the max height between left and right plus one
        # Outside of DFS function, return balanced[0]

        balanced = [True] 

        def dfs(root):

            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            if abs(left - right) > 1:
                balanced[0] = False

            return 1 + max(left, right)

        dfs(root)
        return balanced[0]



