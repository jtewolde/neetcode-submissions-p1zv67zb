class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Approach: Use binary search to split the search for where the target num starts/ends
        # Create a helper binary search function that takes target value as parameter
        # Initialize left and right pointers where left = 0 and right = len(nums)
        # Create a middle variable that takes left + (right - left) // 2 for index of middle value
        # If number at middle is greater than or equal to target, move right pointer to middle for searching left side
        # Otherwise, move left pointer to mid + 1 to search right side and return left pointer for binary search function
        # Outside of helper function, create start variable that is the output of binarySearch(target)
        # See if start has the same length of nums or the output of start doesn't equal target, return [-1 , -1]
        # Otherwise, return interval from start and binarySearch(target + 1) - 1

        # Create a helper binary search function that takes target value as parameter
        def binarySearch(target):
             # Initialize left and right pointers where left = 0 and right = len(nums)
            left, right = 0, len(nums)

            while left < right:
                # Create a middle variable that takes left + (right - left) // 2 for index of middle value
                mid = left + (right - left) // 2
                # If number at middle is greater than or equal to target, move right pointer to middle for searching left side
                if nums[mid] >= target:
                    right = mid
                # Otherwise, move left pointer to mid + 1 to search right side and return left pointer for binary search function
                else:
                    left = mid + 1
                    
            return left

        # Outside of helper function, create start variable that is the output of binarySearch(target)
        start = binarySearch(target)
        # See if start has the same length of nums or the output of start doesn't equal target, return [-1 , -1]
        if start == len(nums) or nums[start] != target:
            return [-1, -1]

        # Otherwise, return interval from start and binarySearch(target + 1) - 1 as final answer
        return [start, binarySearch(target + 1) -  1]