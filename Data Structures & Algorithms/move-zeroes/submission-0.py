class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # First Approach: Use Two-Pointers to move zeros to right side of array
        # Logic: Use left pointer at start of array to process non-zero elements
        # Right pointer to iterate through elements in nums array
        # If right pointer encounters non-zero element, swap elements at left and right pointer
        # Increment left pointer to move down nums array

        # Initialize left pointer for boundary between processed and non-processed elements
        left = 0
        
        # Iterate through nums array with right pointer
        for right in range(len(nums)):

            # If element at right pointer is not-zero, swap elements at left and right pointers
            # Increment left pointer as well with right pointer to move down nums array
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
