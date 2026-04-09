# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        # Approach: Use DFS function to traverse through entire BST nodes
        # Create difference variable to keep track of minimum difference between node.val and target
        # Create closestNode variable to keep track of smallest and closest node in BST
        # For every node encountered, compare the node's value to target value to calculate the absolute difference
        # Update ans variable based on two cases where curr diff is smaller than best diff
        # Or the diff of node is the same but the node.val is smaller than before

        # Initialize ans and finalDiff variables to keep track of closest node to target
        # And finalDiff to keep track of smallest difference between node.val and target
        ans = 0
        finalDiff = float('inf')

        # Create/Declare DFS function that takes root node as argument
        def dfs(root):
            # Base Case: If node is null, return zero
            if not root:
                return 0

            # Calculate the current abs difference between current node and target value
            # Access the outer scope variables of ans and finalDiff to use in DFS
            currDiff = abs(target - root.val)
            nonlocal ans, finalDiff

            # Update the final diff variable if currDiff is less than it 
            # Or If both differences are equal but the node's value is less than last node's value
            if currDiff < finalDiff or (currDiff == finalDiff and root.val < ans):
                finalDiff = currDiff
                ans = root.val

            # Use BST property to decide which path to take next for DFS to get closer to target with nodes
            # If the target is less than current node, go left for lesser values
            # If the target is more than current node, go right for greater values
            if target < root.val:
                next_node = root.left
            else:
                next_node = root.right

            # Use DFS on next node
            dfs(next_node)

        # Call DFS on root of tree and return ans variable for final answer
        dfs(root)
        return ans

            
            