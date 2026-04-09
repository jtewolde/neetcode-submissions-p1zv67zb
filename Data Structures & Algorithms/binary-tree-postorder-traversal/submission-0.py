# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Post Traversal means starting with left child/node > parent node > right node
        # Approach: Create an postorder funciton that uses recursion, similar to inorder
        # Only change is that the parent/middle noode will be appended to ans array, then left > right
        
        # Initialze ans array that will store node values
        ans = []

        # Create inorder function that takes node as argument
        def postorder(node):
            # Base case to handle empty nodes
            if not node:
                return 

            # Use recursion to peform post traversal by starting iwth left child
            # Append the node's value to ans array
            # Do the same for right child/node

            postorder(node.left)
            postorder(node.right)
            ans.append(node.val)

        # Run inorder starting at root
        postorder(root)
        return ans