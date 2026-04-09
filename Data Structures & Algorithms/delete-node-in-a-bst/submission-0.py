# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # Approach: Use Recursion to locate the node to be deleted from BST
        # If the node is found inside the BST, delete it from the tree
        # Restructure the tree to make it a valid BST by moving nodes into correct positions
        # Depending on if the deleted node has children, there are multiple ways to make the BST valid
        # If the node had no children, simply just delete the node
        # If the node had one child, use that child to replace where the deleted node was
        # If the node has two children, find the "in-order successor" and attach the deleted node's left subtree to successor's left
        # "In-order successor" is the leftmost node in the right subtree

        # If the root node is None, then return None
        if not root:
            return None

        # Search where the node to be deleted resides either in left or right subtree by comparing root.val with key
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        
        # If current root does match key val, check if root node has any left or right children,
        # If it only has a left child, return that child and vice versa
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            # Find the in-order successor by first starting at root.right,
            # Use a loop to go far left as possible 
            curr = root.right
            while curr.left:
                curr = curr.left
            # Attach entire left subtree of root(deleted node) to successor's left child
            curr.left = root.left
            result = root.right 
            # Delete root node from BST and return the right subtree
            del root
            return result 

        return root



      