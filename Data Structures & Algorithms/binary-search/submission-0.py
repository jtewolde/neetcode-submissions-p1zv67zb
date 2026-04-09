class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initial approach using Binary Search
        # Create two variables, low = 0, high = len(nums) - 1,
        # Create while loop where the condition is when low < high
        # Initialize a variable, mid = (low + high) // 2
        # If nums[mid] < target, then low will be equal to mid + 1 b/c it is on the upper half
        # If nums[mid] > target, the high will be equalt to mid - 1 b/c target is on lower half
        # If nums[mid] == target, then return mid

        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            middle_val = nums[mid] # Element with mid index

            if middle_val < target:
                low = mid + 1
            elif middle_val > target:
                high = mid - 1
            elif middle_val == target:
                return mid
            
        return -1 