class Solution:
    def arraySign(self, nums: List[int]) -> int:
        # First Approach: Use iteration to get the total product of the nums array and return 1, -1, or 0 depending on sign of final product
        # Optimal Approach: Iterate through every number in nums array and count the number of negative nums.
        # If the count is even, return 1 as the negatives cancel out, If odd, then return -1 or return 0 if there is a zero

        # Initialize count variable for counting number of negative numbers
        negCount = 0

        # Iterate through the each number inside of nums and determine if current num is zero first. Return zero if true and break loop
        # If num is negative, then increment negCount
        for num in nums:
            if num == 0:
                return 0
            elif num < 0:
                negCount += 1
        return -1 if negCount % 2 else 1