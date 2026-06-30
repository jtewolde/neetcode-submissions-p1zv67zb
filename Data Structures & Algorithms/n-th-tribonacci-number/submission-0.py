class Solution:
    def tribonacci(self, n: int) -> int:
        # Approach: Use Bottom-Up DP to build up to the final solution from the base cases
        # Start with the first three known values, 0, 1, and 1.
        # Continue to iterate and compute each value after until reaching T(N)

        # First, create base case checker to see if current n value is the first three values
        # Then, determine what base value of n is at current iteration
        if n <= 2:
            return 1 if n != 0 else 0

        # Initialize DP array with size of n + 1 and each value as zero for now
        # Then, make index 1 and 2 to be initialize at 1
        dp = [0] * (n + 1)
        dp[1] = dp[2] = 1

        # Iterate through each index, starting from 3 to indx + 1
        for indx in range(3, n + 1):
            # Compute the current tribonacci number by taking the sum of last three numbers
            dp[indx] = dp[indx - 1] + dp[indx - 2] + dp[indx - 3]

        return dp[n]