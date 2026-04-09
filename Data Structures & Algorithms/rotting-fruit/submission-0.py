from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Approach to solving this problem is by using a level by level BFS

        # Initialize queue variable, that keeps track of positions of rotten oranges
        rotten_oranges = []

        # Create variables to keep track of num of fresh oranges and time taken to rot all oranges
        fresh_oranges, minutes = 0, 0

        # Initialize variables, ROWS AND COLS, to get the dimensions of the grid
        rows, cols = len(grid), len(grid[0])

        # Iterate through the entire 2d grid
        # If current pos = 1 (fresh orange), then add one to fresh variable
        # If current pos = 2 (rotten orange), then add the position to the queue
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh_oranges += 1
                if grid[i][j] == 2:
                    rotten_oranges.append((i, j))

        # Create directions nested array to provide directions where rotten can spread to fresh oranges
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Perform while loop while the queue is not empty and there are still fresh oranges
        while rotten_oranges and fresh_oranges > 0:
            # Iterate through length of queue, pop out position of rotten oranges
            for _ in range(len(rotten_oranges)):
                i, j = rotten_oranges.pop(0)

                # Iterate through the directions array
                # Apply those four directions to current position of rotten orange
                for dx, dy in directions:
                    x, y = i + dx, j + dy

                    # If the new position is out of bounds or the orange at
                    # that position isn't fresh, then continue and disregard it
                    if (x < 0 or x >= rows or 
                        y < 0 or y >= cols or 
                        grid[x][y] != 1):
                        continue    

                    # If the orange at the position is fresh, turn it rotten by setting it to 2
                    # Add the position of new rotten orange to queue
                    # Decrement fresh oranges down one
                    grid[x][y] = 2
                    rotten_oranges.append((x, y))
                    fresh_oranges -= 1

            # Increment timeTaken (minutes) by one after each level
            minutes += 1

        # If there are no fresh oranges left, return time, else return -1
        if fresh_oranges > 0:
            return -1
        return minutes
