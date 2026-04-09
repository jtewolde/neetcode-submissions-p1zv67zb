# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Initial approach for this problem
        # Use BFS to navigate through tree, going level to level instead of going depth
        # Implement BFS by first creating a queue where same level nodes can be appended and popped off
        # Add the root node to the queue first

        # Create while loop to iterate through non-empty queue
        # Create variable to store len of queue
        # Create array for level of tree

        # Iterate through len of queue
        # Pop current node in queue out, check to see if popped out node is null
        # If not, append val of node to the level's array
        # Add left and right children of popped out node to queue
        # Append level array to the ans array, then return ans array
        
        ans = []
        queue = deque()
        queue.append(root)

        while queue:
            qLength = len(queue)
            level = []

            for i in range(qLength):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)

            if level:  # This now correctly checks after finishing the level
                ans.append(level)

        return ans