class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Approach for solving this DP problem is to using the Kadane's Algorthim
        # Goal is to find the subarray that produces the maximum product
        # One complication is that negatives are complicate the problem where multipying two negatives can be positive
        # Or could flip current results
        # Strategy is to track the maximum and minimum of each ending position in array
        # B/c the minimum can become he max if mulitpled by negative num if most negative

        # Initialize ans that tracks the global max substring to 1
        # curMin tracks the current minimum for current position in nums
        # curMax tracks the current maximum for current position in nums
        ans = nums[0]
        curMin, curMax = 1, 1

        # Iterate through every number in nums array directly
        for num in nums:
            # Create temp variable that stores product of current Max and number
            # To be used in the curMin min comparison later to get old curMax
            temp = curMax * num

            # Update curMax where it takes the maximum between the current num,
            # current num * curMax, and current num * curMin for any negative number that could make it postive
            curMax = max(num, curMax * num, curMin * num)

            # Similar to curMax updating but instead taking/tracking the minimum
            # We track the minimum b/c a negative num could flip it to positive and make it maximum
            curMin = min(num, temp, curMin * num)

            # Update the ans variable with the max between itself and curMax
            ans = max(ans, curMax)

        return ans


