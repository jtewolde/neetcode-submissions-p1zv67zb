class Solution:
    def rob(self, nums: List[int]) -> int:
        # Approach for solving this House Robber problem is to use Memoization
        # There are two recursive decisions to rob a house:
        # Rob current house, skip the next house
        # Skip the current house, rob the next house immediately

        # Step 1: Preinitialize memo array that has -1 as value at each index
        # Step 2: Create DFS function that takes index as argument
        # Step 3: Create base cases for dfs function
        # Base case 1: If current index is out of bounds from nums array, return 0
        # Base case 2: If memo val at current index doesn't equal -1, return that memo
        # Step 4: Create two expressions that represent two decisions
        # Decision 1: Rob the current house and skip the next house (nums[i] + dfs(i + 2)
        # Decision 2: Skip the current house and immediately rob the next house (dfs(i + 1) 
        # Set memo at current index to the max between both decisions

        # Preinitialize memo array that has -1 as value at each index
        memo = [-1] * len(nums)

        # Create DFS function that takes index as arg
        def dfs(index):
            # Initialize base cases
            if index >= len(nums):
                return 0
            if memo[index] != -1:
                return memo[index]

            # Create two variables that represent two decisions to make when robbing houses
            rob_current = nums[index] + dfs(index + 2)
            skip_current = dfs(index + 1)

            # Set memo at current index to max between both decisions
            # Return memo at current index
            memo[index] = max(rob_current, skip_current)
            return memo[index]

        return dfs(0)




