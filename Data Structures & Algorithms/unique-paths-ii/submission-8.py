class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # Goal: Compute and return the total number of unique paths taken to get to bottom right target element in grid
        # Grid is filled with zeros that represent open cells and 1's are obstacles to avoid.
        # Approach: Use 2D bottom-up dynamic programming to build the solution iteratively from the target cell back to the start
        # Each cell will store the number of ways to reach the target from that cell. Obstacles will store zero.
        # However, only one row of cells need to be processed at a time.

        # Initialize variables for length of row and cols and 1D DP array of size X - 1 filled with 0's
        # Set last cell (target) to one to get most optimal solution.
        X, Y = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * Y
        dp[Y - 1] = 1

        # Iterate through each row and col in reverse, starting from target to moving to start cell
        for row in reversed(range(X)):
            for col in reversed(range(Y)):
                # Check if current cell is an obstacle, if so, then set cell in DP to 9
                if obstacleGrid[row][col] == 1:
                    dp[col] = 0
                # Also, check if col + 1 is in bounds within grid, then add dp[col + 1] to dp[col]
                elif col + 1 < Y:
                    dp[col] += dp[col + 1]

        return dp[0]