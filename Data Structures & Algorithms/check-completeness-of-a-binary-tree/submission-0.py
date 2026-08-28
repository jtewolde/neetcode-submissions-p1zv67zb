# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        # Approach: Use BFS to traverse through each level and node of tree to determine if the BST is complete
        # A BST is complete when all levels in the tree is completed and filled
        # If a node is null, then expect that the other adjacent nodes and/or children are null as well

        # Initialize queue using deque with root node already inside
        queue = deque([root])

        # Process the nodes in BFS order level by level
        while queue:
            # Pop a node from queue and then adds its left and right children to the queue
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)
            # Otherwise, if the node was null, then drain the remaining queue
            else:
                while queue:
                    # If the next node is non-null, then return False as it shouldn't be null afterwards
                    if queue.popleft():
                        return False
        return True
