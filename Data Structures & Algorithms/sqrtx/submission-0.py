class Solution:
    def mySqrt(self, x: int) -> int:
        # Logic: Find the ans to sqrt root for x-number with Binary Search
        # Approach: Use Binary Search to find median nubmer from 0 to x
        # Calculate median with left and right pointers
        # Then, use median val to calculate hypothetical sqrt of x

        # Initialize left and right pointers for binary search
        # Also, create ans vairable to return final sqrt of x
        left = 0
        right = x
        ans_sqrt = 0

        # Iterate through values of x for Binary Search to find Sqrt(x)
        while left <= right:
            # Find middle value from 0 - x to calculate sqrt(x)
            mid = left + (right - left) // 2

            # Determine if sqrt(x) is greater than x, then move right pointer down one
            if mid * mid > x:
                right = mid - 1

            # If sqrt(x) is less than x, then move left pointer up one to increase for next iteration
            # Set ans variable to mid value 
            elif mid * mid < x:
                left = mid + 1
                ans_sqrt = mid

            # Otherwise, return mid for current iteration.
            else:
                return mid

        return ans_sqrt



