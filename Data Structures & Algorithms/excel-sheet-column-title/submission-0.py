class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # Approach: Use iteration to compute the corresponding column letters to represent colNumber
        # Iteration from this will go in reverse, building the string right to left
        # In this problem, it is essential creating a Base-26 digit system like Base-10
        # With base 10, every digit has 10 different numbers where a new digit is added to number once it reaches its last num
        # The same will happen with this problem where each letter will have 26 possible chars
        # Example: 8 > 9 > 10. Y > Z > AA

        # Initialize ans variable as an empty list to collect characters
        ans = []

        # Build out final string while the given colNumber is greater than zero
        while columnNumber > 0:
            # Decrement colNumber by one b/c character mapping starts at 1 instead of 0 to be zero-indexed
            # Compute the offset by taking the modular division of colNumber by 26
            columnNumber -= 1
            offset = columnNumber % 26

            # Add the offset to the ASCII value of A and make it back into a character to append to ans
            # Update colNumber by doing integer division by 26
            ans += (chr(ord('A') + offset))
            columnNumber //= 26
        
        # Reverse the ans array and convert into a string for final answer
        return ''.join(reversed(ans))


