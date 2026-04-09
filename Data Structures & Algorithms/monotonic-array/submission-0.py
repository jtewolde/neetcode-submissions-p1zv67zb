class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        # Optimal Approach: Create two flags for tracking if array is monotonic-increasing/decreasing
        # Initialize both increasing and decreasing flags to be false by default
        # Iterate through the nums array and compare numbers at current index to next index
        # If num at curr index is greater than num at next index, set increasing flag to true
        # If num at curr index is less than num at next index, set decreasing flag to true
        # Return the result of OR opreation between increasing and decreasing flags

        # Initialize both increasing and decreasing flags to be True by default
        increaseFlag, decreaseFlag = True, True

        # Iterate through the nums array and compare numbers at current index to next index
        for i in range(len(nums) - 1):
            # If num at curr index is not greater than num at next index, set increasing flag to False
            if not (nums[i] <= nums[i + 1]):
                increaseFlag = False

            # If num at curr index is not less than num at next index, set decreasing flag to False
            if not (nums[i] >= nums[i + 1]):
                decreaseFlag = False

        return increaseFlag or decreaseFlag
