# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Initial approach using DFS
        # Create a modified DFS function where it takes the node and the max val
        # Base Case: If current node is null, then return 0
        # Create numOFGood variable to keep track of number of good nodes in tree
        # Set numOfGood to 1 if the current node.val is greater than or equal to maxVal
        # Update maxVal with the max between current node.val and maxVal
        # Run DFS on both left and right children and add the results to the numOfGood variable
        # Return numOfGood from DFS function
        # Return the result of DFS(root, root.val)

        def dfs(node, maxVal):
            if not node:
                return 0
            
            numOfGood = 1 if node.val >= maxVal else 0
            maxVal = max(node.val, maxVal)
            numOfGood += dfs(node.left, maxVal)
            numOfGood += dfs(node.right, maxVal)

            return numOfGood

        return dfs(root, root.val)

