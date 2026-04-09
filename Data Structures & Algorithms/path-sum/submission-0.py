# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Approach: Implement DFS to traverse through the entire BST
        # Use the node.val to add with other nodes to see if path's sum equals targetSum
        # When the path ends with a leaf node(node that has no children), compare curSum with targetSum
        # If curSum == targetSum, return True. Else, return False

        # Implement DFS function that takes root node and current sum of path as arguments
        def dfs(root, curSum):
            # If there is no such node, return False
            if not root:
                return False
            # Update the current sum of the path by adding the current node's value
            curSum += root.val

            # If the current node is a leaf node and the current sum of path equals the targetSum
            if root.left == None and root.right == None and curSum == targetSum:
                return True
            
            # Take the sum from either left or right path taken
            return dfs(root.left, curSum) or dfs(root.right, curSum)

        # Start DFS with root node of tree with curSum starting at zero
        return dfs(root, 0)

            