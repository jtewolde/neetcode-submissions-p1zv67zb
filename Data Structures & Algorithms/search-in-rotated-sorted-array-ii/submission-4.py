class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # Logic: Use Binary Search to find the middle value in nums, see if target is in nums
        # Create two pointers to find the target
        # Find the middle value in the nums array
        # Determinge if target is in left and right section of nums
        
        # Initialize the two pointers for binary search
        left, right = 0, len(nums) - 1

        while left <= right:
            # Calculate the middle value in nums
            mid = (left + right) // 2

            # Automatically return true if the middle val is the target
            if nums[mid] == target:
                return True

             # Check left side of nums array
            if nums[left] < nums[mid]:
                if nums[left] <= target < nums[mid]:  # Target in left
                    # Shrink search area to left side
                    right = mid - 1
                else:  # Go right
                    left = mid + 1
                    
            elif nums[left] > nums[mid]:  # Right half is sorted
                if nums[mid] < target <= nums[right]:  # Target in right
                    left = mid + 1
                else:
                    right = mid - 1

            else:
                left += 1

        return False
