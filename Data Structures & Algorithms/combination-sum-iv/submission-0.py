class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # Approach: Use bottom-up Dynamic Programming to build up the final solution
        # By computing the different number of ways to reach each sum from 0 to target.
        
        # Initialize dp array by using a hashmap to set base case
        # Where the ways of summing to zero is only 1 way
        dp = { 0 : 1 }

        # Iterate through all totals ranging from 1 to target and make the current total in DP array 0
        for total in range(1, target + 1):
            dp[total] = 0
            # For each number in the nums array, check if the total - current num exists in DP
            # If true, add that count to dp[total]. Otherwise, set the count to zero
            for num in nums:
                dp[total] += dp.get(total - num, 0)
        # Return the built up dp array for target as final answer
        return dp[target]

