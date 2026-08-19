class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # Approach: Use a 2D DP array that utilizes a bottom up techinque where you start at the target element in grid
        # Then, build the path that has the minimum sum from using sum of previous cell below and cell to the right
        # Take the minimum between the two cells and add to the current cell value

        # Initialize rows and cols variable that stores dimensions of the given grid
        ROWS, COLS = len(grid), len(grid[0])

        # Expand the grid by adding cells below and to the right of the target cell with infinite values
        # Create base case where cell below target starts at zero to compute the paths properly
        dp = [[float('inf')] * (COLS + 1 ) for _ in range(ROWS + 1)]
        dp[ROWS - 1][COLS] = 0

        # Iterate through the entire gird in verse, starting at the target cell
        for row in range(ROWS - 1, -1, -1):
            for col in range(COLS - 1, -1, -1):
                # Set the current cell in dp array as the sum of the current cell in grid and the minimum between cell below and cell to the right
                dp[row][col] = grid[row][col] + min(dp[row + 1][col], dp[row][col + 1])
        # Return the result of dp array at the starting cell, that should have minimum path sum
        return dp[0][0]
