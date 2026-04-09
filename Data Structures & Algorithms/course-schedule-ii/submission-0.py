class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Approach for solving this version of Course Schedule II is using DFS and cycle detection
        # The structure of the code will be the same as the first Course Schedule
        # Instead of returning boolean value, it will return an array that shows an order of courses

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
        # Initialize order array that stores the order of courses
        states = [UNVISITED] * numCourses
        order = []

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
            # Append current node to order array if the node is valid and has no cycle
            order.append(node)
            return True
            
        # For each number that is a course in the rangoe of numCourses
        for index in range(numCourses):
            # Run dfs on index and if the result of DFS is False, 
            # Return empty array as not possible to finish all courses
            if not dfs(index):
                return []
        # Regardless, return the order of courses
        return order