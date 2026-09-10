class Solution:
    def minSwaps(self, s: str) -> int:
        # Approach: Use a greedy algothrim to track the imbalance directly by tracking the amount of close parenthesis
        # The close counter variable will increase when encountering close parenthesis or decrease when encountering open parenthesis

        # Initialize close and maxClose variable where close will actively increase/decrease based on # of open or close brackets
        # Where maxClose will be the worst-case imbalance and get the max number of unmatched closing brackets
        close, maxClose = 0, 0

        # Iterate through each bracket in the string
        for bracket in s:
            # Determine if the current bracket is opening or closing, if closing then decrement close counter
            # Increment close counter for the inverse
            if bracket == '[':
                close -= 1
            else:
                close += 1
            
            # Update maxClose with the maximum between current close counter and maxClose value
            maxClose = max(close, maxClose)
        return (maxClose + 1) // 2
