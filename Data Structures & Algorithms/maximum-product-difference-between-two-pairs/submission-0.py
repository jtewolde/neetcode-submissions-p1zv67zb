class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        # First Approach: Sort the entire nums array to have easy access to the largest and smallest values
        # For the max product difference between two pairs, get the top 2 minimum and maximum values from array
        # Set the product of the first two indexes be the minimum product
        # Then, get the product of the last two indexes for the maximum product
        # Finally, get the difference between the max and min product for final answer

        nums.sort()
        minProduct = nums[0] * nums[1]
        maxProduct = nums[-1] * nums[-2]

        return (maxProduct - minProduct)