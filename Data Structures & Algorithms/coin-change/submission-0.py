class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # The pattern/approach needed to solve this problem is by using DP Array and Bottom-Up
        # Base cases for this problem, if amount = 0, return 0 as there are no amount of coins
        
        
        # Initialize dp array that represnets min num of coins to make up that amout
        # Make the zero index of dp array(dp[0] = 0) equal zero for the base case if amount = 9
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        # Create nested for loop where first loop goes through different amounts
        # Second loop goes through each coin in coins array
        for am in range(1, amount + 1):
            for coin in coins:
                # Calculate difference between current amount val and coin
                # See if difference is greater than zero, then continue searching
                diff = am - coin
                if diff >= 0:
                    # Update dp[am] with the minimum of its current val and previous mins of coins for other amounts
                    dp[am] = min(dp[am], 1 + dp[diff])

        # Return result of dp[amount] if the amount val as changed, if not, return -1
        return dp[amount] if dp[amount] != amount + 1 else -1
        

