class Solution:
    def minOperations(self, s: str) -> int:
        # First Approach: Use Iteration to traverse through string and change binary char based on previous index
        # Determine what pattern the string is going either starting with '1' or '0'
        # Starting with '1' means even indexes are '1' and odd indexes are '0'
        # Starting with '0' means odd indexes are '1' and odd indexes are '1'
        # Initialize count that keeps tracks of changes needed to create a alternating binary string
        # Iterate through string with index
        # If the current index is even and the char is '0', increment count as it should be 1
        # Vice versa, if the current index is odd and the char is '1', increment count
        # After, return the minimum between count and length - count 

        # Initialize count that keeps tracks of changes needed to create a alternating binary string
        count = 0

        # Iterate through string with index
        for i in range(len(s)):
            # If the current index is even and the char is '0', increment count as it should be 1
            if i % 2 == 0 and s[i] == '0':
                count += 1
            # Vice versa, if the current index is odd and the char is '1', increment count
            elif i % 2 == 1 and s[i] == '1':
                count += 1
        # After, return the minimum between count and length - count
        return min(count, len(s) - count)