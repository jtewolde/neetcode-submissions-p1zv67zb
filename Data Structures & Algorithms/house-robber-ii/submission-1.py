class Solution:
    def rob(self, nums: List[int]) -> int:
        # Approach for solving this problem is using top-down DP approach
        # Similar to House Robber 1, however, the main difference is that you can rob first and last house together
        # Synposis: Have to create two linear subproblems -> Rob first house and don't rob last and vice versa
        # In terms of indexes: Rob first house/not rob last: [0 to n-2]. Rob last and not first: [1, n - 1]

        # Base case: If there is only one number, return that number
        if len(nums) == 1:
            return nums[0]
    
        def helper(nums):
            # Initialize two variables, rob1 and rob2, 
            # which represents the maximum amount of money from robbing previous two houses
            # [rob1, rob2, num, num + 1, ...]
            rob1, rob2 = 0, 0

            # Iterate through each number in nums array
            for num in nums:
                # Create newRob variable that is the maximum between current number + rob1 and rob2
                newRob = max(num + rob1, rob2)
                # Move forward into nums array by setting rob1 to rob2 and rob2 to newRob
                rob1 = rob2
                rob2 = newRob

            # Return rob2 as it will be the maximum of the entire input array
            return rob2

        # Return the maximum between both decisions of robbing first/last house
        return max(helper(nums[1:]), helper(nums[:-1]))
