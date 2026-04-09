class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Approach for solving this problem by using Binary Search
        # Create two variables, left = 1 and right = max num from piles
        # These two represent the range of which k can be to eat all bananas at h hours,
        # Create res variable to keep track of min int of k. By default, set it to right as the max of piles will be guarantee answer
        # Perform Binary search with while loop of left <= right
        # Initialize k variable represnting mid where it will equal left + right // 2
        # Additionally, create totalHours variable to keep track of hours for each value of k to see if it is equal or less than h
        # Loop through each pile in piles array
        # For each pile, add the ceiling of p/k to hours variable with math.ceil
        # If totalHours <= given h, then update res variable with the min value between current res and k value
        # Also, set the right pointer to be k - 1 in order to make totalHours bigger
        # Else, just set left pointer to k + 1 to make totalHours smaller if needed
        # Then, just return res as final answer

        left, right = 1, max(piles)
        res = right

        while left <= right:
            k = (left + right) // 2
            totalHours = 0

            for p in piles:
                totalHours += math.ceil(p/k)

            if totalHours <= h:
                res = min(res, k)
                right = k - 1
            else: 
                left = k + 1

        return res












