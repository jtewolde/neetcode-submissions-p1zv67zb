class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        # Approach: Use iteration to check if current element is greater or less than next element
        # Create two counter variables: one for tracking num of increasing subarrays
        # Another for counting num of decreasing subarrays
        # Iterate through nums array, increase or decrease counter variables depending on if the subarrays are increasing or decreasing
        # Update ans variable with max between current ans, increaseCount and decreaseCount
        
        # Initialize increaseCount and decreaseCount for tracking num of increasing/decreasing subarrays in nums
        # Ans variable is to get the maximum length between the two subarrays lengths
        decreaseCount = 1
        increaseCount = 1
        ans = 1

        # Iterate through the entire nums array
        for i in range(len(nums) - 1):
            # Case 1: If subarray is decreasing, increment decrese count by one
            # Reset increaseCount back to one
            if nums[i] > nums[i + 1]:
                decreaseCount += 1
                increaseCount = 1
            # Case 2: If subarray is increasing, increment increaseCount by one
            # Reset decreaseCount back to one
            elif nums[i] < nums[i + 1]:
                increaseCount += 1
                decreaseCount = 1
            # Case 3: If subarray has same equal elements, reset both counts back to one
            else:
                increaseCount = 1
                decreaseCount = 1
            
            # Update ans with maximum between current ans and both counts
            ans = max(ans, increaseCount, decreaseCount)

        return ans