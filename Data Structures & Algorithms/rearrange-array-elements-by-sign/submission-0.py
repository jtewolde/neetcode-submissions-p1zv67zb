class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # Approach: Use two pointer techinque to track different positions in the nums array simultaneously
        # Initialize pointers, a and b, where a starts at 0-index for even indexes and b starts at 1-index for odd indexes
        # Also, create an ans array that will store the rearranged elements by sign
        # Iterate through nums array using c pointer
        # See if nums[c] is positive or negative and determine where it goes on ans array
        # If positive, place the num at nums[a] and increment a pointer by 2 to next even index
        # If negative, place num at nums[b] and increment b pointer by 2 to next odd index
        # After iterating through every number, return ans as final rearranged array

        # Initialize pointers, a and b, where a starts at 0-index for even indexes and b starts at 1-index for odd indexes
        # Also, create an ans array that will store the rearranged elements by sign with length of nums array
        a, b = 0, 1
        ans = [0] * len(nums)

        # Iterate through nums array using c pointer
        # See if nums[c] is positive or negative and determine where it goes on ans array
        for c in range(len(nums)):
            # If positive, place the num at nums[a] and increment a pointer by 2 to next even index
            if nums[c] > 0:
                ans[a] = nums[c]
                a += 2
            # If negative, place num at nums[b] and increment b pointer by 2 to next odd index
            else:
                ans[b] = nums[c]
                b += 2

        return ans