# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Optimal approach using Iterative DFS
        # Create a stack with the initial element being the root node and its depth, being one
        # Create a counter to keep track of max depth of all nodes in the tree
        # Loop through the entire stack while it is not empty
        # Pop out the top of the stack, creating variables for the node and the depth
        # Update the counter for the max depth of node
        # Create if statement to see if current node is not null
        # Then, add the node and depth of the left and right children of current node
        # Finally, return counter variable for final answer

        stack = [[root, 1]]
        ans = 0

        while stack:
            node, depth = stack.pop()

            if node:
                ans = max(ans, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])

        return ans



