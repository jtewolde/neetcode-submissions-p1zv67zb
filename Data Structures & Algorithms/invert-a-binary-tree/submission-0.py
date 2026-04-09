# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Inverting Binary tree means swapping the left and right children's positions
        # Approach of this problem: 
        # Create base case if the root is None, return None
        # Else, swap the left and right children where root.left = root.right and vice versa
        # Then, recursively call invertTree function on both children
        # Return the root

        if not root:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root