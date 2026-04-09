class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        # Approach: Use Iteration to calculate maximum sum of increasing subarrays in nums
        # Initialize maxStreak varialbe that will hold the current max sum from subarray that is increasing
        # Iterate through nums array, add first elememt automatically to maxStreak
        # If next element is greater, add element to maxStreak and continue until next element isn't greater
        # Reset maxStreak if subarray is in decreasing pattern
        # Return maxStreak as final answer

        # Initialize maxStreak and curSum that has first element as the starting value
        # maxStreak tracks the maximum sum of all increasing subarrays in nums
        # curSum tracks the current running sum of subarrays
        maxStreak = nums[0]
        curSum = nums[0]

        # Iterate through nums, skipping first element at index 0
        for i in range(1, len(nums)):
            # Case 1: If subarray is decreasing where the current element is less than previous
            # Reset curSum back to zero for next subarray
            if nums[i] <= nums[i - 1]:
                curSum = 0
            # Case 2: Subarray is increasing where current element is greater than previous
            # Add current element to curSum and update maxStreak by taking max val between the two
            curSum += nums[i]
            maxStreak = max(curSum, maxStreak)

        return maxStreak