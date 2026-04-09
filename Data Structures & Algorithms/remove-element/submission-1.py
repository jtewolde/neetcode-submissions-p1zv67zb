class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Two Pointers approach: 
        # Initialize left and right pointers where left = 0 and right = len(nums)
        # Create while loop that continues while left < right
        
        # Initialize left and right pointers where left = 0 and right = len(nums)
        left = 0
        right = len(nums)

        # Create while loop that continues when left < right
        while left < right:
            # If number at left pointer equals val, decrement right pointer by one to take number out of nums
            # Set number at left to number at right to "remove"
            if nums[left] == val:
                right -= 1
                nums[left] = nums[right]
            # Otherwise, go to the next number by incrementing left pointer by one
            else:
                left += 1
        # Finally, return right as it will return new length of nums
        return right