# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Initial approach using Inorder Tranversal DFS
        # Time Complexity of Solution: O(N)

        # Create an ans array that will have all of the nodes of tree in order and sorted
        # Initialize a DFS function with node as the parameter
        # Create base case of if not node, then return out of function
        # Then, perform recurisve DFS on left child of node, append the node.val in the ans array, then do DFS to right child
        # Outside of DFS function, call DFS function on root,
        # Return val in ans array with index being K - 1

        ans = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            ans.append(node.val)
            dfs(node.right)

        dfs(root)
        return ans[k - 1]









