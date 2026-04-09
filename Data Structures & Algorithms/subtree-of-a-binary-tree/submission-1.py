# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Approach of solving this problem is by using DFS
        # Pseudocode is to create a helper function to see if a portion of the root tree
        # is the same tree as the subroot tree
        # Create two helper functions to get the solution, isSameTree and hasSubTree
        # The helper function, sameTree, will be like the previous problem, "Same Tree" but being used as a helper function
        # hasSubtree function will determine the result of if there is a subtree in root using the isSameTree function

        # SameTree helper function to see if two trees are the same
        def isSameTree(p, q):
             # Both roots are null
            if not p and not q:
                return True
            # Both roots are the same and not null
            if p and q and p.val == q.val:
                return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
            else:
                return False

        # Helper function to solve the problem by using isSameTree function
        def hasSubtree(root):
            # If root node is null, there is no subtree, resulting in false
            if not root:
                return False
            # If root and subroot are the same tree, then return True
            if isSameTree(root, subRoot):
                return True

            # Recursively call hasSubtree function on the children of root to see if there is a subroot on either of them
            return hasSubtree(root.left) or hasSubtree(root.right)

        return hasSubtree(root)



