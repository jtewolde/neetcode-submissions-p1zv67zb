class Solution:
    def integerBreak(self, n: int) -> int:
        # Optimal Approach: Use a top-down DP approach, caching, and recursive DFS to solve the subproblems and break up n value
        # DP Caching is used so we don't have to solve the same subproblem again like breaking down 3 or 2.

        # Initialize dp hashmap for caching broken down nums, where the base case starts wwith 1
        dp = { 1 : 1 }

        # Create recursive DFS funciton that takes current num as parameter
        def dfs(num):
            # Check if the current num is in the cache, if so -> return the result of the num from the cache
            if num in dp:
                return dp[num]

            # Initialize the dp result of num to be zero if it equals the n value, otherwise make the result equal to num
            dp[num] = 0 if num == n else num
            
            # Iterate through each number from 1 to num - 1
            for i in range(1, num):
                # Create val variable that will hold the product between two numbers after breaking down num
                # Then, take the max between current result for num in dp cache and product value
                val = dfs(i) * dfs(num - i)
                dp[num] = max(dp[num], val)
            return dp[num]
        
        return dfs(n)

