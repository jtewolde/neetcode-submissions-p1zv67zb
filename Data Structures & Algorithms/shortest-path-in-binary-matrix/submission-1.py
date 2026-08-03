class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # Synposis: Traverse through the grid, starting from top left element(0,0) to bottom right(n - 1, n - 1). 
        # The binary grid has only 0 and 1's where the 1's in the grid act as obstacles. Also, you can traverse in grid diagonally as well.
        # Approach: Use BFS to traverse through the grid and find the shortest path to get to the bottom right of the grid.

        # Initialize necessary variables for BFS like queue for holding current path taken. Put (0, 0, 1) in queue for starting at top left
        # Also, create visited set to hold elements in grid that was already visited in traversal, start with 0, 0
        N = len(grid)
        queue = deque([(0, 0, 1)]) # row, col, length
        visited = set([(0, 0)])

        # If starting and/or destination cell in grid have 1's, then return -1
        if grid[0][0] or grid[N - 1][N - 1]:
            return -1

        # Initialize directions array that will hold all of the directions that could be used to traverse to bottom right element
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]

        while queue:
            # Pop out recent added cell from the queue and take the info on row, col, and length
            # Then, determine if current popped cell is the destination cell. If so, return the length
            row, col, length = queue.popleft()
            if row == N - 1 and col == N - 1:
                return length

            # For each of the 8 directions, check if the current neighbor is valid, meaning if it is unvisited
            for dr, dc in directions:
                # Initialize coordinates from current cell's neighbors
                neighborRow, neighborCol = row + dr, col + dc
                # Determine if the current neighbor is valid by checking if it is visited and within bounds of grid
                if (0 <= neighborRow < N and 0 <= neighborCol < N and grid[neighborRow][neighborCol] == 0 and (neighborRow, neighborCol) not in visited):
                    queue.append((neighborRow, neighborCol, length + 1))
                    visited.add((neighborRow, neighborCol))

        return -1