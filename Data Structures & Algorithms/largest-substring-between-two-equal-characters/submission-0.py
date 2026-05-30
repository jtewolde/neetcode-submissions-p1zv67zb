class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        # Approach: Use a hashmap to track the first occurrence of each char in string
        # Then, iterate through the string and see if current char exists in the hashmap
        # If true, compute the distance between first occurrence and update the maximum ans
        # Otherwise, put current char into the hashmap at current index
        # Return ans as final answer

        # Initialize hashmap for trackign first occurrence of characters in string
        # Also, create ans variable to store max length between equal chars
        # At default, it will equal -1 as if there are no chars at appear twice in string
        char_indexMap = {}
        ans = -1

        # Use enumerate to iterate through string with index and char
        for indx, char in enumerate(s):
            # Case 1: If current char exists in hashmap already
            # Update ans with maximum difference between current difference to new difference between first occurrence and second occurrence
            if char in char_indexMap:
                ans = max(ans, indx - char_indexMap[char] - 1)
            # Otherwise, enter current char into the hashmap with index
            else:
                char_indexMap[char] = indx
        return ans