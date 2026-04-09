class Solution:
    def climbStairs(self, n: int) -> int:
        # The approach for solving this problem is by using Bottom-Up Dynamic Programming
        # Use Tabulation to store the different ways to get to n stairstep, 
        # Solve using fibboncai sequence as addign up the results of previous two steps will get the result of current step
        # Step 1: Create the base cases for the known results
        # With this problem, we know that if n == 1 or == 2, return both of those values
        # Step 2: Initialize a DP array that stores all of the results for each step,
        # Make all of the indexes equal to zero except for first two indexes, where it will equal one and two
        # Step 3: Create for loop that starts after 2 as we know the base cases for first two steps
        # Set the current index at dp to equal the sum of the previous two steps

        # Base cases for first two steps:
        if n == 1:
            return 1
        if n == 2:
            return 2

        # Initialize DP array that stores num of steps to reach top of staircase at each index
        dp = [0] * n

        # Make first two indexes of dp array as base cases for first two steps
        dp[0] = 1
        dp[1] = 2

        for x in range(2, n):
            dp[x] = dp[x - 2] + dp[x - 1]

        return dp[n-1]
