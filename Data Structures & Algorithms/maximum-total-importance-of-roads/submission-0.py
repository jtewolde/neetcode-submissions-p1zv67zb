class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        # Problem: Assign distinct values from 1 to n onto the "cities" and nodes in the roads graph.
        # The goal is to maximize total importance/sum of values assigned to its two endpoints/nodes
        # Approach: Use a greedy approach to count number of edges for each road,
        # Then, assign the larger values to the cities/nodes in graph that appear more in roads/has more edges
        
        # Initialize array filled with zeros taht count number of edges for each node in graph
        # Also, create label and ans variable for storing total importance of roads and label
        edge_count = [0] * n
        label = 1
        ans = 0

        # Iterate through each node in roads graph and count the num of edges for each node
        for node1, node2 in roads:
            edge_count[node1] += 1
            edge_count[node2] += 1

        # Sort the edge count array and iterate through each edge count 
        for count in sorted(edge_count):
            # Incremenet ans with the product between the curr label and edge count, then increment label by one
            ans += label * count
            label += 1
        return ans
