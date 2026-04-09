# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # Approach: Use DFS to iterate and compare both trees's elements to merge trees
        # First, establish base case of if either root node is null, return the other tree
        # Then, If both current nodes of both trees are not null then create new TreeNode with sum of nodes
        # Use recursive DFS by calling mergeTrees function on both right and left children of current node of both trees
        # Return head of new Treenode to return merged tree

        # Establish base case to deal with case if either root node of trees are null,
        # Return the other tree as a result
        if root1 == None:
            return root2
        elif root2 == None:
            return root1

        # Create new merged node which value is the sum of both tree's root node
        merged_node = TreeNode(root1.val + root2.val)

        # Use recursion on both left and right children on root node to create children of merged tree
        merged_node.left = self.mergeTrees(root1.left, root2.left)
        merged_node.right = self.mergeTrees(root1.right, root2.right)

        return merged_node



        