class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Techinque to solving this Graph problem is by using DFS
        # This problem's core is seeing if there is a cycle in the graph

        # Synopsis: Initialize an adjacency list with defaultDict(list) to map courses with prequisites
        # Iterate through prequesites array and append/map 'a' and 'b' value as key-value pair
        # Create constants for UNVISITED = 0, VISITING = 1, AND VISITED = 2 states when iterating through courses
        # Create state array that keep tracks of visiting state of each vertex/course
        # Declare a DFS function where it takes a node as the parameter
        # Get the state of the current node and see if state of node is VISITED, return true, If VISITING, return false
        # Set current state of node to VISITING, then iterate through neighbors of current node and run DFS on neighbor
        # If the neighbor returns False where the neighbor is currently being VISITING, then there is a cycle in graph
        # If not, set state of node to VISITED and return True
        # Outside of DFS function, iterate with range of numCourses provided
        # Run DFS on each number in range of NumCourses, if the result is False, Return False
        # By default, return True

        # Create constants for states of visiting nodes in graph
        UNVISITED = 0
        VISITING = 1
        VISITED = 2

        # Create adjacency list to build graph of courses
        adj = defaultdict(list)
        courses = prerequisites

        # Map each a, b as a key-value pair and append it to the adj list
        for a, b in courses:
            adj[a].append(b)

        # Initialize states array that keep track of state for each course, all being UNVISITED first
        states = [UNVISITED] * numCourses

        # Initialize DFS function which takes node as a parameter, with it being a course
        def dfs(node):
            # Take the state of the current node from states array
            state = states[node]

            # See if course's state if VISITED or VISITING, 
            # Return True or False depending on state
            if state == VISITED:
                return True
            elif state == VISITING:
                return False

            # Set state of node to VISITING before running DFS on node
            states[node] = VISITING

            # Go through neighbor courses of current node
            # Run DFS on each neighbor, if result is False, it means there is a cycle in graph
            # Return False
            for neighbor in adj[node]:
                if not dfs(neighbor):
                    return False

            # Set state of current node to VISITED if neighbors are all VISITED
            states[node] = VISITED
            return True
            
        # For each number that is a course in the rangoe of numCourses
        for index in range(numCourses):
            # Run dfs on index and if the result of DFS is False, return False
            if not dfs(index):
                return False
        return True





