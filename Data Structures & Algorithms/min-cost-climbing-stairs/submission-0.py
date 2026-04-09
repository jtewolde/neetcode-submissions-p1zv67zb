class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Approach to solving this DP problem is to use Memoization and Top-Down DP
        # Synposis: For this problem, the goal is to find the minimum cost of traversing to the end of cost array
        # You can start at either index 0 and 1. 
        # First, create an array, memo, that is initialized as -1 at each index with len(cost)
        # Create DFS function that takes index as argument
        # Iterate through length of cost, starting from index 2 to end of cost
        # Set the base cases: If the current index is greater than or equal to end of cost array, return 0
        # If the current memo's val doesn't equal -1 (was modified), return that current moo
        # Set val of memo[i] to equal cost of current position and the minimum cost of climbing one or two steps
        # Return memo at the current index(memo[i])

        # Initialize memo array where each index has val of -1, length of cost array
        memo = [-1] * len(cost)

        # Create DFS function that takes index as argument
        def dfs(i):
            # Base cases: If index is out of bounds of length of cost
            # If value at memo[i] isn't equal to -1, return current memo
            if i >= len(cost):
                return 0
            if memo[i] != -1:
                return memo[i]

            # Set current memo to equal cost[i] + minimum of dfs between one or two steps
            memo[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))

            # Return current memo at index
            return memo[i]

        # Return minimum cost of DFS starting at index 0 and 1
        return min(dfs(0), dfs(1))



