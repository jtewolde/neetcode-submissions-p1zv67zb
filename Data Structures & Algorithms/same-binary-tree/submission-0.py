# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Initial appraoch using recursive DFS:
        # First, compare both roots of trees to see if they are null, return true
        # If both roots are the same val and are not null, use recursion on left and right children
        # If one root is null and the other is not, return False,

        # Then, recursively call DFS on both left and right on both trees
        # If left and right children of both trees are the same, return Trye

        # Both roots are null
        if not p and not q:
            return True
        # Both roots are the same and not null
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False


