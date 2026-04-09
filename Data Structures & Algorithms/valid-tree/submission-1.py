class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Approach for solving this graph problem is using DFS to detect cycles
        # Similar to Course Schedule problems, create an adjecency list to map nodes with edges
        # Create a visit set that has visited nodes stored

        # If there are not enough edges or too many nodes, 
        # A tree can't be constructed, return False
        if len(edges) >  (n - 1):
            return False

        # Initialize adjencey list and visited set for nodes
        adjList = defaultdict(list)
        visited = set()

        # Iterate through edges list, map out connections of nodes to edges
        # B/C it is undirected graph, add both direction between nodes
        # A --> B and B --> A
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)

        # Initialize DFS function that takes in node and 
        def dfs(node, parent):
            # See if current node has already been visited, return False as there is a cycle
            if node in visited:
                return False

            visited.add(node)

            # Iterate through all children/neighbors of node,
            for neighbor in adjList[node]:
                # IF the current neighbor is the parent node, skip it as it is expected and doesnt count as cycle
                if neighbor == parent:
                    continue
                # If result from DFS on neighbor is false, return False
                if not dfs(neighbor, node):
                    return False

            return True

        return dfs(0, -1) and len(visited) == n
            