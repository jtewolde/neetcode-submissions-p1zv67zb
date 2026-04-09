class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Approach for solving this problem is to use level by level BFS to find all paths
        # Goal is to replace land cells with its distance to treasure chests

        # Initialize a queue variable to keep track of all treasure chest positions and visited cells
        queue = []

        # Create visited variable to track visited cells with hashset
        # Variables for tracking dimensions of grid
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])

        # Create a helper function, addCell, to add new cells to queue and visited set if conditions are met
        def addCell(row, col):
            # If the current position is out of bounds, already visited, or is a cell that can't be traversed
            if (row < 0 or row == ROWS or 
                col < 0 or col == COLS or
                (row, col) in visited or
                grid[row][col] == -1):
                return
            visited.add((row, col))
            queue.append([row, col])


        # Iterate through entire grid and add all of treasure chests into the queue and visited
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    queue.append([i, j])
                    visited.add((i, j))

        # Initialize distance variable to keep track of distance from each open cell to treasure
        distance = 0

        # Perform while loop when the queue is not empty
        while queue:
            # Iterate through loop for length of queue amount of times
            # Pop out position of cell and set the cell to the distance 
            for _ in range(len(queue)):
                row, col = queue.pop(0)
                grid[row][col] = distance
                addCell(row + 1, col)
                addCell(row - 1, col)
                addCell(row , col + 1)
                addCell(row , col - 1)

            distance += 1



