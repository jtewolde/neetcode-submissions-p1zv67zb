class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        # Approach: Use Greedy method to find combination of buying two chocolates to have leftover money
        # You want to buy the lowered priced chocolates to minimize sum of prices and have more leftover
        # First, sort the entire prices array so lowered priced chocolates are in front of array
        # Get the first two elements from chocolates array and get sum of both prices
        # Compare cost of chocolates to money
        # If cost > money, return money as final answer as you can't buy with no debt
        # If cost < money, return the difference between the two for leftovers

        # Sort prices array so first two elements are least priced chocolates
        prices.sort()

        # Initialize cost variable that sums up first two elements
        cost = prices[0] + prices[1]

        # Check if cost of first two elements is less than or greater than money,
        # If graeter than, return money as you'll be in debt
        # Otherwise if less or equal to, return the difference between the two
        if money < cost:
            return money
        else:
            return money - cost