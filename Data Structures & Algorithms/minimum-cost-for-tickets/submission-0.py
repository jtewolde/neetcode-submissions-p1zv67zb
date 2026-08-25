class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # Approach: Use a 1D DP Bottom-Up approach to build out the dp array results for finding the minimum cost of traveling each day
        # Bottom-Up in this problem is iterating through days array and building the DP array in reverse.

        # Initialize DP array filled with zeros for each cell at the length of n, being the length of days array
        n = len(days)
        dp = [0] * (n + 1)

        # Iterate through the indexes of day array in reverse and initialize dp value of current index with infinite
        for indx in range(n - 1, -1, -1):
            dp[indx] = float('inf')
            curr = indx
            
            # Iterate through each pass duration pair with the cost and duration
            for duration, cost in zip([1, 7, 30], costs):
                while curr < n and days[curr] < days[indx] + duration:
                    curr += 1
                # Set the dp value of the current index to the minimum of all options
                dp[indx] = min(dp[indx], cost + dp[curr])
        return dp[0]