class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        # Approach: Use two pointers approach to get the max and min element
        # First, sort the nums array so that mininum elements are left and max elements are right of arrays
        # Initialize left pointer at zero and right pointers at end of nums array
        # Also, create mod variable that represents mod 10^9 + 7
        # Create for loop that iterates through nums array using enumerate to get both element and index of left pointer
        # Check if the sum of elements are left and right pointer is less than or equal to target
        # If greater than, shrink the right pointer inward
        # If sum is less than, continue with while loop
        # Create if statement that the index of left pointer is less than index of right pointer
        # If valid subsequence, increment ans variable with 2^(right - left) using pow method
        # Then, use modular division on ans with mod variable for final answer

        # First, sort the nums array so that mininum elements are left and max elements are right of arrays
        # Initialize left pointer at zero and right pointers at end of nums array
        # Also, create mod variable that represents mod 10^9 + 7
        nums.sort()
        right = len(nums) - 1
        ans = 0
        mod = 10**9 + 7

        # Create for loop that iterates through nums array using enumerate to get both element and index of left pointer
        for left, val in enumerate(nums):
            # Check if the sum of elements are left and right pointer is less than or equal to target
            # If greater than, shrink the right pointer inward
            while left <= right and val + nums[right] > target:
                right -= 1

             # Create if statement that the index of left pointer is less than index of right pointer
            if left <= right:
                # If valid subsequence, increment ans variable with 2^(right - left) using pow method
                # Then, use modular division on ans with mod variable for final answer
                ans += pow(2, right - left, mod)
                ans %= mod

        return ans





