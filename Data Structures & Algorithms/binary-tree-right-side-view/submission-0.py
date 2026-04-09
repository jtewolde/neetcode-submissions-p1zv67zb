# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Approach with problem using Breadth First Search
        # Use BFS to navigate through tree, going level to level instead of going depth
        # Implement BFS by first creating a queue where same level nodes can be appended and popped off
        # Add the root node to the queue first
        # Create ans variable to keep track of final answer of right nodes in tree

        # Create while loop to iterate through non-empty queue
        # Create variable to store len of queue
        # Create variable rightside to keep track of nodes

        # Iterate through len of queue
        # Pop current node in queue out, check to see if popped out node is null
        # If node not null, update rightSide to current node
        # Append left and right children of current node to queue
        #

        ans = []
        queue = deque([root])

        while queue:
            qLength = len(queue)
            rightSide = None

            for i in range(qLength):
                node = queue.popleft()
                if node:
                    rightSide = node
                    queue.append(node.left)
                    queue.append(node.right)

            if rightSide:
                ans.append(rightSide.val)

        return ans 
                




