class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Pseudocode for this soluiton:
        # Initialze a proft variable to track profit between two indexs
        # Use Two pointers strategy where left begins at 0 and right at 1
        # Use a while loop to iterate sliding window
        
        # Initialize left and right pointers
        left = 0
        right = 1
        
        max_profit = 0 # set initial profit to zero

        # Loop until the right pointer reaches end of array
        while right < len(prices):
            # If left price less than right price, there is a profit
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left] 
                max_profit = max(max_profit, profit)
            else:
                left = right

            right += 1

        return max_profit
