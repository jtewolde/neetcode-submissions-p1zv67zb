class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # Approach: Use DFS to traverse through the entire tree, finding nodes that are apples.
        # Also, tracking the amount of "time" to collect all applies in the given tree.

        # Create an adjacency list to track the neighbors of each node in the tree
        # Iterate through each parent and child in the array, update the adjacency list with each node's parent and children
        neighbors = {indx: [] for indx in range(n)}
        for parent, child in edges:
            neighbors[parent].append(child)
            neighbors[child].append(parent)

        # Initialize DFS helper function that takes current node and parent as parameters
        def dfs(curr, parent):
            # Create time variable to track how long it takes to find all apple nodes on subtree
            time = 0
            # Iterate through every child node for the given current node
            # If the child is the same value as the parent, then continue with DFS
            for child in neighbors[curr]:
                if child == parent:
                    continue

                # Recursively call DFS on child's subtree to find the apple nodes.
                # Then, if the current child is an apple or childTime is greater than 0, 
                # Increment time variable with childtime + 2 to simulate traversing up and down
                childTime = dfs(child, curr)
                if childTime > 0 or hasApple[child]:
                    time += 2 + childTime
            return time
        return dfs(0, -1)

