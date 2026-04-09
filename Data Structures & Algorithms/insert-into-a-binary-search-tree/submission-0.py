# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Approach: Use Recurison to find the right place to insert node into valid BST
        # Compare current node's value with val to see whether to compare with more nodes on left or right subtree
        # If val < node.val, call recursive function on the left subtree
        # If val > node.val, call recrusive function on right subtree
        # Finish searching for valid insert position if current node is null,
        # Create a TreeNode with val at that position

        # Base Case: If current node is null, then current position is valid for inserting
        # Create TreeNode with val as value for node
        if not root:
            return TreeNode(val)

        # Compare current node's value with val to insert to see which subtree is insert in
        # Left subtree if val is less than current node's val > use recursion on root.left
        # Right subtree if val is greater than current node's val > use recursion on root.right
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        elif val > root.val:
            root.right = self.insertIntoBST(root.right, val)

        # Return root for entire BST after insertion
        return root
            
