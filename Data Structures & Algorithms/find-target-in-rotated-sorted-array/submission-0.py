class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initial approach by using Binary Search
        # Perform binary search on array by creating two pointers, left and right
        # Loop through array while left <= right
        # Create middle value of (left + right) // 2
        # First, if target is equal to middle, return index of mid
        # See if the target is in either the left side or right side of sorted array

        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:  # Target in left
                    right = mid - 1
                else:  # Go right
                    left = mid + 1
                    
            else:  # Right half is sorted
                if nums[mid] < target <= nums[right]:  # Target in right
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1

