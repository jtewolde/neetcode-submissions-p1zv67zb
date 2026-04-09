class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Goal: Return all number of different paths to take to get to target position(m - 1, n - 1).
        # Directions that we can move is down([m][n - 1]) or right([m + 1][n])
        # Approach: This problem will be solved by using a 2D DP array or memoization with Hash Map to cache previous visited paths
        # Base Case is that there is only one way to reach starting point(dp[0][0] = 1)
        # In order to get number of paths for a position, you can add cells next to each other
        # dp[x][y] = dp[x-1][y] + dp[x][y-1]

        # Initialize 2-D DP Array with the dimensions of m * n, where dp[x][y] represents num of paths to reach cell(x,y)
        # Create base case for starting cell to be 1
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        # Fill each cell in 2-D DP table from top to bottom > left to right
        # For each cell, calculate the num of different paths to reach cell(x,y) using equation
        # dp[x][y] = dp[x-1][y] + dp[x][y-1]
        for x in range(m):
            for y in range(n):
                # Add paths from cell above as long as it is in bounds
                if x > 0:
                    dp[x][y] += dp[x - 1][y]
                # Add paths from cell to the left as long as it is in bounds
                if y > 0:
                    dp[x][y] += dp[x][y - 1]

        # Return final answer to reach number of paths to reach bottom-right target
        return dp[m - 1][n - 1]
