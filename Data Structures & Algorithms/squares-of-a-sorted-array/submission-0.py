class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Brute force approach: Iterate through all nums in nums array
        # Square each number in the array,
        # Sort the array and return the final nums array
        # Runtime: O(N) - Linear

        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]

        return sorted(nums)