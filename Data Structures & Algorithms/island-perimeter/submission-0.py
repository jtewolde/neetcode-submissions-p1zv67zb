class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # Approach: Use iteration to iterate through all cells on grid to find land cells
        # First, initialize perimeter variable to store the total perimeter of land cells
        # Also, initialize row/col variables to get the number of rows and cols in grid
        # Create nested for loop to iterate through all cells in grid
        # If encountering a land cell, increment perimeter by 4 initially
        # Check if the cell above/below or left/right of it is land, 
        # Then subtract 2 from perimeter as they share a adjacent side
        # After iteration, return total perimeter

        # First, initialize perimeter variable to store the total perimeter of land cells
        # Also, initialize row/col variables to get the number of rows and cols in grid
        perimeter = 0
        row, col = len(grid), len(grid[0])

        # Create nested for loop to iterate through all cells in grid
        for r in range(row):
            for c in range(col):
                # If encountering a land cell, increment perimeter by 4 initially
                if grid[r][c] == 1:
                    perimeter += 4

                    # Check if the cell above/below or left/right of it is land, 
                    # Then subtract 2 from perimeter as they share a adjacent side
                    if r and grid[r - 1][c] == 1:
                        perimeter -= 2
                    if c and grid[r][c - 1] == 1:
                        perimeter -= 2
        # After iteration, return total perimeter
        return perimeter
