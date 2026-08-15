class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Approach: Use a Greedy algorithm to just capture the rise in price movement to get all of the profits
        # Strategy is to buy when the price is low and sell when the price is high for profit
        # In terms of the solution, iterate through the prices array starting at index 1.
        # Compare values at index i and index i + 1 to see if there was a rise in price or not
        # If there is a rise, get the difference between both prices and add to profit variable and return it

        # Initialize profit variable to store all profits gained from buying/selling in prices
        profit = 0

        # Iterate through each prices, starting from day/index 1 to the last day
        for indx in range(1, len(prices)):
            # Compare prices and see if price at current day is higher than previous day's
            # If true, then get the difference between both days' prices and add to profit variable
            if prices[indx] > prices[indx - 1]:
                diff = (prices[indx] - prices[indx - 1])
                profit += diff

        return profit