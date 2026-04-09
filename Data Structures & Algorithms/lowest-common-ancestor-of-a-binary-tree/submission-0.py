# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Approach: Use DFS/Recursion to traverse through entire tree to find nodes in P and Q inside of BST
        # LCA means the lowest/deepest node in BST that both nodes, p and q, are descendants/children of
        # Use Recursion/DFS to search both subtrees of BST to find p and q nodes, return node itself

        # Establish base case if root node of tree is null or equals one of p and q
        # Return that root node as it is LCA
        if root is None or root == p or root == q:
            return root

        # Recursively search for both subtrees of root to find p and q
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both left and right are not null nodes, return root as it is the LCA
        if left and right:
            return root

        # Otherwise, return the subtree that isn't null
        return left if left else right