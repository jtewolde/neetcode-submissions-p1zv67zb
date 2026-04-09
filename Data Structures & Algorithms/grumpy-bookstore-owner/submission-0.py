class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # Approach: Use sliding window techinque to find the window that has the maximum of happy customers
        # Initialize window counter that stores number of customers in current window
        # And happy counter that stores number of customers that are happy with owner
        # Use left and right pointers to represnt the boundaries of window
        # Iterate through entire length of the grumpy array with right pointer
        # If owner is grumpy(== 1) at current index, add customers value at right pointer to window
        # Otherwise, add customers at right pointer to happy counter
        
        # Initialize window counter that stores number of customers in current window
        # And happy counter that stores number of customers that are happy with owner
        left = 0
        window = maxWindow = 0
        happy = 0

        # Iterate through entire length of the grumpy array with right pointer
        for right in range(len(customers)):
            if grumpy[right] == 1:
                window += customers[right]
            else:
                happy += customers[right]

            # If window size exceeds minutes, then shrink from the left
            # By removing customers at left pointer if they are grumpy
            # And moving left pointer forward
            if right - left + 1 > minutes:
                if grumpy[left] == 1:
                    window -= customers[left]
                left += 1

            # Update maximum value of window
            maxWindow = max(window, maxWindow)

        return happy + maxWindow
        


