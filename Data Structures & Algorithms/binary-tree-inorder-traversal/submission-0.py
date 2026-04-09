# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # In-Order Traversal means starting with left child/node > parent node > right node
        # It will start at root node, go down to left children
        # Approach: Create an inorder funciton that uses recursion
        
        # Initialze ans array that will store node values
        ans = []

        # Create inorder function that takes node as argument
        def inorder(node):
            # Base case to handle empty nodes
            if not node:
                return 

            # Use recursion to peform inorder traversal by startign iwth left child
            # Append the node's value to ans array
            # Do the same for right child/node
            inorder(node.left)
            ans.append(node.val)
            inorder(node.right)

        # Run inorder starting at root
        inorder(root)
        return ans

        