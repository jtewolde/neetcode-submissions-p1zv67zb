class StockSpanner:

    # Approach: Use a monotonic stack data structure to store all daily price quotes and their spans as a pair
    # Inside of next function: 
    # Compare the given int with last four prices of stock to see if it is equal or less than while the stack is not empty
    # When a new price arrives, pop out all of the previous prices that are equal or less than new price
    # If current price is greater than or equal to last price, add the span of previous price to current price's span
    # Append pair of price and span to the stack
    
    # Initialize init stack variable to store daily price quotes and their spans
    def __init__(self):
        self.stack = [] # pair: (price, span)

    def next(self, price: int) -> int:
        span = 1 # Initialize span as 1 since first price will have no previous prices

        # Make sure that the stack is not empty and the previous price on top of stack is less than new price
        while self.stack and self.stack[-1][0] <= price:
            # Pop out previous prices/spans from stack and add previous span to new span
            previous_price, previous_span = self.stack.pop()
            span += previous_span

        # Append new price and new span to the stack
        self.stack.append((price, span))

        return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)