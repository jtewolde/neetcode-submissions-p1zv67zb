class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Goal: Find and return the unique elements from nums array without duplicates
        # Return the number of unique elements of nums
        # First approach: Convert nums array into sorted hashset to remove duplicates automatically
        # Runtime: O(N Log N)

        # Second approach: Use Two Pointers techinque to solve problem where same elements are next to each other
        # Left pointer will track index to each unique element and also represent number of unique elements
        # Right pointer will iterate through entire array and compare element next to it to see if it is unique
        # Have both pointers start at 
        # Runtime: O(N)

        # Initialize left and right pointers to start at index 1
        left = 1
        for right in range(1, len(nums)):
            # See if current number at right pointer is unique by comparing to number next to it
            if nums[right] != nums[right - 1]:
                # Move unique number at right to left pointer
                nums[left] = nums[right]
                left += 1
        # return left pointer as final answer since it represnts number of unique elements in nums array
        return left