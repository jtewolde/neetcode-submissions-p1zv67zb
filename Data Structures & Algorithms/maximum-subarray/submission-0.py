class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Approach to solving this problem using Greedy Method -> Kadane's Algorithm
        # This will be similar to Sliding Window
        # First, craete two variables, maxSum to track max sub array while going through, set initlally to -inf
        # Then, curSum variable to track to current sum of a given sub array and set initially to 0
        # Iterate through the entire nums array with for loop
        # See if curSum is negative, if so, reset it to zero and discard past nums
        # Add current number to the curSum
        # Update maxSum with maximum between current val of maxSum and curSum
        # Return maxSum as final answer

        maxSum = float('-inf')
        curSum = 0

        for num in nums:
            if curSum < 0:
                curSum = 0

            curSum += num
            maxSum = max(maxSum, curSum)

        return maxSum
