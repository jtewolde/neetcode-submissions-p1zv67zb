class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        # Approach: Use basic iteration to place a split in the nums array and determine if the split is valid
        # The split is valid if the left side of the split > right side of split
        # Count the number of valid splits encountered in the iteration of the nums array

        # Initialize left and right variables to store total sum from left and right side of split
        # Also, create countValid that will store the number of valid splits
        right = sum(nums)
        left = 0
        countValid = 0
        
        # Iterate through the nums array
        for idx in range(len(nums) - 1):
            # Increment left variable with new number at curr iteration and decrement right variable
            left += nums[idx]
            right -= nums[idx]

            # Check if the split is valid by determining left >= right side of split
            # Increment countValid variable if true
            if left >= right:
                countValid += 1
        return countValid
