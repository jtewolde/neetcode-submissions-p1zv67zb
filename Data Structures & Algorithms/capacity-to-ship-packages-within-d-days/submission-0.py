class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Approach: Use Binary Search to figure out minimum capacity of ship to store weights

        # First, initialize left and right pointers for binary search
        # With left = max element in weights where right = sum of all elements in weights
        # Then, create ans variable that stores minimum capacity to store all weights as final ans
        left, right = max(weights), sum(weights)
        ans = right

        # Create helper function, canShip, to determine if current capacity can ship all weights with parameter of cap
        # Inside of helper function, initialize ships variable to 1 and cap to given capcity from parameter
        def canShip(cap):
            ships, currentCap = 1, cap
            # Iterate through all of the weights in the array
            # Determine if the difference between current cap and weight < 0, 
            # If so, increment ships by one and reset current cap back to previous val
            for w in weights:
                if currentCap - w < 0:
                    ships += 1
                    currentCap = cap
            # Otherwise, decrement currCap with current weight,
            # return the boolean if ships <= days
                currentCap -= w
            return ships <= days

        # Then, perform binary search using left and right pointers to get midCap value
        while left <= right:
            # Use helper function to determine if current capacity value is valid and can ship all weights
            midCap = (left + right) // 2

            # If true, update ans with the minimum between cap and current ans, 
            # Then, move right pointer to midpoint
            if canShip(midCap):
                ans = min(ans, midCap)
                right = midCap - 1
            # Otherwise, move left pointer to mid point
            else:
                left = midCap + 1
        return ans





