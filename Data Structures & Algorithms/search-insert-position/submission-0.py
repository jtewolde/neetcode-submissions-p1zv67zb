class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Logic: Use binary search to find the mid poitnt of the array,
        # Use the midpoint to find where target should be in the array
        # Return the index where target needs to be sorted and inserted in
        # Or return the index where target is in array if found

        # Initialize pointers for binary search
        # and variable to track index of target value in nums
        left = 0
        right = len(nums) - 1
        t_index = 0

        # Loop through nums array to find middle point
        while left <= right:
            # Find middle of nums array with left/right pointers
            midpoint = (left + right) // 2

            # Find where target val falls in nums array
            # Case 1: Left Side of nums array
            if target <= nums[midpoint]:
                right = midpoint - 1

            # Case 2: Right side of nums array
            elif target >= nums[midpoint]:
                left = midpoint + 1

            # Case 3: Target is in nums array
            # Return the index of midpoint for answer
            elif target == nums[midpoint]:
                return midpoint
                
        # Else, return left pointer as it is the index where the target would be inserted in
        return left