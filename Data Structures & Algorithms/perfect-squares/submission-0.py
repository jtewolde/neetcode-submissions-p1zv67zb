class Solution:
    def numSquares(self, n: int) -> int:
        # Approach: Use a Bottom-Up DP approach for build up base cases with iteration 
        # Strategy is to compute the minimum number of perfect squares for previous values from 1 to n
        # With bottom-up, the goal is to build up the squares of the target value by building up the squares all of previous values

        # Initialize DP Array where its length is n + 1 where each starting value is n
        # Also, create base case for DP array that dp[0] is 0 as the squares in 0 are zero.
        dp = [n] * (n + 1)
        dp[0] = 0

        # Iterate through every target value ranging from 1 to n
        for target in range(1, n + 1):
            # Also, iterate through every perfect square(s * s) that don't exceed target
            for s in range(1, target + 1):
                # Calculate the square value and determine if the square value doesn't exceed target
                # If true, break from the loop
                square = s * s
                if target - square < 0:
                    break

                # Update the value of dp[target] by getting the minimum between itself and perfect squares of previous values + 1
                dp[target] = min(dp[target], dp[target - square] + 1)

        return dp[n]