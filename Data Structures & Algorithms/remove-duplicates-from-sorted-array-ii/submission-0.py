class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Approach: Use a two-pointers techinque to remove duplicates of elements in nums array
        # Goal is to remove duplicates so that there are at least two occurances of each unique element
        # The logic is that the left pointer tracks where to write and place new elements after deleting duplicats

        # Initialize left and right pointers for iterating through entire nums array and finding duplicates and replacing their position after removal
        left, right = 0, 0

        # Iterate through nums array using right pointer and start current count of unique number at one
        while right < len(nums):
            count = 1
            
            # Iterate through group of duplicates while right pointer is in bounds and next element is the same
            # Count how many duplicates there are for a group of duplicates by advancing right pointer and incrementing count
            while right + 1 < len(nums) and nums[right] == nums[right + 1]:
                right += 1
                count += 1

            # Write at minimum 2 copies of the element depending on count starting at position left
            # Then, advance left pointer and move to the next group of numbers
            for indx in range(min(2, count)):
                nums[left] = nums[right]
                left += 1
            # Advance right pointer regardless
            right += 1

        # Return left pointer as final answer for new length of nums array without more than 2 duplicates
        return left