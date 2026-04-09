class Solution:
    def maxDepth(self, s: str) -> int:
        # Approach: Use Greedy/Iteration to find the maximum depth of parenthesis in string s
        # To find the maximum depth, use two counters to keep track of depth size
        # Create depth counter that only increases when encountering left parenthesis and decrement for right parenthesis
        # If encountering a character, update hte max counter with maximum depth with depth counter

        # Initialize depth counter for tracking current dpeth
        # maxDepth counter for trackign the maximum depth of parentheses to be returned
        depth, maxDepth = 0, 0

        # Iterate through each character in string
        # Determine if current char is left/right parenthesis, then increment/decrement depth counter
        # If char is a letter, update maxDepth with new maximum from depth or current depth
        for char in s:
            if char == "(":
                depth += 1
            elif char == ')':
                depth -= 1
            maxDepth = max(depth, maxDepth)

        return maxDepth

