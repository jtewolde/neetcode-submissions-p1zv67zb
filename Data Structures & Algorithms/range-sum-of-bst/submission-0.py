# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # Approach: Use DFS to traverse through entire BST to get valid nodes in range
        # See if the current node is within range of low and high variables,
        # If so, add node.val to the ans variable to get the rangeSum
        # If node > low, search left subtree to get more valid nodes
        # If node < high, search right subtree to get more nodes within range
        # Then If node within [low, high], search both subtrees 

        # Initialize DFS function that takes node as argument to see if node is within range
        def dfs(root):

            # Create ans variable that stores the sum of BST nodes that fall within range
            ans = 0
            # If current node is none, then return zero
            if not root:
                return 0

            # Determine if current node's value falls within range: Set ans to the node's value
            # If node's value is greater than low or less than high, use DFS on left and right subtrees and add results to ans
            if low <= root.val <= high:
                ans = root.val
            if root.val > low:
                ans += dfs(root.left)
            if root.val < high:
                ans += dfs(root.right)
                
            return ans

        return dfs(root)
                
