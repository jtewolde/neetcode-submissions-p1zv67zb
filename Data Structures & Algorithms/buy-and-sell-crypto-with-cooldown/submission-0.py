class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # In this problem, we can make two decisions with each having their own subdecisions on each day
        # Decision 1: Are we hold a stock? > Keep or sell the stock we have
        # Decision 2: Are we not holding a stock > Buying a stock or not
        # After selling a NeetCoin, you need to be on cooldown, means skipping one index
        # Approach: Use caching and recursive DFS Function to solve this problem
        # The DFS Function will have two arguments, indx for curr index and a boolean to indicate if you can buy or not
        
        # Notes: 
        # If buying NeetCoin > indx + 1 (go to next day)
        # If selling NeetCoin > indx + 2 (skip one day to account for cooldown)

        # Initialize DP hash set for caching known results from recursion
        # The key will be (indx, buying boolean), value will be max_profit
        dp = {}

        # Create DFS recursion function that takes current index and buying boolean
        def dfs(indx, buying):
            # Establish base cases: If out of bounds > return zero for no profit
            if indx >= len(prices):
                return 0
            # If current result is in cache, return from cache
            if (indx, buying) in dp:
                return dp[(indx, buying)]

            # Create cooldown that skips a day in prices array while still buying state
            cooldown = dfs(indx + 1, buying)

            # Establish if statements for both decisions on whether buying or selling
            if buying:
                # If buying coin, call dfs function and change to not buying state after buying
                # Subtract from max profit as buying decreases profit
                buy = dfs(indx + 1, not buying) - prices[indx]
                # Cache results of max profit between buying and cooldown
                dp[(indx, buying)] = max(buy, cooldown)
            else:
                # Call dfs function with skipping two days b/c of cooldown after selling
                # Add to max profit as selling would increase profit
                sell = dfs(indx + 2, not buying) + prices[indx]
                # Cache results of max profit between buying and cooldown
                dp[(indx, buying)] = max(sell, cooldown)

            return dp[(indx, buying)]

        return dfs(0, True)





