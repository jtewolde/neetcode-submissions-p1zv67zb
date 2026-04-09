class Solution:
    def arrangeCoins(self, n: int) -> int:
        # Optimal Approach: Use Binary Search with a math equation to solve this problem
        # Goal: Find the maximum number of complete rows created with n coins

        # First, create low and high boundaries for binary search where:
            # - Low = 1 b/c n > 0 and each row should have at least one coin
            # - High = n 
        low, high = 1, n
        ans = 0 # Final answer variable

        # Create while loop for binary search where low <= high and find midpoint
        while low <= high:
            midpoint = (low + high) // 2
            # Use math formula: (mid /2)*(mid + 1) to calculate num of coins to complete row
            coins = (midpoint / 2) * (midpoint + 1)
            # Create if statement on if number of coins exceed number of rows,
            # If so, move high pointer to mid - 1
            if coins > n:
                high = midpoint - 1
            # Otherwise, update ans with max betweeen ans and midpoint and move low pointer to mid + 1
            else:
                low = midpoint + 1
                ans = max(ans, midpoint)
        return ans


