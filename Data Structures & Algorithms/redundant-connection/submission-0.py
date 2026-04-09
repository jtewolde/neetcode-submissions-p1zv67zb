class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Approach for solving this problem is by using Union Find algo to solve
        # Union Find is a method to solving graph problems where it finds the redundant edge in the graph
        # Synopsis: Preinitialize array, parent array where it stores the parent node of each node
        # Create a find function where it finds the parent node of a given node
        # Then, process every edge in graph, find the parents of both edges
        # Compare the parents of both nodes, if they are the same, that is the redundant edge, return it
        # If the nodes are in different components, set the parent of one node to another to connect them

        # Initialize parent array where each node is it's own separate component
        parent = list(range(len(edges)))

        # Create recursive find function where it finds the root parent of given node
        # As long as the parent of a node is not itself
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        # Process each edge [a, b], find the root parent of both nodes
        # Using a - 1 and b - 1 because problem asks for nodes from 1 to n but array is 0-indexed 
        for a, b in edges:
            parentA, parentB = find(a - 1), find(b - 1)

            # Immediately check if the parents of both nodes of edge are the same
            # If so, then return the edge as it creates the cycle in graph
            if parentA == parentB:
                return [a, b]

            # If the two nodes have different parents, 
            # Then unite both nodes by making one root parent of node to equal the other's parents
            parent[parentA] = parentB

        # By default, return empty array
        return []

            

        



