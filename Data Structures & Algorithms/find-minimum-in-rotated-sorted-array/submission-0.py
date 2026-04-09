class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Initial approach using Binary Search:
        # First, perform one binary search on the nums array to find the cut
        # where it is the minimum of the array
        # When finding middle of array, determine if the current mid is in
        # the left side of the sorted array where greater numbers are, if middle is less than left pointer
        # or if the pivot is in the right side, where lesser numbers are, if middle is greater than left pointer
        
        # Initialize left and right pointers
        left = 0
        right = len(nums) - 1
        ans = nums[0] # Array to keep track of possible minimums

        while left <= right:
            # if the array segment is sorted, take left pointer as it is the minimum
            if nums[left] < nums[right]:
                ans = min(ans, nums[left]) # Find minimum
                break

            middle = (left + right) // 2 # Create middle variable
            ans = min(ans, nums[middle]) # Put middle value in ans array
            
            # If middle is greater than left pointer, search right side of sorted array
            if nums[middle] >= nums[left]:
                left = middle + 1
            else:
                right = middle - 1

        return ans



