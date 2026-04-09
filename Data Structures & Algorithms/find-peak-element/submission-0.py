class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # Approach: Use Two pointers/Binary Search techinque to copare elemtns at different indexes together
        # First, initialize left and right pointers, where left starts at 0 and right starts at end
        # Also, create maxPeak variable to keep track of peak element currentlry encountered in nums
        # Iterate through nums array with two pointers with while loop
        # Compare elements at left/right pointers to see which is greater

        # Initialize left and right pointers for comparing elements to find peak element
        # maxPeak to update and keep track of current peak element in nums
        left, right = 0, len(nums) - 1
        maxPeak = 0

        # Use Binary Search to find the middle value and compare elements next to mid
        while left < right:
            # Compute middle value for binary search
            mid = (left + right) // 2

            # If middle element is greater than element right of it, 
            # Search the left side of nums by setting right to mid
            if nums[mid] > nums[mid + 1]:
                right = mid
            # Otherwise, search the right side of nums
            else:
                left = mid + 1

        # Peak element should be at left pointer, return left element
        return left