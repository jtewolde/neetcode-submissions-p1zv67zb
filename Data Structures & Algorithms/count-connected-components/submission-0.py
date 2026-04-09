class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Initial approach for solving this problem is by using DFS on graph like previous problems
        
        # Create adjencey list for mapping edges to nodes and visited set to store visited nodes
        adjList = defaultdict(list)
        visited = set()

        # Iterate through indices in edges list, map out connections to nodes
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)

        # Initialize DFS function that takes in node
        # Iterate through neighbors of node, sees if it has already been visited, if not, use DFS on neighbor
        def dfs(node):
            for neighbor in adjList[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)

        # Initialize connections counter to count number of connections as final answer
        connections = 0

        # Loop through each node, see if teh current node is not visited, call DFS on it
        # Add the node to the visited set and increment connections variable by 1
        for node in range(n):
            if node not in visited:
                dfs(node)
                visited.add(node)
                connections += 1

        return connections
                